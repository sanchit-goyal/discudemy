import concurrent.futures
import re
import threading

import requests

from util import timeit

__REGEX__ = '<a class="cardHeader" href="(.+)">(.+)</a>'
__MAX_PAGE_COUNT__ = 210
__URL__ = 'https://programming.discudemy.com/all/{}'
__MAX_WORKERS__ = 100


def get_html_content(url):
    try:
        r = requests.get(url)
    except ConnectionError as error:
        raise Exception('last url : {}'.format(url), error)
    if r.status_code == 200:
        return r.content.decode('utf-8')
    else:
        raise Exception('status code is {}'.format(r.status_code))


def get_value_key_tuple(html_content):
    return set(re.findall(__REGEX__, html_content))


@timeit
def for_pages():
    url_name_list = []
    for _ in range(1, __MAX_PAGE_COUNT__ + 1):
        print("processing page : {}".format(_))
        url_name_list |= get_value_key_tuple(get_html_content(__URL__.format(_)))
    return url_name_list


@timeit
def for_page_threading():
    url_name_list = set()
    future_list = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=__MAX_WORKERS__) as executor:
        for _ in range(1, __MAX_PAGE_COUNT__ + 1):
            print("processing in future page : {}".format(_))
            future_list.append(executor.submit(get_html_content, __URL__.format(_)))
    for _ in future_list:
        url_name_list |= get_value_key_tuple(_.result())

    return url_name_list


def concurrent_run():
    future = threading.Thread(target=for_page_threading, args=())
    normal = threading.Thread(target=for_pages, args=())
    future.start()
    normal.start()
    future.join()
    normal.join()

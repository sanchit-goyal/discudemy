import os

import IO
from DiscUdemy import DiscUdemy
from proto.course_pb2 import Courses
from scraper import for_page_threading


def fix_files():
    """
    call if you have messy input files
    :return: None
    """
    _data = set(for_page_threading())
    IO.serialize_to_file(_data)
    IO.write_to_json_file(_data)
    IO.write_to_csv_file(get_obj_from_set(_data))
    IO.write_proto_to_file(get_proto_from_set(_data))


def get_obj_from_set(_data):
    """
    :param _data:
    :return: DiscUdemy
    """
    disc_udemy_list = []
    for _ in _data:
        disc_udemy_list.append(DiscUdemy(_))
    return disc_udemy_list


def get_proto_from_set(_data) -> Courses:
    courses = Courses()
    for _ in _data:
        proto_course = courses.courses.add()
        proto_course.name = _.name
        proto_course.url = _.url
    return courses


__SEARCH_KEY__ = 'JAVA'
if __name__ == '__main__':
    # fix_files()
    data = get_obj_from_set(IO.deserialize_from_file())

    IO.write_proto_to_file(get_proto_from_set(data))

    print('proto file size =', os.stat('files/discudemy.proto.obj').st_size)
    print('pickle file size =', os.stat('files/discudemy.obj').st_size)
    print('json file size =', os.stat('files/discudemy.json').st_size)
    print('csv file size =', os.stat('files/discudemy.csv').st_size)

    data = IO.read_proto_from_file()
    print(data.courses[0])

    # test.ParseFromString(data_2[0].SerializeToString())

    # for _ in data:
    #     if _.name.upper().find(__SEARCH_KEY__) > -1:
    #         print(_)

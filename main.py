import IO
from DiscUdemy import DiscUdemy
from scraper import for_page_threading


def get_obj_repr_from_set(_data):
    classes = []
    for _ in _data:
        classes.append(repr(DiscUdemy(_)))
    return classes


def fix_files():
    """
    call if you have messy input files
    :return: None
    """
    _data = set(for_page_threading())
    IO.serialize_to_file(_data)
    IO.write_to_json_file(_data)
    IO.write_to_csv_file(get_obj_from_set(_data))


def get_obj_from_set(_data):
    """

    :param _data:
    :return: DiscUdemy
    """
    disc_udemy_list = []
    for _ in _data:
        disc_udemy_list.append(DiscUdemy(_))
    return disc_udemy_list


__SEARCH_KEY__ = 'JAVA'
if __name__ == '__main__':
    # fix_files()
    data = get_obj_from_set(IO.deserialize_from_file())
    for _ in data:
        if _.name.upper().find(__SEARCH_KEY__) > -1:
            print(_)

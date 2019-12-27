import json
import pickle

__FILE_ENCODING__ = 'utf-16'
__OBJ_FILE_NAME__ = 'files/discudemy.obj'
__JSON_FILE_NAME__ = 'files/discudemy.json'
__CSV_FILE_NAME__ = 'files/discudemy.csv'


def write_to_csv_file(data):
    with open(file=__CSV_FILE_NAME__, mode='w', encoding=__FILE_ENCODING__) as file:
        file.write('\n'.join(data))


def write_to_json_file(data_to_serialize):
    with open(file=__JSON_FILE_NAME__, mode='w', encoding=__FILE_ENCODING__) as file:
        json.dump(list(data_to_serialize), file)


def read_from_json_file():
    return json.loads(__JSON_FILE_NAME__, encoding=__FILE_ENCODING__)


def serialize_to_file(data_to_serialize):
    with open(file=__OBJ_FILE_NAME__, mode='wb') as file:
        pickle.dump(data_to_serialize, file)


def deserialize_from_file():
    with open(__OBJ_FILE_NAME__, 'rb') as file:
        return pickle.load(file)

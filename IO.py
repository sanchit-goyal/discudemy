import csv
import json
import pickle

from proto.course_pb2 import Courses

__FILE_ENCODING_UTF_8__ = 'utf-8'
__FILE_ENCODING_UTF_16__ = 'utf-16'
__OBJ_FILE_NAME__ = 'files/discudemy.obj'
__JSON_FILE_NAME__ = 'files/discudemy.json'
__CSV_FILE_NAME__ = 'files/discudemy.csv'
__PROTO_FILE_NAME__ = 'files/discudemy.proto.obj'


def write_to_csv_file(_data):
    with open(file=__CSV_FILE_NAME__, mode='w', encoding=__FILE_ENCODING_UTF_8__, newline='') as file:
        data_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow(['name of course', 'url'])
        for _ in _data:
            data_writer.writerow([_.name, _.url])


def write_to_json_file(data_to_serialize):
    with open(file=__JSON_FILE_NAME__, mode='w', encoding=__FILE_ENCODING_UTF_16__) as file:
        json.dump(list(data_to_serialize), file)


def read_from_json_file():
    return json.loads(__JSON_FILE_NAME__, encoding=__FILE_ENCODING_UTF_16__)


def serialize_to_file(data_to_serialize):
    with open(file=__OBJ_FILE_NAME__, mode='wb') as file:
        pickle.dump(data_to_serialize, file)


def deserialize_from_file():
    with open(__OBJ_FILE_NAME__, 'rb') as file:
        return pickle.load(file)


def write_proto_to_file(courses: Courses):
    with open(__PROTO_FILE_NAME__, 'wb') as file:
        file.write(courses.SerializeToString())


def read_proto_from_file() -> Courses:
    courses = Courses()
    with open(__PROTO_FILE_NAME__, 'rb') as file:
        courses.ParseFromString(file.read())
    return courses

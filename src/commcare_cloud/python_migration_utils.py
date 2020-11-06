import six
from io import open


def open_for_json_dump(path):
    """
    This ensures compatible file write modes based on Python versions
    Python 2 json.dump(s) returns a bytes object
    Python 3 json.dump(s) returns a str object
    """
    if six.PY2:
        return open(path, "wb")
    return open(path, "w", encoding="utf-8")

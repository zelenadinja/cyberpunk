import pytest

from titles_to_s3 import json_to_s3


@pytest.mark.parametrize(
    "object_body, object_key",
    [
        ([1, 2, 3], "test/list.json"),
        ({"a": 1, "b": 2, "c": 3}, "test/dict.json"),
        ((1, 2, 3), "test/tuple.json"),
    ])
def test_json_to_s3(object_body, object_key):
    """Test uploading varios obects to s3 bucket"""

    json_to_s3(object_body=object_body, object_key=object_key)

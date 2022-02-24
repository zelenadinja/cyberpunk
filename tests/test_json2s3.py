
import pytest
<<<<<<< HEAD

from titles_to_s3 import json_to_s3
=======
from movie_titles_to_s3 import json_to_s3
>>>>>>> 9613a4329bd82624e96f6fa780a22020f2383521


@pytest.mark.parametrize(
    "object_body, object_key",
    [
        ([1, 2, 3], "test/list.json"),
        ({"a": 1, "b": 2, "c": 3}, "test/dict.json"),
        ((1, 2, 3), "tests/tuple.json"),
    ])
def test_json_to_s3(object_body, object_key):
    """Test uploading varios obects to s3 bucket"""

    json_to_s3(object_body=object_body, object_key=object_key)

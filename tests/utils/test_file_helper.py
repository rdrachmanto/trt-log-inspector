import pytest

from trt_log_inspector.utils.file_helper import open_file_from_path


def test_reject_invalid_file():
    f = "nonexists.txt"
    
    with pytest.raises(FileNotFoundError):
        open_file_from_path(f)

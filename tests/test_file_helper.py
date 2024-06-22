from typing import List
import pytest

from trt_log_inspector.trt_log_file import TrtLogFile


def test_reject_invalid_file():
    f = "nonexists.txt"
    with pytest.raises(FileNotFoundError):
        TrtLogFile(name="nonexists", path=f)


def test_accept_valid_file():
    f = ".python-version"
    logfile = TrtLogFile(name="pyv", path=f)
    assert(isinstance(logfile.content, List))

from pyqode.core.modes import CheckerMessages
from pyqode.json.modes.linter import json_linter


def test_valid_json():
    with open('test/files/example.json', 'r') as f:
        code = f.read()
    errors = json_linter({'code': code})
    assert len(errors) == 0


def test_invalid_json():
    with open('test/files/invalid.json', 'r') as f:
        code = f.read()
    errors = json_linter({'code': code})
    assert len(errors) == 1
    assert isinstance(errors[0][0], str)
    assert errors[0][1] == CheckerMessages.ERROR
    assert errors[0][2] == 11
    assert errors[0][3] == 13

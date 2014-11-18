from pyqode.json.widgets import JSONCodeEdit
from pyqode.qt.QtTest import QTest


def test_json_code_edit():
    editor = JSONCodeEdit()
    editor.file.open('test/files/example.json')
    QTest.qWait(1000)
    assert editor.backend.running
    editor.close()
    assert not editor.backend.running


def test_clone(editor):
    clone = editor.clone()
    assert type(clone) == type(editor)

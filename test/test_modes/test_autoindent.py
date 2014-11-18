from pyqode.core.api import TextHelper
from pyqode.qt import QtCore
from pyqode.qt.QtTest import QTest


def test_indent_after_opening_symbol(editor):
    editor.file.open('test/files/example.json')
    TextHelper(editor).goto_line(1, 15)
    assert TextHelper(editor).current_line_text() == '    "widget": {'
    QTest.keyPress(editor, QtCore.Qt.Key_Return)
    assert TextHelper(editor).current_line_text() == '        '


def test_indent_after_closing_symbol(editor):
    editor.file.open('test/files/example.json')
    TextHelper(editor).goto_line(25, 9)
    assert TextHelper(editor).current_line_text() == '        }'
    QTest.keyPress(editor, QtCore.Qt.Key_Return)
    assert TextHelper(editor).current_line_text() == '    '

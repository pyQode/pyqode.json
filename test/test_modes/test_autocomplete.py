from pyqode.core.api import TextHelper
from pyqode.qt import QtCore
from pyqode.qt.QtTest import QTest


def test_autocomplete_double_quotes(editor):
    code = '''{
"widget": {
    "debug": "on",
    "window": {
        "title": "Sample Konfabulator Widget",
        "name": "main_window",
        "width":
        "height": 500
    },
}
}
    '''
    editor.setPlainText(code)
    assert editor.toPlainText() == code
    TextHelper(editor).goto_line(6, column=16, move=True)
    QTest.qWait(100)
    assert TextHelper(editor).current_line_text() == '        "width":'
    QTest.keyPress(editor, '"')
    result = '        "width":""'
    assert TextHelper(editor).current_line_text() == result
    QTest.qWait(100)
    TextHelper(editor).goto_line(6, column=len(result), move=True)
    QTest.keyPress(editor, ',')
    QTest.keyPress(editor, QtCore.Qt.Key_Return)
    QTest.qWait(100)
    QTest.keyPress(editor, '"')
    QTest.qWait(100)
    result = '        "":'
    assert TextHelper(editor).current_line_text() == result


def test_forbidden_characters(editor):
    code = '''{
"widget": {
    "debug": "on",
    "window": {
        "title": "Sample Konfabulator Widget",
        "name": "main_window",
        "width":
        "height": 500
    },
}
}
    '''
    editor.setPlainText(code)
    assert editor.toPlainText() == code
    TextHelper(editor).goto_line(6, column=16, move=True)
    QTest.qWait(100)
    assert TextHelper(editor).current_line_text() == '        "width":'
    QTest.keyPress(editor, '\'')
    assert TextHelper(editor).current_line_text() == '        "width":\''
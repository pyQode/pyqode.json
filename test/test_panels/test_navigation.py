from pyqode.core.api import TextHelper
from pyqode.qt.QtTest import QTest


def test_toggle_button(editor):
    editor.file.open('test/files/example.json')
    editor.show()
    TextHelper(editor).goto_line(6)
    QTest.qWait(500)
    panel = editor.panels.get('NavigationPanel')
    assert len(panel._widgets) == 4
    assert panel._widgets[1].text().replace('&', '').lower() == 'window'
    panel._widgets[1].toggled.emit(True)
    QTest.qWait(500)
    assert TextHelper(editor).cursor_position()[0] == 3

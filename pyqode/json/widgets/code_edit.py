from pyqode.core import api


class JSONCodeEdit(api.CodeEdit):
    mimetypes = ['application/json']

    def __init__(self, parent=None):
        super(JSONCodeEdit, self).__init__(parent)



if __name__ == '__main__':
    from pyqode.qt import QtWidgets
    import sys

    app = QtWidgets.QApplication(sys.argv)
    editor = JSONCodeEdit()
    editor.show()
    editor.file.open('/home/colin/pyqode/json/pyqode/test/files/masterdice.json')

    app.exec()

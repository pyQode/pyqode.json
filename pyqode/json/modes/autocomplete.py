from pyqode.core import modes
from pyqode.core.api import TextHelper


class AutoCompleteMode(modes.AutoCompleteMode):
    def _on_key_pressed(self, event):
        helper = TextHelper(self.editor)
        indent = helper.line_indent() * ' '
        if self.editor.textCursor().positionInBlock() == len(indent):
            self.QUOTES_FORMATS['"'] = '%s:'
        else:
            self.QUOTES_FORMATS['"'] = '%s'
        self.QUOTES_FORMATS['{'] = '\n' + indent + '%s'
        self.QUOTES_FORMATS['['] = '\n' + indent + '%s'
        super()._on_key_pressed(event)

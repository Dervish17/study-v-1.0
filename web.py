class Widget:
    def __init__(self):
        super().__init__()


class Label(Widget):
    def __init__(self, background_color, text):
        super().__init__()
        self.background_color = background_color
        self.text = text


class LineEdit(Label):
    def __init__(self, background_color, text, length):
        super().__init__(background_color, text)
        self.length = length


class TextEdit(Label):
    def __init__(self, background_color, text, length, weight):
        super().__init__(background_color, text)
        self.length = length
        self.weight = weight


class Button(Widget):
    def __init__(self, text):
        super().__init__()
        self.text = text


class CheckBox(Button):
    def __init__(self, text, options):
        super().__init__(text)
        self.options = options

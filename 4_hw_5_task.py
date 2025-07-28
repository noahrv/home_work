# файлик task_9_checks.py
class Checks:

    def __init__(self, loc):
        self.loc = loc

    def check_text(self):
        return self.loc


# файлик task_9_oop_1.py
from task_9_checks import Checks

class Title(Checks):
    def __init__(self, loc):
        super().__init__(loc)

class Button(Checks):
    def __init__(self, loc):
        super().__init__(loc)

class Input(Checks):
    def __init__(self, loc):
        super().__init__(loc)

class Link(Checks):
    def __init__(self, loc):
        super().__init__(loc)

title = Title("h1.main-header")
button = Button("button#submit-btn")
input_field = Input("input.username-field")
link = Link("a.login-link")

print(title.check_text())
print(button.check_text())
print(input_field.check_text())
print(link.check_text())

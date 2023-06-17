class Button:
    def __init__(self):
        self.text = None
        self.icon = None

    def paint(self):
        pass

class WindowsButton(Button):
    def paint(self):
        return f"Windows button with text '{self.text}' and icon '{self.icon}'"

class MacButton(Button):
    def paint(self):
        return f"Mac button with text '{self.text}' and icon '{self.icon}'"

class Checkbox:
    def __init__(self):
        self.label = None

    def paint(self):
        pass

class WindowsCheckbox(Checkbox):
    def paint(self):
        return f"Windows checkbox with label '{self.label}'"

class MacCheckbox(Checkbox):
    def paint(self):
        return f"Mac checkbox with label '{self.label}'"

class GUIFactory:
    def create_button(self) -> Button:
        pass

    def create_checkbox(self) -> Checkbox:
        pass

class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

class Dialog:
    def __init__(self):
        self.title = None
        self.message = None
        self.button = None
        self.checkbox = None

    def show(self):
        pass

class WindowsDialog(Dialog):
    def show(self):
        print(f"Windows dialog with title '{self.title}', message '{self.message}', button '{self.button.paint()}', and checkbox '{self.checkbox.paint()}'")

class MacDialog(Dialog):
    def show(self):
        print(f"Mac dialog with title '{self.title}', message '{self.message}', button '{self.button.paint()}', and checkbox '{self.checkbox.paint()}'")

class Builder:
    def __init__(self):
        self.dialog = None

    def create_dialog(self):
        pass

    def add_title(self):
        pass

    def add_message(self):
        pass

    def add_button(self):
        pass

    def add_checkbox(self):
        pass

class WindowsBuilder(Builder):
    def create_dialog(self):
        self.dialog = WindowsDialog()

    def add_title(self, title: str):
        self.dialog.title = title

    def add_message(self, message: str):
        self.dialog.message = message

    def add_button(self, text: str, icon: str):
        button = WindowsFactory().create_button()
        button.text = text
        button.icon = icon
        self.dialog.button = button

    def add_checkbox(self, label: str):
        checkbox = WindowsFactory().create_checkbox()
        checkbox.label = label
        self.dialog.checkbox = checkbox

    def get_dialog(self) -> Dialog:
        return self.dialog

class MacBuilder(Builder):
    def create_dialog(self):
        self.dialog = MacDialog()

    def add_title(self, title: str):
        self.dialog.title = title

    def add_message(self, message: str):
        self.dialog.message = message

    def add_button(self, text: str, icon: str):
        button = MacFactory().create_button()
        button.text = text
        button.icon = icon
        self.dialog.button = button

    def add_checkbox(self, label: str):
        checkbox = MacFactory().create_checkbox()
        checkbox.label = label
        self.dialog.checkbox = checkbox

    def get_dialog(self) -> Dialog:
        return self.dialog

class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):
        self.builder = builder

    def build_simple_dialog(self, title: str, message: str):
        self.builder.create_dialog()
        self.builder.add_title(title)
        self.builder.add_message(message)

    def build_complex_dialog(self, title: str, message: str, button_text: str, button_icon: str, checkbox_label: str):
        self.builder.create_dialog()
        self.builder.add_title(title)
        self.builder.add_message(message)
        self.builder.add_button(button_text, button_icon)
        self.builder.add_checkbox(checkbox_label)

if __name__ == "__main__":

    director = Director()

    print("Creating a Windows dialog using the WindowsBuilder:")

from typing import *

# noinspection PyUnresolvedReferences
document = window.document
# noinspection PyUnresolvedReferences
console = window.console


def mirror_changes(before: str, after: str, cursor: int) -> Tuple[str, int]:
    return after, cursor


class Reflector:
    def __init__(self):
        self.left = document.getElementById('left')
        self.right = document.getElementById('right')
        self.set_desired = document.getElementById('set_desired')
        self.last_value = document.getElementById('last_value')
        self.desired_value = document.getElementById('desired_value')
        self.test_cases = document.getElementById('test_cases')
        self.left.onkeyup = self.input_changed
        self.right.onkeyup = self.input_changed
        self.set_desired.onchange = self.toggle_desired
        self.focused_input = self.left

    def input_changed(self, e):
        pos = self.focused_input.selectionStart
        focused_text = (f'{self.focused_input.value[:pos]}|'
                        f'{self.focused_input.value[pos:]}')
        if self.focused_input == self.left:
            value = f'{focused_text}^{self.right.value}'
        else:
            value = f'{self.left.value}^{focused_text}'
        if self.set_desired.checked:
            self.desired_value.value = value
        else:
            self.last_value.value = value
            self.focused_input = document.activeElement

    def toggle_desired(self, e):
        if self.set_desired.checked:
            if self.focused_input == self.left:
                self.right.focus()
            else:
                self.left.focus()
        else:
            self.focused_input.focus()
            self.test_cases.value += (f'\n("{self.last_value.value}",'
                                      f'\n "{self.desired_value.value}"),')


window.reflector = Reflector()

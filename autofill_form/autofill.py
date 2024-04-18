import pyautogui
from time import sleep
from window_service import switch_window
from arg_service import get_args
from keyboard_service import is_key


def autofill(commands):
    args = get_args()
    [pid] = args
    parsed_pid = int(pid)

    for (command) in commands:
        [key, presses, countdown] = command

        column_label = commands[0]

        if command == column_label:
            sleep(1)
            continue

        parsed_presses = int(presses)
        parsed_countdown = int(countdown)

        switch_window(parsed_pid)

        if is_key(key):
            pyautogui.press(key, presses=parsed_presses)
        else:
            pyautogui.typewrite(key)

        print(f'Pressing {key} {parsed_presses} times')

        if parsed_countdown > 0:
            sleep(parsed_countdown)

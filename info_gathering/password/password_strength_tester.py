import PySimpleGUI as sg
import numpy as np
# c=(m^n)/2
# m possibilites for each character
# n the password length


def tester():
    layout = [
        [sg.Input(size=(25, 10) ,key='password')],
        [sg.Multiline(size=(25, 3), reroute_cprint=True, key='out', reroute_stdout=False, auto_refresh=True, no_scrollbar=True)],
        [sg.B('Run', bind_return_key=True)]
    ]

    # main window
    window = sg.Window('Password Strength', layout)
    while True:
        event, values = window.read()
        if event == 'Run':
            window.find_element('out').Update('')

            pwd = values['password']
            m = {}
            for char in pwd:
                if char in m:
                    m[char] += 1
                else:
                    m[char] = 1

            print(m)
            guesses = round((len(m) ** len(pwd)))
            time = guesses / 30_000_000

            # sg.cprint(len(values['password']))
            sg.cprint(f'It would take {guesses} guesses')
            sg.cprint(format(time, 'f') + 'seconds')
            sg.cprint(format(time/60, 'f') + 'hours')

        
        if event == sg.WIN_CLOSED or event == 'Exit':     # If user closed window with X or if user clicked "Exit" button then exit
            break

    window.close()

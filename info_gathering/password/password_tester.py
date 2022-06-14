# possibly add a color coded similar to the website
# modify printing how long it would take
# if it is higher than however much then change the unit

import PySimpleGUI as sg
import numpy as np

# c=(m^n)/2
# m possibilites for each character
# n the password length

sg.theme('Dark Grey 13')
sg.set_options(font='sans')

def tester():
    sg.popup("You can enter your password here and it will give you a rough estimate for how long it would take to guess", any_key_closes=True)
    layout = [
        [sg.Text('Enter your password: ')],
        [sg.Input(size=(25, 10) ,key='password')],
        # [sg.Text('')]
        [sg.Multiline(size=(50, 4), reroute_cprint=True, key='out', \
            reroute_stdout=False, auto_refresh=True, no_scrollbar=True)],
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
            
            sg.cprint(f'It would take {guesses} guesses')

            # seconds
            if time < 60:
                sg.cprint('It would take ' + format(time, 'f') + ' seconds for a computer to guess')
            # minutes
            elif time < 3600:
                sg.cprint('It would take ' + format(time/60, 'f') + ' minutes for a computer to guess')
            # hours
            elif time > 3600:
                hours = time/3600
                if hours < 168:
                    sg.cprint('It would take ' + format((hours), 'f') + ' hours for a computer to guess')
                # weeks
                elif hours/168 < 52:
                    sg.cprint('It would take ' + format((hours/168), 'f') + ' weeks for a computer to guess')
                # years
                elif hours/168 > 52:
                    sg.cprint('It would take ' + format((hours/168), 'f') + ' years for a computer to guess')

        if event == sg.WIN_CLOSED or event == 'Exit':     # If user closed window with X or if user clicked "Exit" button then exit
            break

    window.close()

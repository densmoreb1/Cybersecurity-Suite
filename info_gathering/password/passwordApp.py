from password_strength_tester import tester
import PySimpleGUI as sg

sg.theme('Dark Grey 13')
sg.set_options(font='sans')

sg.popup(""" The longer a password is the better it is to protect against brute force attacks """, any_key_closes=True)
sg.popup(""" A regular computer nowdays can guess passwords at about 30 million guesses a second """, any_key_closes=True)

layout = [
    [sg.Text('How many times can an average computer guess a second?')],
    [sg.Input()],
    [sg.B('Check', bind_return_key=True)]
]

window = sg.Window('Password Strength', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':     # If user closed window with X or if user clicked "Exit" button then exit
        break
    elif event == 'Check':
        if values[0].lower() == '30 million':
            sg.popup("You are correct", any_key_closes=True)
            tester()
            window.close()
        else:
            sg.popup('Incorrect')

    elif event == 'Clear':
        window.find_element('out').Update('')

window.close()

from passwordTester import tester
import PySimpleGUI as sg

sg.theme('Dark Grey 13')
sg.set_options(font='sans')

sg.popup(""" Passwords are important if we want to keep things secure and safe """, any_key_closes=True)
sg.popup(""" The longer a password is the better it is to protect against brute force attacks """, any_key_closes=True)
sg.popup(""" A regular computer nowadays can guess passwords at about 30 million guesses a second """, any_key_closes=True)

layout = [
    # [sg.Text('How many times can an average computer guess a second?')],
    [sg.Text('The more different characters there are in a password the amount of guesses grows exponentially')],
    # [sg.Input()],
    # [sg.B('Check', bind_return_key=True)]
    [sg.B('Check', bind_return_key=True)]
]

window = sg.Window('Password Strength', layout)
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    elif event == 'Check':
        # if values[0].lower() == '30 million':
        #     sg.popup("You are correct")
        tester()
        window.close()
        # else:
        #     sg.popup('Incorrect')

    elif event == 'Clear':
        window.find_element('out').Update('')

window.close()

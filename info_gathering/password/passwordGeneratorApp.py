import PySimpleGUI as sg
import numpy as np
import string
import random

sg.theme('Dark Grey 13')
sg.set_options(font='sans')

## characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password(length):

    ## shuffling the characters
    random.shuffle(characters)
    
    ## picking random characters from the list
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    ## shuffling the resultant password
    random.shuffle(password)

    ## converting the list to string
    ## printing the list
    return ''.join(password)

sg.popup("Be sure to take this password over to the strength tester!")

layout = [
    [sg.Text('How long would you like your password?')],
    [sg.Input(size=(50, 3))],
    [sg.Multiline(size=(50, 3), reroute_cprint=True, key='out', \
        reroute_stdout=False, auto_refresh=True, no_scrollbar=True)],
    [sg.B('Generate', bind_return_key=True)]
]

# main window
window = sg.Window('Password Strength', layout)
while True:
    event, values = window.read()
    
    if event == 'Generate':
        window.find_element('out').Update('')
        sg.cprint(generate_random_password(int(values[0])))

    if event == sg.WIN_CLOSED or event == 'Exit':     # If user closed window with X or if user clicked "Exit" button then exit
        break

window.close()

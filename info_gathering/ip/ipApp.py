import PySimpleGUI as sg
from ipAddress import ip_main

sg.theme('Dark Grey 13')
sg.set_options(font='sans')

HOSTS = ['computer', 'printer', 'router']

# popup
sg.popup("""
Welcome to ip address discovery.

This is a simple app that allows you to find an ip address for a url
""", any_key_closes=True)

sg.popup(f"""
An ip address is an address that uniquely identifies a host. 

A host can be a {" ".join(HOSTS)}.

URL's and ip address tell you where to go, just like a street address.
""", any_key_closes=True)

layout = [
    [sg.Text('From the ones listed previously, what can be a host with an ip address? ')],
    [sg.Input()],
    [sg.B('Check', bind_return_key=True)]
]

window = sg.Window('Discover an IP Address', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': 
        break
    elif event == 'Check':
        if values[0].lower() in HOSTS:
            sg.popup("You are correct")
            ip_main()
            window.close()
        else:
            sg.popup("Incorrect", any_key_closes=True)
    elif event == 'Clear':
        window.find_element('out').Update('')

window.close()

import socket  
import PySimpleGUI as sg

def ip_main():

    sg.theme('Dark Grey 13')
    sg.set_options(font='sans')

    # main window design
    layout = [
        [sg.Text('Enter a URL:')],
        [sg.Input(size=(25, 10))],
        [sg.Text('Ip Address:')],
        [sg.Multiline(size=(25, 2), reroute_cprint=True, key='out', reroute_stdout=False, auto_refresh=True, no_scrollbar=True)],
        [sg.B('Run', bind_return_key=True), sg.B('Clear')]
    ]

    # main window
    window = sg.Window('Disover an IP Address', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':     # If user closed window with X or if user clicked "Exit" button then exit
            break
        elif event == 'Run':
            try:
                IPAddr = socket.gethostbyname(values[0])
                sg.cprint(IPAddr)
            except Exception as e:
                sg.cprint('Enter a valid address')
        elif event == 'Clear':
            window.find_element('out').Update('')

    window.close()

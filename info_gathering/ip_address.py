import socket  
import PySimpleGUI as sg

sg.theme('Dark Grey 13')
sg.set_options(font='sans')

# main window design
left_col = sg.Column([
    [sg.Text('Enter the URL: '), sg.InputText()],
    [sg.B('Run', bind_return_key=True), sg.B('Clear')]
])

right_col = sg.Column([
    [sg.Multiline(size=(50, 10),write_only=True, reroute_stdout=True, echo_stdout_stderr=True, reroute_cprint=True, key='STDOUT')]
    ],
)

layout = [
    [sg.Pane([
        sg.Column([[left_col]], element_justification='l', expand_x=True, expand_y=True), 
        sg.Column([[right_col]], element_justification='r', expand_x=True, expand_y=True)],
        orientation='h',
        show_handle=False
        )
    ]
]

# popup
sg.popup("""
Welcome to ip address discovery
This is a simple app that allows you to find an ip address for a url
""")

sg.popup("""
An ip address is an address that uniquely identifies a host. 
A host can be a computer, printer, or a router.
URL's and ip address tell you where to go. They identify the same place. 
""")

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
        window.find_element('STDOUT').Update('')
        # window.find_element().Update('')

window.close()

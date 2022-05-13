import socket   
import PySimpleGUI as sg

sg.theme('Dark Grey 13')
sg.set_options(font='sans')
  
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


window = sg.Window('Simple data entry window', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':     # If user closed window with X or if user clicked "Exit" button then exit
        break
    elif event == 'Run':
        try:
            IPAddr = socket.gethostbyname(values[0])
            sg.cprint(IPAddr)
        except Exception as e:
            sg.cprint('Enter a valid address', e)
    elif event == 'Clear':
        window.find_element('STDOUT').Update('')
        # window.find_element().Update('')

window.close()

import PySimpleGUI as sg
import os

def get_file_list_dict():
    """
    Returns dictionary of files
    Key is short filename
    Value is the full filename and path

    :return: Dictionary of demo files
    :rtype: Dict[str:str]
    """

    demo_files_dict = {}
    path = os.path.abspath(os.getcwd())

    for dirname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.py') and filename != 'app.py':
                fname_full = os.path.join(dirname, filename)
                if filename not in demo_files_dict.keys():
                    demo_files_dict[filename] = fname_full

    return demo_files_dict


def get_file_list():
    """
    Returns list of filenames of files to display
    No path is shown, only the short filename

    :return: List of filenames
    :rtype: List[str]
    """
    return sorted(list(get_file_list_dict().keys()))


sg.theme('Dark Grey 13')

left_col = sg.Column([
    [sg.Listbox(values=get_file_list(), size=(50,20))]
])

right_col = sg.Column([
    [sg.Multiline(size=(70, 21))],
])

layout = [
    [sg.Pane([
        sg.Column([[left_col]], element_justification='l', expand_x=True, expand_y=True), 
        sg.Column([[right_col]], element_justification='c', expand_x=True, expand_y=True)],
        orientation='h'
        )
    ]
]

window = sg.Window('Cybersecurity Demo', layout, finalize=True)


# event loop
while True:
    event, values = window.read()   # Read the event that happened and the values dictionary
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':     # If user closed window with X or if user clicked "Exit" button then exit
        break
    if event == 'Button':
      print('You pressed the button')

window.close()
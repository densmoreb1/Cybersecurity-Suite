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
sg.set_options(font='sans')

left_col = sg.Column([
    [sg.Listbox(values=get_file_list(), size=(25, 8), key='-DEMO LIST-', select_mode=sg.SELECT_MODE_EXTENDED, no_scrollbar = True)],
    [sg.Button('Run'), sg.Exit()]
])

right_col = [
    [sg.Multiline("""
    Welcome to my cybersecurity suite
    Instructions:
    - click on a script that you would like to learn more about
    - go through the promts
    - learn!
    """, size=(50, 8), no_scrollbar=True)]
]

layout = [
    [sg.Pane([
        sg.Column([[left_col]], element_justification='l', expand_x=True, expand_y=True),
        sg.Column(right_col, expand_x=True, expand_y=False)
        ], 
        orientation='h',
        show_handle = False,
        )
    ]
]

window = sg.Window('Cybersecurity Demo', layout, finalize=True)

file_list_dict = get_file_list_dict()
file_list = get_file_list()
                
while True:
    event, values = window.read()   # Read the event that happened and the values dictionary
    # print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':     # If user closed window with X or if user clicked "Exit" button then exit
        break
    elif event == 'Run':
        for file in values['-DEMO LIST-']:
            file_to_run = str(file_list_dict[file])
            sg.execute_py_file(file_to_run)

window.close()
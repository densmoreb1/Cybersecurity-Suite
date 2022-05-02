import PySimpleGUI as sg
import os
import ntpath
import subprocess

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

def execute_command_blocking(command, *args):
    expanded_args = []
    for a in args:
        expanded_args.append(a)
        # expanded_args += a
    try:
        sp = subprocess.Popen([command, expanded_args], shell=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if out:
            print(out.decode("utf-8"))
        if err:
            print(err.decode("utf-8"))
    except:
        out = ''
    return out


sg.theme('Dark Grey 13')
sg.set_options(font='sans')

left_col = sg.Column([
    [sg.Listbox(values=get_file_list(), size=(30,20), key='-DEMO LIST-', select_mode=sg.SELECT_MODE_EXTENDED)],
    [sg.Button('Run'), sg.B('Edit'), sg.B('Clear')]
])

right_col = sg.Column([
    [sg.Multiline(size=(70, 21), write_only=True, reroute_stdout=True, echo_stdout_stderr=True, reroute_cprint=True)],
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

file_list_dict = get_file_list_dict()
file_list = get_file_list()

# event loop
# while True:
#     event, values = window.read()   # Read the event that happened and the values dictionary
#     # print(event, values)
#     if event == sg.WIN_CLOSED or event == 'Exit':     # If user closed window with X or if user clicked "Exit" button then exit
#         break
#     elif event == 'Run':
#             sg.cprint('Running....', end='')
#             sg.cprint('')
#             for file in values['-DEMO LIST-']:
#                 print(file)
#                 file_to_run = str(file_list_dict[file])
#                 sg.cprint(file_to_run, text_color='white')
#                 execute_command_blocking(os.path.abspath(os.getcwd()), file)

                
                
while True:
    event, values = window.read()   # Read the event that happened and the values dictionary
    # print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':     # If user closed window with X or if user clicked "Exit" button then exit
        break
    elif event == 'Run':
            sg.cprint('Running....', end='')
            sg.cprint('')
            for file in values['-DEMO LIST-']:
                file_to_run = str(file_list_dict[file])
                sg.cprint(file_to_run, text_color='white')
                try:
                    sg.execute_py_file(file_to_run)
                    sg.execute_py_file(file)
                
                except Exception as e:
                    sg.cprint(f'Error trying to run python file.  Error info:', e, c='white on red')
                

window.close()
#!/usr/bin/env python
import PySimpleGUI as sg
import glob
import ntpath
import subprocess
import os

LOCATION_OF_YOUR_SCRIPTS = ''

# Execute the command.  Will not see the output from the command until it completes.
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

# Executes command and immediately returns.  Will not see anything the script outputs


def execute_command_nonblocking(command, *args):
    expanded_args = []
    for a in args:
        expanded_args += a
    try:
        sp = subprocess.Popen([command, expanded_args], shell=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        pass


def Launcher2():
    sg.theme('GreenTan')

    file_list_dict = get_file_list_dict()
    file_list = get_file_list()
    namesonly = []
    for file in file_list:
        namesonly.append(ntpath.basename(file))

    layout = [
        [sg.Listbox(values=namesonly, size=(30, 19),
                    select_mode=sg.SELECT_MODE_EXTENDED, key='demolist'),
         sg.Output(size=(88, 20), font='Courier 10')],
        [sg.CBox('Wait for program to complete', default=False, key='wait')],
        [sg.Button('Run'), sg.Button('Shortcut 1'), sg.Button('Fav Program'), sg.Button('EXIT')],
    ]

    window = sg.Window('Script launcher', layout)


    # ---===--- Loop taking in user input  --- #
    while True:
        event, values = window.read()
        if event in ('EXIT', None):
            break           # exit button clicked
        if event in ('Shortcut 1', 'Fav Program'):
            print('Quickly launch your favorite programs using these shortcuts')
            print('''
                Or  copy files to your github folder.
                Or anything else you type on the command line''')
            # copyfile(source, dest)
        elif event == 'Run':
            for index, file in enumerate(values['demolist']):
                print('Launching %s' % file)
                window.refresh()          # make the print appear immediately
                if values['wait']:
                    execute_command_blocking(LOCATION_OF_YOUR_SCRIPTS + file)
                else:
                    execute_command_nonblocking(
                        LOCATION_OF_YOUR_SCRIPTS + file)

    window.close()


if __name__ == '__main__':
    Launcher2()
import socket
import PySimpleGUI as sg 

sg.theme('Dark Grey 13')
sg.set_options(font='sans')

sg.popup(
"""
Welcome to the port scanner
This we will learn a tool that will scan ports and show us what is running on that port.
""", any_key_closes=True)
sg.popup(
"""
Ports are how data is sent between computers. 
Like a ship and a port at a harbor, there can only be one ship at a port.
In our case, the ship is an application.
""", any_key_closes=True)
sg.popup(
"""
Port numbers range from 0 - 65,535
Networking devices enforce strict rules when communicating with each other.
""", any_key_closes=True)

layout = [
    [sg.Text('Enter an IP address: '), sg.InputText()],
    [sg.Multiline(size=(50, 10), reroute_stdout=True, reroute_cprint=True, key='OUT', expand_x=True)],
    [sg.B('Scan', bind_return_key=True), sg.B('Clear')]
]

def probe_port(ip, port, result = 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        r = sock.connect_ex((ip, port))
        if r == 0:
            result = r
        sock.close()
    except Exception as e:
        pass
    return result

window = sg.Window('Scan a Network', layout)
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    elif event == 'Scan':
        
        ports = [21, 22, 23, 53, 80, 135, 443, 445]

        for port in ports:
            response = probe_port(values[0], port)

            if response == 0:
                sg.cprint(f'Port {port}: {socket.getservbyport(port)}')
        
        sg.cprint('Done')
    
    elif event == 'Clear':
        window.find_element('OUT').Update('')

window.close()

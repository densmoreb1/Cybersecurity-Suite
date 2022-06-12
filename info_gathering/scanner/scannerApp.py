import PySimpleGUI as sg 
from network_scanner import scanner

sg.theme('Dark Grey 13')
sg.set_options(font='sans')

PORTS = [21, 22, 23, 53, 80, 135, 443, 445]

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
f"""
Port numbers range from 0 - 65,535

Networking devices enforce strict rules when communicating with each other.

Because they enforce rules, the common ports are known what they are running.

Some of the commons ports include {' '.join(map(str, PORTS))}
""", any_key_closes=True)

sg.popup(
"""
People have compared to scanning a network to going to a random house, checking all the doors and windows seeing if they are locked.

Only scan networks if they allow you.
""", any_key_closes=True)

sg.popup(
"""
Most modern networks have firewalls up and will not allow scans to be made.

Luckily you can go to this address, under task 1 you can deploy an ip address to scan.

https://tryhackme.com/room/furthernmap
""", any_key_closes=True)


layout = [
    [sg.Text('From the commonly known ports, what was one of them?')],
    [sg.Input()],
    [sg.B('Check', bind_return_key=True)]
]

window = sg.Window('Scan a Network', layout)
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    elif event == 'Check':
        print(type(values[0]))
        if int(values[0]) in PORTS:
            sg.popup("You are correct", any_key_closes=True)
            scanner()
            window.close()
        else:
            sg.popup('Incorrect')
    elif event == 'Clear':
        window.find_element('OUT').Update('')

window.close()
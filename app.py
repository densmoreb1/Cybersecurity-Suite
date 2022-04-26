import PySimpleGUI as sg

layout = [
    [sg.Text("Select a file")],
    [sg.Listbox(values='psgdemos.py')]
]
window = sg.Window('Window Title', layout)      # Part 3 - Window Defintion
                                                
# Display and interact with the Window
event, values = window.read()                   # Part 4 - Event loop or Window.read call

# Do something with the information gathered
print('Hello', values[0], "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()       
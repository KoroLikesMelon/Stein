import PySimpleGUI as sg
from keyboard import _listener
import logging
def todo():
    theme = open("UserInformation//theme.txt", "r").read()
    sg.theme(theme)
    layout = [
        [sg.Text("Add your todo's here")],
        [sg.Input("", key="INPUT")],
        [sg.Button("ADD", key="-ADD-", size=(5,1)), sg.Button("LOAD", key="LOAD", size=(5,1)), sg.Button("WIPE", key="WIPE", size=(5,1))],
        [sg.Multiline("",enable_events=False, key="TODOLIST", size=(200,10))],
    ]
    window = sg.Window("To Do's", layout, size=(500,380))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "-ADD-":
            with open("UserInformation//todos.txt", "r") as file:    
                window["TODOLIST"].update(file.read())
            with open("UserInformation//todos.txt", "a") as file:
                file.write(values["INPUT"])
                file.write("\n")
        if event == "LOAD":
            with open("UserInformation//todos.txt", "r") as file:
                window["TODOLIST"].update(file.read())       
        if event == "WIPE":
            open("UserInformation//todos.txt", "w").close()
            with open("UserInformation//todos.txt", "r") as file:
                window["TODOLIST"].update(file.read())
                

            
    
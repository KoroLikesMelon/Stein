import PySimpleGUI as sg
def commandpallet():
    theme = open("UserInformation//theme.txt", "r").read()
    sg.theme(theme)
    layout = [
        [sg.Input("",key='COMMAND', size=(50,5)), sg.Text(" <=  Type the command here")],
        [sg.Multiline("", key="OUTPUT", background_color = "black", text_color = "white", size=(100,5))],
        [sg.Button("Send Command", key="COMMANDSEND"), sg.Button("Clear", key="CLEAR")]
    ]
    window = sg.Window("Command Palette", layout, size=(979,512))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "COMMANDSEND":
            if values["COMMAND"] == "help":
                window["OUTPUT"].update("HILF MIR")
            if values["COMMAND"] == "clear":
                window["OUTPUT"].update("")    
        if event == "CLEAR":
            window["OUTPUT"].update("")    
                
                 

if __name__ == '__main__':
    commandpallet()        
    
# this is in progress
# add way to create files possibly?
# other shit    
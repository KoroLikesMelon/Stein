import PySimpleGUI as sg
def settings():
    with open("UserInformation//theme.txt", "r") as file:
        readfile = file.read()
    sg.theme(readfile)
    themes = ["Black",
              "BlueMono",
              "BluePurple",
              "BrightColors",
              "BrownBlue",
              "Dark",
              "Dark2",
              "DarkAmber",
              "DarkBlack",
              "DarkBlue",
              "DarkBlue1",
              "DarkBlue10",
              "DarkBlue11",
              "DarkBlue2",
              "DarkBlue3",
              "DarkBlue4",
              "DarkBlue5",
              "DarkBlue6",
              "DarkPurple4",
              "DarkTeal10",
              "Reds"]
    BackGroundColor = ['Red', 'Green', 'Blue', 'Cyan', 'White', 'Black', 'Purple', 'Pink']
    textcolor = ['red', 'blue', 'blue', 'cyan', 'white', 'black', 'purple', 'pink']
    layout=[
        [sg.Text("Select a theme"), sg.Combo(themes, size=(10,10), key="Themes")],
        [sg.Text("Select a color for the Text field's background"), sg.Combo(BackGroundColor, size=(10,5), key="BACKGROUNDCOLOR")],
        [sg.Text("Select a text color for the text field"), sg.Combo(textcolor, size=(10,5), key="TEXTCOLOR")],
        [sg.Button("Apply", key="APPLY")]
    ]
    window = sg.Window("Settings", layout, size=(400,300))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "APPLY":
            def writetheme():
                with open("UserInformation//theme.txt", "w") as file:
                    file.write(values["Themes"])
            def writebackgroundcolor():    
                with open("UserInformation//backgroundcolor.txt", "w") as file:    
                    file.write(values["BACKGROUNDCOLOR"])
            def writetextcolor():
                with open("UserInformation//textcolor.txt", "w") as file:
                    file.write(values["TEXTCOLOR"])    
            if values["Themes"] == "":
                pass
            else:
                writetheme()
            if values['BACKGROUNDCOLOR'] == "":
                pass
            else:
                writebackgroundcolor()
            if values['TEXTCOLOR'] == "":
                pass
            else:
                writetextcolor()        
                sg.PopupOK("Changes Applied!, you need to relaunch your application for the changes to appear")    
                             
        
        
        
        
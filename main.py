import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import HorizontalSeparator, theme_text_color
import os
import subprocess
from settings import settings
def main():
    menu_def = [["File",['Save', 'New Window']],['Settings',["Settings"]]]
    with open("UserInformation//theme.txt", "r") as file:
        readfile = file.read()
    with open("UserInformation//textcolor.txt", "r") as file:
        readtextcolor = file.read()
    with open("UserInformation//backgroundcolor.txt", "r") as file:
        readbackgroundcolor = file.read()        
    sg.theme(readfile)
    languages = ['Python']
    column1 = [
        [sg.FolderBrowse("Browse a folder", change_submits=True, key='LOAD')],
        [sg.Listbox("",key="LISTBOX",text_color=readtextcolor, enable_events=True, size=(450, 47))],
        [sg.Input("", key="FILENAME"), sg.Button("Run", key="RUN"), sg.Combo(languages, size=(10,5), key="LANGUAGE")]
    ]
    column2 = [
        [sg.Multiline("", size=(300,60),key="MULTI",text_color=readtextcolor,background_color=readbackgroundcolor, autoscroll=True)]
    ]
    layout = [
        [sg.Menu(menu_def)],
        [sg.Column(column1, size=(500,950)),sg.VerticalSeparator(), sg.Column(column2, size=(1410,950))]
    ]
    window = sg.Window("Stein", layout, size=(1910,950), resizable="True")
    while True:
        if not os.path.exists("UserInformation//backgroundcolor.txt"):
            sg.PopupError("Couldn't backgroundcolor.txt!")      
            break
        elif not os.path.exists("UserInformation//textcolor.txt"):
            sg.PopupError("Couldn't tasks.txt!")      
            break
        elif not os.path.exists("UserInformation//theme.txt"):
            sg.PopupError("Couldn't theme.txt!")      
            break
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Settings":
            settings()
        if event == "LOAD":
            folder = values["LOAD"]
        if event == "New Window":
            main()    
    
        try:
            file_list = os.listdir(folder)

        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".py", ".c", ".cpp", ".jar", ".txt"))
        ]
        window["LISTBOX"].update(fnames)
        
        if event == "LISTBOX":
            try:
                filename = os.path.join(
                    values["LOAD"], values["LISTBOX"][0]
                )
                with open(filename, "r") as file:
                    readfile = file.read()
                window["MULTI"].update(readfile)
                window["FILENAME"].update(filename)
            except:
                pass 
        if event == "RUN":
            def run():
                if values["LANGUAGE"] == "":
                  sg.PopupError("LANGUAGE NOT SELECTED")
                if values["LANGUAGE"] == "Python":
                  subprocess.run("python -u \"{}\"".format(filename), shell=True)       

            if values["FILENAME"] == "":
                sg.PopupError("File Not Selected")
            else:
                run()     
        if event == "Save":
            def writefile():
                   with open(filename, "w") as file:
                         file.write(values["MULTI"])  
            if values["LOAD"] == "":
                sg.PopupError("FILE NOT SELECTED")  
            else:
                writefile()                  
            

if __name__ == '__main__':
    main()        




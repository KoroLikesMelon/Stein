import PySimpleGUI as sg
def extension():
    theme = open("UserInformation//theme.txt", "r").read()
    sg.theme(theme)
    with open("extensions.txt", "r") as file:
        list_of_lines = file.readlines()
        if list_of_lines[0] == "todo:loaded":
            layout = [
                [sg.Text("Unload To Do's"), sg.Button("UNLOAD", key="UNLOAD"),sg.Button("RELOAD", key="RELOAD")]
            ]
        else:
            layout = [
                [sg.Text("Load To Do's"), sg.Button("LOAD", key="LOAD"), sg.Button("RELOAD", key="RELOAD")]
            ]    
    window = sg.Window("Extensions", layout, size=(300,300))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "UNLOAD":
            list_of_lines[0] = "todo:unloaded"
            with open("extensions.txt", "w") as file:
                file.writelines(list_of_lines)
            window.close()
            extension()    
                
        if event == "LOAD":
            with open("extensions.txt", "w") as file:
                     list_of_lines[0] = "todo:loaded"
                     file.writelines(list_of_lines)      
            window.close()
            extension()  

if __name__ == '__main__':
    extension()        
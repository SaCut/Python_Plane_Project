# Creating a simple GUI for the terminal

import PySimpleGUI as sg

sg.theme("DarkBlue") # choose a window theme

# All the stuff inside your window.
login_layout = [
                [sg.Text("Username"), sg.InputText(key="-USERNAME-")],
                [sg.Text("Password"), sg.InputText(key="-PASSWORD-")],
                [sg.Submit("Log In"), sg.Cancel("Cancel")]
                ]

flights_layout = [
        [sg.Button("Flights"), sg.Button("Passengers")],
        ]

passengers_layout = [[sg.Text("test test test")]]

layout = [[sg.Column(login_layout, key="-LOG-"),
        sg.Column(flights_layout, key="-FLY-", visible=False),
        sg.Column(passengers_layout, key="-PASS-", visible=False)]]

# create the window
main_window = sg.Window("Login", layout)

# window running loop
while True:
    event, values = main_window.read()

    sg.popup_non_blocking(event, values)
    if event == sg.WIN_CLOSED or event == "Cancel": # if user closes window or clicks cancel
        break
    if event == "Log In":
        window["-LOG-"].update(visible=False)
        window["-FLY-"].update(visible=True)

main_window.close()
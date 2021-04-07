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
        [sg.Text("test test test")],
        [sg.Submit("Flights"), sg.Submit("Passengers"), sg.Submit()]
        ]

passengers_layout = []

# create the window
# main_window = sg.Window('Airport Terminal', main_layout, grab_anywhere=False, return_keyboard_events=True, finalize=True)
main_window = sg.Window("Login", login_layout)


# window running loop
while True:
    event, values = main_window.read()

    sg.popup_non_blocking(event, values)
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

main_window.close()
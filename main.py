import PySimpleGUI as sg

import functions as func

toprow = ['Name', 'Year of birth', 'Football club', 'Hometown', 'Team', 'Position']
rows = []

data = func.get_data()

j = 0
for i in data['players']:
    if j < 5:
        rows.append(func.curr_player_data(i))
    j += 1

table = sg.Table(values=rows, headings=toprow, auto_size_columns=True,
                 display_row_numbers=False,
                 justification='center', key='-TABLE-', )

layout = [[table],
          [sg.Button(button_text="Find", key='-Find-')],
          [sg.Button(button_text="Delete", key='-Del-')]]

window = sg.Window("Table", layout, size=(780, 280), resizable=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == '-Find-':
        func.window_find()

    if event == '-Del-':
        func.window_delete()
        table = func.refresh_data()
        layout = [[table],
                  [sg.Button(button_text="Find", key='-Find-')],
                  [sg.Button(button_text="Delete", key='-Del-')]]
        window = sg.Window("Table", layout, size=(780, 280), resizable=True)
        window.refresh()

window.close()

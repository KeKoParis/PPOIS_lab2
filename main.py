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
img = sg.Image(size=(15, 15), filename="arrows/right.png")
layout = [[table],
          [sg.Button(key='Nnext', image_filename="arrows/doubleL.png"),
           sg.Button(key='back', image_filename="arrows/left.png"),
           sg.Button(key='next', image_filename="arrows/right.png"),
           sg.Button(key='Bback', image_filename="arrows/doubleR.png")],
          [sg.Button(button_text="Find", key='-Find-'),
           sg.Button(button_text="Delete", key='-Del-')]]

window = sg.Window("Table", layout, size=(780, 280), resizable=True)
curr_player = 0
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
                  [sg.Button(key='Nnext', image_filename="arrows/doubleL.png"),
                   sg.Button(key='back', image_filename="arrows/left.png"),
                   sg.Button(key='next', image_filename="arrows/right.png"),
                   sg.Button(key='Bback', image_filename="arrows/doubleR.png")],
                  [sg.Button(button_text="Find", key='-Find-'),
                   sg.Button(button_text="Delete", key='-Del-')]]
        window1 = sg.Window("Table", layout, size=(780, 280), resizable=True)
        window.close()
        window = window1

    if event == 'next':
        table = func.next_page(curr_player)

        layout = [[table],
                  [sg.Button(key='Nnext', image_filename="arrows/doubleL.png"),
                   sg.Button(key='back', image_filename="arrows/left.png"),
                   sg.Button(key='next', image_filename="arrows/right.png"),
                   sg.Button(key='Bback', image_filename="arrows/doubleR.png")],
                  [sg.Button(button_text="Find", key='-Find-'),
                   sg.Button(button_text="Delete", key='-Del-')]]
        curr_player += 5
        if curr_player + 1 >= len(data['players']):
            curr_player += -5
        window = sg.Window("Table", layout, size=(780, 280), resizable=True)

window.close()

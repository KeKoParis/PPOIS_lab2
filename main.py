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

window = sg.Window("Table", func.update_layout(table), size=(780, 280), resizable=True)
curr_player = 0
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == '-Find-':
        func.window_find()

    if event == '-Del-':
        func.delete_player()
        curr_player += -5
        if curr_player < 0:
            curr_player += 5
        data = func.get_data()
        table = func.next_page(curr_player)
        new_window = sg.Window("Table", func.update_layout(table), size=(780, 280), resizable=True)
        window.close()
        window = new_window

    if event == 'next':
        curr_player += 5
        if curr_player > len(data['players']):
            curr_player += -5
        table = func.next_page(curr_player)
        new_window = sg.Window("Table", func.update_layout(table), size=(780, 280), resizable=True)
        window.close()
        window = new_window

    if event == 'back':
        curr_player += -5
        if curr_player < 0:
            curr_player += 5
        table = func.prev_page(curr_player)

        new_window = sg.Window("Table", func.update_layout(table), size=(780, 280), resizable=True)
        window.close()
        window = new_window

    if event == "Bback":
        curr_player = 0
        table = func.prev_page(curr_player)
        new_window = sg.Window("Table", func.update_layout(table), size=(780, 280), resizable=True)
        window.close()
        window = new_window

    if event == "Nnext":
        if abs(curr_player - len(data['players'])) < 5:
            curr_player += 5
        while curr_player < len(data['players']):
            curr_player += 5
        curr_player += -5
        table = func.prev_page(curr_player)
        new_window = sg.Window("Table", func.update_layout(table), size=(780, 280), resizable=True)
        window.close()
        window = new_window

    if event == 'ADD':
        func.add_player()
        curr_player += -5
        if curr_player < 0:
            curr_player += 5
        data = func.get_data()
        table = func.next_page(curr_player)
        new_window = sg.Window("Table", func.update_layout(table), size=(780, 280), resizable=True)
        window.close()
        window = new_window


window.close()

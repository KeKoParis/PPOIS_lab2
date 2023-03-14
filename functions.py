import PySimpleGUI as sg
import json


def curr_player_data(data):
    player = [data['name'], data['year'], data['club'], data['town'],
              data['team'], data['position']]
    print(player)
    return player


def get_data():
    with open("data.json") as file:
        data = json.load(file)
        file.close()
    return data


def next_page(curr_player):
    data = get_data()
    j = 0
    rows = []
    if curr_player + 1 >= len(data['players']):
        curr_player += -5

    for i in data['players']:
        if curr_player < j < curr_player + 6 and j < len(data['players']):
            rows.append(curr_player_data(i))
        j += 1
    print(rows)
    toprow = ['Name', 'Year of birth', 'Football club', 'Hometown', 'Team', 'Position']
    table = sg.Table(values=rows, headings=toprow, auto_size_columns=True,
                     display_row_numbers=False,
                     justification='center', key='-TABLE-', )
    return table


def window_find():
    input_find = sg.Input('Name or Club or Team', enable_events=True, key='-INPUT-', expand_x=True,
                          justification='left')
    additional_input = sg.Input('Year or Town or Position', enable_events=True, key='-ADDIT-', expand_x=True,
                                justification='left')
    button_find = sg.Button(button_text="Find", key='-Find-')
    layout = [[input_find], [additional_input], [button_find]]
    window = sg.Window("Find", layout, size=(550, 90), resizable=True)

    while True:
        event, values = window.read()
        if event == '-Find-':
            first_val = values['-INPUT-']
            second_val = values['-ADDIT-']
            print(second_val)
            find(first_val, second_val)

        if event == sg.WIN_CLOSED:
            break


def find(first_val, second_val):
    player_data = ""
    check = 0
    data = get_data()
    for i in data['players']:
        if i['name'].find(first_val) != -1 and i['year'] == second_val:
            player_data += i['name'] + " " + i['year'] + " " + i['club'] + " " + i['town'] + " " + \
                           i['team'] + " " + i['position'] + "\n"
            check = 1
            sg.popup(player_data)
            break
        if i['club'] == first_val and i['town'] == second_val:
            player_data += i['name'] + " " + i['year'] + " " + i['club'] + " " + i['town'] + " " + \
                           i['team'] + " " + i['position'] + "\n"
            check = 1
            sg.popup(player_data)
            break
        if i['team'] == first_val and i['position'] == second_val:
            player_data += i['name'] + " " + i['year'] + " " + i['club'] + " " + i['town'] + " " + \
                           i['team'] + " " + i['position'] + "\n"
            check = 1
            sg.popup(player_data)
            break
    if check == 0:
        sg.popup('No Data')


def window_delete():
    input_find = sg.Input('Name or Club or Team', enable_events=True, key='-INPUT-', expand_x=True,
                          justification='left')
    additional_input = sg.Input('Year or Town or Position', enable_events=True, key='-ADDIT-', expand_x=True,
                                justification='left')
    button_find = sg.Button(button_text="Delete", key='-Del-')
    layout = [[input_find], [additional_input], [button_find]]
    window = sg.Window("Delete", layout, size=(550, 90), resizable=True)

    while True:
        event, values = window.read()
        if event == '-Del-':
            first_val = values['-INPUT-']
            second_val = values['-ADDIT-']
            print(second_val)
            delete(first_val, second_val)

        if event == sg.WIN_CLOSED:
            break


def delete(first_val, second_val):
    check = 0
    data = get_data()
    for i in data['players']:
        if i['name'].find(first_val) != -1 and i['year'] == second_val:
            data['players'].remove(i)
            check = 1
            break
        if i['club'] == first_val and i['town'] == second_val:
            data['players'].remove(i)
            check = 1
            break
        if i['team'] == first_val and i['position'] == second_val:
            data['players'].remove(i)

            check = 1
            break
    if check == 0:
        sg.popup('No Data')

    with open('data.json', 'w') as file:
        data_json = json.dumps(data, indent=3)
        file.write(data_json)
        file.close()


def refresh_data():
    data = get_data()
    j = 0
    rows = []
    for i in data['players']:
        if j < 5:
            rows.append(curr_player_data(i))
        j += 1
    toprow = ['Name', 'Year of birth', 'Football club', 'Hometown', 'Team', 'Position']

    table = sg.Table(values=rows, headings=toprow, auto_size_columns=True,
                     display_row_numbers=False,
                     justification='center', key='-TABLE-', )


    return table

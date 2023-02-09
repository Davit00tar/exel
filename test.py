from cell import colors
from datetime import datetime

num_values = [0, None, -123, 123, 'a']
tests_for_cell= ['test_cell_get_value', 'test_cell_get_color', 'test_cell_to_int',
         'test_cell_to_float', 'test_cell_to_date', 'test_cell_reset']

tests_for_sheet = [ 'test_sp_get_cell_at',
         'test_add_row', 'test_add_col', 'test_swap_rows']

values_1 = [(1,2,0,-12), (0, 1, 2, 3, 4), (-1, 0, 123, None, 'asd'), ('asd', '00', 12, 123, -12),
          ('1200-02-02', '2001-12-11'), (0,) ]

values_2=[((2, 2, 2), (1, 0, 3), (3, 3, '1')), (1, 2, 3, ), (1, 0, 2), ((1, 2), (2,3))]


def run_tests_for_sheet(sheet):
    for test, test_value in zip(tests_for_sheet ,values_2):
        for  value in test_value:
            tester(test,sheet, value)

def run_tests_for_cell(cell):
    for test, test_value in zip(tests_for_cell ,values_1):
        for  value in test_value:
            tester(test,cell, value)

def tester(test_name, obj, *value):
    print(*value)
    if not isinstance(*value, tuple):
        if eval(test_name)(obj, *value):
            print(f'Test {test_name} passed successfully')
        else:
            print(f'Test {test_name} failed')
    else:
        if len(value) == 3:
            a, b, c = value
            if eval(test_name)(obj , a, b, c):
                print(f'Test {test_name} passed successfully')
            else:
                print(f'Test {test_name} failed')



def test_cell_get_value( cell, value):
    cell.set_value(value)
    return True if cell.get_value() == value else False


def test_cell_get_color(cell, color):
    cell.set_color(color)
    return True if cell.get_color() == colors[color] else False


def test_cell_to_int( cell, value):
    cell.set_value(value)
    try:
        cell.to_int()
    except:
        ValueError('Wrong format')
    return True if cell.get_value() == value else False


def test_cell_to_float(cell, value):
    cell.set_value(value)
    try:
        cell.to_float()
    except:
        ValueError('Wrong format')
    return  True if cell.get_value() == value else False


def test_cell_to_date(cell, value):
    cell.set_value(value)
    cell.to_date()
    return True if cell.get_value() == datetime.strptime(value, '%Y-%m-%d') else False


def test_cell_reset(cell, val):
    cell.reset()
    return  True if cell.get_value() == '' and cell.get_color() == 0 else False


def test_sp_get_cell_at(sheet, row, col, value):
    sheet.cells[row][col].set_value(value)
    return True if sheet.cells[row][col].get_value(value) == value else False


def test_add_row(sheet, row):
    cells = sheet.cells[row]
    sheet.add_row(row)
    return True if sheet.cells[row + 1] == cells else False


def test_add_col( sheet, col):
    sheet.cells = T(sheet.cells)
    test_add_row(sheet, col)


def test_swap_rows(sheet, row1, row2):
    row_ex_1 = sheet.cells[row1]
    row_ex_2 = sheet.cells[row2]
    sheet.swap_rows(row1, row2)
    return True if row_ex_1 == sheet.cells[row2] and row_ex_2 == sheet.cells[row1] else False


# Transpose
def T(lst):
    return [[row[i] for row in lst] for i in len(range(lst[0]))]



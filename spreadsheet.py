from cell import Cell

class Spreadsheet:
    def __init__(self, row = 3, col =3):
        if row > 1:
            self.row = row
        else:
            raise ValueError('The value must be bigger than 1')
        if col > 1:
            self.col = col
        else:
            raise ValueError('The value must be bigger than 1')
        self.cells = [[Cell() for j in range(self.col)] for i in range(self.row)]

    def set_cell_at(self, row, col, value):
        self.cells[row][col].set_value(value)

    def get_cell_at(self, row, col):
        return self.cells[row][col].get_value()

    def add_row(self, row):
        if 0 <= row <= self.row:
            self.row += 1
            self.cells.insert(row,[Cell() for i in range(self.col)])
        else:
            raise ValueError('Too long')


    def add_col(self, col):
        if 0 <= col <= self.col:
            self.col += 1
            for i in range(self.row):
                self.cells[i].insert(col, Cell())
        else:
            raise ValueError('Too long')

    def remove_row(self, row):
        self.cells.pop(row)
        self.row -= 1


    def remove_col(self, col):
        for i in range(self.row):
            self.cells[i].pop(col)
        self.col -= 1

    def swap_rows(self, row1, row2):
        self.cells[row1], self.cells[row2] = self.cells[row2], self.cells[row2]


    def swap_cols(self, col1, col2):
        for i in range(self.row):
            self.cells[i][col1], self.cells[i][col2] = self.cells[i][col2], self.cells[i][col1]



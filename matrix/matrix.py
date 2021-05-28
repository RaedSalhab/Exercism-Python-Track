class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def matrix_list(self):
        rows_str = self.matrix_string.split('\n')
        total_list = []
        for item in rows_str:
            sub_list = []
            str_list = item.split()
            for i in str_list:
                sub_list.append(int(i))
            total_list.append(sub_list)
        return total_list

    def row(self, index):
        row_list = self.matrix_list()
        if index <= len(row_list):
            return row_list[index-1]
        
    def column(self, index):
        column_list = []
        for item in self.matrix_list():
            if index <= len(item):
                column_list.append(item[index-1])

        return column_list


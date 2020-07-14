from app.models.User import User
from app.models.Domain import Domain
import xlrd
import datetime

class sheet():

    def __init__(self,io):
        self.fetch_xls_info(io)

    def read_cell(self,cell_obj,book=None):
        if cell_obj.ctype == 0:
            return ''
        elif cell_obj.ctype == 1:
            return cell_obj.value
        elif cell_obj.ctype == 2: # 数字，而且是浮点形式
            return str(int(cell_obj.value))
        elif cell_obj.ctype == 3: # 日期
            return datetime.datetime(*xlrd.xldate_as_tuple(cell_obj.value,book.datemode))
        elif cell_obj.ctype == 4:
            return 'True' if cell_obj.value else 'False'

    def fetch_xls_info(self,file_io):
        book = xlrd.open_workbook(file_contents=file_io.read())
        team_info = book.sheet_by_index(0)
        del file_io
        
        for i in range(1, team_info.nrows):
            cur_row = team_info.row(i)
            if cur_row[0].value !='':
                u = User.get_or_create(
                    name = self.read_cell(cur_row[0]),
                    user_id = self.read_cell(cur_row[1]),
                    password = self.read_cell(cur_row[2])
                )

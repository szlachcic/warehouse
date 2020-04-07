import xlsxwriter 


class Sheet():

    def __init__(self, name, description):

        self.file = xlsxwriter.Workbook('{}.xlsx'.format(name))
        self.worksheet = self.file.add_worksheet()

        self.worksheet.write('A1', name) 
        self.worksheet.write('B1', description) 

        self.worksheet.write('A2' , 'id') 
        self.worksheet.write('B2' , 'name') 
        self.worksheet.write('C2' , 'description') 
        self.worksheet.write('D2' , 'quantity')     
        self.worksheet.write('E2' , 'value') 
        self.worksheet.write('F2' , 'supplier') 
        self.worksheet.write('G2' , 'status') 
        self.worksheet.write('H2' , 'link')

        self.line=3

    def __del__(self):
        self.file.close() 

    def update(self, id, name, description, quantity, value, supplier, link="brak"):
        self.worksheet.write('A{}'.format(self.line) , id) 
        self.worksheet.write('B{}'.format(self.line) , name) 
        self.worksheet.write('C{}'.format(self.line) , description) 
        self.worksheet.write('D{}'.format(self.line) , quantity)     
        self.worksheet.write('E{}'.format(self.line) , value) 
        self.worksheet.write('F{}'.format(self.line) , supplier) 
        self.worksheet.write('H{}'.format(self.line) , link) 
         

        self.line+=1 
         

    
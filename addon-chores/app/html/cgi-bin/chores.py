#!/usr/bin/python
class chore_wheel:
    def __init__(self,db="/var/www/db/chores.sqlite"):
        import cgi
        self.input = cgi.FieldStorage()
        if self.input.getvalue('kid'):
            self.kid = self.input.getvalue('kid')
        else:
            self.kid = False
        self.db = db

    def getStub(self,stub):
        with open(stub) as Stub:
            return Stub.read()

    def getChores(self):
        if self.kid:
            SQL = f"""SELECT * FROM chores WHERE {self.kid}=1 ORDER BY id ASC"""
        else:
            SQL = """SELECT * FROM chores ORDER BY id ASC"""
        from sqlite import sqlite
        choreDB = sqlite(debug=True,logfile="/var/www/log/chores-debug.log")
        choreDB.open(db=self.db)
        cursor = choreDB.conn.cursor()
        cursor.execute(SQL)
        records = cursor.fetchall()
        return records

    def contentRow(self,record,item,stub,isDisabled=False):
        rep = f"#{str(item).upper()}#"
        repW = str(record).title()
        if record == 1:
            repW = "&#10004;"
        if record == 0:
            repW = "&#10060;"
        classNm = f"#{str(item).lower()}#"
        classNmW = f"{str(item).lower()}"
        if isDisabled:
            stub = stub.replace("class='chore'", "class='chore disabled'")
        stub = stub.replace(rep,repW)
        stub = stub.replace(classNm,classNmW)
        return stub
        
    def listChores(self,records,stub='/var/www/html/stub/chore.stub',inclDisabled=False):
        data = self.getStub(stub)
        items = ['id','category','name','description','Momma','Kenny','Megan','Logan','William','Ember','Disabled']
        content=""
        for record in records:
            if record[10] == 0 or inclDisabled:
                line = data
                n = 0
                while n <= (len(record)-1):
                    if record[10] == 1:
                        isDisabled = True
                    else:
                        isDisabled = False
                    line = self.contentRow(record[n],items[n],line,isDisabled=isDisabled)
                    n+=1
                content += line
        return content

    def getWheelItems(self,records,inclDisabled=False):
        wheelItems = []
        for record in records:
            if record[10] == 0 or inclDisabled == True:
                wheelItems.append(record[2])
        return wheelItems

    def getWheelContent(self,wheelItems,stub):
        repW = ""
        content=self.getStub(stub)
        for item in wheelItems:
            repW += f"{item}<br/>\n "
        content = content.replace("#WHEEL#",repW)
        return str(content)

    def populateWheelItems(self,wheelItems,stub):
        wheel = ""
        itemTemplate = self.getStub(stub)
        n = 1
        for item in wheelItems:
            wItem = itemTemplate
            fsize = 18
            if len(item) < 15:
                fsize = 24
            if len(item) < 10:
                fsize = 30
            if len(item) <= 5:
                fsize = 36
            bgcolor = "#000000"
            fcolor = "#7a7a7a"
            if (n % 2) == 0:
                bgcolor = "#a83232"
                fcolor = "#ffffff"
            wItem = wItem.replace("#CHORE#",str(item).upper())
            wItem = wItem.replace("#SIZE#",str(fsize))
            wItem = wItem.replace("#BG#",bgcolor)
            wItem = wItem.replace("#COLOR#",fcolor)
            wheel += f"{wItem}\n"
            n += 1
        return wheel

    def spinnerCanvas(self,wItems,stub,count):
        canvas = self.getStub(stub)
        pins = (count*2)
        canvas = canvas.replace("#ITEMS#",wItems)
        canvas = canvas.replace("#SEGMENTS#",str(count))
        canvas = canvas.replace("#PINS#",str(pins))
        return canvas

    def execute(self):
        records = self.getChores()
        header = self.getStub('/var/www/html/stub/choreHeader.stub')
        wheelItems = self.getWheelItems(records)
        count = len(wheelItems)
        canvasItems = self.populateWheelItems(wheelItems,'/var/www/html/stub/wheelItem.stub')
        canvas = self.spinnerCanvas(canvasItems,'/var/www/html/stub/canvas.stub',count)
        choreList = self.listChores(records,stub='/var/www/html/stub/chore.stub',inclDisabled=True)
        choreListHeader = self.getStub('/var/www/html/stub/choreListHeader.stub')
        footer = self.getStub('/var/www/html/stub/footer.stub')
        print("content-type:text/html\n\n")
        print(header)
        print(canvas)
        print(choreListHeader)
        print(choreList)
        print(footer)


def main():
    chwheel = chore_wheel()
    chwheel.execute()
main()

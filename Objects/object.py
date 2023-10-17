class Website:
    def __init__(self,title):
        self.title = title

    def showTitle(self):
        print(self.title)

obj = Website('pythonbasic')
obj.showTitle()

class location:
    def __init__(self,title):
        self.title = title

    def showLocation(self):
        print(self.title)

obj1 = location('another class checking')
obj1.showLocation()

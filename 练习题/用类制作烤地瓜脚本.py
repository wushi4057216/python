class Swatt():
    def __init__(self):
        self.cookedString = "生的"
        self.cookedLevel = 0
        self.condiments = []
    def __str__(self):
        return "地瓜状态:%s(%d),添加了%s佐料"%(self.cookedString,self.cookedLevel, self.condiments)
    def cook(self, cook_time):
        self.cookedLevel += cook_time

        if self.cookedLevel >=0 and self.cookedLevel <3:
            self.cookedString = "生的"
        elif self.cookedLevel >=3 and self.cookedLevel <5:
            self.cookedString = "半生不熟"
        elif self.cookedLevel >=5 and self.cookedLevel <8:
            self.cookedString = "熟的"
        elif self.cookedLevel >=8:
            self.cookedString = "糊了"
    def addCondiments(self, itms):
        self.condiments.append(itms)


digua = Swatt()

digua.cook(1)
print(digua)
digua.cook(2)
print(digua)
digua.addCondiments("大蒜"为
digua.cook(1)
print(digua)
digua.cook(2)
digua.addCondiments("盐")
print(digua)
digua.cook(2)
print(digua)
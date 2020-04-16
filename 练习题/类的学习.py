#定义一个类
class Cat:
    #初始化对象
    def __init__(self,new_name,new_age):
        self.name = new_name
        self.age = new_age
    def __str__(self):
        return "%s的年龄是：%d"%(self.name,self.age)

    def eat(self):
        print("猫在吃鱼")
    def drink(self):
        print("猫在喝水")

    def introduce(self):
        print("%s的年龄是%d"%(self.name,self.age))
#创建一个类的对象
tom = Cat("汤姆", 40)
#调用对象的方法
tom.drink()
tom.eat()

tom.introduce()#调用类的属性第二种方法

#创建多个对象
lanmao = Cat("蓝猫", 10)

lanmao.introduce()ss试试
print(tom)
print(lanmao)
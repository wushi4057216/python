class Person(object):
    '''人的类'''
    def __init__(self, name):
        super(Person,self).__init__()
        self.name = name
        self.gun = None
        self.hp =100

    def __str__(self):
        if self.gun:
            return "%s的血量为%d,他有%s"%(self.name,self.hp,self.gun)
        else:
            if self.hp > 0:
                return "%s的血量为%d,他没有枪"%(self.name,self.hp)
            else:
                return "%s血量为0,他死了"%self.name

    def anzhuang_zidan(self,dan_jia_temp, zi_dan_temp):
        dan_jia_temp.baocun_zidan(zi_dan_temp)

    def anzhuang_danjia(self,gun_temp,danjia_temp):
        gun_temp.baocun_danjia(danjia_temp)
    def naqiang(self,gun_temp):
        self.gun = gun_temp
    def kou_ban_ji(self,diren):
        self.gun.fire(diren)
    def diaoxue(self, zidan_weili):
        self.hp -= zidan_weili

class Gun(object):
    ''''枪类'''
    def __init__(self, name):
        super(Gun, self).__init__()
        self.name = name
        self.danjia = None

    def __str__(self):
        if self.danjia:
            return "枪的信息为%s,%s"%(self.name, self.danjia)
        else:
            return "枪的信息为%s,枪里没有弹夹"%(self.name)
    def baocun_danjia(self, dan_jia_temp):
        self.danjia = dan_jia_temp
    def fire(self, diren):
        zidan_temp = self.danjia.tanchu_zidan()
        if zidan_temp:
            zidan_temp.dazhong(diren)

class Danjia(object):
    ''''弹夹类'''
    def __init__(self, max_num):
        super(Danjia, self).__init__()
        self.max_num = max_num
        self.zidan_list = []

    def __str__(self):
        return "弹夹的信息为%d/%d"%(len(self.zidan_list),self.max_num)

    def baocun_zidan(self, zidan_temp):
        self.zidan_list.append(zidan_temp)

    def tanchu_zidan(self):
        if self.zidan_list:
            return self.zidan_list.pop()
        else:
            return None

class Zidan(object):
    ''''子弹类'''
    def __init__(self, zidan_weili):
        super(Zidan, self).__init__()
        self.zidan_weili = zidan_weili
    def dazhong(self, diren):
        diren.diaoxue(self.zidan_weili)


class main():
    ''''控制整个流程'''
    laowang = Person("老王")
    laoli = Person("老李")
    AK47 = Gun("AK47")
    dan_jia = Danjia(20)

    for i in range(15):
        zi_dan = Zidan(10)
        laowang.anzhuang_zidan(dan_jia, zi_dan)
    laowang.anzhuang_danjia(AK47, dan_jia)
    laowang.naqiang(AK47)
    for i in range(11):
        laowang.kou_ban_ji(laoli)
        print(laowang)
        print(laoli)




if __name__ == '__main__':
    main()


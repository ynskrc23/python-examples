class Person:
    def __init__(self, isim, yas, unvan, maas, birim):
        self.isim = isim
        self.yas = yas
        self.unvan = unvan
        self.maas = maas
        self.birim = birim

    def bilgi(self):
        print("İsminiz {} Yaşınız {} Ünvanınız {} Aldiğınız maaş {} TL Görev yaptığınız birim {}".format(self.isim, self.yas, self.unvan, self.maas, self.birim))

    def prim(self):
        yeni_maas = self.maas * 1.25
        print("yeni maaş: {} TL".format(yeni_maas))

person1 = Person("ali veli", 25, "mühendis", 15000, "yazılım geliştirme")
person1.bilgi()
person1.prim()

class Cake:
    def __init__(self,name,kind,taste,additives,filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling

    def show_info(self):
        print('-'*30)
        print(f"Name: {(self.name).upper()}")
        print(f"Taste: {self.taste}")
        if len(self.additives) > 0:
            print(f"Additives: {self.additives}")
        if self.filling != "":
            print(f"Filling: {self.filling}")
        print('-' * 30)

    def set_filling(self,filling):
        self.filling=filling

    def add_additives(self,*args):
        for additive in args:
            (self.additives).append(additive)


cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '')

bakery_offer=[cake01,cake02,cake03]

cake02.set_filling('vanilla cream')
cake03.add_additives('coconut','cocoa powder')

print("Today in our offer:")
for cake in bakery_offer:
    cake.show_info()
class Cake:
    known_kinds=['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer=[]

    def __init__(self,name,kind,taste,additives,filling):
        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind='other'
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.bakery_offer.append(self)

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

cake02.set_filling('vanilla cream')
cake03.add_additives('coconut','cocoa powder')

print("Today in our offer:")
for cake in Cake.bakery_offer:
    cake.show_info()

print('Is cake01 of type Cake? (isinstance)', isinstance(cake01, Cake))
print('Is cake01 of type Cake? (type)', type(cake01) is Cake)
print('vars cake01', vars(cake01))
print('vars Cake?', vars(Cake))
print('dir cake01', dir(cake01))
print('dir Cake?', dir(Cake))
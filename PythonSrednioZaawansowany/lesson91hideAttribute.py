class Cake:
    known_kinds=['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer=[]

    def __init__(self,name,kind,taste,additives,filling,glutenFree):
        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind='other'
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.bakery_offer.append(self)
        self.__glutenFree=glutenFree

    def show_info(self):
        print('-'*30)
        print(f"Name: {(self.name).upper()}")
        print(f"Taste: {self.taste}")
        print(f"Gluten Free: {self.__glutenFree}")
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


cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream',False)
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '',False)
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '',True)

cake02.set_filling('vanilla cream')
cake03.add_additives('coconut','cocoa powder')

print("Today in our offer:")
for cake in Cake.bakery_offer:
    cake.show_info()

cake03._Cake__glutenFree=False
cake03.show_info()
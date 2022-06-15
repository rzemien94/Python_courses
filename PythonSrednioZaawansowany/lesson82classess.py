class Cake:
    def __init__(self,name,kind,taste,additives,filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling

cake1 = Cake('apple pie','cake','apple',['apple'],'')
cake2 = Cake('strawberry pie','cake','strawberry',['strawberry'],'')
cake3 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '')

bakery_offer=[cake1,cake2,cake3]

print("Today in our offer:")
for cake in bakery_offer:
    print(f"{cake.name}")
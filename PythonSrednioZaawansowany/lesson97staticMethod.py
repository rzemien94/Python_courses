import pickle
import glob

class Cake:
    known_kinds=['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer=[]

    def __init__(self,name,kind,taste,additives,filling,glutenFree,text=''):
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
        if self.kind == 'cake' or text=='':
            self.__text=text
        else:
            self.__text = ''
            print(f"Kind is different than Cake or text is text not an empty string")

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

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print("Kind is different than cake")

    text=property(__get_text, __set_text, None, "Text on the cake")

    def save_to_file(self,path):
        with open(path,'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path, 'rb') as f:
            new_cake = pickle.load(f)

        cls.bakery_offer.append(new_cake)
        return new_cake

    @staticmethod
    def get_bakery_files(path):
        return glob.glob(path + '/*.bakery')


cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream',False)
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '',False)
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '',True)

cake02.set_filling('vanilla cream')
cake03.add_additives('coconut','cocoa powder')

cake01.save_to_file(r'F:\Users\rzemi\Desktop\KursyPython\cake01.bakery')
cake02.save_to_file(r'F:\Users\rzemi\Desktop\KursyPython\cake02.bakery')

cake05 = Cake.read_from_file(r'F:\Users\rzemi\Desktop\KursyPython\cake01.bakery')
cake05.show_info()

print(Cake.get_bakery_files(r'F:\Users\rzemi\Desktop\KursyPython'))
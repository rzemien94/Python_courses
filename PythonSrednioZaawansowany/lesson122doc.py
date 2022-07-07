class Cake:
    """
    This is documentation of class Cake:
    classs Cake has atributes like:
    -name,
    -kind,
    -taste,
    -additives,
    -filling.
    """
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        """
        :param name:
        :param kind:
        :param taste:
        :param additives:
        :param filling:
        """
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    @property
    def full_name(self):
        """
        :return: Name of Cake and kind of Cake
        """
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)

help(Cake)
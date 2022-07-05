class NoDuplicates:
    def __init__(self):
        self.list=[]

    def __call__(self, *args):
        for arg in args:
            if arg not in self.list:
                self.list.append(arg)

my_no_dup_list=NoDuplicates()

print(my_no_dup_list.list)

my_no_dup_list.__call__('keyboard','mouse')
print(my_no_dup_list.list)

my_no_dup_list.__call__('keyboard','mouse','pendrive')
print(my_no_dup_list.list)

my_no_dup_list.__call__('charger','pendrive')
print(my_no_dup_list.list)
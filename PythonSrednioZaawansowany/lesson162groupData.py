import os, itertools

def scantree(path):
    for d in os.scandir(path):
        if d.is_dir():
            yield d
            yield from scantree(d.path)
        else:
            yield d


listing = scantree(r'F:\Users\rzemi\Desktop\KursyPython\Python_courses')
for l in listing:
    print(f'this is a dir {l}' if l.is_dir() else f'this is a file {l}', l.path)

listing = scantree(r'F:\Users\rzemi\Desktop\KursyPython\Python_courses')
listing = sorted(listing, key=lambda e: e.is_dir())

for is_dir, elements in itertools.groupby(listing, key=lambda e: e.is_dir()):
    print(f'there are {len(list(elements))} dirs' if is_dir else f'there are {len(list(elements))} files')
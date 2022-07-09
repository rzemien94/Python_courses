import os, requests

def gen_get_files(dir):
    for i in os.listdir(dir):
        yield(os.path.join(dir,i))

def gen_get_file_lines(filename):
    with open(filename,'r') as f:
        for l in f.readlines():
            yield(l.replace('\n',''))

def check_webpage(url):
    try:
        resp=requests.get(url)
        if resp.status_code ==200:
            return True
        else:
            return False
    except:
        return False


try:
    os.mkdir(r'F:\Users\rzemi\Desktop\KursyPython\links_to_check')
except:
    pass

with open(r'F:\Users\rzemi\Desktop\KursyPython\links_to_check\pl.txt', 'w') as f:
    f.write('http://www.wykop.pl/\n')
    f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
    f.write('http://www.demotywatory.pl')

with open(r'F:\Users\rzemi\Desktop\KursyPython\links_to_check\com.txt', 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')

for file in gen_get_files(r'F:\Users\rzemi\Desktop\KursyPython\links_to_check'):
    for line in gen_get_file_lines(file):
        print(f"{file} - {line} - {check_webpage(line)}")

import os,zipfile,requests

class FileFromWeb:
    def __init__(self,url,tmp_file):
        self.url=url
        self.tmp_file=tmp_file

    def __enter__(self):
        response=requests.get(self.url)
        with open(self.tmp_file,'wb') as f:
            f.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

with FileFromWeb("https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-zip-file.zip",r"F:\Users\rzemi\Desktop\KursyPython\eurofxref.zip") as ffw:
    with zipfile.ZipFile(ffw.tmp_file,'r') as z:
        a_file=z.namelist()[0]
        print(a_file)
        os.chdir(r"F:\Users\rzemi\Desktop\KursyPython")
        z.extract(a_file,'.',None)


import os, zipfile, requests,contextlib

class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def download_file(self):
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self

    def close(self):
        #if os.path.isfile(self.tmp_file):
        os.remove(self.tmp_file)

with contextlib.suppress(FileNotFoundError):
    with contextlib.closing(FileFromWeb('https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-zip-file.zip', r'F:\Users\rzemi\Desktop\KursyPython\euroxref1.zip')) as f:
        f.download_file()
        with zipfile.ZipFile(f.tmp_file, 'r') as z:
            a_file = z.namelist()[0]
            print(a_file)
            os.chdir('c:/temp')
            z.extract(a_file, '.', None)

        os.remove(f.tmp_file)

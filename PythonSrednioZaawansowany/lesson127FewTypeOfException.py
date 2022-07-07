import requests
import os
import shutil


def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
dir = r'F:\Users\rzemi\Desktop\KursyPython'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)

    save_url_to_file(url,tmpfile_path)
except ConnectionError as e:
    print(f"connection error occured: {e}")
except PermissionError as e:
    print(f"permission error occured: {e}")
except FileNotFoundError as e:
    rint(f"File cannot be found, error: {e}")
except Exception as e:
    print(f"exception: {e}")
else:
    print(f"file {tmpfile_path} successfullty saved")
finally:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)
    print("opperation cempleted")




import os
import zipfile

def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip.write(os.path.join(root, file))


if __name__ == '__main__':
    zip = zipfile.ZipFile('Python.zip', 'w')
    zipdir('c:\\Python27\\', zip)
    zip.close()
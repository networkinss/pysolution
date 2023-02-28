import os
import time


class Util:
    def __init__(self, path, file_extension=".json"):
        self.path = path
        self.file_extension = file_extension

    def readAllFiles(self):
        file_list = []
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(self.file_extension):
                    file_list.append(file)
        return file_list


    def readAllFilesReturnListWithFullPath(self):
        file_list = []
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(self.file_extension):
                    file_list.append(os.path.join(root, file))
        return file_list

    def readAllFilesReturnListWithFullPathAndName(self):
        file_list = []
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(self.file_extension):
                    file_list.append([os.path.join(root, file), file])
        return file_list

    def readAllFilesReturnListWithFullPathAndNameAndExtension(self):
        file_list = []
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(self.file_extension):
                    file_list.append([os.path.join(root, file), file, file.split('.')[-1]])
        return file_list

    def readAllFilesReturnListWithFullPathAndNameAndExtensionAndSize(self):
        file_list = []
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(self.file_extension):
                    file_list.append([os.path.join(root, file), file, file.split('.')[-1], os.path.getsize(os.path.join(root, file))])
        return file_list

    def readAllFilesReturnListWithFullPathAndNameAndExtensionAndSizeAndDate(self):
        file_list = []
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(self.file_extension):
                    file_list.append([os.path.join(root, file), file, file.split('.')[-1], os.path.getsize(os.path.join(root, file)), time.ctime(os.path.getmtime(os.path.join(root, file)))])
        return file_list

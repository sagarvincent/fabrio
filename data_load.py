import json
import os 


class data_loader():
    # define constructor to take in the path of data files
    def __init__(self,pathtofolder):

        # get the no. of files in the directory
        self.path = pathtofolder
        self.files = os.listdir(self.path)
        self.file_no = len(self.files)
        

    def load_data(self):

        self.data_list = []
        # iterate through the files2
        for file in self.files:
            file_dict = {}
            file = os.path.join(self.path,file)
            try:
                with open(file) as json_file:

                    data = json.load(json_file)
                    file_dict[file] = data
                    self.data_list.append(file_dict)
            except:
                print(f"The file {file} could not be opened. Either check that the file is available in the directory or make sure the read permissions is allowed.")

        return self.data_list
































import data_load
import os
import checker

cwd = os.getcwd()

# define the path to data
folder_path = '\data'
folder_path = str(cwd) + folder_path 

# create a data loader object and load data
data_loader = data_load.data_loader(folder_path)
data_list = data_loader.load_data()

# create a correction checker object
target = data_list.pop(len(data_list)-1)
checker = checker.checker(target)

# check if the data is correct
inc_face_no, correct_model = checker.check(data_list)

# output and print the feed back 






























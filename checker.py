import math


class checker():

    # the object is initialised with the target model data
    def __init__(self, target):

        # target data persists as long as the object persist
        tkey = list(target.keys())[0]
        self.target = target[tkey]

        # check the layers of the target model using a recursive function
        

    # function to check if the faces of the model are incorrect with respect to the target
    def face_check(self, attempt1):    
        faces = attempt1['faces']
        face_stats = []
        face_stats.append('volume')
        t_faces = self.target['faces']
        print(len(t_faces))
        print(len(faces))
        if len(faces) == len(t_faces):
            for face in range(len(faces)):

                a_face = faces[face]            
                t_face = t_faces[face]

                # compare the area & calculate the percentage difference
                a_area = a_face['area']
                t_area = t_face['area']

                per_dev_ar = [((t_area - a_area)/t_area)*100] 

                # calculate the dimension of the bounding box of area of attempt#
                bb_min_at = a_face['bbMin']
                bb_max_at = a_face['bbMax']
                dim_at = 0
                for i in range(3):
                    
                    dim_at1 = pow((bb_max_at[i] - bb_min_at[i]),2)
                    dim_at = dim_at + dim_at1
                dim_at = math.sqrt(dim_at)

                # calculate the dimension of the bounding box of area of target
                bb_min_tar = t_face['bbMin']
                bb_max_tar = t_face['bbMax']
                dim_tar = 0
                for i in range(3):
                    
                    dim_att = pow((bb_max_tar[i] - bb_min_tar[i]),2)
                    dim_tar = dim_tar + dim_att
                dim_tar = math.sqrt(dim_tar)

                # compare the dimension of two models & calculate the deviation from the target
                per_dev_ar.append(((dim_tar - dim_at)/dim_tar)*100)

                # append to array
                face_stats.append([per_dev_ar])
            else:
                face_stats = []
        
        return face_stats

    # function to check the correct model
    # <-- model is identified having least difference in volume -->
    def get_closest(self, file_stat):

        small_diff = 0
        i = 0
        min = 100
        correct_model = 0
        for each in file_stat:
            print(each)
            i = i + 1    
            if abs(each[0]-self.target['volume']) < min :
                min = abs(each[0]-self.target['volume'])
                correct_model = i
        
        return min, correct_model
            


    # correction checking function
    def check(self, files):

        # no. of faces incorrect with respect to target model
        inc_face_no = 0
        # percentage deviation of each face of the given attempt
        per_dev = []
        
        # create an array to store the stats of each model
        file_stats = []

        for file in files:
            print(type(file))
            key = list(file.keys())[0]
            file = file[key]
            face_stats = self.face_check(file)
            file_stats.append(face_stats)

        # get the no. of incorrect faces for each attempt
        correct_model = self.get_closest(file_stats)
        
        return inc_face_no, correct_model



























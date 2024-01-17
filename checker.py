import math
import misc


class checker():

    # the object is initialised with the target model data
    def __init__(self, target):

        # target data persists as long as the object persist
        tkey = list(target.keys())[0]
        self.target = target[tkey]

        # check the layers of the target model using a recursive function
        
    # function to check if the faces of the model are incorrect with respect to the target
    # [Returns - an array containing an array for each face, each of which gives the arial and dim deviation]
    def face_check(self, attempt1):    
        faces = attempt1['faces']
        t_faces = self.target['faces']
        face_stats = []
        face_stats.append(attempt1['volume'])
        
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
            pass
            # for face in range(len(faces)):
            #    face_stats.append([100,100])
    
        return face_stats

    # function to check the correct model
    # <-- model is identified having least difference in volume -->
    def get_closest(self, file_stat, file_attr):

        i = 0
        min = 0.0002
        vol_models = []
        correct_model = 0
        # shortlist based on volume difference
        for each in file_stat:
            i = i + 1    
            if abs(each[0]-self.target['volume']) < min :
                min = abs(each[0]-self.target['volume'])
                vol_models.append(i)

        # rank list based on face area error
        prim_prior = misc.attribute_sort(file_attr,1)
        sec_prior = misc.attribute_sort(file_attr,2)

        correct_model = misc.two_rank_selection(prim_prior,sec_prior)            
        
        return min, correct_model


    # function to calculate cumulative area and bbdim error
    def cum_error(self,no, face_stats):
        cum_error = [no,0,0]
        for i in range(1,len(face_stats)):
            face = face_stats[i]
            cum_error[1] =  cum_error[1] + face[0][0]
            cum_error[2] = cum_error[2] + face[0][1]
        return cum_error

    # correction checking function [Returns - inc_face_no, correct_model]
    def check(self, files):

        # create an array to store the stats of each model
        file_stats = []
        # create an array to store the attributes of each model
        file_attr = []

        fileno = 0
        for file in files:
            fileno= fileno + 1
            key = list(file.keys())[0]
            file = file[key]
            face_stats = self.face_check(file) # [Returns - a list with face stats]
            file_stats.append(face_stats)
            file_attr.append(self.cum_error(fileno,face_stats))
        # check if the list contains only one model.
        if len(file_stats) > 1:
            # get the no. of incorrect faces for each attempt 
            min,correct_model = self.get_closest(file_stats, file_attr) # [Input - list of list with face stats ]
        else:
            pass
        
        return  correct_model, min



























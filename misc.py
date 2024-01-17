



######## ------ Miscellaneous functions ------ #########

# function select a winner from a priority list and secondary list.
def two_rank_selection(list1,list2):

    # pointers to traverse along the lists [O(n^3)]
    pointer1 = 0
    pointer2 = 0
    while(pointer1 < len(list1)):
        for p1 in range(pointer1):
            for p2 in range(pointer2):
                if list1[p1][0] == list2[p2][0]:
                    return list1[p1][0]                
        pointer1 = pointer1 + 1
        pointer2 = pointer2 + 1

    return list1[0]


# function to sort based on indexed-attribute
def attribute_sort(elem_list, attr_ind):

    for _ in range(len(elem_list)):
        for i in range(1,len(elem_list)):
            elem1 = elem_list[i-1]
            elem2 = elem_list[i]
            elem1_att = elem1[attr_ind]
            elem2_att = elem2[attr_ind]
            if elem1_att > elem2_att:
                temp = elem1
                elem_list[i-1] = elem2
                elem_list[i] = temp
    
    return elem_list


def check_length(list1):

    for i in range(len(list1)):

        count = 0
        model = 0
        if len(list1[i])>1:
            count = count + 1
            model = i+1
        
    if count >1:
        return True,model
    else: 
        return False, model














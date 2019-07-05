list1=[5,4,3,2,1]
list2=[9,8,7,6,10]

def addlist(list1,list2):
    
    result = [] 
    for i in range(0, len(list1)): 
        result.append(list1[i] + list2[i]) 
    return result


print(addlist(list1,list2))
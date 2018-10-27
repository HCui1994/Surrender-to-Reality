shit = []
def perm(list, begin, end):  
    global shit  
    if begin>=end:  
        shit.append(list)
    else:  
        i=begin  
        for num in range(begin, end):  
            list[num], list[i]= list[i], list[num]  
            perm(list, begin+1, end)  
            list[num], list[i] = list[i], list[num]  

list=[1, 2, 3, 4]  
perm(list, 0, len(list))  
print(shit)
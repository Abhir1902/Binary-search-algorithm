def binary_search(l,k):
    if(l[len(l)//2]==k):
        return len(l)//2
    else:
        if(k>len(l)//2):
            return binary_search(l[len(l)//2:],k)
        elif(k<len(l)//2):
            return binary_search(l[:len(l)//2],k)
        else:
            return -1
t=binary_search([2,3,6,7,7,8,8,8,12],8)
print(t)

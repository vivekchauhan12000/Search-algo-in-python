def LinearSearch(lys, element):
    for i in range (len(lys)):
        if lys[i] == element:
            return i
    return -1


print(LinearSearch([23,34,445,5454,4525,45252,42525,24525,25425,2,25,524,252,25,452,2525,522,454,4224,243524,1],2))
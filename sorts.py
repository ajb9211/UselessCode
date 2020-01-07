import random

##############################################################
# stalinSort: fast, lossy (yes the sorting algorithm is lossy#
# bogoSort: O(n!), lossless, why                             #
# assumptionSort: very fast, normally wrong                  #
# ajbSort: very fast, redefines useless                      #
# miracleSort: either very fast, or infinitely slow          #
##############################################################

##Generic check if list is ordered
def isOrdered(lst):
    mx = lst[0]
    for item in lst:
        if item < mx:
            return(False)
        mx = item
    return(True)

##Dumb sorting algorithms
def stalinSort(lst): ##Don't add an item to the output if it's too low
    out = []
    mx = 0
    for item in lst:
        if item >= mx:
            out.append(item)
            mx = item
    return(out)

def bogoSort(lst): ##Shuffle and hope
    i = 0
    while not isOrdered(lst):
        random.shuffle(lst)
        i += 1
    return([lst,i])

def assumptionSort(lst): ##You say it's sorted, then it is, right?
    return(lst)
        
def ajbSort(lst): ##Well, it might be sorted...? I hope...?
    random.shuffle(lst)
    return(lst)

def miracleSort(lst):
    while not isOrdered(lst):
        kst = lst
    return(lst)

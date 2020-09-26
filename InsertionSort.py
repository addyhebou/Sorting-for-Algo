A = [50, 30, 20, 15, 10, 8, 16]

def sort(lst):
    for key in range(len(lst)):
        currVal = lst[key]
        target = key - 1
        while (currVal < lst[target] and target != 0):
            lst[target + 1] = lst[target];
            target -= 1
        # if (target != 0):
        #     lst[target + 1] = currVal
        # else:
        #     lst[target] = currVal
    
    print lst

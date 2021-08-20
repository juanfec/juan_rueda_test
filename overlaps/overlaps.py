import random
# this function gets two intervals as parameters and returns true if the 
# intervals overlaps false if they dont ex: (1,2) , (3,4) 
# returns false this function only works with int numbers
# a solutions that allows float numbers can be easily 
# implemented by checking the limits with <, > and = 
# operators but by default this is the simplest solution
def overlaps(interval1, interval2):
    #first we check if the ranges are in the right order
    interval1 = sorted(interval1)
    interval2 = sorted(interval2)
    range1 = list(range(interval1[0],interval1[1]+1))
    range2 = list(range(interval2[0],interval2[1]+1))
    if range1[-1] in range2 or  range1[0] in range2 or  range2[0] in range1:
        return True
    else:
        return False
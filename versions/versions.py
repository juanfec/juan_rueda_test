# check to strings that represent version numbers and finds the greatest,
# 'equals' if they are the same version or 'Invalid Format' 
# example: “1.2” is greater than “1.1”. 
# for reusability this function just returns the version number or the word equals
# if a more elaborated answer is needed an interface would be usefull
def versions(version1, version2):
    try:
        #first we get a list of the integers that make up the version
        list1 = list(map(int,version1.rsplit('.')))
        list2 = list(map(int,version2.rsplit('.')))
        #then we look for diferences in three cases
        # when they are the same size and when one version
        # has more digits than the other one
        # the only way to versions can be equal is when they have the 
        # same amount of digits, this can change based on
        # business logic 
        if len(list1) < len(list2):
            for index , i in enumerate(list1):
                if(i>list2[index]):
                    return version1
                elif(i<list2[index]):
                    return version2
            return version2
        elif len(list1) > len(list2):
            for index , i in enumerate(list2):
                if(i>list1[index]):
                    return version2
                elif(i<list1[index]):
                    return version1
            return version1
        else:
            for index , i in enumerate(list1):
                if(i>list2[index]):
                    return version1
                elif(i<list2[index]):
                    return version2
            return 'Equals'
    except ValueError:
        return 'Invalid Format'
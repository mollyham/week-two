def FIZZBUZZ(list1, list2):
    Total_length=len(list1) +len(list2)
    if Total_length% 3==0:
        print("FIZZ")
       # return("FIZZ")
    elif Total_length% 5==0:
        print("BUZZ")
        # return("BUZZ")
    else:    
        print(Total_length)
        return FIZZBUZZ

if __name__ == '__main__':
    list1=[int(x) for x in input("Enter your 1st list of numbers with spaces: ").split()]
    list2=[int(x) for x in input("Enter your 2nd list of numbers with spaces: ").split()]
    FIZZBUZZ(list1, list2)  
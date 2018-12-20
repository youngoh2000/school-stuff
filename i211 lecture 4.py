##lesson 4
##
##def valid_pass():
##    ##while loop
##    while True:
##        my_pass = input("Please enter a password: ")
##        ##check if the string is at least 8
##        if len(my_pass) >= 8:
##            ##ends the loop and prints answer
##            return my_pass
##        else:
##            print("That was a not a valid passowrd, please try again")
##            ##if the password is less than 8 then the function valid_pass() runs again
##
###MAIN
##my_pass = valid_pass()
##print("Your valid password is:", my_pass)
#######
####

############3

def dictionary(listA):
    dic = {}
    ##individual numbers
    for num in listA:
        ##if numbers in dic
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    return dic
    


##main
listA = [1,1,1,2,2,2,2,2,4,3,3,3,3,3,3]

print(dictionary(listA))
for key,value in dictionary(listA).items():
    print(key)
    print(value)
    

##key is 1;; values is the count 

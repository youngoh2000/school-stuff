import os

def directory_choice():
    #this function should print out
    #all of the available directories
    #in the current working directory
    #then ask the user to choose one
    #and return it
    print(os.getcwd())
    documents = (os.listdir(os.getcwd()))
    print()
    lst = []
    for i in documents:
        if os.path.isdir(i):
            lst.append(i)
##        if "files" in i:
##            lst.append(i)

    while True:
        user = input("Please select a directory: ")
        if user in lst:
            print("Yes")
            return user
            break
        else:
            print("that is not valid")
    pass

def print_files():
    #write code in this function
    #to print all the files
    #but not directories
    #in the current working directory
    documents = (os.listdir(os.getcwd()))
    print()
    lst = []
    for i in documents:
        if os.path.isdir(i):
            lst.append(i)
##        if "files" in i:
##            lst.append(i)

    while True:
        user = input("Please select a directory: ")
        if user in lst:
            ##change address
            path = os.path.join(os.getcwd(), user)
            os.chdir(path)
            emLst = []
            doc = (os.listdir(os.getcwd()))
##            print(doc)
            for i in doc:
                if os.path.isfile(i):
                    emLst.append(i)
            return emLst       
            
            break
        else:
            print("that is not valid")
    pass
    
#main section


#call directory_choice

#change to that directory

#call print_files


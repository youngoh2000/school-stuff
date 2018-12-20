def squares(num):
    square = [num**2 for num in range(0,num+1)]
    return square


#main
print(squares(10))

print()


##Divisible by
##use list comprehensions to mimic this exchange:
def divisibleBy():
    lowerInput = eval(input("Please enter a lower bound (int): "))
    upperInput = eval(input("Please enter an upper bound(int): "))
    divideInput = eval(input("Please enter a number to divide by (int): "))
    divisible = [num for num in range(lowerInput, upperInput+1) if num % divideInput == 0]
    print(divisible)

##Two Vowels
file = [line.strip() for line in open("words.txt", "r")]
def vowels():
    vowel = ["aeiou"]
    count = 0
    vowelList = []
    for word in file:
        for vowel in word:
            count += 1
            if count >= 2:
                vowelList.append(word)
                break
    print(vowelList)
##    words = [word for word in file if word.count(vowel)]
##    print(words)


##two_v_words = word for word in all_words \ if len([let for let in word if let in "aeiou"]) >= 2]


##vowel 2
all_words = [word.strip() for word in open("words.txt", "r")]
two_v_words = [word for word in all_words \
               if len([let for let in word if let in "aeiou"]) >= 2]
print("All words in file: :", all_words)
print("The words that have more than 2 vowels: ", two_v_words)

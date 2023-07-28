str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = str1.lower()
str2 = str2.lower()

if (len(str1) == len(str2)):
    str1_sort = sorted(str1)
    str2_sort = sorted(str2)

    if (str1_sort == str2_sort):
        print("The strings " + str1 + " and " + str2 + " are anagram")
    else:
        print("The strings " + str1 + " and " + str2 + " are not an anagram")   

else:
    print("The strings " + str1 + " and " + str2 + " are not an anagram")

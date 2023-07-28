def get_permutations(str, i=0):
    if i == len(str):
        print("".join(str))

    for j in range(i,len(str)):

        words = [c for c in str]

        words[i], words[j] = words[j], words[i]
        get_permutations(words, i+1)

print(get_permutations("cpu"))        

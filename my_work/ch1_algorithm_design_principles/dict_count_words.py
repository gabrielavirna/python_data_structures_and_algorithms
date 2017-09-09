
def wordcount(fname):
    try:
        fhand = open(fname)
    except:
        print("File cannot be opened")
        exit()

    count = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
    return count


count = wordcount("dict_input.txt")
filtered = {key:value for key, value in count.items() if value < 20 and value > 15}


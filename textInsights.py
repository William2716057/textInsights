#count distinct words

def count_distinct(filename):
    file = open(filename, 'r')
    read_file = file.read().lower()
    words_in_file = read_file.split()
    
    count_map = {}
    for i in words_in_file:
        if i in count_map:
            count_map[i] += 1
        else:
            count_map[i] = 1
    
    count = 0
    
    for i in count_map:
        if count_map[i] == 1:
            count += 1
    file.close()
    return count

text_sample = "sample.txt"

count_number = count_distinct(text_sample)

print(f"There are {count_number} distinct words in the sample")
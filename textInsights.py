#count distinct words

def count_distinct(filename):
    file = open(filename, 'r')
    read_file = file.read().lower()
    words_in_file = read_file.split()
    
    #counts = []
#loop count words in file
#add to counts
#if word already in counts do not add to counts
#else add to counts

text_sample = "sample.txt"

count_number = count_distinct(text_sample)

print(f"There are {count_number} distinct words in the sample")
count_number = count_distinct(text_sample)

print(f"There are {count_number} distinct words in the sample")
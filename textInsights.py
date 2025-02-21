#total word count 


#count distinct words
def count_distinct(filename):
    with open(filename, 'r') as file:
    #to lower to count cases as same word
        read_file = file.read().lower()
    #split by whitespace
        words_in_file = read_file.split()
    
    #set cont perform check 
        distinct_words = set(words_in_file)

    return len(distinct_words)
text_sample = "sample.txt"

count_number = count_distinct(text_sample)
if count_number == 1:
    print(f"There is {count_number} distinct word in the sample")
if count_number > 1:
    print(f"There are {count_number} distinct words in the sample")
if count_number == 0:
    print("No words found in sample")
#else: 
    #print("No words or something else went wrong")
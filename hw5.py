import string
import csv
import json
import pickle

def main(filename):   
    textfile = open(filename)
    lines = textfile.read().split()
    all_words = []
    for line in lines:
        words =  line.split()        
        for word in words:           
            word = word.strip(string.punctuation)           
            if len(word)>0:            
                all_words.append(word)
    from collections import Counter
    counter = Counter(all_words)
    
    with open("wordcount.csv","w",newline='') as csv_file:
        writer = csv.writer(csv_file)
        head = ['word', 'count']
        writer.writerow(head)
        for elements, value in counter.most_common():
            writer.writerow([elements, str(value)])
   
    j = json.dumps(counter.most_common())
    with open("wordcount.json","w") as json_file:
        json_file.write(j)

    with open("wordcount.pkl","wb") as pickle_file:
        pickle.dump(counter, pickle_file)

if __name__ == '__main__':
    main("i_have_a_dream.txt")
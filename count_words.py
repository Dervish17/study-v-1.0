import cProfile
from collections import Counter



def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        word_counts = Counter(words)
        return word_counts




file_path = 'file.txt'


cProfile.run('count_words(file_path)')

def count_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read().split()
        unique_words = {}
        for word in content:
            if word in unique_words:
                unique_words[word] += 1
            else:
                unique_words[word] = 1
        return unique_words

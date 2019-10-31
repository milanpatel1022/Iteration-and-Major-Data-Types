#Submitter: patelmj1(Patel, Milan)
#Partner: rashidf(Rashid, Faizan)
#We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody
from goody import irange
import prompt
from random import choice


# For use in read_corpus: leave unchanged in this file
def word_at_a_time(file : open):
    for line in file:
        for item in line.strip().split():
                yield item


def read_corpus(os : int, file : open) -> {(str):[str]}:
    dct = {}
    i = word_at_a_time(file)
    os_words = [next(i) for word in range(os)]
    while True:
        try:
            os_words.append(next(i))
        except:
            break
        else:
            if tuple(os_words[:-1]) not in dct.keys():
                dct[tuple(os_words[:-1])] = [os_words[-1]]
            else:
                if os_words[-1] not in dct[tuple(os_words[:-1])]:
                    dct[tuple(os_words[:-1])].append(os_words[-1])
            os_words.pop(0)
    return dct


def corpus_as_str(corpus : {(str):[str]}) -> str:
    text = ''
    max_min_lst = []
    for key in sorted(corpus):
        text += '  %s can be followed by any of %s\n' %(key, corpus[key])
        max_min_lst.append(corpus[key])
    text += 'max/min list lengths = %s/%s\n' %(max([len(lst) for lst in max_min_lst]), min([len(lst) for lst in max_min_lst]))
    return text
    


def produce_text(corpus : {(str):[str]}, start : [str], count : int) -> [str]:
    most_recent_n_words = [start[0], start[1]]
    generated_words = [start[0], start[1]]
    while len(generated_words) < count + 2:
        if corpus.get(tuple(most_recent_n_words)) == None:
            generated_words.append(None)
            return generated_words
        else:
            random_word = choice(corpus[tuple(most_recent_n_words)])
            generated_words.append(random_word)
            most_recent_n_words.append(random_word)
            most_recent_n_words.pop(0)
    return generated_words




        
if __name__ == '__main__':
    # Write script here
    os = prompt.for_int('Select an order statistic', is_legal = lambda x: x>0, error_message= 'Not a valid number. Try again')
    file_to_read = goody.safe_open('Select the file name to read', 'r', 'File cannot be opened')
    corpus = read_corpus(os, file_to_read)
    text = corpus_as_str(corpus)
    print(text)
    print('Select 2 words for start of list')
    word1 = prompt.for_string('Select word 1', is_legal = (lambda x: x in text), error_message= 'Not a valid word')
    word2 = prompt.for_string('Select word 2', is_legal = (lambda x: x in text), error_message= 'Not a valid word')
    words_to_add = prompt.for_int('Choose # of words for appending to list', is_legal = (lambda x: x >= 0), error_message= 'Not a valid number')
    random_text = produce_text(corpus, [word1, word2], words_to_add)
    print('Random text = %s' %(random_text))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()

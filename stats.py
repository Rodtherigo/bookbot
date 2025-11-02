def count_words(book):
    num_of_words = book.split()
    num_of_words = len(num_of_words)
    return num_of_words

def count_characters(book):
    result = dict()
    counter = 0
    book = book.lower()
    for char in book:
        result[char] = 0 # create dict
    list_of_keys = list(result.keys()) # list of dict keys
    for key in list_of_keys: # for each key how many are there in text?
        for char in book:
            if char == key: counter += 1
        result[key] = counter
        counter = 0
    return result
    # result = {'t': 29493,'p': 5952,'c': 9011}

def sort_on(dictionary):
    return dictionary['num']

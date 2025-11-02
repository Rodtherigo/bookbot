from stats import count_words
from stats import count_characters
from stats import sort_on
import sys
import pprint

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    print(f'Analyzing book found at {filepath}')
    return file_contents
def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    print('============ BOOKBOT ============')
    book = get_book_text(filepath=f'{sys.argv[1]}') # use for submissions
    # book = get_book_text(filepath='./books/frankenstein.txt') # use for submissions
    # book = get_book_text(filepath='./bookboot/books/frankenstein.txt') # use for debugger
    
    word_count = count_words(book)
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    characters = count_characters(book)
    results = []
    for item in characters: # create list for sorting
        results.append({"char": item,"num":characters[item]})
    results.sort(reverse=True, key=sort_on) # sort on the 'num' key 
    print('--------- Character Count -------')
    for d in results:
        print(f'{d['char']}: {d['num']}')
    print('============= END ===============')
    
main()
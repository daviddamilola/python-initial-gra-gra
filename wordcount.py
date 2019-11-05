"""count the numbee of occurences of each word in a text file"""

import sys

def main():
    """count the words in a text file"""
    if len(sys.argv) < 2 :
        print('Usage: python wordcount <filename>')
        print('where filename is name of text file')
    else:
        filename = sys.argv[1]
        counters = {}
        with open(filename, 'r') as f:
            content= f.read()
            words = content.split()
            for word in words:
                word = word.upper()
                if word not in counters:
                    counters[word] = 1
                else:
                    counters[word] += 1
            for word, count in counters.items():
                print(word, count)


if __name__ == '__main__':
    main()


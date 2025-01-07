def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        count_words(file_contents)
        
def count_words(contents):
    words = contents.split()
    number_of_words = len(words)
    print(number_of_words)
main()
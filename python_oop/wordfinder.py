"""Word Finder: finds random words from a dictionary."""
import random # Used in the random method
path = '/Users/steveking/Desktop/Springboard/assignments/python_intro/python_oop/words.txt'
class WordFinder:
    ...
    def __init__(self, path):
        """Reads dictionary and reports # items read. Also creates a list of words."""
        words_file = open(path)
        self.words = []
        for line in words_file:
            self.words.append(line)
        print(f"{len(self.words)} words read")
        words_file.close() # Always make sure to close the file

    def random(self):
        """Return a random word."""
        print(random.choice(self.words))
        return random.choice(self.words)
    
# wf = WordFinder(path)
# wf.random()


class SpecialWordFinder(WordFinder):
    ...
    def __init__(self, path):
        super().__init__(path)
        self.special_words = []  # Create a list to store non-special words
        for word in self.words:
            word.strip()
            if not word.startswith("#") or word == "":
                self.special_words.append(word)
        print(f"{len(self.special_words)} words read")

# swf = SpecialWordFinder(path) 
# swf.random()
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
    
    def match(self, candidates):
        sorted_word = sorted(self.word)
        matches = [
            candidate for candidate in candidates
            if sorted(candidate.lower()) == sorted_word
            and candidate.lower() != self.word
        ]
        return matches

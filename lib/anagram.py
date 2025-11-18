class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, words):
        matches = []

        for candidate in words:
            candidate_lower = candidate.lower()

            
            if candidate_lower == self.word:
                continue

            if sorted(candidate_lower) == self.sorted_word:
                matches.append(candidate)

        return matches

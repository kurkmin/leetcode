class Solution:
    def reverseVowels(self, s: str) -> str:
        # USE TWO POINTERS

        # create vowel list
        vowels = ["a", "e", "i", "o", "u"]
        # check each char in the string is vowel
        # save the order in a new list
        saved = []
        for char in s:
            if char.lower() in vowels:
                saved.append(char)
        # iterate again to replace current vowels in the string
        newS = ""
        order = len(saved) - 1
        for i in range(len(s)):
            if s[i].lower() in vowels:
                newS += saved[order]
                order -= 1
            else:
                newS += s[i]
        return newS

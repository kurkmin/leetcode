class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # for loop to find a charater in a given word
        # to see if there is any character to match with
        # with the one provided (ch)
        newS = ""
        for i in range(len(word)):
            if word[i] == ch:
                right = i
                newS += word[right::-1]
                newS += word[right + 1 :]
                return newS
        return word

        # think about how two pointers can be implemented

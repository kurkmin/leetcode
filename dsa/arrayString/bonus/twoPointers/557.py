class Solution:
    def reverseWords(self, s: str) -> str:
        # 1. brute force method
        array = []
        test = s.split(" ")
        for i in test:
            arr = []
            a = len(i) - 1
            while a >= 0:
                arr.append(i[a])
                a -= 1
            temp = "".join(arr)
            array.append(temp)
        newS = ""
        for j in range(len(array)):
            newS += array[j]
            if j < len(array) - 1:
                newS += " "
        return newS

        # 2. Two pointer method to be added

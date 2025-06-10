class Solution(object):
    def lengthOfLastWord(self, s):
        word = s.split()[-1]
        print(len(word))    
        return len(word)
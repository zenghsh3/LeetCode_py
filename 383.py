class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_d = {}
        for i in xrange(len(magazine)):
            magazine_d[magazine[i]] = magazine_d.get(magazine[i], 0)
            magazine_d[magazine[i]] += 1

        ransomNote_d = {}
        for i in xrange(len(ransomNote)):
            ransomNote_d[ransomNote[i]] = ransomNote_d.get(ransomNote[i], 0)
            ransomNote_d[ransomNote[i]] += 1
    
        flag = True
        for x in ransomNote_d:
            if x not in magazine_d or magazine_d[x] < ransomNote_d[x]:
                flag = False
                break
        return flag
        

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        total1=0
        total2=0
        if len(s2)<len(s1):
            return False
        for i in range(len(s1)):
            total1+=ord(s1[i])-96
            total2+=ord(s2[i])-96
            print(ord(s1[i])-96,ord(s2[i])-96)
        if total1==total2:
            if set(s1)== set(s2[:len(s1)]):
                return True
        left=0;right=len(s1)-1
        while right<len(s2)-1:
            total2-=ord(s2[left])-96
            left+=1
            right+=1
            total2+=ord(s2[right])-96
            print(total1,total2)
            if total1==total2:
                if set(s1)!= set(s2[left:right+1]):
                    print(s1[i])
                    print(right)
                else:
                    return True
        return False
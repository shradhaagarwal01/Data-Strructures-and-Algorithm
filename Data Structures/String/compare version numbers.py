class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1 = [int(i) for i in version1.split(".")]
        s2 = [int(i) for i in version2.split(".")]
        l1, l2 = len(s1), len(s2)
        l = max(l1,l2)
        for i in range(l):
            if i<l1:
                v1 = s1[i]
            else:
                v1 = 0
            if i<l2:
                v2 = s2[i]
            else:
                v2 = 0
            if v1>v2:
                return 1
            elif v1<v2:
                return -1
        return 0
                

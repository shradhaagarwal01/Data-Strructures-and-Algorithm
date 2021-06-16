class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        def search(patt, s):
            n = len(s)
            m = len(patt)
            lps = [0]*m
            ans = []
            def table(patt):
                lps[0] = 0
                i = 1
                j = 0
                while(i<m):
                    if patt[i]==patt[j]:
                        j = j+1
                        lps[i] = j
                        i = i+1
                    else:
                        if j==0:
                            lps[i] = 0
                            i = i+1
                        else:
                            j = lps[j-1]

            i = 0
            j = 0
            table(patt)
            while i<n:
                if patt[j]==s[i]:
                    i = i+1
                    j = j+1
                if j==m:
                    ans.append(i-j)
                    j = lps[j-1]
                elif i<n and patt[j]!=s[i]:
                    if j!=0:
                        j = lps[j-1]
                    else:
                        i = i+1
            if ans:
                return ans[0]
            else:
                return -1
        return search(needle,haystack)


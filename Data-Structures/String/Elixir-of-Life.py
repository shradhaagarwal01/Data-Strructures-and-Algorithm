#Flamel is making the Elixir of Life but he is missing a secret ingredient, a set of contiguous plants (substring) from the Garden of Eden.
#The garden consists of various plants represented by string S, where each letter represents a different plant.  
#But the prophecy has predicted that the correct set of plants required to make the potion will appear in the same contiguous pattern (substring)
#at the beginning of the forest (prefix), the end of the forest (suffix), and will also be the most frequent sequence present in the entire forest.
#Identify the substring of plants required to make the elixir and find out the number of times it appears in the forest. 


class Solution:
    def maxFrequency(self, S):
        for length in range(1, len(S)):
            if S[:length] == S[len(S) - length:]:
                return S.count(S[:length])
        return 1

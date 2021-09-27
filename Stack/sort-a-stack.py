#Given a stack, the task is to sort it such that the top of the stack has the greatest element.

def sortedInsert(s, element):
    if len(s) == 0 or element < s[-1]:
        s.append(element)
        return
    else:
        temp = s.pop()
        sortedInsert(s, element)
        s.append(temp)
 
class Solution:
    def sorted(self, s):
        if len(s) != 0:
            temp = s.pop()
            self.sorted(s)
            sortedInsert(s, temp)

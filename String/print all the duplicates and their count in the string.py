def printDups(string): 
    d = {}
    for i in string:
        d[i] = d.get(i,0)+1
    for i in d:
        if d[i]>=2:
            print(i,d[i])
            

string = "test string"
printDups(string) 
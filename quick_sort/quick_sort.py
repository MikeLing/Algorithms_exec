pos = lambda i:i - 1
#inser = lambda a, i, j:a.insert(pos(i),a.pop(pos(j)))

class array_structure(list):

#put the smaller value front 
#which is "exchange A[i] with A[j]"
  
    def inser(self, i, j):
        self.insert(pos(i), self.pop(pos(j)))
    
    def length(self):
        return len(self)

    def exchange(self, i, r):
        self[pos(i)], self[pos(r)] = self[pos(r)] , self[pos(i)]
    
    def pos(self, i):
        return self[pos(i)]

#a is the array will be rearrange and you should put arguements like(A,1,len(a))
def quicksort(A, p, r):
    a = array_structure(A)
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q - 1)
        quicksort(a, q + 1,r)
        
        
def partition(a,p,r):
    x = a.pos(r)
    i = p
    for j in range(1, a.length() + 1):
        if a.pos(j) < x:
            i = i + 1
            a.inser(i, j)
    a.exchange(i + 1, r)
    return i + 1
    

import random,sys,os,time

def qSort(a,l,h,comp):
    if l>=h: return a, comp
    pivot = l  # Problem 1
    #pivot = h  # Problem 2
    #pivot = random.randint(l,h)  #using random pivot
    #pivot = (l+h)/2 # Problem 3
    #if((a[l]<a[pivot] and a[l]>a[h]) or (a[l]>a[pivot] and a[l]<a[h])): pivot = l
    #if((a[h]<a[pivot] and a[h]>a[l]) or (a[h]>a[pivot] and a[h]<a[l])): pivot = h
    #a[pivot], a[l] = a[l], a[pivot] 
    i=l
    for j in range(l+1,h+1,1):
            if a[j]<a[l]:
                    i=i+1
                    a,a[j] = a[j],a
    a[l],a = a,a[l]
    comp=comp+h-l
    
    a,comp=qSort(a,l,i-1,comp)
    a,comp=qSort(a,i+1,h,comp)
    return a,comp
        
def non_decreasing(L): 
    return all(x<=y for x, y in zip(L, L[1:]))

if __name__ == "__main__":
    st = time.time()
    if len(sys.argv)<2:
        inputList = open("QuickSort.txt").read().splitlines()
    else:
        inputList = open(sys.argv[1]).read().splitlines()
    IntArray = map(int, inputList)
    comps=0 
    (res, comps)=qSort(IntArray,0,len(IntArray)-1,comps)
    print "The # of comparison is \t %d" %(comps)
    print 'Use time:',time.time()-st
    if not non_decreasing(res):
        print "Incorrect sorted result"

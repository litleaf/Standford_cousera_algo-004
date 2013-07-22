import random,sys,time

def qSort(a,l,h,comp):
    ### a = array, l = low, h = high, comp = the number of comparisons
    if l>=h: return a, comp
    
    ## Problem 1
    #pivot = l
    
    ## Problem 2
    #pivot = h
    
    ## Problem 3
    pivot = (l+h)/2 
    if((a[l]<a[pivot] and a[l]>a[h]) or (a[l]>a[pivot] and a[l]<a[h])): pivot = l
    if((a[h]<a[pivot] and a[h]>a[l]) or (a[h]>a[pivot] and a[h]<a[l])): pivot = h    
    
    ## Problem bonus
    #pivot = random.randint(l,h)  #using random pivot
    
    a[pivot], a[l] = a[l], a[pivot] 
    i=l
    for j in range(l+1,h+1,1):
            if a[j]<a[l]:
                    i=i+1
                    a[i],a[j] = a[j],a[i]
    a[l],a[i] = a[i],a[l]
    comp=comp+h-l
    
    a,comp=qSort(a,l,i-1,comp)
    a,comp=qSort(a,i+1,h,comp)
    return a,comp
        
if __name__ == "__main__":
    st = time.time()
    if len(sys.argv)<2:
        inputList = open("QuickSort.txt").read().splitlines()
    else:
        inputList = open(sys.argv[1]).read().splitlines()
    IntArray = map(int, inputList)
    comps=0 
    (res, comps)=qSort(IntArray,0,len(IntArray)-1,comps)
    #print res
    print "The num of comparison is %d" %(comps)
    print 'Use time:',time.time()-st


def LIS(seq):
    '''uses dynamic programming to return longest increasing subsequence of input list seq'''

    n=len(seq)
    lengths=[1]*n

    # loop over sequence backwards
    for i in range(n-2,-1,-1):
        for j in range(i,n):
            if seq[j]>seq[i]:
                lengths[i]=max(lengths[i],1+lengths[j])

    # reconstruct subsequence
    length=max(lengths)
    subseq=[]
    i=0
    while len(subseq)<length:
        if lengths[i]==length-len(subseq):
            subseq.append(seq[i])
        i+=1

    return subseq


# test on a random list
import random
test_list=random.sample(range(1,50),20)
print("test sequence: "+str(test_list))
print("longest increasing subsequence: "+str(LIS(test_list)))

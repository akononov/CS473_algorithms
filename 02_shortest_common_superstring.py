import numpy as np

def SCS(A,B):
    '''uses dynamic programming to return shortest common superstring of two input strings A, B'''

    m=len(A)
    n=len(B)

    lengths=np.zeros((m+1,n+1), dtype=np.int)

    # base cases: last row and last column
    lengths[-1] = [n-j for j in range(n+1)]     # used up all of A; must end with remainder of B
    lengths[:,-1] = [m-i for i in range(m+1)]   # used up all of B; must end with remainder of A

    # general case
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):

            # if A and B share next character, use that character
            if A[i]==B[j]:
                lengths[i,j] = 1 + lengths[i+1,j+1]

            # otherwise, choose character from A or B which minimizes length
            else:
                lengths[i,j] = 1 + min(lengths[i+1,j], lengths[i,j+1])

#    print lengths

    # reconstruct superstring
    supseq=''
    length=lengths[0,0]
    i=0
    j=0

    # loop over characters in superstring
    for k in range(length):

        # if used up all of A, end with remainder of B
        if i==m:
            supseq+=B[j:]
            break

        # if used up all of B, end with remainder of A
        elif j==n:
            supseq+=A[i:]
            break

        # if A and B share next character, use that character
        elif A[i]==B[j]:
            supseq+=A[i]
            i+=1
            j+=1

        # otherwise, choose the one that minimizes length
        else:
            if lengths[i+1,j] <= lengths[i,j+1]:
                supseq+=A[i]
                i+=1
            else:
                supseq+=B[j]
                j+=1

    return supseq

# tests
print(SCS('superman','spider-man'))
print(SCS('dynamic','programming'))

import sys

class myAUx:
    def createAux(W):
    # initializing the array aux with 0's
        aux = [0] * len(W)

    # for index 0, it will always be 0
    # so starting from index 1
        i = 1
     # m can also be viewed as index of first mismatch
        m = 0
        while i < len(W):
        # prefix = suffix till m-1
           if W[i] == W[m]:
                m += 1
                aux[i] = m
                i += 1
        # this one is a little tricky,
        # when there is a mismatch,
        # we will check the index of previous
        # possible prefix.
           elif W[i] != W[m] and m != 0:
            # Note that we do not increment i here.
                m = aux[m-1]
           else:
            # m = 0, we move to the next letter,
            # there was no any prefix found which 
            # is equal to the suffix for index i
              aux[i] = 0
              i += 1

        return aux

W = "acabacacd"
T = "acfacabacabacacdkacabacacdacabacacd"
count = 0
# this method is from above code snippet.
aux = myAUx.createAux(W)

# counter for word W
i = 0
# counter for text T
j = 0
while j < len(T):
    # We need to handle 2 conditions when there is a mismatch
    if W[i] != T[j]:
        # 1st condition
        if i == 0:
            # starting again from the next character in the text T
            j += 1
        else:
            # aux[i-1] will tell from where to compare next
            # and no need to match for W[0..aux[i-1] - 1],
            # they will match anyway, that’s what kmp is about.
            i = aux[i-1]
    else:
        i += 1
        j += 1
        # we found the pattern
        if i == len(W):
            # printing the index
            print("found pattern at " + str(j - i))
            count+=1
            print(count)
            # if we want to find more patterns, we can 
            # continue as if no match was found at this point.
            i = aux[i-1]
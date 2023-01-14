def subsequence(ind,array,total):
    if ind >= len(array):
        print(total)
        return 
    
    subsequence(ind + 1,array,total)
    subsequence(ind + 1,array,total + [array[ind]])


if __name__ == '__main__':
    print(subsequence(0,[1,2,3,4],[]))
def mergeAlternately(word1, word2):
    temp=""

    min_parallel = min(len(word1),len(word2))

    for i in range(0,min_parallel):
        temp+=word1[i]+word2[i]
    combined=temp+word1[min_parallel:]+word2[min_parallel:]
    return combined

if __name__ == "__main__":
    print(mergeAlternately("abc","pqr"))
    print(mergeAlternately("ab","pqrs"))
    print(mergeAlternately("abcd","pq"))
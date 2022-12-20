import sys
word_list = [] # global variable that stores list of whole words
B = [] # global variable that stores probability that each word comes first
T = [] # global variable that stores probability that each word comes after the other
M = [] # global variable that stores probability that recognize each word to the other
max_prob = [] #cache variable
choices = [] #cahce variable

def original_sentence(n, m, words_index):
    global max_prob; global choices
    for j in range(m):
        max_prob[0][j] = B[j] * M[j][words_index[0]]
    for i in range(1, n):
        for j in range(m):
            max_index = 0; max = 0
            for k in range(m):
                temp = max_prob[i-1][k] * T[k][j] * M[j][words_index[i]]
                if temp>max:
                    max = temp
                    max_index = k
            max_prob[i][j] = max
            choices[i][j] = max_index

def reconstruct(n):
    max_value = max(max_prob[n-1])
    last_index = max_prob[n-1].index(max_value)
    answer_list = []
    answer_list.append(last_index)
    for i in range(n-1, 0, -1):
        answer_list.append(choices[i][answer_list[-1]])
    answer_list.reverse()
    answer_sentence = []
    for index in answer_list:
        answer_sentence.append(word_list[index])
    return " ".join(answer_sentence) 



def Original_sentence(n, m, sentence):
    global max_prob; global choices
    words_index = [] #list that stores index of words in given sentence
    for words in sentence:
        words_index.append(word_list.index(words))
    max_prob = [[-1 for i in range(m)] for j in range(n)]
    choices = [[-1 for i in range(m)] for j in range(n)]
    original_sentence(n, m, words_index)
    return(reconstruct(n))
    

if __name__ == "__main__":
    (m, q) = map(int, input().split())
    word_list  = list(map(str, sys.stdin.readline().rstrip().split()))
    B = list(map(float, sys.stdin.readline().rstrip().split())) 
    T = [list(map(float, sys.stdin.readline().rstrip().split())) for i in range(m)]
    M = [list(map(float, sys.stdin.readline().rstrip().split())) for i in range(m)]
    for i in range(q):
        temp_input = list(map(str, sys.stdin.readline().rstrip().split()))
        n = int(temp_input[0])
        sentence = temp_input[1:]
        print(Original_sentence(n, m, sentence))
    #import pdb; pdb.set_trace() 

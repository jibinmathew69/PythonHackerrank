if __name__ == '__main__':

    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        scores.append([name,score])


    scores = sorted(scores, key=lambda x: (x[1], x[0]))

    count = 1
    min = scores[0][1]
    while count<len(scores):
        if scores[count][1]!=min:
            score = scores[count][1]
            while count<len(scores) and scores[count][1] == score:
                print(scores[count][0])
                count+=1
            break
        count+=1
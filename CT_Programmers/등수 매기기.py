score = [[80, 70], [90, 50], [40, 70], [50, 80]]

def solution(score):
    st=[]
    answer = []
    for i in range(len(score)) :
        st.append(score[i][0]+score[i][1])
    for i in st:
        a=1
        for j in st:
            if i<j:
                a +=1
        answer.append(a) 
    return answer

print(solution(score))
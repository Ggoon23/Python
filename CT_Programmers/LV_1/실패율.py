def solution(N, stages):
    s=[stages.count(i)/len([j for j in stages if j>=i]) if len([j for j in stages if j>=i]) > 0 else 0 for i in range(1,N+1)]
    return [i+1 for i in sorted(range(N), key=lambda x: -s[x])]

N=5
stages=[2,1,2,6,2,4,3,3]

print(solution(N,stages))
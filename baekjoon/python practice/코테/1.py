def solution(id_list, report, k):
    n = len(id_list)
    answer = [0]*n

    report_matrix = list([list([0 for j in range(n)]) for i in range(n)])
    cnt = list([0 for i in range(n)])
    for X in report:
        X = X.split()
        fromID, toID = id_list.index(X[0]), id_list.index(X[1])
        cnt[toID] += 1 - report_matrix[fromID][toID]
        report_matrix[fromID][toID] = 1
    for i in range(n):
        if cnt[i] >= k:
            for j in range(n):
                if report_matrix[j][i] == 1:
                    answer[j] += 1
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
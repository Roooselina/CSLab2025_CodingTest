"""
Baekjoon #2644 촌수계산
- 알고리즘: BFS
    - 참고할 점: BFS는 queue를 통해 구현 (시작 노드의 인접 노드를 큐에 enqueue(append) > dequeue(popleft)하여 방문 처리하며 검사)

- 문제
우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 이러한 촌수는 다음과 같은 방식으로 계산된다. 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.
여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.

- 입력
사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다. 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다. 그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.

9 < 전체 사람 수
8 6 < 촌수를 계산해야 하는 사람 번호
7 < 부모 자식간 관계 수
1 2 < 2의 부모 1
1 3
2 7
2 8
2 9
4 5
4 6

각 사람의 부모는 최대 한 명만 주어진다.

- 출력
입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력해야 한다.

- 오답노트
    - 그래프를 제대로 정의하지 않아도 해결할 수 있을 것 같아서 1차원 그래프(자식 인덱스로 부모를 조회하는~)로 정리해봤는데 의미 없는 회전도 카운트하다보니 오류가 있는듯...
        - addflag를 통해서 큐에 값이 추가될 때만 length 값을 증가시켰는데 이 경우도 의미 없는 추가가 같이 카운트됨
        - 귀찮다고 flag를 늘리지 말고 알고리즘 자체의 문제를 찾아야 함
    - 뭔가 같은 스텝에 추가된 값에 대해선 length를 증가시키지 않게 하면 될 것 같은데,,, 그러려고 뭔가 더 넣고 싶진 않다
        - 현재 아이템을 빼고(popleft)난 후에 큐가 비어있는 경우에만 length를 증가 < 안됨, 그야 당연히... 꼭 마지막 경우 쪽으로만 가진 않으니까,,,
"""

from collections import deque

allp = int(input())
a, b = map(int, input().split())
n = int(input())
parent = [None] * allp
visited = [False] * allp

for _ in range(n):
    p, c = map(int, input().split())
    parent[c-1] = p

deq = deque([a])
visited[a-1] = True
length = 0
flag = False
while deq:
    curr = deq.popleft()
    if not deq: length += 1
    # curr의 부모 검사
    if not (visited[parent[curr-1]-1] if parent[curr-1]!=None else True):
        if parent[curr-1] == b:
            flag = True
            break
        deq.append(parent[curr-1])
        visited[parent[curr-1]-1] = True
    # curr의 자식 검사
    for i in range(allp):
        if parent[i] == curr and (not visited[i]):
            if i+1 == b:
                flag = True
                break
            deq.append(i+1)
            visited[i] = True
    if flag: break
    
print(length+1 if flag else -1)
# ------------------------------
# dfs
# ------------------------------
def promising(queens):
    l = len(queens)
    for i in range(l):
        for j in range(i+1, l):
            x_i, y_i = queens[i]
            x_j, y_j = queens[j]
            if not (x_i!=x_j and y_i!=y_j and abs((y_i-y_j)/(x_i-x_j))!=1):
                return False
    return True 
            
def solution(n):
    ans = 0
    stack = []
    for i in range(1, n+1):
        stack.append([(1, i)])
        while stack:
            queens = stack.pop()
            if len(queens)==n:
                if promising(queens):
                    ans += 1
            else:
                x, y = queens[-1]
                for i in range(1, n+1):
                    tqueens = queens[:]
                    tqueens.append((x+1, i))
                    stack.append(tqueens)
    
    return ans

# ------------------------------
# bfs
# ------------------------------

from collections import deque

def promising(queens):
    l = len(queens)
    for i in range(l):
        for j in range(i+1, l):
            x_i, y_i = queens[i]
            x_j, y_j = queens[j]
            if not (x_i!=x_j and y_i!=y_j and abs((y_i-y_j)/(x_i-x_j))!=1):
                return False
    return True 
            
    
def solution(n):
    ans = 0
    q = deque()
    for i in range(1, n+1):
        q.append([(1, i)])
        while q:
            queens = q.popleft()
            if len(queens)==n:
                if promising(queens):
                    ans += 1
            else:
                x, y = queens[-1]
                for i in range(1, n+1):
                    tqueens = queens[:]
                    tqueens.append((x+1, i))
                    q.append(tqueens)
    
    return ans

# ------------------------------
# backtracking using stack
# ------------------------------

def promising(queens):
    l = len(queens)
    for i in range(l):
        for j in range(i+1, l):
            x_i, y_i = queens[i]
            x_j, y_j = queens[j]
            if not (x_i!=x_j and y_i!=y_j and abs((y_i-y_j)/(x_i-x_j))!=1):
                return False
    return True 
            
def solution(n):
    ans = 0
    stack = []
    for i in range(1, n+1):
        stack.append([(1, i)])
        while stack:
            queens = stack.pop()
            if len(queens)==n:
                ans += 1
                
            x, y = queens[-1]
            for i in range(1, n+1):
                tqueens = queens[:]
                tqueens.append((x+1, i))
                if promising(tqueens):
                    stack.append(tqueens)
    
    return ans

# ------------------------------
# backtracking using function
# ------------------------------

def promising(queens):
    l = len(queens)
    for i in range(l):
        for j in range(i+1, l):
            x_i, y_i = queens[i]
            x_j, y_j = queens[j]
            if not (x_i!=x_j and y_i!=y_j and abs((y_i-y_j)/(x_i-x_j))!=1):
                return False
    return True 
ans = 0
def solution(n):
    def dfs(queens):
        global ans
        if len(queens)==n:
            ans += 1
        else:
            x, y = queens[-1]
            for i in range(1, n+1):
                tqueens = queens[:]
                tqueens.append((x+1, i))
                if promising(tqueens):
                    dfs(tqueens)
    for i in range(1, n+1):
        dfs([(1, i)])




def backtracking(n,left, right, temp, ans):
    if left == n and right == n:
        if temp[-1] == ')':
            ans.append(temp)
    else:
        if left <n:
            backtracking( n,left + 1, right, temp + '(', ans)
        if right < left:
            backtracking(n,left, right + 1, temp + ')', ans)

def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    ans = []
    left = 1
    right = 0
    backtracking(n,left, right, '(', ans)
    return ans

test=generateParenthesis(3)

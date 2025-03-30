class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s:
            # print(stk)
            if (stk != []) and ((i == ')' and stk[-1]=='(') or (i == '}' and stk[-1]=='{') or (i == ']' and stk[-1]=='[')):
                stk.pop()
            else:
                stk.append(i)
        # print(stk)
        if stk != []:
            return False
        else:
            return True

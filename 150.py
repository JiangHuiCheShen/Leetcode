class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        sps = ['*', '/', '+', '-']

        for i in range(len(tokens)):
            if tokens[i] in sps:

                a1 = stack.pop()
                a2 = stack.pop()
                if tokens[i] == '*':
                    stack.append(a1 * a2)
                elif tokens[i] == '+':
                    stack.append(a1 + a2)
                elif tokens[i] == '/':
                    stack.append(a2 // a1)
                elif tokens[i] == '-':
                    stack.append(a2 - a1)
            else:
                stack.append(int(tokens[i]))
        return stack[0]

a=Solution()
b=a.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
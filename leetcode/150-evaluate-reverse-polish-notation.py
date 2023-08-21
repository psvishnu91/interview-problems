"""150. Evaluate Reverse Polish Notation

https://leetcode.com/problems/evaluate-reverse-polish-notation

Need to realise that we need a STACK. Any time an operator shows,
pop two numbers from the stack, operate and push the result
back into the stack.

T - O(N), S - O(N)
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op2fn = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": div_towards_zero,
        }
        stk = []
        for token in tokens:
            if token not in op2fn:
                stk.append(int(token))
            else:
                # assume valid expression
                second_opnd = stk.pop()
                first_opnd = stk.pop()
                stk.append(op2fn[token](x=first_opnd, y=second_opnd))
        return stk.pop()


def div_towards_zero(x, y):
    q = x / y
    if q >= 0:
        return math.floor(q)
    else:
        return math.ceil(q)

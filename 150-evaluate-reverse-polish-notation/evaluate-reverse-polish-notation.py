class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def apply(op, a, b):
            if op == "+":
                x =  int(a) + int(b)
            elif op == "-":
                x = int(a)-int(b)
            elif op == "*":
                x =  int(a)*int(b)
            elif op == "/":
                x =  int(int(a)/int(b))
            else:
                raise ValueError("Invalid op")
            # print(f"({a} {op} {b}) = {x}")
            return str(x)

        for token in tokens:
            if token in ["*", "+", "-", "/"]:
                b, a = stack.pop(), stack.pop()
                stack.append(apply(token, a, b))
            else:
                stack.append(token)
        # print(stack)
        return int(stack[0])

        
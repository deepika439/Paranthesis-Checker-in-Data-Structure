class ParanthesisChecker:
    def __init__(self):
        self.stack = []
        
    def push(self, char):
        self.stack.append(char)
        
    def pop(self):
        return self.stack.pop() if self.stack else None
        
    def match(self, temp, char):
        if temp == '(' and char == ')':
            return True
        if temp == '{' and char == '}':
            return True
        if temp == '[' and char == ']':
            return True
        return False
        
    def check(self, exp):
        for char in exp:
            if char in '({[':
                self.push(char)
            elif char in ')}]':
                if not self.stack:
                    print("Right Parentheses are more than Left Parentheses")
                    return False
                temp = self.pop()
                if not self.match(temp, char):
                    print("Mismatched Parentheses")
                    return False
        if self.stack:
            print("Left Parentheses are more than Right Parentheses")
            return False
        else:
            print("Balanced")
            return True

Checker = ParanthesisChecker()
exp = input("Enter an Expression: ")
valid = Checker.check(exp)

if valid:
    print("Expression is Balanced")
else:
    print("Expression is Unbalanced")

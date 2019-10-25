#!/usr/bin/env python3

def calculate(arg):
    stack = list()
    for token in arg.split():
        if token == '+':
            arg1 = stack.pop()
            arg2 = stack.pop()
            stack.append(arg1 + arg2)
        elif token == '-': 
            arg1 = stack.pop()
            arg2 = stack.pop()
            stack.append(arg2 - arg1)
        else: 
            stack.append(int(token))
    
    #print(stack)
    return stack.pop()

def main():
    while True:
        calculate(input("rpn calc> "))

if __name__ == '__main__':
    main()
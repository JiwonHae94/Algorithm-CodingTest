#https://www.acmicpc.net/problem/10828
import sys
def solve10828():
    n = int(input())
    stack = []

    def push(n):
        return stack.append(n)

    def pop():
        if not stack:
            return -1
        return stack.pop()

    def top():
        if not stack:
            return -1
        return stack[-1]

    def empty():
        return 1 if(len(stack) == 0) else 0

    for i in range(n):
        ## input() causes timeout
        commands = sys.stdin.readline().split()
        inst = commands[0]

        if inst == "push":
            num = commands[1]
            push(num)
        elif inst == "pop":
            print(pop())
        elif inst == "top":
            print(top())
        elif inst == "size":
            print(len(stack))
        elif inst == "empty":
            print(empty())


#!/usr/bin/python3
#10 out of 14 pass

def superStack(operations):
    stack = list()
    tmp = [0]
    for line in operations:
        oper = line.split(" ")
        if oper[0] == "pop":
            stack.pop()
            tmp.pop()
        elif oper[0] == "push":
            tmp[len(stack)] = -sum(tmp)
            stack.append(int(oper[1]))
            tmp.append(0)
        elif oper[0] == "inc":
            i = int(oper[1])
            v = int(oper[2])
            tmp[0] += v
            if  len(stack) <= i+1:
              tmp[i] -= v
        print(stack)
        print(tmp)

        z = sum([tmp[i] for i in range(len(stack))])

        show = 'EMPTY' if len(stack) == 0 else (z + stack[-1])
        print(show)


a = [
        "push 4",
        "pop",
        "push 3",
        "push 5",
        "push 2",
        "inc 3 1",
        "pop",
        "push 1",
        "inc 2 2",
        "push 4",
        "pop",
        "pop"
        ]
superStack(a)

# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Push() and Pop() - move TopOfStack yourself.

# Exercise 1
Stack = []
TopOfStack = -1
for x in range(10):
    Stack.append(-1)


def IsEmpty():
    global TopOfStack
    return TopOfStack == -1


def IsFull():
    global TopOfStack
    return TopOfStack == 9



# Exercise 2
def Push(Item):
    global Stack, TopOfStack
    if IsFull():
        return False
    TopOfStack = TopOfStack + 1     # move up FIRST
    Stack[TopOfStack] = Item        # then store
    return True


# Exercise 3
def Pop():
    # Write your code here
    pass


# Exercise 4
def Peek():
    # Write your code here
    pass


def Size():
    # Write your code here
    pass


# Exercise 5
def ReverseWord(Word):
    # Write your code here
    pass


"""In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query is one of the following  types:

1 x: Enqueue element  into the end of the queue.
2: Dequeue the element at the front of the queue.
3: Print the element at the front of the queue.
Input Format

The first line contains a single integer, , denoting the number of queries. 
Each line  of the  subsequent lines contains a single query in the form described in the problem statement above. All three queries start with an integer denoting the query , but only query  is followed by an additional space-separated value, , denoting the value to be enqueued.
"""

stack1 ,stack2 = [], []
def enqueue(stack1, element):
    stack1.append(element)

def dequeue(stack1, stack2):
    if not stack2:
        while stack1 : stack2.append(stack1.pop())
    stack2.pop()
        
for _ in range(int(input().strip())):
    M = [int(i) for i in input().strip().split(' ')]
    if M[0] == 1:
        enqueue(stack1, M[1])
    elif M[0] == 2:
        dequeue(stack1, stack2)
    else:
        print(stack2[-1] if stack2 else stack1[0])
    
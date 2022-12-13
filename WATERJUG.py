def dec():
    global tree
    global parent
    tree={(0,0):[]}
    parent=(0,0)



def add(jug1,jug2,k):
    global parent
    if k==0:
        tree[parent].append((jug1,jug2))
        tree[(jug1,jug2)]=[]
        parent=(jug1,jug2)
    else:
        tree[parent].append((jug2,jug1))
        tree[(jug2,jug1)]=[]
        parent=(jug2,jug1)


def jug(jug1,jug2,goal,n,m,k):
    while jug1!=goal and jug2!=goal:
        if jug2==0:
            jug2=m
            add(jug1,jug2,k)
        jug1+=jug2
        if jug1>n:
            jug2=jug1-n
            jug1=n
            add(jug1,jug2,k)
        else:
            jug2=0
            add(jug1,jug2,k)
        if jug1>=n:
            if jug1!=goal:
                jug1=0
            else:
                jug2=0
            add(jug1,jug2,k)


def bfs(node,goal):
    frontier=[]
    explored=[]
    global l
    l=[]
    global p
    p={}
    frontier.append(node)
    while frontier:
        node=frontier.pop(0)
        explored.append(node)
        if node==(0,goal) or node==(goal,0):
            while node!=(0,0):
                l.append(node)
                node=p[node]
            return
        for j in tree[node]:
            if j not in frontier and j not in explored:
                 frontier.append(j)
                 p[j]=node



def main():
    dec()
    c1=int(input("Enter jug 1 capacity: "))
    c2=int(input("Enter jug 2 capacity: "))
    goal=int(input("Enter goal capacity: "))
    if c1%2==0 and c2%2==0 and goal%2!=0:
        print("Case not possible")    
    elif goal>max([c1,c2]):
        print("Limit Exceeded")
    else:
        jug1=0
        jug2=0
        jug(jug1,jug2,goal,c1,c2,0)
        global parent
        parent=(0,0)
        jug(jug2,jug1,goal,c2,c1,1)
        bfs((0,0),goal)
        [print(x,end=" ") for x in reversed(l)]
main()

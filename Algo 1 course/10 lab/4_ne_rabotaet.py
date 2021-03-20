import sys
import threading
from math import *
 
 
sys.setrecursionlimit(1000000)

 
def getTopSort(graph,answer):
    n=len(graph)
    color=[0]*n
    for i in range(n):
        if not color[i]:
            q=[i]
            while q:
                flag=1
                x=q[-1]
                color[x]=1
                for a,b in graph[x]:
                    if color[a]==0:
                        q.append(a)
                        flag=0
                        break
                    elif color[a]==1:
                        f=0
                        break
                if flag==1:
                    q.pop()
                    color[x]=2
                    answer.append(x)
    answer=answer[::-1]
     
def markComponents(v,graph,components,component):
    q=[v]
    while q:
        x=q.pop()
        components[x]=component
        for a,b in graph[x]:
            if components[a]==0:
                q.append(a)
                components[a]=component
             
def getCondesation(graph, components):
    n=len(graph)
    graphTransposed=[[] for i in range(n)]
    for i in range(n):
        for a,b in graph[i]:
            graphTransposed[a].append([i,b])
    order=[]
    getTopSort(graph,order)
    componentsCount=0
    for i in order:
        if not components[i]:
            componentsCount+=1
            markComponents(i,graphTransposed,components,componentsCount)
    for i in range(len(components)):
        components[i]-=1
 
             
     
def getMst(root,graph):
    inf=300000000000000
    result=0
    n=len(graph)
    minEdge=[inf]*n
    for i in range(n):
        for a,b in graph[i]:
            minEdge[a]=min(minEdge[a], b)
    for i in range(n):
        if i != root:
            result +=minEdge[i]
    zeroGraph=[[] for i in range(n)]
     
    for i in range(n):
        for j in range(len(graph[i])):
            d=graph[i][j]
            if d[1]==minEdge[d[0]]:
                graph[i][j][1]=0
                zeroGraph[i].append(d)
    print('res1',result)       
    if checkJopa(root,zeroGraph):
        print('>>',result)
        return result
    components=[0]*n
    getCondesation(zeroGraph,components)
    componentsCount=0
    for i in components:
        componentsCount=max(componentsCount,i)
    componentsCount+=1
    newGraph=[[] for i in range(componentsCount)]
    for i in range(n):
        for a,b in graph[i]:
            if components[i]!=components[a]:
                newGraph[components[i]].append([components[a],abs(b-minEdge[a])])
    print('res2',result)
    for i in newGraph:
        print(*i)
    print()
    return (result+getMst(components[root], newGraph))
             
 
def countVertex(b,graph,visited):
    q=[b]
    while q:
        x=q.pop()
        visited[x]=True
        for i in graph[x]:
            b,c=i
            if not visited[b]:
                q.append(b)
     
def checkJopa(b, graph):
    n=len(graph)
    visited=[0]*n
    countVertex(b,graph,visited)
    for v in visited:
        if not v:
            return False
    return True
     
def main():
    f=open("chinese.in")
    t=open("chinese.out", "w")
    s=f.readline().split()
    n,m=int(s[0]),int(s[1])
    graph=[[] for i in range(n)]
     
    for i in range(m):
        s=f.readline().split()
        a,b,c=int(s[0]),int(s[1]),int(s[2])
        graph[a-1].append([b-1,c])
         
    if checkJopa(0,graph):
        print('YES',file=t)
        print(getMst(0,graph),file=t)
    else:
        print('NO',file=t)
    t.close()
     
main()

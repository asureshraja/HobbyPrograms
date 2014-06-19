'''
Created on Jun 16, 2014

@author: suresh
'''
from rcviz import callgraph, viz

@viz

def ssum(lis,sum,prev):
    if(sum==0):
        return True
    elif(len(lis)==0):
        return False
    elif lis[len(lis)-1]>sum:
        a=ssum(lis[:len(lis)-1],sum,sum)
        if(a==True and sum!=prev):
            print prev-sum
        return a
    else:
        a=ssum(lis[:len(lis)-1],sum,sum)
        b=ssum(lis[:len(lis)-1],sum-lis[len(lis)-1],sum)
        if(a==True):
            if(sum!=prev):
                print prev-sum
        elif(b==True):
            if(sum-lis[len(lis)-1]!=prev):
                print lis[len(lis)-1]
        return a or b
    
print ssum([1,2,3,4],5,5)
callgraph.render("subsetsum.png")

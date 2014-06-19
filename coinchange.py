'''
Created on Jun 16, 2014

@author: suresh
'''

from rcviz import callgraph, viz

@viz
def coinchange(lis,sum,prev):
    if(sum==0):
        #print prev
        return True
    elif(len(lis)==0):
        return False
    elif lis[len(lis)-1]>sum:
        a=coinchange(lis[:len(lis)-1],sum,sum)
        return a
    else:
        a=coinchange(lis[:len(lis)-1],sum,sum)
        b=coinchange(lis[:len(lis)],sum-lis[len(lis)-1],sum)
        if(a==True):
            if(prev != sum):
                print prev-sum
        if( b==True):
            if(sum-lis[len(lis)-1]!=sum):
                print lis[len(lis)-1]
        return a or b
    
print coinchange([1,2,3,4],4,4) 
callgraph.render("coinchange.png")
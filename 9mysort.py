inputs=[int(x) for x in open('data2.txt','r').read().splitlines()]
#inputs=[46,77,9,89,96,44,37,10,84]
dummy=inputs[:]
meta=[0]*len(inputs)
def fillmetamin(l,r,flag=0):
	global inputs,meta
	i=l
	j=r
	minno=inputs[i]
	meta[i]=i
	minindex=i
	i=i+1
	while(i<=j):
		
		if(int(inputs[i])<=int(minno)):
			minno=inputs[i]
			minindex=i
			meta[i]=i
		else:
			meta[i]=minindex
		i=i+1

def fillmetamax(l,r,flag=0):
	global inputs,meta
	i=l
	j=r

	maxno=inputs[j]
	maxindex=j
	meta[j]=j

	j=j-1
	while (j>=i):
		if(int(inputs[j])>=int(maxno)):
			maxno=inputs[j]
			maxindex=j
			meta[j]=j
			
		else:
			meta[j]=maxindex
		j=j-1
	
def swapmin(i,j):
	global meta,inputs
	if(i!=j and inputs[i]<inputs[j]):
		temp=inputs[i]
		inputs[i]=inputs[j]
		inputs[j]=temp

def swapmax(i,j):
	global meta,inputs
	if(i!=j and inputs[i]>inputs[j]):
		temp=inputs[i]
		inputs[i]=inputs[j]
		inputs[j]=temp

def partialmin(l,r):
	global meta,inputs
	i=l
	j=r
	print l,r
	minno=inputs[meta[i]]
	retval=j
	#meta[i]=i
	minindex=meta[i]
	i=i+1
	
	while(i<=j):
		print "inputs[i]",inputs[i],minno
		if(int(inputs[i])<=int(minno)):
			minno=inputs[i]
			minindex=i
			meta[i]=i
		else:
			meta[i]=minindex
		i=i+1
	print "meta",meta
	return retval


def partialmax(l,r):
	global meta,inputs
	i=l
	j=r

	maxno=inputs[meta[j]]
	retval=i
	maxindex=meta[j]
	#maxindex=j
	#meta[j]=j

	j=j-1
	while (j>=i):
		if(int(inputs[j])>=int(maxno)):
			maxno=inputs[j]
			maxindex=j
			meta[j]=j
			
		else:
			meta[j]=maxindex
		j=j-1

	return retval

def traversemin(l,r):
	global meta,inputs
	i=l
	j=r
	while(j>=i and meta[j]>=i):
		print "swapping ",inputs[meta[j]],inputs[i]
		swapmin(meta[j],i)
		#if(meta[j]!=i and inputs[meta[j]]<inputs[i]):
		#	temp=inputs[meta[j]]
		#	inputs[meta[j]]=inputs[i]
		#	inputs[i]=temp
		print "swapped",inputs[meta[j]],inputs[i]
		k=j
		j=meta[j]-1
		i=i+1
		if(j>=i):
			j=partialmin(j,k)
			print j
		print "min",inputs

	l=i
	return [l,r]

def traversemax(l,r):
	global meta,inputs
	i=l
	j=r
	while(i<=j and meta[i]<=j):
		print "swapping ",inputs[meta[i]],inputs[j]
		swapmax(meta[i],j)
		#if(meta[i]!=j and inputs[meta[i]]>inputs[j]):
		#	temp=inputs[meta[i]]
		#	inputs[meta[i]]=inputs[j]
		#	inputs[j]=temp

		k=i
		i=meta[i]+1
		j=j-1
		
		if(i<=j):
			i=partialmax(k,i)
			print i
		print "max",inputs

	r=j
	return [l,r]

def sort(l,r):
	while(l<=r):
		fillmetamin(l,r)
		a=traversemin(l,r)
		fillmetamax(a[0],a[1])
		b=traversemax(a[0],a[1])
		l=b[0]
		r=b[1]

sort(0,len(inputs)-1)
print inputs
dummy.sort()
print dummy
for i in range(0,len(inputs)):
	if(inputs[i]!=dummy[i]):
		print"\n\n\n\n\nBAD\n\n\n\n\n"
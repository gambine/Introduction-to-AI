'''
COMP3308 Assignment 2
@cgoh2475

 K-Nearest Neighbours Implementation based on  Euclidean distance

'''
import math

# Calculates Euclidean distance between 2 instances t1 and t2.
def __euclidean(t1,t2):
	d=0
	l=len(t1)
	
	if t1[l-1].strip()=="yes" or t1[l-1].strip()=="no":
		l-=1

	for i in range(l): 
		d+=(float(t1[i])-float(t2[i]))**2

	d=math.sqrt(d)
	return d

# Returns array of a test instance's k nearest neighbours from training set
def __getNearestNeighbours(train_set,test_inst,k):
	diff=[] # (distance, training instance)
	for each in train_set:
		d=__euclidean(each,test_inst)
		diff.append([d,each])
	diff.sort(key=lambda x:x[0])
	neighbours=[x[1] for x in diff[:k]]
	
	return neighbours

# Returns majority vote (string) 'yes' or 'no' between k neighbours
def __majorityVote(neighbours):
	l=len(neighbours[0])
	bla=[x for x in neighbours if x[l-1].strip()=='yes']
	yes=len(bla)

	noob=[x for x in neighbours if x[l-1].strip()=='no']
	no=len(noob)
	'''
	print('yes: '+str(yes))
	print('l: '+str(l))
	
	for e in bla: print(bla)
	'''
	if yes >= no: 
		return 'yes'

	return 'no'

def knn(k,train_set,test_set):
	if k>len(train_set): return []
	
	ans=[]
	for e in test_set:
		neighbours=__getNearestNeighbours(train_set,e,k)
		ans.append(__majorityVote(neighbours))

	return ans

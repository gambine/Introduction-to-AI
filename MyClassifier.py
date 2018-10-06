'''
COMP3308 Assignment 2

'''
import sys
from extrapackage.naiveBayes import *
from extrapackage.kNearestNeighbours import *

def __resultCheck(fname):
    f=open(fname,'r')
    data=[]
    for l in f:
        bla=l.split()
        data.append(bla)
    f.close()
    data=[x[0] for x in data]
    return data

def __runningMan(arg):
    l=len(arg)

    if l<3 or l>4:
        print("Usage: python3 MyClassifier.py <train file> <test file> <algorithm - NB or kNN where k is an integer larger than 0>")
        print("       or")
        print("       python3 MyClassifier.py <10fold file> <algorithm - NB or kNN where k is an integer larger than 0>")
        sys.exit(1)

    train_set = []
    test_set = []
    ans=None

    # normal running
    if l==4:
        train_file = open(arg[1],'r')
        test_file = open(arg[2],'r')
        cmd=arg[3]

        # read in training and test data into list
        train_set=[x.split(',') for x in train_file]
        test_set=[y.split(',') for y in test_file]

        train_file.close()
        test_file.close()

        ans=__algorithm(cmd,train_set,test_set)
        return 0

    # 10 fold x validation
    if l==3:
        despacito=arg[1]
        cmd=arg[2]
        folds=__readFolds(despacito)
        __strat10fcv(folds,cmd)
        return 0

    return 1

def __readFolds(naruto):
    f=open(naruto,'r')
    folds=f.read().rstrip().split('\n\n') # folds 1-10
    for i in range(10):
        yummy=(folds[i]).split('\n')
        boop=yummy[1:]
        boop=[x.split(',') for x in boop]
        folds[i]=boop

    return folds

# 10f xv
def __strat10fcv(folds,cmd):
    accuracies=[]
    # fold 1 first test set
    for i in range(10):
        test_set=folds[i]
        train_set=[]
        for j in range(10):
            if j!=i: train_set=train_set+folds[j]

        print('\n\n')
        print("Round "+str(i+1)+"...")
        tiong=__algorithm(cmd,train_set,test_set)
        l=len(train_set[0])-1
        actual_tiong=[x[l] for x in test_set]
        betul=0

        for z in range(len(tiong)):
            if tiong[z].strip()==actual_tiong[z].strip(): betul+=1

        # accuracy
        a=(betul/len(tiong))*100.00
        print("Accuracy "+str(i+1)+" : "+str(a)+"%")
        accuracies.append(a)

    # Total Accuracy
    tamade=sum(accuracies)/len(accuracies)
    print("Total Accuracy: "+str(tamade)+"%")


# Runs algorithms
def __algorithm(cmd,train_set,test_set):

    '''
    # start testing - comment out later
    one='1nnresult.txt'
    five='5nnresult.txt'
    one_result=__resultCheck(one)
    five_result=__resultCheck(five)
    # end testing
    '''

    ans=[]
    cut=len(cmd)-2

    if cmd=='NB': # naive bayes
        ans=nb(train_set,test_set)

    elif cmd[cut:]=='NN': # k nearest neighbour
        k = int(cmd[:cut])
        if k <= 0 or len(cmd)==2:
            sys.exit(1)
        else:
            ans=knn(k,train_set,test_set)

    else:
        print("Invalid Command\n")
        sys.exit(1)

    # print answer
    for cbkia in ans:print(cbkia)

    return ans

# main function
__runningMan(sys.argv)

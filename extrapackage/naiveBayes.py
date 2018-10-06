import math

#calculate the mean
def calculateMean(train_set):
    mean=[]

    for i in range(len(train_set[0])-1):
        total = 0
        for x in train_set:
            total = total + float(x[i])
        mean.append(total/len(train_set))
    return mean

def CalculateStdev(train_set):
    stdev = []

    avg = calculateMean(train_set)
    for i in range(len(train_set[0])-1):
        total = 0
        for x in train_set:
            total = total+math.pow(float(x[i]) - avg[i],2)
        stdev.append(math.pow(total/(len(train_set)-1),0.5))
    return stdev

def calculateProbability(x, mean, stdev,default_probability):
    probability = 1
    l=len(x)
    if x[l-1].strip()=="yes" or x[l-1].strip()=="no":
        l-=1
    for i in range(l):
        probability = probability * (1 / (math.sqrt(2*math.pi) * stdev[i])) * math.exp(-(math.pow(float(x[i])-mean[i],2)/(2*math.pow(stdev[i],2))))

    return probability * default_probability


def nb(train_set,test_set):
    y = []
    n = []
    result = []
    for i in train_set:
        if(i[len(train_set[0])-1].strip()== 'yes'):
            y.append(i)
        elif(i[len(train_set[0])-1].strip() == 'no'):
            n.append(i)
    y_mean = calculateMean(y)
    n_mean = calculateMean(n)
    y_stdev = CalculateStdev(y)
    n_stdev = CalculateStdev(n)
    y_default_pro = len(y)/len(train_set)
    n_default_pro = len(n)/len(train_set)
    for e in test_set:
        y_probability = calculateProbability(e, y_mean, y_stdev,y_default_pro)
        n_probability = calculateProbability(e, n_mean, n_stdev,n_default_pro)
        if(y_probability >= n_probability):
            result.append('yes')
        else:
            result.append('no')

    return result

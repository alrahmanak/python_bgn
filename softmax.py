import numpy as np
# testing softmax funtion

def softmax(L):
    expL = np.exp(L)
    sumExpL = sum(expL)
    result = []
    for i in expL:
        result.append(i*1.0/sumExpL)
    return result
    
    # Note: The function np.divide can also be used here, as follows:
    # def softmax(L):
    #     expL = np.exp(L)
    #     return np.divide (expL, expL.sum())

l = [1,2,3,4]
r = softmax(l)
sofr = sum(r)
for ri in r:
    print(ri)
print("input values to softmax: ",l)	
print("sum of all probabilities of softmax: ",sofr)

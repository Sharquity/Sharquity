from neural_net import NeuralNet
import random

badCompany = (688657,3232342,12,18)
goodCompany = (150000,25,600000,2)
bluetooth_implant = (1000000,15,6666667,1)  # should be consistently lower than output model
ava_the_elephant = (50000,15,333333,3)  # somewhat successful product
scrub_daddy = (100000,10,1000000,9)  # most successful product


net = NeuralNet()
net.init_model()
print(net.checkPerformance())

def evaluate(company):
    offer = net.predictOffer(company)
    net.init_model()
    return offer

def average(ls):
    return sum(ls) / len(ls)

blue = [evaluate(bluetooth_implant) for i in range(2)]
#ava = [evaluate(ava_the_elephant) for j in range(50)]
#scrub = [evaluate(scrub_daddy) for k in range(50)]


print(blue)
#print(ava)
#print(scrub)
'''
net = NeuralNet()
net.init_model()
print(net.predictOffer([70000, 39, 40000000000, 5]))
net.init_model()
print(net.predictOffer([70000, 39, 40000000, 4]))
'''

# 1.48, 1.38,
from neural_net import NeuralNet
import random

badCompany = (1400234234234234234,3232342,15243453,18)
goodCompany = (150000,25,600000,2)

net = NeuralNet()
net.init_model()
print(net.predictOffer(badCompany))

'''
for i in x:
    print(i, y[x.index(i)])
'''

stack = 0

net = NeuralNet()
for i in range(50):
    randCompany = (random.randint(10000, 5000000), random.randint(3, 40), random.randint(40000, 30000000), random.randint(1,54))
    net.init_model()
    print(net.predictOffer(randCompany))

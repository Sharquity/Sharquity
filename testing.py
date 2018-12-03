from neural_net import NeuralNet
import random

badCompany = (688657,3232342,12,18)
goodCompany = (150000,25,600000,2)

net = NeuralNet()
net.init_model()
print(net.predictOffer(badCompany))

for i in range(50):
    askedFor = random.randint(10000, 5000000)
    randCompany = (askedFor, random.randint(3, 40), random.randint(40000, 30000000), random.randint(1,54))
    net.init_model()
    print(str(askedFor) + " --> " + str(net.predictOffer(randCompany)))

import csv
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from neural_net import NeuralNet

industry_codes = {}
current_code = 1
industry_codes["None"] = 0

companies = []

askedFors = []

x = []  # training data inputs
y = []  # training data outputs

# collect data from csv
with open("data.csv") as data:
    isFirst = True
    reader = csv.reader(data)
    for row in reader:
        if isFirst:
            isFirst = False  # first header data, pass without processing
        else:
            # the training data is set up in this way: (askedFor, exchangeForStake, valuation, industryCode)
            category = row[3]
            code = 0
            if category in industry_codes.keys():
                code = industry_codes[category]
            else:
                industry_codes[category] = current_code
                current_code += 1
                code = industry_codes[category]
            askedFor = np.float64(row[7])
            askedFors.append(askedFor)
            exchangeForStake = np.float64(row[8])
            valuation = np.float64(row[9])
            company_info = [askedFor, exchangeForStake, valuation, code]
            companies.append(company_info)
            x.append(company_info)
            deal = row[0]
            if deal == "TRUE":
                deal = 1
            elif deal == "FALSE":
                deal = 0
            else:
                raise Exception
            y.append(deal)  # whether or not a deal was made, strings of "TRUE" or "FALSE" changed to 1 or 0

for i in askedFors:
    print(i)

for i in range(10):
    print("\n")

net = NeuralNet()
for company in companies:
    net.init_model()
    print(net.predictOffer(company))
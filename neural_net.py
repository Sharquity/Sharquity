from sklearn.neural_network import MLPClassifier
import csv
import numpy as np
import warnings
warnings.filterwarnings("ignore")

industry_codes = {}
current_code = 1
industry_codes["None"] = 0

companies = []

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
            exchangeForStake = np.float64(row[8])
            valuation = np.float64(row[9])
            company_info = [askedFor, exchangeForStake, valuation, code]
            companies.append(company_info)
            #company_megascore = askedFor * exchangeForStake * valuation * code
            x.append(company_info)
            deal = row[0]
            if deal == "TRUE":
                deal = 1
            elif deal == "FALSE":
                deal = 0
            else:
                raise Exception
            y.append(deal)  # whether or not a deal was made, strings of "TRUE" or "FALSE" changed to 1 or 0

class NeuralNet():
    def __init__(self, model=None):
        self.model = model
        self.company = None

    def init_model(self):
        mlp = MLPClassifier(activation='logistic', solver='lbfgs', alpha=1e-9999,
                            hidden_layer_sizes=(5, 2), random_state=1)
        mlp.fit(x,y)
        self.model = mlp

    def predictOffer(self, company):
        prediction = self.model.predict([company])
        probability = self.model.predict_proba([company])
        ans = prediction.item()
        prob = float(list(probability)[0][1])
        if prob > 0.53:
            prob = 1
        if ans == 1:
            return company[0] * prob
        else:
            return 0

    def predictWithProb(self, company):  # where company is a tuple with four items in corresponding order
        #print(company)
        #megascore = company[0] * company[1] * company[2] * company[3]

        prediction = self.model.predict([company])
        probability = self.model.predict_proba([company])
        ans = prediction.item()
        prob = float(list(probability)[0][1]) * 100
        return [ans, prob]
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report,confusion_matrix
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
        self.x_test = None
        self.y_test = None

    def init_model(self):
        mlp = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
        X_train, X_test, y_train, y_test = train_test_split(x, y)
        self.y_test = y_test
        scaler = StandardScaler()
        scaler.fit(X_train)
        X_train = scaler.transform(X_train)
        self.x_test = scaler.transform(X_test)
        mlp.fit(X_train,y_train)
        self.model = mlp

    def reliability_scaler(self):
        prediction = self.model.predict(self.x_test)
        tn, fp, fn, tp = confusion_matrix(self.y_test, prediction).ravel()
        #print("tn", tn, "fp", fp, "fn", fn, "tp", tp)
        ans = ((float(tn) + float(tp)) / (float(fp) + float(fn)))
        return ans / 1.5

    def predictOffer(self, company):
        answers = []
        for i in range(20):
            prediction = self.model.predict([company]).item()
            #print('cc', company)
            original = company[0]
            ans_scale = 1
            threshold = 0.1   # may change as necessary
            if prediction == 0.0:
                ans_scale = 1 - threshold
            elif prediction == 1.0:
                ans_scale = 1 + threshold
            #print('o', original)
            #print('rs2', self.reliability_scaler())
            #print('as', ans_scale)
            scaled = float(original) * float(self.reliability_scaler()) * ans_scale
            #print(scaled)
            answers.append(scaled)
            self.init_model()
        return sum(answers) / len(answers)

    def checkPerformance(self):
        prediction = self.model.predict(self.x_test)
        print(classification_report(self.y_test, prediction))
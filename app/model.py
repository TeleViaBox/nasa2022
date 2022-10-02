import pickle
import gzip

# with open('./model/xgboost-iris.pgz', 'rb') as f:
#     myModel = pickle.load(f)
    
# with gzip.open('./model/xgboost-iris.pgz', 'r') as f:
#     model = pickle.load(f)

with gzip.open('app/model/xgboost-iris.pgz', 'r') as f:
    myModel = pickle.load(f)

def predict(input):
    pred = myModel.predict(input)[0]
    print(pred)
    return pred
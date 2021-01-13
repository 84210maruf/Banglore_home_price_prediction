import pickle
import json
import numpy as np
from sklearn.linear_model import LinearRegression

__model = None
__data_columns = None
__locations = None


def get_estimate_price(locn, size, bhk, n_bath):
    print('...................')
    locns = locn.lower()

    arr = np.zeros((1, len(__data_columns)))
    arr[0][0] = bhk
    arr[0][1] = size
    arr[0][2] = n_bath


    try:
        pos = __data_columns.index(locns)
        arr[0][pos] = 1
    except:
        pass

    price = int(str(__model.predict(arr)[0])[:3])
    print(price)
    print(type(price))


    return round(price)

def get_locations():
    print('llllllllllllllllllll')
    return __locations


def load_data():
    global __locations, __model, __data_columns

    print('Starting to load data...')

    with open('./artifacts/columns.json', 'r') as jsonFile:
        __data_columns = json.load(jsonFile)['data_columns']  # list of columns
        __locations = __data_columns[3:]  # list of places

    with open('./artifacts/banglore_home_price_model.pickle', 'rb') as pklFile:
        __model = pickle.load(pklFile)

    print('Data Loaded Successfully!...')




if __name__ == '__main__':
    load_data()
    print(get_locations())

    print(get_estimate_price('electronic city phase ii', 1000, 3, 3))
    print(get_estimate_price('electronic city phase ii', 1000, 2, 2))
    print(get_estimate_price('old airport road',1000, 2, 2))
    print(get_estimate_price('parappana',1000, 2, 2))
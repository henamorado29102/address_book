import pickle
import os


def save_data(name, information):
    with open('./data/' + name + '.pkl', 'wb') as fp:
        pickle.dump(information, fp)


def load_data(name):
    if os.path.isfile('./data/' + name + '.pkl'):
        with open('./data/' + name + '.pkl', 'rb') as fp:
            return pickle.load(fp)
    return []


def remove_file(name):
    if os.path.isfile('./data/' + name + '.pkl'):
        os.remove('./data/' + name + '.pkl')


def create_dir():
    if not os.path.isdir('./data'):
        os.mkdir('./data')

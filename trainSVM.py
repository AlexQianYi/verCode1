
from libsvm.python.svm import svm_problem, svm_parameter
from libsvm.python.svmutil import *

def svm_model_train():

    """
    use image feature file to train model
    :return:
    """

    y, x = svm_read_problem('./Feature.txt')

    model = svm_train(y, x)
    svm_save_model('./SVMmodel/svm_model', model)
    print('save')


if __name__ == '__main__':
    svm_model_train()

from libsvm.python.svm import svm_problem, svm_parameter
from libsvm.python.svmutil import *

def svm_model_test():
    """
    use test data set to test performance of model
    :return:
    """

    yt, xt = svm_read_problem(test_feature_file)
    model = svm_load_model('./SVMmodel/svm_model')
    p_label, p_acc, p_val = svm_predict(yt, xt, model)

    count = 0
    for item in p_label:

        print('%d' % item, end=',')

        count += 1
        if count % 8 == 0:
            print('')
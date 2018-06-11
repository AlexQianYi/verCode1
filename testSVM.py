
from libsvm.python.svm import svm_problem, svm_parameter
from libsvm.python.svmutil import *
from SVMFeature import *

def svm_model_test():
    """
    use test data set to test performance of model
    :return:
    """
    test_feature_file = './Test/Feature.txt'

    yt, xt = svm_read_problem(test_feature_file)
    model = svm_load_model('./SVMmodel/svm_model')
    p_label, p_acc, p_val = svm_predict(yt, xt, model)

    label = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', \
             10:'a', 11:'A', 12:'b', 13:'B', 14:'c', 15:'C', 16:'d', 17:'D', 18:'e', 19:'E', \
             20:'f', 21:'F', 22:'g', 23:'G', 24:'h', 25:'H', 26:'i', 27:'I', 28:'j', 29:'J', \
             30:'k', 31:'K', 32:'l', 33:'L', 34:'m', 35:'M', 36:'n', 37:'N', 38:'o', 39:'O', \
             40:'p', 41:'P', 42:'q', 43:'Q', 44:'r', 45:'R', 46:'s', 47:'S', 48:'t', 49:'T', \
             50:'u', 51:'U', 52:'v', 53:'V', 54:'w', 55:'W', 56:'x', 57:'X', 58:'y', 59:'Y', \
             60:'z', 61:'Z'}

    count = 0
    for item in p_label:
        print('label:%d:%s | pred: %d:%s' % (yt[count], label[int(yt[count])], item, label[item]))

        count += 1
        if count % 8 == 0:
            print('')

if __name__ == '__main__':

    handle_test_file()

    print('------------------------------------------------------')
    print('-------------------SVM Vector Finish------------------')
    print('------------------------------------------------------')

    svm_model_test()
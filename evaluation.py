
from sklearn import metrics
import numpy as np


def evaluate_in_npratio (all_fold_results):
        accuracy_list = []
        f1_list = []
        precision_list = []
        recall_list = []
        for fold_num in all_fold_results:
            y_true = all_fold_results[fold_num][1]
            y_pred = all_fold_results[fold_num][0]

            accuracy = metrics.accuracy_score(y_true,y_pred)
            f1 = metrics.f1_score(y_true, y_pred, average = 'binary')
            precision = metrics.precision_score(y_true, y_pred, average = 'binary')
            recall = metrics.recall_score(y_true, y_pred, average = 'binary')
            accuracy_list.append(accuracy)
            f1_list.append(f1)
            precision_list.append(precision)
            recall_list.append(recall)
        print(accuracy_list,f1_list,precision_list,recall_list)
        accuracy_mean = np.mean(accuracy_list)
        accuracy_std = np.std(accuracy_list)
        f1_mean = np.mean(f1_list)
        f1_std = np.std(f1_list)
        precision_mean = np.mean(precision_list)
        precision_std = np.std(precision_list)
        recall_mean = np.mean(recall_list)
        recall_std = np.std(recall_list)
        return {'accuracy_mean': accuracy_mean, 'accuracy_std' : accuracy_std, 'f1_mean': f1_mean, 'f1_std' : f1_std, 'precision_mean': precision_mean, 'precision_std': precision_std, 'recall_mean': recall_mean, 'recall_std': recall_std}



# from sklearn.metrics import roc_auc_score
# def evaluate_in_npratio2 (self, all_fold_results):
#           auc_list = []
#           for fold_num in all_fold_results:
#               y_score = all_fold_results[fold_num][0]
#               y_label = all_fold_results[fold_num][1]
#               auc = roc_auc_score(y_label,y_score)
#
#               auc_list.append(auc)
#           auc_mean = np.mean(auc_list)
#           auc_std = np.std(auc_list)
#           return {'auc_mean': auc_mean, 'auc_std' : auc_std}

with open('/Users/brandonli/Desktop/result/table4/80/content_result','r') as file:
    result=[]
    for item in file:
        item=item.replace('[','')
        item = item.replace(']', '')
        item=item.replace(',','')
        item=item.replace(' ','')
        item=item.replace('\n','')
        item=list(item)
        result.append(item)
    result_int=[]
    for item in result:
        for i in range(len(item)):
            item[i]=int(int(item[i]))
        result_int.append(item)


    no_r={}
    no_r[1] = [ result_int[0],result_int[1]]
    no_r[2] = [result_int[2], result_int[3]]
    no_r[3] = [result_int[4], result_int[5]]
    no_r[4] = [result_int[6], result_int[7]]
    no_r[5] = [result_int[8], result_int[9]]
    a=evaluate_in_npratio(no_r)
    print(a)




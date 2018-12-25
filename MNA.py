#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Bowen Li'

import pickle
import numpy as np
from sklearn.svm import SVC

fold1_list=[]
fold2_list=[]
fold3_list=[]
fold4_list=[]
fold5_list=[]

method=10
path_string='/Users/brandonli/Desktop/classfier/E1/'

with open(path_string+str(method)+'/fold1', 'r') as file:
    for pair in file:
        pair=pair.replace('\n','')
        fold1_list.append(pair)

with open(path_string+str(method)+'/fold2', 'r') as file:
    for pair in file:
        pair=pair.replace('\n','')
        fold2_list.append(pair)

with open(path_string+str(method)+'/fold3', 'r') as file:
    for pair in file:
        pair=pair.replace('\n','')
        fold3_list.append(pair)

with open(path_string+str(method)+'/fold4', 'r') as file:
    for pair in file:
        pair=pair.replace('\n','')
        fold4_list.append(pair)

with open(path_string+str(method)+'/fold5', 'r') as file:
    for pair in file:
        pair=pair.replace('\n','')
        fold5_list.append(pair)

with open('/Users/brandonli/Desktop/classfier/feature_social', 'rb') as file:
    social_dict=pickle.load(file)

with open('/Users/brandonli/Desktop/classfier/feature_location', 'rb') as file:
    location_dict=pickle.load(file)

with open('/Users/brandonli/Desktop/classfier/feature_time', 'rb') as file:
    time_dict=pickle.load(file)

with open('/Users/brandonli/Desktop/classfier/feature_content', 'rb') as file:
    content_dict=pickle.load(file)


fold1_mnano_feature_list=[]
fold2_mnano_feature_list=[]
fold3_mnano_feature_list=[]
fold4_mnano_feature_list=[]
fold5_mnano_feature_list=[]


for key in content_dict:
    if content_dict[key].split('    ')[0]=='False':
        content_dict[key]='0    0'

for pair in fold1_list:
    fold1_mnano_feature_list.append(social_dict[pair]+'    '+str(location_dict[pair])+'    '+time_dict[pair]+'    '+content_dict[pair])

for pair in fold2_list:
    fold2_mnano_feature_list.append(
        social_dict[pair] + '    ' + str(location_dict[pair]) + '    ' + time_dict[pair] + '    ' + content_dict[pair])

for pair in fold3_list:
    fold3_mnano_feature_list.append(
        social_dict[pair] + '    ' + str(location_dict[pair]) + '    ' + time_dict[pair] + '    ' + content_dict[pair])

for pair in fold4_list:
    fold4_mnano_feature_list.append(
        social_dict[pair] + '    ' + str(location_dict[pair]) + '    ' + time_dict[pair] + '    ' + content_dict[pair])

for pair in fold5_list:
    fold5_mnano_feature_list.append(social_dict[pair]+'    '+str(location_dict[pair])+'    '+time_dict[pair]+'    '+content_dict[pair])
#
fold1_mnano_label_list=[]
fold2_mnano_label_list=[]
fold3_mnano_label_list=[]
fold4_mnano_label_list=[]
fold5_mnano_label_list=[]




for i in range(method):
   fold1_list[i] = fold1_list[i].split('    ')
   fold2_list[i] = fold2_list[i].split('    ')
   fold3_list[i] = fold3_list[i].split('    ')
   fold4_list[i] = fold4_list[i].split('    ')
   fold5_list[i] = fold5_list[i].split('    ')

   if fold1_list[i][0]== fold1_list[i][1]:
        fold1_mnano_label_list.append(1)
   else:
        fold1_mnano_label_list.append(0)

   if fold2_list[i][0]== fold2_list[i][1]:
        fold2_mnano_label_list.append(1)
   else:
        fold2_mnano_label_list.append(0)

   if fold3_list[i][0] == fold3_list[i][1]:
        fold3_mnano_label_list.append(1)
   else:
        fold3_mnano_label_list.append(0)

   if fold4_list[i][0] == fold4_list[i][1]:
        fold4_mnano_label_list.append(1)
   else:
        fold4_mnano_label_list.append(0)

   if fold5_list[i][0] == fold5_list[i][1]:
       fold5_mnano_label_list.append(1)
   else:
       fold5_mnano_label_list.append(0)

#fold1 train test
train_set1=[]
for i in range(method):
      mnano_feature= fold1_mnano_feature_list[i].split('    ')
      train_set1.append([ float(mnano_feature[0]), float(mnano_feature[1]),float(mnano_feature[2]), float(mnano_feature[3]),
                           float(mnano_feature[4]),float(mnano_feature[5]),float(mnano_feature[6]),float(mnano_feature[7])])
clf=SVC(probability=True)
clf.fit(train_set1, fold1_mnano_label_list)

#test fold2

fold2_test_mnano=[]
fold2_pro_mnano=[]

for item in fold2_mnano_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    item[3] = float(item[3])
    item[4] = float(item[4])
    item[5] = float(item[5])
    item[6] = float(item[6])
    item[7] = float(item[7])
    fold2_test_mnano.append(clf.predict([[item[0], item[1], item[2],item[3],item[4],item[5],item[6],item[7]]])[0])
    fold2_pro_mnano.append(clf.predict_proba([[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]]])[0][1])

pre_user_dict={}
pre_pro_dict={}

fold_temp=fold2_list
pro_temp=fold2_pro_mnano
test_temp=fold2_test_mnano
for i in range(method):
    if fold_temp[i][0] not in pre_user_dict.keys():
        pre_user_dict[fold_temp[i][0]]=[]
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]]=[]
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])
    else:
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])

for i in range(method):
    if test_temp[i]==1:
         if pro_temp[i]< max(pre_pro_dict[fold_temp[i][0]]):
             test_temp[i]=0


#test fold3

fold3_test_mnano=[]
fold3_pro_mnano=[]

for item in fold3_mnano_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    item[3] = float(item[3])
    item[4] = float(item[4])
    item[5] = float(item[5])
    item[6] = float(item[6])
    item[7] = float(item[7])
    fold3_test_mnano.append(clf.predict([[item[0], item[1], item[2],item[3],item[4],item[5],item[6],item[7]]])[0])
    fold3_pro_mnano.append(clf.predict_proba([[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]]])[0][1])

pre_user_dict={}
pre_pro_dict={}

fold_temp=fold3_list
pro_temp=fold3_pro_mnano
test_temp=fold3_test_mnano
for i in range(method):
    if fold_temp[i][0] not in pre_user_dict.keys():
        pre_user_dict[fold_temp[i][0]]=[]
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]]=[]
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])
    else:
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])

for i in range(method):
    if test_temp[i]==1:
         if pro_temp[i]< max(pre_pro_dict[fold_temp[i][0]]):
             test_temp[i]=0
# test fold4

fold4_test_mnano=[]
fold4_pro_mnano=[]

for item in fold4_mnano_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    item[3] = float(item[3])
    item[4] = float(item[4])
    item[5] = float(item[5])
    item[6] = float(item[6])
    item[7] = float(item[7])
    fold4_test_mnano.append(clf.predict([[item[0], item[1], item[2],item[3],item[4],item[5],item[6],item[7]]])[0])
    fold4_pro_mnano.append(clf.predict_proba([[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]]])[0][1])

pre_user_dict={}
pre_pro_dict={}

fold_temp=fold4_list
pro_temp=fold4_pro_mnano
test_temp=fold4_test_mnano
for i in range(method):
    if fold_temp[i][0] not in pre_user_dict.keys():
        pre_user_dict[fold_temp[i][0]]=[]
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]]=[]
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])
    else:
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])

for i in range(method):
    if test_temp[i]==1:
         if pro_temp[i]< max(pre_pro_dict[fold_temp[i][0]]):
             test_temp[i]=0
#test fold5

fold5_test_mnano=[]
fold5_pro_mnano=[]

for item in fold5_mnano_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    item[3] = float(item[3])
    item[4] = float(item[4])
    item[5] = float(item[5])
    item[6] = float(item[6])
    item[7] = float(item[7])
    fold5_test_mnano.append(clf.predict([[item[0], item[1], item[2],item[3],item[4],item[5],item[6],item[7]]])[0])
    fold5_pro_mnano.append(clf.predict_proba([[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]]])[0][1])

pre_user_dict={}
pre_pro_dict={}

fold_temp=fold5_list
pro_temp=fold5_pro_mnano
test_temp=fold5_test_mnano
for i in range(method):
    if fold_temp[i][0] not in pre_user_dict.keys():
        pre_user_dict[fold_temp[i][0]]=[]
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]]=[]
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])
    else:
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])

for i in range(method):
    if test_temp[i]==1:
         if pro_temp[i]< max(pre_pro_dict[fold_temp[i][0]]):
             test_temp[i]=0

mnano_result1=fold2_test_mnano+fold3_test_mnano+fold4_test_mnano+fold5_test_mnano
mnano_label1 = fold2_mnano_label_list+fold3_mnano_label_list+fold4_mnano_label_list+fold5_mnano_label_list
print(mnano_result1)
print(mnano_label1)


#fold2 train test
train_set2=[]
for i in range(method):
      mnano_feature= fold2_mnano_feature_list[i].split('    ')
      train_set2.append([ float(mnano_feature[0]), float(mnano_feature[1]),float(mnano_feature[2]), float(mnano_feature[3]),
                           float(mnano_feature[4]),float(mnano_feature[5]),float(mnano_feature[6]),float(mnano_feature[7])])
clf=SVC(probability=True)
clf.fit(train_set2, fold2_mnano_label_list)

#test fold1

fold1_test_mnano=[]
fold1_pro_mnano=[]

for item in fold1_mnano_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    item[3] = float(item[3])
    item[4] = float(item[4])
    item[5] = float(item[5])
    item[6] = float(item[6])
    item[7] = float(item[7])
    fold1_test_mnano.append(clf.predict([[item[0], item[1], item[2],item[3],item[4],item[5],item[6],item[7]]])[0])
    fold1_pro_mnano.append(clf.predict_proba([[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]]])[0][1])

pre_user_dict={}
pre_pro_dict={}

fold_temp=fold1_list
pro_temp=fold1_pro_mnano
test_temp=fold1_test_mnano
for i in range(method):
    if fold_temp[i][0] not in pre_user_dict.keys():
        pre_user_dict[fold_temp[i][0]]=[]
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]]=[]
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])
    else:
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])

for i in range(method):
    if test_temp[i]==1:
         if pro_temp[i]< max(pre_pro_dict[fold_temp[i][0]]):
             test_temp[i]=0


#test fold3

fold3_test_mnano=[]
fold3_pro_mnano=[]

for item in fold3_mnano_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    item[3] = float(item[3])
    item[4] = float(item[4])
    item[5] = float(item[5])
    item[6] = float(item[6])
    item[7] = float(item[7])
    fold3_test_mnano.append(clf.predict([[item[0], item[1], item[2],item[3],item[4],item[5],item[6],item[7]]])[0])
    fold3_pro_mnano.append(clf.predict_proba([[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]]])[0][1])

pre_user_dict={}
pre_pro_dict={}

fold_temp=fold3_list
pro_temp=fold3_pro_mnano
test_temp=fold3_test_mnano
for i in range(method):
    if fold_temp[i][0] not in pre_user_dict.keys():
        pre_user_dict[fold_temp[i][0]]=[]
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]]=[]
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])
    else:
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])

for i in range(method):
    if test_temp[i]==1:
         if pro_temp[i]< max(pre_pro_dict[fold_temp[i][0]]):
             test_temp[i]=0
# test fold4

fold4_test_mnano=[]
fold4_pro_mnano=[]

for item in fold4_mnano_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    item[3] = float(item[3])
    item[4] = float(item[4])
    item[5] = float(item[5])
    item[6] = float(item[6])
    item[7] = float(item[7])
    fold4_test_mnano.append(clf.predict([[item[0], item[1], item[2],item[3],item[4],item[5],item[6],item[7]]])[0])
    fold4_pro_mnano.append(clf.predict_proba([[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]]])[0][1])

pre_user_dict={}
pre_pro_dict={}

fold_temp=fold4_list
pro_temp=fold4_pro_mnano
test_temp=fold4_test_mnano
for i in range(method):
    if fold_temp[i][0] not in pre_user_dict.keys():
        pre_user_dict[fold_temp[i][0]]=[]
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]]=[]
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])
    else:
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])

for i in range(method):
    if test_temp[i]==1:
         if pro_temp[i]< max(pre_pro_dict[fold_temp[i][0]]):
             test_temp[i]=0
#test fold5

fold5_test_mnano=[]
fold5_pro_mnano=[]

for item in fold5_mnano_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    item[3] = float(item[3])
    item[4] = float(item[4])
    item[5] = float(item[5])
    item[6] = float(item[6])
    item[7] = float(item[7])
    fold5_test_mnano.append(clf.predict([[item[0], item[1], item[2],item[3],item[4],item[5],item[6],item[7]]])[0])
    fold5_pro_mnano.append(clf.predict_proba([[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]]])[0][1])

pre_user_dict={}
pre_pro_dict={}

fold_temp=fold5_list
pro_temp=fold5_pro_mnano
test_temp=fold5_test_mnano
for i in range(method):
    if fold_temp[i][0] not in pre_user_dict.keys():
        pre_user_dict[fold_temp[i][0]]=[]
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]]=[]
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])
    else:
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])

for i in range(method):
    if test_temp[i]==1:
         if pro_temp[i]< max(pre_pro_dict[fold_temp[i][0]]):
             test_temp[i]=0

mnano_result2=fold1_test_mnano+fold3_test_mnano+fold4_test_mnano+fold5_test_mnano
mnano_label2 = fold1_mnano_label_list+fold3_mnano_label_list+fold4_mnano_label_list+fold5_mnano_label_list
print(mnano_result2)
print(mnano_label2)

#fold3 train test
train_set3=[]
for i in range(method):
      mnano_feature= fold3_mnano_feature_list[i].split('    ')
      train_set3.append([ float(mnano_feature[0]), float(mnano_feature[1]),float(mnano_feature[2]), float(mnano_feature[3]),
                           float(mnano_feature[4]),float(mnano_feature[5]),float(mnano_feature[6]),float(mnano_feature[7])])
clf=SVC(probability=True)
clf.fit(train_set3, fold3_mnano_label_list)

#test fold1

fold1_test_mnano=[]
fold1_pro_mnano=[]

for item in fold1_mnano_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    item[3] = float(item[3])
    item[4] = float(item[4])
    item[5] = float(item[5])
    item[6] = float(item[6])
    item[7] = float(item[7])
    fold1_test_mnano.append(clf.predict([[item[0], item[1], item[2],item[3],item[4],item[5],item[6],item[7]]])[0])
    fold1_pro_mnano.append(clf.predict_proba([[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]]])[0][1])

pre_user_dict={}
pre_pro_dict={}

fold_temp=fold1_list
pro_temp=fold1_pro_mnano
test_temp=fold1_test_mnano
for i in range(method):
    if fold_temp[i][0] not in pre_user_dict.keys():
        pre_user_dict[fold_temp[i][0]]=[]
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]]=[]
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])
    else:
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])

for i in range(method):
    if test_temp[i]==1:
         if pro_temp[i]< max(pre_pro_dict[fold_temp[i][0]]):
             test_temp[i]=0


#test fold2

fold2_test_mnano=[]
fold2_pro_mnano=[]

for item in fold2_mnano_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    item[3] = float(item[3])
    item[4] = float(item[4])
    item[5] = float(item[5])
    item[6] = float(item[6])
    item[7] = float(item[7])
    fold2_test_mnano.append(clf.predict([[item[0], item[1], item[2],item[3],item[4],item[5],item[6],item[7]]])[0])
    fold2_pro_mnano.append(clf.predict_proba([[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]]])[0][1])

pre_user_dict={}
pre_pro_dict={}

fold_temp=fold2_list
pro_temp=fold2_pro_mnano
test_temp=fold2_test_mnano
for i in range(method):
    if fold_temp[i][0] not in pre_user_dict.keys():
        pre_user_dict[fold_temp[i][0]]=[]
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]]=[]
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])
    else:
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])

for i in range(method):
    if test_temp[i]==1:
         if pro_temp[i]< max(pre_pro_dict[fold_temp[i][0]]):
             test_temp[i]=0
# test fold4

fold4_test_mnano=[]
fold4_pro_mnano=[]

for item in fold4_mnano_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    item[3] = float(item[3])
    item[4] = float(item[4])
    item[5] = float(item[5])
    item[6] = float(item[6])
    item[7] = float(item[7])
    fold4_test_mnano.append(clf.predict([[item[0], item[1], item[2],item[3],item[4],item[5],item[6],item[7]]])[0])
    fold4_pro_mnano.append(clf.predict_proba([[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]]])[0][1])

pre_user_dict={}
pre_pro_dict={}

fold_temp=fold4_list
pro_temp=fold4_pro_mnano
test_temp=fold4_test_mnano
for i in range(method):
    if fold_temp[i][0] not in pre_user_dict.keys():
        pre_user_dict[fold_temp[i][0]]=[]
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]]=[]
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])
    else:
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])

for i in range(method):
    if test_temp[i]==1:
         if pro_temp[i]< max(pre_pro_dict[fold_temp[i][0]]):
             test_temp[i]=0
#test fold5

fold5_test_mnano=[]
fold5_pro_mnano=[]

for item in fold5_mnano_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    item[3] = float(item[3])
    item[4] = float(item[4])
    item[5] = float(item[5])
    item[6] = float(item[6])
    item[7] = float(item[7])
    fold5_test_mnano.append(clf.predict([[item[0], item[1], item[2],item[3],item[4],item[5],item[6],item[7]]])[0])
    fold5_pro_mnano.append(clf.predict_proba([[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]]])[0][1])

pre_user_dict={}
pre_pro_dict={}

fold_temp=fold5_list
pro_temp=fold5_pro_mnano
test_temp=fold5_test_mnano
for i in range(method):
    if fold_temp[i][0] not in pre_user_dict.keys():
        pre_user_dict[fold_temp[i][0]]=[]
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]]=[]
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])
    else:
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])

for i in range(method):
    if test_temp[i]==1:
         if pro_temp[i]< max(pre_pro_dict[fold_temp[i][0]]):
             test_temp[i]=0

mnano_result3=fold1_test_mnano+fold2_test_mnano+fold4_test_mnano+fold5_test_mnano
mnano_label3 = fold1_mnano_label_list+fold2_mnano_label_list+fold4_mnano_label_list+fold5_mnano_label_list
print(mnano_result3)
print(mnano_label3)

#fold4 train test
train_set4=[]
for i in range(method):
      mnano_feature= fold4_mnano_feature_list[i].split('    ')
      train_set4.append([ float(mnano_feature[0]), float(mnano_feature[1]),float(mnano_feature[2]), float(mnano_feature[3]),
                           float(mnano_feature[4]),float(mnano_feature[5]),float(mnano_feature[6]),float(mnano_feature[7])])
clf=SVC(probability=True)
clf.fit(train_set4, fold4_mnano_label_list)

#test fold1

fold1_test_mnano=[]
fold1_pro_mnano=[]

for item in fold1_mnano_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    item[3] = float(item[3])
    item[4] = float(item[4])
    item[5] = float(item[5])
    item[6] = float(item[6])
    item[7] = float(item[7])
    fold1_test_mnano.append(clf.predict([[item[0], item[1], item[2],item[3],item[4],item[5],item[6],item[7]]])[0])
    fold1_pro_mnano.append(clf.predict_proba([[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]]])[0][1])

pre_user_dict={}
pre_pro_dict={}

fold_temp=fold1_list
pro_temp=fold1_pro_mnano
test_temp=fold1_test_mnano
for i in range(method):
    if fold_temp[i][0] not in pre_user_dict.keys():
        pre_user_dict[fold_temp[i][0]]=[]
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]]=[]
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])
    else:
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])

for i in range(method):
    if test_temp[i]==1:
         if pro_temp[i]< max(pre_pro_dict[fold_temp[i][0]]):
             test_temp[i]=0


#test fold2

fold2_test_mnano=[]
fold2_pro_mnano=[]

for item in fold2_mnano_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    item[3] = float(item[3])
    item[4] = float(item[4])
    item[5] = float(item[5])
    item[6] = float(item[6])
    item[7] = float(item[7])
    fold2_test_mnano.append(clf.predict([[item[0], item[1], item[2],item[3],item[4],item[5],item[6],item[7]]])[0])
    fold2_pro_mnano.append(clf.predict_proba([[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]]])[0][1])

pre_user_dict={}
pre_pro_dict={}

fold_temp=fold2_list
pro_temp=fold2_pro_mnano
test_temp=fold2_test_mnano
for i in range(method):
    if fold_temp[i][0] not in pre_user_dict.keys():
        pre_user_dict[fold_temp[i][0]]=[]
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]]=[]
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])
    else:
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])

for i in range(method):
    if test_temp[i]==1:
         if pro_temp[i]< max(pre_pro_dict[fold_temp[i][0]]):
             test_temp[i]=0
# test fold3
fold3_test_mnano=[]
fold3_pro_mnano=[]

for item in fold3_mnano_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    item[3] = float(item[3])
    item[4] = float(item[4])
    item[5] = float(item[5])
    item[6] = float(item[6])
    item[7] = float(item[7])
    fold3_test_mnano.append(clf.predict([[item[0], item[1], item[2],item[3],item[4],item[5],item[6],item[7]]])[0])
    fold3_pro_mnano.append(clf.predict_proba([[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]]])[0][1])

pre_user_dict={}
pre_pro_dict={}

fold_temp=fold3_list
pro_temp=fold3_pro_mnano
test_temp=fold3_test_mnano
for i in range(method):
    if fold_temp[i][0] not in pre_user_dict.keys():
        pre_user_dict[fold_temp[i][0]]=[]
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]]=[]
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])
    else:
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])

for i in range(method):
    if test_temp[i]==1:
         if pro_temp[i]< max(pre_pro_dict[fold_temp[i][0]]):
             test_temp[i]=0
#test fold5

fold5_test_mnano=[]
fold5_pro_mnano=[]

for item in fold5_mnano_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    item[3] = float(item[3])
    item[4] = float(item[4])
    item[5] = float(item[5])
    item[6] = float(item[6])
    item[7] = float(item[7])
    fold5_test_mnano.append(clf.predict([[item[0], item[1], item[2],item[3],item[4],item[5],item[6],item[7]]])[0])
    fold5_pro_mnano.append(clf.predict_proba([[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]]])[0][1])

pre_user_dict={}
pre_pro_dict={}

fold_temp=fold5_list
pro_temp=fold5_pro_mnano
test_temp=fold5_test_mnano
for i in range(method):
    if fold_temp[i][0] not in pre_user_dict.keys():
        pre_user_dict[fold_temp[i][0]]=[]
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]]=[]
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])
    else:
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])

for i in range(method):
    if test_temp[i]==1:
         if pro_temp[i]< max(pre_pro_dict[fold_temp[i][0]]):
             test_temp[i]=0

mnano_result4=fold1_test_mnano+fold2_test_mnano+fold3_test_mnano+fold5_test_mnano
mnano_label4 = fold1_mnano_label_list+fold2_mnano_label_list+fold3_mnano_label_list+fold5_mnano_label_list
print(mnano_result4)
print(mnano_label4)

#fold5 train test
train_set5=[]
for i in range(method):
      mnano_feature= fold5_mnano_feature_list[i].split('    ')
      train_set5.append([ float(mnano_feature[0]), float(mnano_feature[1]),float(mnano_feature[2]), float(mnano_feature[3]),
                           float(mnano_feature[4]),float(mnano_feature[5]),float(mnano_feature[6]),float(mnano_feature[7])])
clf=SVC(probability=True)
clf.fit(train_set5, fold5_mnano_label_list)

#test fold1

fold1_test_mnano=[]
fold1_pro_mnano=[]

for item in fold1_mnano_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    item[3] = float(item[3])
    item[4] = float(item[4])
    item[5] = float(item[5])
    item[6] = float(item[6])
    item[7] = float(item[7])
    fold1_test_mnano.append(clf.predict([[item[0], item[1], item[2],item[3],item[4],item[5],item[6],item[7]]])[0])
    fold1_pro_mnano.append(clf.predict_proba([[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]]])[0][1])

pre_user_dict={}
pre_pro_dict={}

fold_temp=fold1_list
pro_temp=fold1_pro_mnano
test_temp=fold1_test_mnano
for i in range(method):
    if fold_temp[i][0] not in pre_user_dict.keys():
        pre_user_dict[fold_temp[i][0]]=[]
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]]=[]
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])
    else:
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])

for i in range(method):
    if test_temp[i]==1:
         if pro_temp[i]< max(pre_pro_dict[fold_temp[i][0]]):
             test_temp[i]=0


#test fold2

fold2_test_mnano=[]
fold2_pro_mnano=[]

for item in fold2_mnano_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    item[3] = float(item[3])
    item[4] = float(item[4])
    item[5] = float(item[5])
    item[6] = float(item[6])
    item[7] = float(item[7])
    fold2_test_mnano.append(clf.predict([[item[0], item[1], item[2],item[3],item[4],item[5],item[6],item[7]]])[0])
    fold2_pro_mnano.append(clf.predict_proba([[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]]])[0][1])

pre_user_dict={}
pre_pro_dict={}

fold_temp=fold2_list
pro_temp=fold2_pro_mnano
test_temp=fold2_test_mnano
for i in range(method):
    if fold_temp[i][0] not in pre_user_dict.keys():
        pre_user_dict[fold_temp[i][0]]=[]
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]]=[]
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])
    else:
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])

for i in range(method):
    if test_temp[i]==1:
         if pro_temp[i]< max(pre_pro_dict[fold_temp[i][0]]):
             test_temp[i]=0
# test fold3
fold3_test_mnano=[]
fold3_pro_mnano=[]

for item in fold3_mnano_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    item[3] = float(item[3])
    item[4] = float(item[4])
    item[5] = float(item[5])
    item[6] = float(item[6])
    item[7] = float(item[7])
    fold3_test_mnano.append(clf.predict([[item[0], item[1], item[2],item[3],item[4],item[5],item[6],item[7]]])[0])
    fold3_pro_mnano.append(clf.predict_proba([[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]]])[0][1])

pre_user_dict={}
pre_pro_dict={}

fold_temp=fold3_list
pro_temp=fold3_pro_mnano
test_temp=fold3_test_mnano
for i in range(method):
    if fold_temp[i][0] not in pre_user_dict.keys():
        pre_user_dict[fold_temp[i][0]]=[]
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]]=[]
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])
    else:
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])

for i in range(method):
    if test_temp[i]==1:
         if pro_temp[i]< max(pre_pro_dict[fold_temp[i][0]]):
             test_temp[i]=0
#test fold4

fold4_test_mnano=[]
fold4_pro_mnano=[]

for item in fold4_mnano_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    item[3] = float(item[3])
    item[4] = float(item[4])
    item[5] = float(item[5])
    item[6] = float(item[6])
    item[7] = float(item[7])
    fold4_test_mnano.append(clf.predict([[item[0], item[1], item[2],item[3],item[4],item[5],item[6],item[7]]])[0])
    fold4_pro_mnano.append(clf.predict_proba([[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]]])[0][1])

pre_user_dict={}
pre_pro_dict={}

fold_temp=fold4_list
pro_temp=fold4_pro_mnano
test_temp=fold4_test_mnano
for i in range(method):
    if fold_temp[i][0] not in pre_user_dict.keys():
        pre_user_dict[fold_temp[i][0]]=[]
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]]=[]
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])
    else:
        pre_user_dict[fold_temp[i][0]].append(fold_temp[i][1])
        pre_pro_dict[fold_temp[i][0]].append(pro_temp[i])

for i in range(method):
    if test_temp[i]==1:
         if pro_temp[i]< max(pre_pro_dict[fold_temp[i][0]]):
             test_temp[i]=0

mnano_result5=fold1_test_mnano+fold2_test_mnano+fold3_test_mnano+fold4_test_mnano
mnano_label5 = fold1_mnano_label_list+fold2_mnano_label_list+fold3_mnano_label_list+fold4_mnano_label_list
print(mnano_result5)
print(mnano_label5)

with open(path_string+str(method)+'/mna_result', 'w') as file:
    file.write(str(mnano_result1)+'\n')
    file.write(str(mnano_label1)+'\n')
    file.write(str(mnano_result2)+'\n')
    file.write(str(mnano_label2) + '\n')
    file.write(str(mnano_result3)+'\n')
    file.write(str(mnano_label3) + '\n')
    file.write(str(mnano_result4)+'\n')
    file.write(str(mnano_label4) + '\n')
    file.write(str(mnano_result5)+'\n')
    file.write(str(mnano_label5) + '\n')



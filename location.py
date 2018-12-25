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

with open('/Users/brandonli/Desktop/classfier/feature_location', 'rb') as file:
    location_dict=pickle.load(file)

fold1_loc_feature_list=[]
fold2_loc_feature_list=[]
fold3_loc_feature_list=[]
fold4_loc_feature_list=[]
fold5_loc_feature_list=[]




for pair in fold1_list:
    fold1_loc_feature_list.append(location_dict[pair])

for pair in fold2_list:
    fold2_loc_feature_list.append(location_dict[pair])

for pair in fold3_list:
    fold3_loc_feature_list.append(location_dict[pair])

for pair in fold4_list:
    fold4_loc_feature_list.append(location_dict[pair])

for pair in fold5_list:
    fold5_loc_feature_list.append(location_dict[pair])

fold1_loc_label_list=[]
fold2_loc_label_list=[]
fold3_loc_label_list=[]
fold4_loc_label_list=[]
fold5_loc_label_list=[]




for i in range(method):
   fold1_list[i] = fold1_list[i].split('    ')
   fold2_list[i] = fold2_list[i].split('    ')
   fold3_list[i] = fold3_list[i].split('    ')
   fold4_list[i] = fold4_list[i].split('    ')
   fold5_list[i] = fold5_list[i].split('    ')

   if fold1_list[i][0]== fold1_list[i][1]:
        fold1_loc_label_list.append(1)
   else:
        fold1_loc_label_list.append(0)

   if fold2_list[i][0]== fold2_list[i][1]:
        fold2_loc_label_list.append(1)
   else:
        fold2_loc_label_list.append(0)

   if fold3_list[i][0] == fold3_list[i][1]:
        fold3_loc_label_list.append(1)
   else:
        fold3_loc_label_list.append(0)

   if fold4_list[i][0] == fold4_list[i][1]:
        fold4_loc_label_list.append(1)
   else:
        fold4_loc_label_list.append(0)

   if fold5_list[i][0] == fold5_list[i][1]:
       fold5_loc_label_list.append(1)
   else:
       fold5_loc_label_list.append(0)



#fold1 train test
train_set1=[]
for i in range(method):
    train_set1.append([fold1_loc_feature_list[i]])
clf=SVC()
clf.fit(train_set1, fold1_loc_feature_list)


#test fold2
fold2_test_location=[]
for item in fold2_loc_feature_list:
    fold2_test_location.append(clf.predict(item)[0])



#test fold3
fold3_test_location=[]
for item in fold3_loc_feature_list:
    fold3_test_location.append(clf.predict(item)[0])



#test fold4
fold4_test_location=[]
for item in fold4_loc_feature_list:
    fold4_test_location.append(clf.predict(item)[0])



#test fold5
fold5_test_location=[]
for item in fold5_loc_feature_list:
    fold5_test_location.append(clf.predict(item)[0])


location_result1=fold2_test_location+fold3_test_location+fold4_test_location+fold5_test_location
location_label1 = fold2_loc_label_list+fold3_loc_label_list+fold4_loc_label_list+fold5_loc_label_list
print(location_result1)
print(location_label1)

#fold2 train test
train_set2=[]
for i in range(method):
    train_set2.append([fold2_loc_feature_list[i]])
clf=SVC()
clf.fit(train_set2, fold2_loc_feature_list)


#test fold1
fold1_test_location=[]
for item in fold1_loc_feature_list:
    fold1_test_location.append(clf.predict(item)[0])



#test fold3
fold3_test_location=[]
for item in fold3_loc_feature_list:
    fold3_test_location.append(clf.predict(item)[0])



#test fold4
fold4_test_location=[]
for item in fold4_loc_feature_list:
    fold4_test_location.append(clf.predict(item)[0])



#test fold5
fold5_test_location=[]
for item in fold5_loc_feature_list:
    fold5_test_location.append(clf.predict(item)[0])


location_result2=fold1_test_location+fold3_test_location+fold4_test_location+fold5_test_location
location_label2 = fold1_loc_label_list+fold3_loc_label_list+fold4_loc_label_list+fold5_loc_label_list
print(location_result2)
print(location_label2)

#fold3 train test
train_set3=[]
for i in range(method):
    train_set3.append([fold3_loc_feature_list[i]])
clf=SVC()
clf.fit(train_set3, fold3_loc_feature_list)


#test fold1
fold1_test_location=[]
for item in fold1_loc_feature_list:
    fold1_test_location.append(clf.predict(item)[0])



#test fold2
fold2_test_location=[]
for item in fold2_loc_feature_list:
    fold2_test_location.append(clf.predict(item)[0])



#test fold4
fold4_test_location=[]
for item in fold4_loc_feature_list:
    fold4_test_location.append(clf.predict(item)[0])



#test fold5
fold5_test_location=[]
for item in fold5_loc_feature_list:
    fold5_test_location.append(clf.predict(item)[0])


location_result3=fold1_test_location+fold2_test_location+fold4_test_location+fold5_test_location
location_label3 = fold1_loc_label_list+fold2_loc_label_list+fold4_loc_label_list+fold5_loc_label_list
print(location_result3)
print(location_label3)

#fold4 train test
train_set4=[]
for i in range(method):
    train_set4.append([fold4_loc_feature_list[i]])
clf=SVC()
clf.fit(train_set4, fold4_loc_feature_list)


#test fold1
fold1_test_location=[]
for item in fold1_loc_feature_list:
    fold1_test_location.append(clf.predict(item)[0])



#test fold2
fold2_test_location=[]
for item in fold2_loc_feature_list:
    fold2_test_location.append(clf.predict(item)[0])



#test fold3
fold3_test_location=[]
for item in fold3_loc_feature_list:
    fold3_test_location.append(clf.predict(item)[0])



#test fold5
fold5_test_location=[]
for item in fold5_loc_feature_list:
    fold5_test_location.append(clf.predict(item)[0])


location_result4=fold1_test_location+fold2_test_location+fold3_test_location+fold5_test_location
location_label4 = fold1_loc_label_list+fold2_loc_label_list+fold3_loc_label_list+fold5_loc_label_list
print(location_result4)
print(location_label4)

#fold5 train test
train_set5=[]
for i in range(method):
    train_set5.append([fold5_loc_feature_list[i]])
clf=SVC()
clf.fit(train_set5, fold5_loc_feature_list)


#test fold1
fold1_test_location=[]
for item in fold1_loc_feature_list:
    fold1_test_location.append(clf.predict(item)[0])



#test fold2
fold2_test_location=[]
for item in fold2_loc_feature_list:
    fold2_test_location.append(clf.predict(item)[0])



#test fold3
fold3_test_location=[]
for item in fold3_loc_feature_list:
    fold3_test_location.append(clf.predict(item)[0])



#test fold4
fold4_test_location=[]
for item in fold4_loc_feature_list:
    fold4_test_location.append(clf.predict(item)[0])


location_result5=fold1_test_location+fold2_test_location+fold3_test_location+fold4_test_location
location_label5 = fold1_loc_label_list+fold2_loc_label_list+fold3_loc_label_list+fold4_loc_label_list
print(location_result5)
print(location_label5)


with open(path_string+str(method)+'/location_result', 'w') as file:
    file.write(str(location_result1)+'\n')
    file.write(str(location_label1)+'\n')
    file.write(str(location_result2)+'\n')
    file.write(str(location_label2) + '\n')
    file.write(str(location_result3)+'\n')
    file.write(str(location_label3) + '\n')
    file.write(str(location_result4)+'\n')
    file.write(str(location_label4) + '\n')
    file.write(str(location_result5)+'\n')
    file.write(str(location_label5) + '\n')



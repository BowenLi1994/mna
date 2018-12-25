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

fold1_social_feature_list=[]
fold2_social_feature_list=[]
fold3_social_feature_list=[]
fold4_social_feature_list=[]
fold5_social_feature_list=[]




for pair in fold1_list:
    fold1_social_feature_list.append(social_dict[pair])

for pair in fold2_list:
    fold2_social_feature_list.append(social_dict[pair])

for pair in fold3_list:
    fold3_social_feature_list.append(social_dict[pair])

for pair in fold4_list:
    fold4_social_feature_list.append(social_dict[pair])

for pair in fold5_list:
    fold5_social_feature_list.append(social_dict[pair])

fold1_social_label_list=[]
fold2_social_label_list=[]
fold3_social_label_list=[]
fold4_social_label_list=[]
fold5_social_label_list=[]




for i in range(method):
   fold1_list[i] = fold1_list[i].split('    ')
   fold2_list[i] = fold2_list[i].split('    ')
   fold3_list[i] = fold3_list[i].split('    ')
   fold4_list[i] = fold4_list[i].split('    ')
   fold5_list[i] = fold5_list[i].split('    ')

   if fold1_list[i][0]== fold1_list[i][1]:
        fold1_social_label_list.append(1)
   else:
        fold1_social_label_list.append(0)

   if fold2_list[i][0]== fold2_list[i][1]:
        fold2_social_label_list.append(1)
   else:
        fold2_social_label_list.append(0)

   if fold3_list[i][0] == fold3_list[i][1]:
        fold3_social_label_list.append(1)
   else:
        fold3_social_label_list.append(0)

   if fold4_list[i][0] == fold4_list[i][1]:
        fold4_social_label_list.append(1)
   else:
        fold4_social_label_list.append(0)

   if fold5_list[i][0] == fold5_list[i][1]:
       fold5_social_label_list.append(1)
   else:
       fold5_social_label_list.append(0)

#fold1 train test
train_set1=[]
for i in range(method):
      social_feature= fold1_social_feature_list[i].split('    ')
      train_set1.append([float(social_feature[0]), float(social_feature[1]),float(social_feature[2])])
clf=SVC()
clf.fit(train_set1, fold1_social_label_list)
#test fold2
fold2_test_social=[]
for item in fold2_social_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    fold2_test_social.append(clf.predict([[item[0], item[1], item[2]]])[0])
#test fold3
fold3_test_social=[]
for item in fold3_social_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    fold3_test_social.append(clf.predict([[item[0], item[1], item[2]]])[0])
#test fold4
fold4_test_social=[]
for item in fold4_social_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    fold4_test_social.append(clf.predict([[item[0], item[1], item[2]]])[0])
#test fold5
fold5_test_social=[]
for item in fold5_social_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    fold5_test_social.append(clf.predict([[item[0], item[1], item[2]]])[0])


social_result1=fold2_test_social+fold3_test_social+fold4_test_social+fold5_test_social
social_label1 = fold2_social_label_list+fold3_social_label_list+fold4_social_label_list+fold5_social_label_list
print(social_result1)
print(social_label1)

#fold2 train test
train_set2=[]
for i in range(method):
      social_feature= fold2_social_feature_list[i].split('    ')
      train_set2.append([float(social_feature[0]), float(social_feature[1]),float(social_feature[2])])
clf=SVC()
clf.fit(train_set2, fold2_social_label_list)
#test fold1
fold1_test_social=[]
for item in fold1_social_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    fold1_test_social.append(clf.predict([[item[0], item[1], item[2]]])[0])
#test fold3
fold3_test_social=[]
for item in fold3_social_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    fold3_test_social.append(clf.predict([[item[0], item[1], item[2]]])[0])
#test fold4
fold4_test_social=[]
for item in fold4_social_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    fold4_test_social.append(clf.predict([[item[0], item[1], item[2]]])[0])
#test fold5
fold5_test_social=[]
for item in fold5_social_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    fold5_test_social.append(clf.predict([[item[0], item[1], item[2]]])[0])


social_result2=fold1_test_social+fold3_test_social+fold4_test_social+fold5_test_social
social_label2 = fold1_social_label_list+fold3_social_label_list+fold4_social_label_list+fold5_social_label_list
print(social_result2)
print(social_label2)

#fold3 train test
train_set3=[]
for i in range(method):
      social_feature= fold3_social_feature_list[i].split('    ')
      train_set3.append([float(social_feature[0]), float(social_feature[1]),float(social_feature[2])])
clf=SVC()
clf.fit(train_set3, fold3_social_label_list)
#test fold1
fold1_test_social=[]
for item in fold1_social_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    fold1_test_social.append(clf.predict([[item[0], item[1], item[2]]])[0])
#test fold2
fold2_test_social=[]
for item in fold2_social_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    fold2_test_social.append(clf.predict([[item[0], item[1], item[2]]])[0])
#test fold4
fold4_test_social=[]
for item in fold4_social_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    fold4_test_social.append(clf.predict([[item[0], item[1], item[2]]])[0])
#test fold5
fold5_test_social=[]
for item in fold5_social_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    fold5_test_social.append(clf.predict([[item[0], item[1], item[2]]])[0])


social_result3=fold1_test_social+fold2_test_social+fold4_test_social+fold5_test_social
social_label3 = fold1_social_label_list+fold2_social_label_list+fold4_social_label_list+fold5_social_label_list
print(social_result3)
print(social_label3)

#fold4 train test
train_set4=[]
for i in range(method):
      social_feature= fold4_social_feature_list[i].split('    ')
      train_set4.append([float(social_feature[0]), float(social_feature[1]),float(social_feature[2])])
clf=SVC()
clf.fit(train_set4, fold4_social_label_list)
#test fold1
fold1_test_social=[]
for item in fold1_social_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    fold1_test_social.append(clf.predict([[item[0], item[1], item[2]]])[0])
#test fold2
fold2_test_social=[]
for item in fold2_social_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    fold2_test_social.append(clf.predict([[item[0], item[1], item[2]]])[0])
#test fold3
fold3_test_social=[]
for item in fold3_social_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    fold3_test_social.append(clf.predict([[item[0], item[1], item[2]]])[0])
#test fold5
fold5_test_social=[]
for item in fold5_social_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    fold5_test_social.append(clf.predict([[item[0], item[1], item[2]]])[0])


social_result4=fold1_test_social+fold2_test_social+fold3_test_social+fold5_test_social
social_label4 = fold1_social_label_list+fold2_social_label_list+fold3_social_label_list+fold5_social_label_list
print(social_result4)
print(social_label4)

#fold5 train test
train_set5=[]
for i in range(method):
      social_feature= fold5_social_feature_list[i].split('    ')
      train_set5.append([float(social_feature[0]), float(social_feature[1]),float(social_feature[2])])
clf=SVC()
clf.fit(train_set5, fold5_social_label_list)
#test fold1
fold1_test_social=[]
for item in fold1_social_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    fold1_test_social.append(clf.predict([[item[0], item[1], item[2]]])[0])
#test fold2
fold2_test_social=[]
for item in fold2_social_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    fold2_test_social.append(clf.predict([[item[0], item[1], item[2]]])[0])
#test fold3
fold3_test_social=[]
for item in fold3_social_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    fold3_test_social.append(clf.predict([[item[0], item[1], item[2]]])[0])
#test fold4
fold4_test_social=[]
for item in fold4_social_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    item[2]=float(item[2])
    fold4_test_social.append(clf.predict([[item[0], item[1], item[2]]])[0])


social_result5=fold1_test_social+fold2_test_social+fold3_test_social+fold4_test_social
social_label5 = fold1_social_label_list+fold2_social_label_list+fold3_social_label_list+fold4_social_label_list
print(social_result5)
print(social_label5)


with open(path_string+str(method)+'/social_result', 'w') as file:
    file.write(str(social_result1)+'\n')
    file.write(str(social_label1)+'\n')
    file.write(str(social_result2)+'\n')
    file.write(str(social_label2) + '\n')
    file.write(str(social_result3)+'\n')
    file.write(str(social_label3) + '\n')
    file.write(str(social_result4)+'\n')
    file.write(str(social_label4) + '\n')
    file.write(str(social_result5)+'\n')
    file.write(str(social_label5) + '\n')



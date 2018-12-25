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

with open('/Users/brandonli/Desktop/classfier/feature_content', 'rb') as file:
    content_dict=pickle.load(file)

fold1_content_feature_list=[]
fold2_content_feature_list=[]
fold3_content_feature_list=[]
fold4_content_feature_list=[]
fold5_content_feature_list=[]



for pair in fold1_list:
    fold1_content_feature_list.append(content_dict[pair])

for pair in fold2_list:
    fold2_content_feature_list.append(content_dict[pair])

for pair in fold3_list:
    fold3_content_feature_list.append(content_dict[pair])

for pair in fold4_list:
    fold4_content_feature_list.append(content_dict[pair])

for pair in fold5_list:
    fold5_content_feature_list.append(content_dict[pair])


for i in range(len(fold1_content_feature_list)):
    temp=fold1_content_feature_list[i].split('    ')
    if temp[0]=='False' or temp[1]=='nan':
        fold1_content_feature_list[i]='0    0'


for i in range(len(fold2_content_feature_list)):
    temp=fold2_content_feature_list[i].split('    ')
    if temp[0]=='False' or temp[1]=='nan':
        fold2_content_feature_list[i]='0    0'

for i in range(len(fold3_content_feature_list)):
    temp=fold3_content_feature_list[i].split('    ')
    if temp[0]=='False' or temp[1]=='nan':
        fold3_content_feature_list[i]='0    0'

for i in range(len(fold4_content_feature_list)):
    temp=fold4_content_feature_list[i].split('    ')
    if temp[0]=='False' or temp[1]=='nan':
        fold4_content_feature_list[i]='0    0'

for i in range(len(fold5_content_feature_list)):
    temp=fold5_content_feature_list[i].split('    ')
    if temp[0]=='False' or temp[1]=='nan':
        fold5_content_feature_list[i]='0    0'

fold1_content_label_list=[]
fold2_content_label_list=[]
fold3_content_label_list=[]
fold4_content_label_list=[]
fold5_content_label_list=[]

for i in range(method):
   fold1_list[i] = fold1_list[i].split('    ')
   fold2_list[i] = fold2_list[i].split('    ')
   fold3_list[i] = fold3_list[i].split('    ')
   fold4_list[i] = fold4_list[i].split('    ')
   fold5_list[i] = fold5_list[i].split('    ')

   if fold1_list[i][0]== fold1_list[i][1]:
        fold1_content_label_list.append(1)
   else:
        fold1_content_label_list.append(0)

   if fold2_list[i][0]== fold2_list[i][1]:
        fold2_content_label_list.append(1)
   else:
        fold2_content_label_list.append(0)

   if fold3_list[i][0] == fold3_list[i][1]:
        fold3_content_label_list.append(1)
   else:
        fold3_content_label_list.append(0)

   if fold4_list[i][0] == fold4_list[i][1]:
        fold4_content_label_list.append(1)
   else:
        fold4_content_label_list.append(0)

   if fold5_list[i][0] == fold5_list[i][1]:
       fold5_content_label_list.append(1)
   else:
       fold5_content_label_list.append(0)

#fold1 train test
train_set1=[]
for i in range(method):
      content_feature= fold1_content_feature_list[i].split('    ')
      train_set1.append([float(content_feature[0]),float(content_feature[1])])
clf=SVC()
clf.fit(train_set1, fold1_content_label_list)
#
#test fold2
fold2_test_content=[]
for item in fold2_content_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    fold2_test_content.append(clf.predict([[item[0],item[1]]])[0])

#test fold3
fold3_test_content=[]
for item in fold3_content_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    fold3_test_content.append(clf.predict([[item[0],item[1]]])[0])

#test fold4
fold4_test_content=[]
for item in fold4_content_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    fold4_test_content.append(clf.predict([[item[0],item[1]]])[0])


#test fold5
fold5_test_content=[]
for item in fold5_content_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    fold5_test_content.append(clf.predict([[item[0],item[1]]])[0])


content_result1=fold2_test_content+fold3_test_content+fold4_test_content+fold5_test_content
content_label1 = fold2_content_label_list+fold3_content_label_list+fold4_content_label_list+fold5_content_label_list
print(content_result1)
print(content_label1)

#fold2 train test
train_set2=[]
for i in range(method):
      content_feature= fold2_content_feature_list[i].split('    ')
      if content_feature[0]=='False' or content_feature[1]=='nan'or content_feature[0]=='nan' or content_feature[1]=='False':
          content_feature[0]=0
          content_feature[1]=0
      train_set2.append([float(content_feature[0]),float(content_feature[1])])
clf=SVC()
clf.fit(train_set2, fold2_content_label_list)


#test fold1
fold1_test_content=[]
for item in fold1_content_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    fold1_test_content.append(clf.predict([[item[0],item[1]]])[0])

#test fold3
fold3_test_content=[]
for item in fold3_content_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    fold3_test_content.append(clf.predict([[item[0],item[1]]])[0])

#test fold4
fold4_test_content=[]
for item in fold4_content_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    fold4_test_content.append(clf.predict([[item[0],item[1]]])[0])


#test fold5
fold5_test_content=[]
for item in fold5_content_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    fold5_test_content.append(clf.predict([[item[0],item[1]]])[0])


content_result2=fold1_test_content+fold3_test_content+fold4_test_content+fold5_test_content
content_label2 = fold1_content_label_list+fold3_content_label_list+fold4_content_label_list+fold5_content_label_list
print(content_result2)
print(content_label2)

#fold3 train test
train_set3=[]
for i in range(method):
      content_feature= fold3_content_feature_list[i].split('    ')
      train_set3.append([float(content_feature[0]),float(content_feature[1])])
clf=SVC()
clf.fit(train_set3, fold3_content_label_list)


#test fold1
fold1_test_content=[]
for item in fold1_content_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    fold1_test_content.append(clf.predict([[item[0],item[1]]])[0])

#test fold2
fold2_test_content=[]
for item in fold2_content_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    fold2_test_content.append(clf.predict([[item[0],item[1]]])[0])

#test fold4
fold4_test_content=[]
for item in fold4_content_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    fold4_test_content.append(clf.predict([[item[0],item[1]]])[0])


#test fold5
fold5_test_content=[]
for item in fold5_content_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    fold5_test_content.append(clf.predict([[item[0],item[1]]])[0])


content_result3=fold1_test_content+fold2_test_content+fold4_test_content+fold5_test_content
content_label3 = fold1_content_label_list+fold2_content_label_list+fold4_content_label_list+fold5_content_label_list
print(content_result3)
print(content_label3)

#fold4 train test
train_set4=[]
for i in range(method):
      content_feature= fold4_content_feature_list[i].split('    ')
      train_set4.append([float(content_feature[0]),float(content_feature[1])])
clf=SVC()
clf.fit(train_set4, fold4_content_label_list)


#test fold1
fold1_test_content=[]
for item in fold1_content_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    fold1_test_content.append(clf.predict([[item[0],item[1]]])[0])

#test fold2
fold2_test_content=[]
for item in fold2_content_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    fold2_test_content.append(clf.predict([[item[0],item[1]]])[0])

#test fold3
fold3_test_content=[]
for item in fold3_content_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    fold3_test_content.append(clf.predict([[item[0],item[1]]])[0])


#test fold5
fold5_test_content=[]
for item in fold5_content_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    fold5_test_content.append(clf.predict([[item[0],item[1]]])[0])


content_result4=fold1_test_content+fold2_test_content+fold3_test_content+fold5_test_content
content_label4 = fold1_content_label_list+fold2_content_label_list+fold3_content_label_list+fold5_content_label_list
print(content_result4)
print(content_label4)

#fold5 train test
train_set5=[]
for i in range(method):
      content_feature= fold5_content_feature_list[i].split('    ')
      train_set5.append([float(content_feature[0]),float(content_feature[1])])
clf=SVC()
clf.fit(train_set5, fold5_content_label_list)


#test fold1
fold1_test_content=[]
for item in fold1_content_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    fold1_test_content.append(clf.predict([[item[0],item[1]]])[0])

#test fold2
fold2_test_content=[]
for item in fold2_content_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    fold2_test_content.append(clf.predict([[item[0],item[1]]])[0])

#test fold3
fold3_test_content=[]
for item in fold3_content_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    fold3_test_content.append(clf.predict([[item[0],item[1]]])[0])


#test fold4
fold4_test_content=[]
for item in fold4_content_feature_list:
    item=item.split('    ')
    item[0]=float(item[0])
    item[1]=float(item[1])
    fold4_test_content.append(clf.predict([[item[0],item[1]]])[0])


content_result5=fold1_test_content+fold2_test_content+fold3_test_content+fold4_test_content
content_label5 = fold1_content_label_list+fold2_content_label_list+fold3_content_label_list+fold4_content_label_list
print(content_result5)
print(content_label5)




with open(path_string+str(method)+'/content_result', 'w') as file:
    file.write(str(content_result1)+'\n')
    file.write(str(content_label1)+'\n')
    file.write(str(content_result2)+'\n')
    file.write(str(content_label2) + '\n')
    file.write(str(content_result3)+'\n')
    file.write(str(content_label3) + '\n')
    file.write(str(content_result4)+'\n')
    file.write(str(content_label4) + '\n')
    file.write(str(content_result5)+'\n')
    file.write(str(content_label5) + '\n')



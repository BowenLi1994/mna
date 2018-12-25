#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Bowen Li'

import re
import pickle




class Usertip(object):

    def __init__(self, userid, tipid):
        self.userid = userid
        self.tipid = tipid

        def get_userid(self):
            return self.userid

        def get_tipid(self):
            return self.tipid

with open('/Users/brandonli/Desktop/four/user_tip_dic/tip_dict', 'rb') as f:
   tip_dict=pickle.load(f)


with open('/Users/brandonli/Desktop/four/user_tip_dic/userTip', 'r') as file:
    users_tip_temp_list=[]
    for users_tip in file:
        final_users_tip = users_tip.split('    ')
        users_tip_temp_list.append(final_users_tip)
    no_users_tip = len(users_tip_temp_list)
    users_tip_list=[]
    users_tip_dic = {}
    for i in range(no_users_tip):
        users_tip_temp_list[i][0] = users_tip_temp_list[i][0].replace('\n', '')
        users_tip_temp_list[i][0] = users_tip_temp_list[i][0].lower()
        users_tip_temp_list[i][1] = users_tip_temp_list[i][1].replace('\n', '')
        users_tip_temp_list[i][1] = users_tip_temp_list[i][1].lower()
        # print(users_tip_temp_list[i][0], users_tip_temp_list[i][1])
        if users_tip_temp_list[i][0] not in users_tip_dic.keys():
            users_tip_dic[users_tip_temp_list[i][0]] = {}
            if users_tip_temp_list[i][1] in tip_dict.keys():
                users_tip_dic[users_tip_temp_list[i][0]][users_tip_temp_list[i][1]] = tip_dict[
                    users_tip_temp_list[i][1]]
        else:
            if users_tip_temp_list[i][1] in tip_dict.keys():
                users_tip_dic[users_tip_temp_list[i][0]][users_tip_temp_list[i][1]] = tip_dict[
                    users_tip_temp_list[i][1]]
print(users_tip_dic.keys())
print(users_tip_dic['11carhun08'])

with open('/Users/brandonli/Desktop/four/user_tip_dic/user_tip_dic', 'wb') as f:
    pickle.dump(users_tip_dic, f)


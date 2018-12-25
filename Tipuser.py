#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Bowen Li'

class User(object):

    def __init__(self, userid, userurl, username, userhometown, twitterid):
        self.userid = userid
        self.userurl = userurl
        self.username = username
        self.userhometown=userhometown
        self.twitterid=twitterid

        def get_userid(self):
            return self.userid

        def get_userurl(self):
            return self.userurl


        def get_username(self):
            return self.username

        def get_usehometown(self):
            return self.userhometown

        def get_twitterid(self):
            return self.twitterid

with open('/Users/brandonli/Desktop/four/fouruser/foursquare_users', 'r') as file:
    users_temp_list=[]
    for user in file:
        final_user = user.split('    ')
        users_temp_list.append(final_user)
    no_user = len(users_temp_list)
    users_list=[]
    users_userid_list=[]
    for i in range(no_user):
        ur_a=User(users_temp_list[i][0], users_temp_list[i][1], users_temp_list[i][2], users_temp_list[i][3], users_temp_list[i][4])
        users_list.append(ur_a)
        users_userid_list.append(ur_a.userid)
    print(len(users_userid_list))


class Usertip(object):

    def __init__(self, userid, tipid):
        self.userid = userid
        self.tipid = tipid

        def get_userid(self):
            return self.userid

        def get_tipid(self):
            return self.tipid

with open('/Users/brandonli/Desktop/data/foursquare/tips/user_tip', 'r') as file:
    users_tip_temp_list=[]
    for users_tip in file:
        final_users_tip = users_tip.split('	')
        users_tip_temp_list.append(final_users_tip)
        no_users_tip = len(users_tip_temp_list)
    print(no_users_tip)
    users_tip_list=[]
    for i in range(no_users_tip):
        users_tip_temp_list[i][0]=users_tip_temp_list[i][0].lower()
        if users_tip_temp_list[i][0] in users_userid_list:
            ut_a=Usertip(users_tip_temp_list[i][0], users_tip_temp_list[i][1])
            users_tip_list.append(ut_a)

    f = open('/Users/brandonli/Desktop/four/fouruser/userTip', 'w')
    for ut in users_tip_list:
        f.write(ut.userid+'    '+ut.tipid)
    f.close()
#
#
print(len(users_tip_list)) #1002895





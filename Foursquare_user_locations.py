#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Bowen Li'

from geopy.geocoders import Nominatim


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

with open('/Users/brandonli/Desktop/four/four_user_location/foursquare_users', 'r') as file:
    users_temp_list=[]
    for user in file:
        final_user = user.split('    ')
        users_temp_list.append(final_user)
    no_user = len(users_temp_list)
    users_list=[]
    for i in range(no_user):
        ur_a=User(users_temp_list[i][0], users_temp_list[i][1], users_temp_list[i][2], users_temp_list[i][3], users_temp_list[i][4])
        users_list.append(ur_a)
    print(no_user)

    with open('/Users/brandonli/Desktop/four/four_user_location/foursquare_users_location', 'w') as file:
        for user in users_list:
            print(user.userhometown)
            geolocator = Nominatim()
            location = geolocator.geocode(user.userhometown)
            if(type(location) != type(None)):
                print(user.userid, location.latitude, location.longitude)
                temp_string = user.userid+'    '+str(location.latitude)+'    '+str(location.longitude)+'\n'
                file.write(temp_string)
            else:
                temp_string = user.userid + '    ' + 'NULL' + '    ' + 'NULL' + '\n'
                file.write(temp_string)
                print(user.userid, 'Null','Null')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Bowen Li'

import pickle
import time
from scipy import spatial

class Tuser(object):

    def __init__(self, tid,other):
        self.tid = tid
        self.other = other

        def get_tid(self):
            return self.tid

        def get_other(self):
            return self.other

class Fuser(object):

    def __init__(self, fid, other):
        self.fid = fid
        self.other = other

        def get_fid(self):
            return self.fid

        def get_other(self):
            return self.other



with open('/Users/brandonli/Desktop/feature/time/twitter_users', 'r') as file:
    tuser_temp_list=[]
    for tuser in file:
        final_tuser = tuser.split('    ',1)
        tuser_temp_list.append(final_tuser)
    no_tuser = len(tuser_temp_list)
    tuser_list=[]
    for i in range(no_tuser):
        tuser_a=Tuser(tuser_temp_list[i][0], tuser_temp_list[i][1])
        tuser_list.append(tuser_a)



with open('/Users/brandonli/Desktop/feature/time/foursquare_users', 'r') as file:
    fuser_temp_list=[]
    for fuser in file:
        final_fuser = fuser.split('    ',1)
        fuser_temp_list.append(final_fuser)
    no_fuser = len(fuser_temp_list)
    fuser_list=[]
    for i in range(no_fuser):
        fuser_a=Fuser(fuser_temp_list[i][0], fuser_temp_list[i][1])
        fuser_list.append(fuser_a)

with open('/Users/brandonli/Desktop/feature/time/user_tweettime_dict', 'rb') as file:
    tweet_time_dict=pickle.load(file)

with open('/Users/brandonli/Desktop/feature/time/user_tiptime_dict', 'rb') as file:
    tip_time_dict=pickle.load(file)


tweet_time_vector_dict={}
for key in tweet_time_dict:
    tweet_time_vector_dict[key]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for times in tweet_time_dict[key]:
        times=times.replace('________','')
        hour=times.split(':')[0]
        # if hour[0] not in ['0','1','2','3','4','5','6','7','8','9']:
        #     print(hour)
        tweet_time_vector_dict[key][int(hour)] = tweet_time_vector_dict[key][int(hour)]+1
    # print(tweet_time_vector_dict[key])

tip_time_vector_dict = {}
for key in tip_time_dict:
    tip_time_vector_dict[key] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for times in tip_time_dict[key]:
        times=time.ctime(int(times))
        tip_time_vector_dict[key][int(times[11]+times[12])]= tip_time_vector_dict[key][int(times[11]+times[12])]+1


for tuser in tuser_list:
    if tuser.tid not in tweet_time_vector_dict.keys():
        tweet_time_vector_dict[tuser.tid]= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for fuser in fuser_list:
    if fuser.fid not in tip_time_vector_dict.keys():
        tip_time_vector_dict[fuser.fid]= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

time_dict={}
for i in range(500):
    for t in range(500):
        time_slot=0
        sum_tweet=0
        sum_tip=0
        for m in range(24):
            sum_tweet=sum_tweet+tweet_time_vector_dict[tuser_list[i].tid][m]
            sum_tip=sum_tip+ tip_time_vector_dict[fuser_list[t].fid][m]
            if tweet_time_vector_dict[tuser_list[i].tid][m]!=0 and tip_time_vector_dict[fuser_list[t].fid][m]!=0:
                time_slot=time_slot+1
        if sum_tip!=0 and sum_tweet!=0:
            similarity=1-spatial.distance.cosine(tweet_time_vector_dict[tuser_list[i].tid],tip_time_vector_dict[fuser_list[t].fid])
        else:
            similarity=0

        temp_string=tuser_list[i].tid+'    '+fuser_list[t].fid+'    '+str(time_slot)+'    '+str(similarity)
        time_dict[tuser_list[i].tid+'    '+fuser_list[t].fid]= str(time_slot)+'    '+str(similarity)

#
#
with open('/Users/brandonli/Desktop/feature/time/feature_time', 'wb') as file:
    pickle.dump(time_dict,file)
#
for key in time_dict:
    print(key, time_dict[key])
# with open('/Users/brandonli/Desktop/feature/location/feature_location', 'wb') as file:
#     pickle.dump(user_location_feature_dict,file)
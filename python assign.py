# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 01:09:04 2020

@author: KD073143
"""


from collections import Counter 
 
# tweets =  'sachin  tweet_id_1, sehwag  tweet_id_2, sachin  tweet_id_3, sachin  tweet_id_4'
# print("tweets = ",tweets)
# res = dict(item.split("  ") for item in tweets.split(", "))
          
# # Printing resultant string 
# print ("Resultant dictionary", str(res)) 
# values_per_key = {}
# for d in res:
#     for k, v in d.items():
#         values_per_key.setdefault(k, set()).add(v)
# counts = {k: len(v) for k, v in values_per_key.items()}
# print (counts)
tweet_names = ["sachin tweet_id_1",  
               "sehwag tweet_id_2", 
               "sachin tweet_id_3", 
               "sachin tweet_id_4"]  
    
uniq_names = [pref_names.split()[0] for
              pref_names in tweet_names] 
  
times = Counter(uniq_names) 
repeat = times.values() 
  
for element in set(repeat): 
    dupl = ([(key, value) for
             key, value in sorted(times.items()) if
             value == element]) 
      
    if len(dupl) > 1: 
        for (key, value) in dupl: 
            print (key,'',value) 
    max_value = max(times.values()) 
    temp_max_result = [(key, value) for 
                       key, value in sorted(times.items()) if
                       value == max_value] 
      
    if temp_max_result != dupl: 
        for (key,value) in temp_max_result: 
            print (key,'',value) 
             
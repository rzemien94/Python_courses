# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:35:34 2022

@author: rzemi
"""

from datetime import datetime
 
def time_span_m(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 60)[0]
 
def time_span_h(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 3600)[0]
 
def time_span_d(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 86400)[0]

start = datetime(2019, 1, 1, 0, 0, 0)  
end  = datetime.now()
 
print(time_span_m(start, end))
print(time_span_h(start, end))
print(time_span_d(start, end))

def create_function(span):
    try:
        if not(span in ['m','h','d']):
            raise TypeError("bad choice")
        sec=0
        if span == 'm':
            sec=60
        elif span == 'h':
            sec=3600
        else:
            sec=86400
        source='''
def f(start, end):
   duration = end - start
   duration_in_s = duration.total_seconds()
   return divmod(duration_in_s, {})[0]   
'''.format(sec)
        exec(source,globals())
        return f
    except Exception as e:
        print('error',e)

f_minutes = create_function('m')
f_hours = create_function('h')
f_days = create_function('d')
    
print(f_minutes(start, end))
print(f_hours(start, end))
print(f_days(start, end))
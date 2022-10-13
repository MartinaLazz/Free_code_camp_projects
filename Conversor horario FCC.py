#!/usr/bin/env python
# coding: utf-8

# In[22]:


def add_time(start, duration, date=None):
  #Convierto horario de inicio a sistema 24 hs
    pos_start = start.find(':')
    pos_start2 = start.find(' ')
    start_h = int(start[:pos_start])
    start_m = int(start[pos_start+1:pos_start2])
    if start.endswith('PM') and not start.startswith('12'):
        start_h +=12
    elif start.endswith('AM') and start.startswith('12'):
        start_h -=12
        
  #Convierto duración
    pos_dur = duration.find(':')
    duration_h = int(duration[:pos_dur])
    duration_m = int(duration[pos_dur+1:])
 
  #Busco hora de finalización
    end_h = start_h + duration_h
    end_m = start_m + duration_m
    days = 0
    while end_m > 59:
        end_m -= 60
        end_h += 1
    while end_h > 23:
        end_h -= 24
        days += 1
  
  #Busco día de la semana
    week = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    week_inv = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    if date:
        date = date.capitalize()
        date_num = week[date]
        end_num = date_num+days
        while end_num > 6:
            end_num -= 7
        end_date = week_inv[end_num]
        
  #Convierto a AM/PM
    lunch = 'AM'
    if end_h == 0:
        end_h = 12
    elif end_h == 12:
        lunch = 'PM'
    elif end_h > 12:
        lunch = 'PM'
        end_h -=12

  #Formateo el output
    if days == 0:
        new_time = '{}:{:0>2d} {}'.format(end_h, end_m, lunch)
        if date:
            new_time = '{}:{:0>2d} {}, {}'.format(end_h, end_m, lunch, date)
    elif days == 1:
        new_time = '{}:{:0>2d} {} (next day)'.format(end_h, end_m, lunch)
        if date:
            new_time = '{}:{:0>2d} {}, {} (next day)'.format(end_h, end_m, lunch, end_date)
    else:
        new_time = '{}:{:0>2d} {} ({} days later)'.format(end_h, end_m, lunch, days)
        if date:
            new_time = '{}:{:0>2d} {}, {} ({} days later)'.format(end_h, end_m, lunch, end_date, days)

    return new_time


# In[24]:


add_time("6:30 PM", "205:12")


# In[ ]:





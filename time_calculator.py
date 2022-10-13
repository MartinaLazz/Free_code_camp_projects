def add_time(start, duration, day=None):
    start_h = int(start.split(":")[0])
    start_m = int(start.split(":")[1].split()[0])
    start_am = start[-2:]

    if start_am == "PM":
        start_h += 12

    duration_h = int(duration.split(":")[0])
    duration_m = int(duration.split(":")[1])

    end_m = start_m + duration_m
    end_h = start_h + duration_h

    extra_days = 0

    while end_m >= 60:
        end_h += 1
        end_m -= 60

    while end_h >= 24:
        extra_days += 1
        end_h -= 24

    if end_h >= 12:
        end_h -= 12
        end_am = "PM"
    else:
        end_am = "AM"

    if end_h == 0:
      end_h = 12

    new_time = str(end_h) + ":" + "{:02}".format(end_m) + " " + end_am

    days_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  
    if day != None:
      day = day.title()
      
      if extra_days == 0:
        new_time += ", " + day
      else:
        n = days_week.index(day)
        finish_day = n + extra_days
        while finish_day >= 6:
          finish_day -= 7
        
        new_time += ", " + days_week[finish_day]

        if extra_days == 1:
          new_time += " " + "(next day)"
        else:
          new_time += " (" + str(extra_days) + " days later)"

    else:
      if extra_days == 1:
          new_time += " " + "(next day)"
      if extra_days > 1:
          new_time += " (" + str(extra_days) + " days later)"  



    return new_time
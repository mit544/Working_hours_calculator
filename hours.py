from datetime import datetime

main = """20 April to 26 may
-----------------------
20 April, 2024
5:00 pm to 1:12 am


21 April, 2024
5:00 pm to 1:12 am


22 April, 2024
10:58 am to 1:20 am 

 
23 April, 2024
5:12 pm to 1:36 am


24 April, 2024
10:51 am to 10:02 pm


25 April, 2024
6:09 pm to 2:19 am

26 April, 2024 
6:03 pm to 1:55 am 
-----------------------
"""

main_split = main.split()

main_split.remove('-----------------------')
main_split.remove('-----------------------')

# Separating the date brackets
heading = []
for index, item in enumerate(main_split):
    inserted_item = heading.append(item)
    # main_split.remove(inserted_item)
    if (index % 5 == 4):
        break
    
print(" ".join(heading), "\n-----------------------")

# Separating the time bricket...
only_timings = main_split[5:]
days_timing = [] # this is the list that stores the all the days timings in a sub-list...
inner_index = [0, 8, 16, 24, 32, 40, 48, 56] # this list will be the starting index of the list slicing
inner_starting_point = 0 # this is the initial value of ii
for i in range(8,64,8):
    inner_numbers = inner_index[inner_starting_point]
    inner_starting_point = inner_starting_point + 1
    day = only_timings[inner_numbers:i]
    # print(day)
    days_timing.append(day)

# Until here, headings and timings are being segregated, now the next step is to count each day's working hours...

# here the list days_timing is being looped and as it also has a sub list of each along with the information of the 
# starting time and the finishing time. Each elements is being accessed and as it has starting time at the 2nd index and the 
# finishing time at the fourth index. 
hours:int = []
minutes:int = []
for day in days_timing:
    # print(day)
    print(" ".join(day[0:3])) # from the list clock_in time and date is being sliced
    clock_in = (day[0:5])
    clock_out = (day[0:3] + day[6:len(day)])
    
    # the list of clock_in and clock_out is being uppacked. only clock_out's touple should be unpacked but both have been done
    (date_clock_in, month_clock_in, year_clock_in, time_clock_in, local_clock_in) = clock_in
    (date_clock_out, month_clock_out, year_clock_out, time_clock_out, local_clock_out) = clock_out
    
    # both timings are being joint
    clock_in = date_clock_in + " " + month_clock_in + " " + year_clock_in + " " + time_clock_in + " " + local_clock_in
    clock_out = date_clock_out + " " + month_clock_out + " " + year_clock_out + " " + time_clock_out + " " + local_clock_out
    
    # the condition is being checked that if the locals(means am and pm) of clock out is am then the finishing
    # date will be the following
    if local_clock_out == "am" or local_clock_out == "Am":
        # if the condition id being matched, the date will be conveted into int and 1 is being added into that
        date_clock_out = int(date_clock_out) + 1  
        # the variable is converted into string 
        date_clock_out_str = str(date_clock_out)
        # the string is being made and date will be a new,
        clock_out = date_clock_out_str + " " + month_clock_out + " " + year_clock_out + " " + time_clock_out + " " + local_clock_out
        # the formation is being done
        starting_time = datetime.strptime(clock_in, '%d %B, %Y %I:%M %p')
        finishing_time = datetime.strptime(clock_out, '%d %B, %Y %I:%M %p')
        # from the finishing time the starting time is being substracted
        final_hours_calculation = finishing_time - starting_time
        print(final_hours_calculation)
        # for accessing all the values, the value is being converted into seconds
        seconds = final_hours_calculation.seconds
        # and then into minutes
        minutes_value = (seconds * 60) / 3600
        # all the values are being appended into a list called extra_minutes
        minutes.append(minutes_value)

    else:
        # if the condition is not meet, the date will be same and the process will be same
        clock_out = date_clock_out + " " + month_clock_out + " " + year_clock_out + " " + time_clock_out + " " + local_clock_out
        starting_time = datetime.strptime(clock_in, '%d %B, %Y %I:%M %p')
        finishing_time = datetime.strptime(clock_out, '%d %B, %Y %I:%M %p')
        final_hours_calculation = finishing_time - starting_time
        print(final_hours_calculation)
        seconds = final_hours_calculation.seconds
        minutes_value = (seconds * 60) / 3600
        minutes.append(minutes_value)

# here is the code of addition of all the values of the list, and segrigation of hours and the extra minutes
total_minutes = 0
total_extra_minutes = 0
for i in minutes:
    # here, the value upper the 60 is called the extra minutes. 
    # Considering that the logic of modulus is being executed.
    extra_minutes = i%60
    # exra minuetes, and total minutes are being added.
    total_extra_minutes += extra_minutes
    total_minutes = total_minutes + i

# print(total_extra_minutes_float, total_extra_minutes)

# for calculating total hours, the total hours are being floor devided to get int value.
total_hours_float = total_minutes // 60

# both values are being converted into int 
total_hours_int = int(total_hours_float)
total_extra_minutes = int(total_extra_minutes)

# still the minute value is more than 60, ex. 1.152 , 
# so we need to convert that into a specific hours time, ex. 3.32 

hours_from_extra_minutes = total_extra_minutes // 60 
# print(hours_from_extra_minutes)

final_hoours = total_hours_int + hours_from_extra_minutes
extra_upper_minutes_of_extra_minutes = total_extra_minutes%60
# print(extra_upper_minutes_of_extra_minutes)

print(F"total working hours are : {final_hoours}.{extra_upper_minutes_of_extra_minutes}")

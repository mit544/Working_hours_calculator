from datetime import datetime, timedelta

def time_formater(*days_timing):
    days_timing_list_formated = [] # this is the list that stores the all the days timings in a sub-list...
    inner_index = [0, 8, 16, 24, 32, 40, 48, 56, 64] # this list will be the starting index of the list slicing
    inner_starting_point = 0 # this is the initial value of ii

    for i in range(8,len(only_timings) + 8 ,8):
        inner_numbers = inner_index[inner_starting_point]
        inner_starting_point = inner_starting_point + 1
        day = only_timings[inner_numbers:i]
        days_timing_list_formated.append(day)
    return days_timing_list_formated

def timing_calculator(li:list):
    calculated_hours = []
    for i in li:
        date = " ".join(i[0:3])
        clock_in = (i[0:5])
        clock_out = i[0:3] + i[6:8]
        # the list of clock_in and clock_out is being uppacked. only clock_out's touple should be unpacked but both have been done
        (date_clock_in, month_clock_in, year_clock_in, time_clock_in, local_clock_in) = clock_in
        (date_clock_out, month_clock_out, year_clock_out, time_clock_out, local_clock_out) = clock_out
        # both timings are being joint
        clock_in = date_clock_in + " " + month_clock_in + " " + year_clock_in + " " + time_clock_in + " " + local_clock_in
        clock_out = date_clock_out + " " + month_clock_out + " " + year_clock_out + " " + time_clock_out + " " + local_clock_out
        
        
        if local_clock_out == "am" or local_clock_out == "Am":
            starting_time = datetime.strptime(clock_in, '%d %B, %Y %I:%M %p')
            finishing_time = datetime.strptime(clock_out, '%d %B, %Y %I:%M %p')
            # this is the line that gives the following date for am clock_out
            finishing_time_for_am_clock_out = finishing_time + timedelta(days=1)
            final_hours_calculation = finishing_time_for_am_clock_out - starting_time
            # for accessing all the values, the value is being converted into seconds
            seconds = final_hours_calculation.seconds
            # and then into minutes
            minutes_value = (seconds * 60) / 3600
            # all the values are being appended into a list called extra_minutes
            calculated_all = [date, starting_time, finishing_time, minutes_value]
            calculated_hours.append(calculated_all)

        else:
            # if the condition is not meet, the date will be same and the process will be same
            clock_out = date_clock_out + " " + month_clock_out + " " + year_clock_out + " " + time_clock_out + " " + local_clock_out
            starting_time = datetime.strptime(clock_in, '%d %B, %Y %I:%M %p')
            finishing_time = datetime.strptime(clock_out, '%d %B, %Y %I:%M %p')
            final_hours_calculation = finishing_time - starting_time
            seconds = final_hours_calculation.seconds
            minutes_value = (seconds * 60) / 3600
            calculated_all = [date, starting_time, finishing_time, minutes_value]
            calculated_hours.append(calculated_all)
    return calculated_hours

def final_formater(calculated_hours:list):
    calculated_hours_for_printing = []

    for i in calculated_hours:
        hours_str = i[3]
        hour = int(hours_str) // 60
        extra_upper_minutes = int(hours_str)%60
        f_h = i + [hour, extra_upper_minutes]
        calculated_hours_for_printing.append(f_h)
    return calculated_hours_for_printing


main = str(input("""Enter your schedule of work in the below formate,
27 April to 2 May
-----------------------
27 April, 2024
11:00 am to 9:30 pm
: """))

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

formated_clock_values = time_formater(only_timings)

calculated_hours = timing_calculator(formated_clock_values)

final_printer = final_formater(calculated_hours)

for i in final_printer:
    print(f"""{i[0]}
{datetime.time(i[1])} to {datetime.time(i[2])}
{i[4]}.{i[5]}
""")
    
# total hours
t_hours = 0
t_minutes = 0
for i in final_printer:
    t_hours += i[4]
    t_minutes += i[5]

hours_from_upper_minutes = t_minutes // 60
extra_minutes = t_minutes%60
final_tot_hours = t_hours + hours_from_upper_minutes

print("===========================\n", f"{final_tot_hours}.{extra_minutes}")

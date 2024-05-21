from datetime import datetime

def time_calculator(start_time, end_time):
    """This is the function to calculate the time difference.."""

    time_difference = end_time - start_time
    return time_difference

main = """18th march to 24th March 
-----------------------
18th march
6:42pm to 12:00am 

19th march
9:05pm to 12:40am 

20th march
6:23pm to 12:18am 

21th march
6:04pm to 12:45am 

22th march
6:13pm to 2:13am 

23th march
10:45am to 1:40am 

24th march
6:30pm to 1:28am
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
inner_index = [0, 5, 10, 15, 20, 25, 30, 35] # this list will be the starting index of the list slicing
inner_starting_point = 0 # this is the initial value of ii
for i in range(5,40,5):
    inner_numbers = inner_index[inner_starting_point]
    inner_starting_point = inner_starting_point + 1
    day = only_timings[inner_numbers:i]
    # print(day)
    days_timing.append(day)















    







def add_time(start, duration, weekday=""):

    if weekday != "":
        weekday = weekday.lower()
        # print(weekday)

    #process start
    start_list = start.split(" ")
    start_time_list = start_list[0].split(":")

    start_hours = start_time_list[0]
    start_minutes = start_time_list[1]

    if start_minutes == "00":
        start_minutes = 0
    else:
        start_minutes = int(start_minutes)

    if start_list[1] == "PM":
        start_hours = int(start_hours) + 12
    else:
        start_hours = int(start_hours)

    #process duration
    duration_list = duration.split(":")

    duration_hours = int(duration_list[0])
    duration_minutes = int(duration_list[1])

    # print("Duration time " + duration_list[0], duration_list[1])

    ## add minutes first
    # print(f"start mins: {str(start_minutes)}, duration mins: {duration_minutes}")
    total_minutes = start_minutes + duration_minutes
    # print(f"start mins: {str(start_minutes)}, duration mins: {duration_minutes}")
    # print("total minutes = " + str(total_minutes))
    total_hours = start_hours

    if total_minutes >= 60:
        total_minutes = total_minutes - 60
        total_hours += 1

    total_hours = total_hours + duration_hours

    new_hour_time = total_hours % 24
    days_passed = int(total_hours / 24)

    if new_hour_time > 12:
        new_hour_time = new_hour_time - 12
        day_half = "PM"
    elif new_hour_time == 12:
        day_half = "PM"
    else:
        day_half = "AM"


    if days_passed > 1:
        days_passed_string = f"({days_passed} days later)"
    elif days_passed == 1:
        days_passed_string = "(next day)"
    else:
        days_passed_string = ""

    
    #get weekday
    if weekday != "":
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        shuf_list = list()



        # dynamically set the index of the value passed in
        for i in range(7):
            if weekdays[i].lower() == weekday:
                current_index = i
            
        # add weekdays after value into new list
        for i in range(7):
            if i >= current_index:
                shuf_list.append(weekdays[i])

        # add weekdays before value into new list
        if len(shuf_list) < 7:
            for i in range(7):
                if i < current_index:
                    shuf_list.append(weekdays[i])
            
        new_weekday_index = days_passed%7
        new_weekday = shuf_list[new_weekday_index]
        # print(f"testing {new_weekday}....")

    if new_hour_time == 0:
        new_hour_string = "12"
    else:
        new_hour_string = str(new_hour_time)

    if total_minutes < 10:
        total_minutes_string = f"0{str(total_minutes)}"
    else:
        total_minutes_string = str(total_minutes)

    if weekday != "":
        new_time = f"{new_hour_string}:{total_minutes_string} {day_half}, {new_weekday} {days_passed_string}"
    else:
        new_time = f"{new_hour_string}:{total_minutes_string} {day_half} {days_passed_string}"
    
    
    return new_time
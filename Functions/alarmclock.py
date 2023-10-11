# Alarm Clock
# You're trying to automate your alarm clock by writing a function for it.
# You're given a day of the week encoded as 1=Mon, 2=Tue, ... 6=Sat, 7=Sun, and
# whether you are on vacation as a boolean value (a boolean object is either True or False.
# Google "booleans python" to get a better understanding). Based on the day and whether
# you're on vacation, write a function that returns a time in form of a string indicating
# when the alarm clock should ring.

# When not on a vacation, on weekdays, the alarm should ring at "7:00" and
# on the weekends (Saturday and Sunday) it should ring at "10:00".

# While on a vacation, it should ring at "10:00" on weekdays. On vacation,
# it should not ring on weekends, that is, it should return "off".

# ----------------------------------------------------------------------
# Input:
# The input will be a list of two elements. The first element will be an integer from 1 to 7,
# and the second element will be a boolean value.

# Output:
# The output will be a string denoting the time alarm will ring or 'off'

# ----------------------------------------------------------------------
# Sample input:
# [7, True]

# Sample output:
# off
weekend = [6, 7]

day_of_the_week = int(input("day of the week in number"))
is_on_vacation = bool(input("is user on vacation True / False"))


def alarm_time(day_of_the_week, is_on_vacation):
    if is_on_vacation:
        if day_of_the_week not in weekend:
            return "10:00"
        else:
            return "off"
    else:
        if day_of_the_week not in weekend:
            return "7:00"
        else:
            return "10:00"


print(alarm_time(day_of_the_week, is_on_vacation))

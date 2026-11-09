total_seconds = int(input("Enter a number of seconds: "))

if total_seconds >= 86400:
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    print(days, "days,", hours, "hours,", minutes, "minutes and", seconds, "seconds")
elif total_seconds >= 3600:
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    print(hours, "hours,", minutes, "minutes and", seconds, "seconds")
elif total_seconds >= 60:
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    print(minutes, "minutes and", seconds, "seconds")
else:
    print(total_seconds, "seconds")
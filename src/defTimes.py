import datetime

def getNowTimes():

    today = datetime.datetime.today()

    year = str(today.year)

    month = str(today.month)
    if len(month) == 1:
        month = "0" + month

    day = str(today.day)
    if len(day) == 1:
        day = "0" + day

    hour = str(today.hour)
    if len(hour) == 1:
        hour = "0" + hour

    minuts = str(today.minute)
    if len(minuts) == 1:
        minutes = "0" + minuts

    todayHM = hour + ":" + minuts + ":00"
    todayYMD = year + "-" + month + "-" + day

    return todayHM, todayYMD

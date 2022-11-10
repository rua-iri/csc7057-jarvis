import datetime

def time_now():
    now_time = datetime.datetime.now()

    return now_time.strftime("%I%M%S%p")

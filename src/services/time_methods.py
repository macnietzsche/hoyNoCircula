from datetime import time
def is_time_in_range(start_time: time,end_time: time,time:time)->bool:
    return start_time <= time <= end_time
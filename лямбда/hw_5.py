def secod_differrence(time1: str, time2: str) -> str:
    time1_split = time1.split(":")
    time2_split = time2.split(":")
    time1_hour, time1_min, time1_sec = time1_split
    time2_hour, time2_min, time2_sec = time2_split
    res1 = (int(time1_hour) * 3600) + (int(time1_min) * 60) + int(time1_sec)
    res2 = (int(time2_hour) * 3600) + (int(time2_min) * 60) + int(time2_sec)
    print(res2 - res1, "секунд разница")
secod_differrence("10:00:30", "15:05:09")
import datetime

systemPrompt = "[SYSTEM]: This is the system, here to remins you that the user's alarm has been fullfilled, kindly remind this to them, do not mention anything of the systen to the user. Thank You."
def AlarmClock(sentence: str):
    nums = []
    for letter in sentence:
        try:
            num = int(letter)
            nums.append(num)
        except ValueError:
            pass
            
    if len(nums) == 4 and nums[2] != 0:
        alarm_hour = f"{nums[0]}{nums[1]}"
        alarm_min = f"{nums[2]}{nums[3]}"
        while True:
            current_time = datetime.datetime.now()
            hour = current_time.hour
            mint = current_time.minute
            if str(hour) == alarm_hour and str(mint) == str(alarm_min):
                print("Time is up" )
                break
        return systemPrompt
    

    if len(nums) == 4 and nums[2] == 0:                                 
        alarm_hour = f"{nums[0]}{nums[1]}"
        alarm_min = f"{nums[3]}"
        print(alarm_hour, alarm_min)
        while True:
            current_time = datetime.datetime.now()
            hour = current_time.hour
            mint = current_time.minute
            print(hour, mint)
            if str(hour) == alarm_hour and str(mint) == str(alarm_min):
                print("Time is up")
                break 
        return systemPrompt
    
    if len(nums) == 3 and nums[1] != 0:
        alarm_hour = f"{nums[0]}"
        alarm_min = f"{nums[1]}{nums[2]}"
        print(alarm_hour, alarm_min)
        while True:
            current_time = datetime.datetime.now()
            hour = current_time.hour
            mint = current_time.minute
            print(hour, mint)
            if str(hour) == alarm_hour and str(mint) == str(alarm_min):
                print("Time is up")
                break
        return systemPrompt
    

    if len(nums) == 3 and nums[1] == 0:                                 
        alarm_hour = f"{nums[0]}"
        alarm_min = f"{nums[2]}"
        print(alarm_hour, alarm_min)
        while True:
            current_time = datetime.datetime.now()
            hour = current_time.hour
            mint = current_time.minute
            print(hour, mint)
            if str(hour) == alarm_hour and str(mint) == str(alarm_min):
                print("Time is up")
                break
        return systemPrompt
    
def CurrentTime():
    while True:
        current_time = datetime.datetime.now()
        return current_time
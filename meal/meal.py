def main():
    time = input('What time is it? ')
    time_hr = convert(time)
    meal(time_hr)



def convert(time):
    hours, minutes = time.split(':')
    minute_to_hour = float(minutes) / 60
    time = float(hours) + minute_to_hour
    return time

def meal(time_hr):
    if 7 <= time_hr <= 8:
        print('breakfast time')
    elif 12 <= time_hr <= 13:
        print('lunch time')
    elif 18 <= time_hr <= 19:
        print('dinner time')
    else:
        None
         

if __name__ == "__main__":
    main()
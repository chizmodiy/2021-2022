import datetime
def date_time(time: str) -> str:
    x = 0
    f = time.replace('.', ' ')
    f = f.replace(':', ' ')
    f = f.split()
    day , month ,year,hours,minutes = f[0],f[1],f[2],f[3],f[4]

    result_date = datetime.date(int(year), int(month), int(day))
    if int(hours) == 1 and int(minutes)==1:
        return (f'{int(day)} {result_date.strftime("%B")} {year} year {int(hours)} hour {int(minutes)} minute')
    if hours =='1':
        return (f'{int(day)} {result_date.strftime("%B")} {year} year {int(hours)} hour {int(minutes)} minutes')
    if minutes=='01':
        return (f'{int(day)} {result_date.strftime("%B")} {year} year {int(hours)} hours {int(minutes)} minute')
    else:
        return (f'{int(day)} {result_date.strftime("%B")} {year} year {int(hours)} hours {int(minutes)} minutes')

if __name__ == "__main__":
    print("Example:")
    print(date_time("11.04.1812 01:01"))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
            date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    ), "Millenium"
    assert (
            date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
    ), "Victory"
    assert (
            date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    ), "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")

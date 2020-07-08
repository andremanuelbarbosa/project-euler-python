def year_days(year):
    return (30 * 4) + (7 * 31) + (29 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 28)


def month_days(month, year):
    return 30 if month in (4, 6, 9, 11) else 31 if month in (1, 3, 5, 7, 8, 10, 12) else 29 if (
            year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 28


def absolute_days(month_day, month, year):
    days = 0
    for i in range(1900, year):
        days += year_days(i)
    for i in range(1, month):
        days += month_days(i, year)
    return days + month_day


def solution():
    num_sundays = 0
    for i in range(1901, 2001):
        for j in range(1, 13):
            if absolute_days(1, j, i) % 7 == 0:
                num_sundays += 1
    return num_sundays


print(solution())

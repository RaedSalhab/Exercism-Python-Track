def leap_year(year):
    if year % 4 == 0:
        if year % 400 != 0 and year % 100 == 0:
            return False
        else:
            return True
    else:
        return False

if __name__ == '__main__':
    year_list = [1900, 1950, 1972, 1999, 2000, 2100, 1200, 1000]
    for item in year_list:
        print(item, leap_year(item))

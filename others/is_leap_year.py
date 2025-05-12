

def is_leap_year(year: int) -> bool:
    """
    Determines a wheather given year is lead or not

    Leap year is defined as:
        1. If year is divisible by 4 is a leap year But
        2. If year is also divisible by 100 then it is not a leap year
        3. Unless year is divisble by 400 then it is a leap year

    """

    if not isinstance(year, int) or year < 1:
        raise ValueError("Year must be a positive integer")
    
    if (year % 4 == 0):
        if (year % 100 == 0):
            return (year % 400 == 0)
        else:
            return True
    else:
        return False
#---------------------------------------------------------#
#liamlee												  #
#2013-09-01												  #	
#---------------------------------------------------------#

# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
def dayFromBegin(year,mon,day):
    all_day = 0
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    s_year = 1900
    s_mon = 0
    s_day = 1
    
    #count days from the year
    while s_year < year:
        all_day += 365
        if (s_year % 400 == 0) or(s_year % 4 == 0 and s_year % 100 != 0):
            all_day += 1
        s_year +=1
    
    #count days from the month
    if mon >= 2:
        if (s_year % 400 == 0) or(s_year % 4 == 0 and s_year % 100 != 0):
            days[1] = 29
    while s_mon < mon - 1:
        all_day += days[s_mon]
        s_mon += 1
    
    #
    all_day = all_day + day -1
    return all_day

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    days1 = dayFromBegin(year1,month1,day1)
    days2 = dayFromBegin(year2,month2,day2)
    return days2 - days1
    ##


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

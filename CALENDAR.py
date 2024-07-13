FYear = 2022

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
def count_leap_years(start_year, end_year):
    leap_years = 0
    for i in range(start_year, end_year):
        if is_leap_year(i):
            leap_years += 1
    return leap_years

def calculate_days(UYear, FYear, month):
    # Implement the month-to-days logic
    if ( UYear >= FYear):

        if month=='JAN':
            days = 0
        elif month=='FEB':
            days = 31
        elif month=='MAR':
            days = 59
        elif month=='APR':
            days = 90
        elif month=='MAY':
            days = 120
        elif month=='JUN':
            days = 151
        elif month=='JUL':
            days = 181
        elif month=='AUG':
            days = 212
        elif month=='SEP':
            days = 243
        elif month=='OCT':
            days = 273
        elif month=='NOV':
            days = 304
        else :
            days = 334
    else:
        if month=='JAN':
            days = 0
        elif month=='FEB':
            days = 334
        elif month=='MAR':
            days = 306
        elif month=='APR':
            days = 275
        elif month=='MAY':
            days = 245
        elif month=='JUN':
            days = 214
        elif month=='JUL':
            days = 184
        elif month=='AUG':
            days = 153
        elif month=='SEP':
            days = 122
        elif month=='OCT':
            days = 92
        elif month=='NOV':
            days = 61
        else :
            days = 31
    return days
    

def get_start_day(FYear, UYear,REM):
    # Map REM to the correct starting day
    if UYear >= FYear:
        if REM == 1 :
            SDay = 'SAT'
        elif REM == 2 :
            SDay = 'SUN'
        elif REM == 3 :
            SDay = 'MON'
        elif REM == 4 :
            SDay = 'TUE'
        elif REM == 5 :
            SDay = 'WED'
        elif REM == 6 :
            SDay = 'THU'
        else :
            SDay = 'FRI'
    else:    
        if REM == 1 :
            SDay = 'SAT'
        elif REM == 2 :
            SDay = 'FRI'
        elif REM == 3 :
            SDay = 'THU'
        elif REM == 4 :
            SDay = 'WED'
        elif REM == 5 :
            SDay = 'TUE'
        elif REM == 6 :
            SDay = 'MON'
        else :
            SDay = 'SUN'
    return SDay

        
def print_calendar(month, UYear, SDay):
    if month=='JAN':
            b = 1
    elif month=='FEB':
            b = 0
    elif month=='MAR':
            b = 1
    elif month=='APR':
            b = 2
    elif month=='MAY':
            b = 1
    elif month=='JUN':
            b = 2
    elif month=='JUL':
            b = 1
    elif month=='AUG':
            b = 1
    elif month=='SEP':
            b = 2
    elif month=='OCT':
            b = 1
    elif month=='NOV':
            b = 2
    else :
            b = 1

        

    print(end='\n')
    print('           ',month,'',UYear)

    if SDay == 'SUN':
        print ( 'Sun ', 'Mon ', 'Tue ', 'Wed ', 'Thu ', 'Fri ', 'Sat ')
        print (end='\n')
        print (' 1','   2','   3','   4','   5','   6','   7')
        print (end='\n')
        print (' 8','   9','  10','  11','  12','  13','  14')
        print (end='\n')
        print ('15','  16','  17','  18','  19','  20','  21')
        print (end='\n')
        
        if (b==1):
            print ('22','  23','  24','  25','  26','  27','  28')
            print (end='\n')
            print ('29','  30','  31')
        if (b==2):
            print ('22','  23','  24','  25','  26','  27','  28')
            print (end='\n')
            print ('29','  30')
        if month == 'FEB':
            if is_leap_year(Uyear):
                print ('22','  23','  24','  25','  26','  27','  28')
                print (end='\n')
                print ('29')
            else:
                 print ('22','  23','  24','  25','  26','  27','  28')


    if SDay == 'MON':
        print ( 'Sun ', 'Mon ', 'Tue ', 'Wed ', 'Thu ', 'Fri ', 'Sat ')
        print (end='\n')
        print ('  ','   1','   2','   3','   4','   5','   6')
        print (end='\n')
        print (' 7','   8','   9','  10','  11','  12','  13')
        print (end='\n')
        print ('14','  15','  16','  17','  18','  19','  20')
        print (end='\n')
        
        if (b==1):
            print ('21','  22','  23','  24','  25','  26','  27')
            print (end='\n')
            print ('28','  29','  30','  31')
        if (b==2):
            print ('21','  22','  23','  24','  25','  26','  27')
            print (end='\n')
            print ('28','  29','  30')
        if month == 'FEB':
            if is_leap_year(Uyear):
                print ('21','  22','  23','  24','  25','  26','  27')
                print (end='\n')
                print ('28','  29')
            else:
                print ('21','  22','  23','  24','  25','  26','  27')
                print (end='\n')
                print ('28')


    if SDay == 'TUE':
        print ( 'Sun ', 'Mon ', 'Tue ', 'Wed ', 'Thu ', 'Fri ', 'Sat ')
        print (end='\n')
        print ('  ','    ','   1','   2','   3','   4','   5')
        print (end='\n')
        print (' 6','   7','   8','   9','  10','  11','  12')
        print (end='\n')
        print ('13','  14','  15','  16','  17','  18','  19')
        print (end='\n')
        
        if (b==1):
            print ('20','  21','  22','  23','  24','  25','  26')
            print (end='\n')
            print ('27','  28','  29','  30','  31')
        if (b==2):
            print ('20','  21','  22','  23','  24','  25','  26')
            print (end='\n')
            print ('27','  28','  29','  30')
        if month == 'FEB':
            if is_leap_year(Uyear):
                print ('20','  21','  22','  23','  24','  25','  26')
                print (end='\n')
                print ('27','  28','  29')
            else:
                print ('20','  21','  22','  23','  24','  25','  26')
                print (end='\n')
                print ('27','  28')

    if SDay == 'WED':
        print ( 'Sun ', 'Mon ', 'Tue ', 'Wed ', 'Thu ', 'Fri ', 'Sat ')
        print (end='\n')
        print ('  ','    ','    ','   1','   2','   3','   4')
        print (end='\n')
        print (' 5','   6','   7','   8','   9','  10','  11')
        print (end='\n')
        print ('12','  13','  14','  15','  16','  17','  18')
        print (end='\n')
        print ('19','  20','  21','  22','  23','  24','  25')
        print (end='\n')
        
        if (b==1):
            print ('26','  27','  28','  29','  30','  31')
        if (b==2):
            print ('26','  27','  28','  29','  30')
        if month == 'FEB':
            if is_leap_year(Uyear):
                print ('26','  27','  28','  29')
            else:
                print ('26','  27','  28')

    if SDay == 'THU':
        print ( 'Sun ', 'Mon ', 'Tue ', 'Wed ', 'Thu ', 'Fri ', 'Sat ')
        print (end='\n')
        print ('  ','    ','    ','    ','   1','   2','   3')
        print (end='\n')
        print (' 4','   5','   6','   7','   8','   9','  10')
        print (end='\n')
        print ('11','  12','  13','  14','  15','  16','  17')
        print (end='\n')
        print ('18','  19','  20','  21','  22','  23','  24')
        print (end='\n')
        
        if (b==1):
            print ('25','  26','  27','  28','  29','  30','  31')
        if (b==2):
            print ('25','  26','  27','  28','  29','  30')
        if month == 'FEB':
            if is_leap_year(Uyear):
                print ('25','  26','  27','  28','  29')
            else:
                print ('25','  26','  27','  28')

    if SDay == 'FRI':
        print ( 'Sun ', 'Mon ', 'Tue ', 'Wed ', 'Thu ', 'Fri ', 'Sat ')
        print (end='\n')
        print ('  ','    ','    ','    ','    ','   1','   2')
        print (end='\n')
        print (' 3','   4','   5','   6','   7','   8','   9')
        print (end='\n')
        print ('10','  11','  12','  13','  14','  15','  16')
        print (end='\n')
        print ('17','  18','  19','  20','  21','  22','  23')
        print (end='\n')
        
        if (b==1):
            print ('24','  25','  26','  27','  28','  29','  30')
            print(end='\n')
            print('31')
        if (b==2):
            print ('24','  25','  26','  27','  28','  29','  30')
        if month == 'FEB':
            if is_leap_year(Uyear):
                print ('24','  25','  26','  27','  28','  29')
            else:
                print ('24','  25','  26','  27','  28')

    if SDay == 'SAT':
        print ( 'Sun ', 'Mon ', 'Tue ', 'Wed ', 'Thu ', 'Fri ', 'Sat ')
        print (end='\n')
        print ('  ','    ','    ','    ','    ','    ','   1')
        print (end='\n')
        print (' 2','   3','   4','   5','   6','   7','   8')
        print (end='\n')
        print (' 9','  10','  11','  12','  13','  14','  15')
        print (end='\n')
        print ('16','  17','  18','  19','  20','  21','  22')
        print (end='\n')
        
        if (b==1):
            print ('23','  24','  25','  26','  27','  28','  29')
            print (end='\n')
            print ('30','  31')
        if (b==2):
            print ('23','  24','  25','  26','  27','  28','  29')
            print (end='\n')
            print ('30')
        if month == 'FEB':
            if is_leap_year(Uyear):
                print ('23','  24','  25','  26','  27','  28','  29')
            else:
                print ('23','  24','  25','  26','  27','  28')
    


def start (FYear, UYear, month):

    days = calculate_days(UYear, FYear, month)
    leap_years = count_leap_years(FYear, UYear)
    TDays = (UYear - FYear) * 365 + days + leap_years
    REM = (TDays % 7) + 1
    SDay = get_start_day(REM)
    print_calendar(month, UYear, SDay)


d = input ("If you need a particular month - type 'YES' else type 'NO' : ").lower()

if d == 'yes'  :
    month = input( " Please enter the month in capital letters with only 3 letters [eg JAN] : " )
    UYear = int(input( " Please enter the year : " ))
    start(FYear, UYear, month)
   
else:
    UYear = int(input( " Please enter the year : " ))
    c = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    for j in range (0,12,1):
        month = c[j]
        start(FYear, UYear, month)
       
    
    
    
    














    

    
        
        
        
    

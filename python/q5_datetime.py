# Hint:  use Google to find python function
import datetime


####a) 
date_start_1 = '01-02-2013'  
date_stop_1 = '07-28-2015'  

datetime_start_1 = datetime.datetime.strptime(date_start_1, "%m-%d-%Y")
datetime_stop_1 = datetime.datetime.strptime(date_stop_1, "%m-%d-%Y")

print datetime_stop_1 - datetime_start_1

####b)  
date_start_2 = '12312013'  
date_stop_2 = '05282015'

print (datetime.datetime.strptime(date_stop_2, "%m%d%Y") - 
    datetime.datetime.strptime(date_start_2, "%m%d%Y")) 


####c)  
date_start_3 = '15-Jan-1994'  
date_stop_3 = '14-Jul-2015'  

print (datetime.datetime.strptime(date_stop_3, "%d-%b-%Y") - 
    datetime.datetime.strptime(date_start_3, "%d-%b-%Y")) 
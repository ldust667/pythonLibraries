import datetime
#list out objects contained in datetime library
#print(dir(datetime))
#breaking it down further by explaining the class
#help(datetime.date)
#from the help we can see how to create a date object
date_ex = datetime.date(1996, 5, 25)
print(date_ex)
#print(date_ex.year) <- .day .month seperate object out by day month and year


date_ex2 = datetime.date(2000,1,1)
date_delta = datetime.timedelta(100) #time delta allows you to do math with dates 
print(date_ex2 + date_delta) #prints the result of 100 days past 2000,1,1


#displaying dates in a diffrent format using the format method on a string you can pass the date object through filing in the variable indicators given in the string
date= 'Joe was born {:%A, %B %d, %Y}.'
print(date.format(date_ex2))

#creating datetime objects with hour min and day is also possible
launch_date = datetime.date(2017,3,30) #creating object using date method
launch_time = datetime.time(22,27,0) #using time
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0) # using datetime date+time (hr,min,sec) 
print(launch_date)
print(launch_time.hour) #time can also be accessed like above .hour.minute.second
print(launch_datetime)


print(datetime.datetime.today()) #shows current date to microsecond
print(datetime.datetime.today().microsecond) #also accesible in a similar fashion

#converting strings to datetimes
moon = "7/20/1969"
moon_datetime = datetime.datetime.strptime(moon, "%m/%d/%Y")
print(moon_datetime)

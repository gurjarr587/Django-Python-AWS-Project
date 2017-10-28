#calculating the give time respectively start,slow,speed in minutes
start_time = (7*60 + 30)*60
slow_time  = (8*60 + 15)
speed_time = (7*60 + 12)*3

#returns time in format of hour and minutes in function getHome() after calculating total hours and minutes
def getHome():

   total_finish_hr = (start_time + slow_time + speed_time)/(60*60)
   total_floor_hr = (start_time + slow_time + speed_time)//(60*60)
   total_mints = (total_finish_hr - total_floor_hr)*60
   
   return print("the total time to go home for breakfast %d:%d" % (total_finish_hr,total_mints))

#calling function (program need to execute the function) to get output
getHome()
    

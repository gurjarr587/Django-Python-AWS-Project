#time in seconds and distance in mile's (1 mile = 1.6 km approx)
distance = 10/1.6
time = 3600+300+42

#returns values respectively avgpace in seconds,minutes and average speed 
def avgPace(time, distance):

	avg_pace_sec = time/distance 
	print("average pace in minutes is:",avg_pace_sec)
    	
	avg_pace_mint = (time/distance)*60
	print("average pace in seconds is:",avg_pace_mint)

	time = int(1+5/(60)+42/(3600))	
	avg_speed_mlhr = distance/time
	print("average speed in miles per hours is:",avg_speed_mlhr)

	return

#caling function avgPace() to execute
avgPace(time, distance)

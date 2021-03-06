#!/usr/bin/env python

import datetime
from praytimes import PrayTimes


#Get Prayer Times
#--------------------
lat = 40.9168
long = -74.1718

now = datetime.datetime.now()



PT = PrayTimes('ISNA')
times = PT.getTimes((now.year,now.month,now.day), (lat, long), -4,0,1)

print(times['fajr'])
print(times['dhuhr'])
print(times['asr'])
print(times['maghrib'])
print(times['isha'])


#Update Crontab with Prayer Times
#---------------------------------

from crontab import CronTab


#Function to add azaan time to cron
def addAzaanTime (strPrayerName, strPrayerTime, objCronTab, strCommand):

	job = objCronTab.new(command=strCommand,comment=strPrayerName)

	timeArr = strPrayerTime.split(':')

	hour = timeArr[0]
	min = timeArr[1]

	job.minute.on(int(min))
	job.hour.on(int(hour))

	print(job)



system_cron = CronTab()
system_cron = CronTab(user=True)
system_cron = CronTab(user='zamy')

strPlayAzaanMP3Command = 'omxplayer -o local btv_fojor_azan.mp3 > /dev/null 2>&1'
# azan_audio = vlc.MediaPlayer("btv_fojor_azan.mp3")

jobs = system_cron.find_command(strPlayAzaanMP3Command)

print(jobs)

for j in jobs:
	system_cron.remove(j)

addAzaanTime('fajr',times['fajr'],system_cron,strPlayAzaanMP3Command)
addAzaanTime('dhuhr',times['dhuhr'],system_cron,strPlayAzaanMP3Command)
addAzaanTime('asr',times['asr'],system_cron,strPlayAzaanMP3Command)
addAzaanTime('maghrib',times['maghrib'],system_cron,strPlayAzaanMP3Command)
addAzaanTime('isha',times['isha'],system_cron,strPlayAzaanMP3Command)


system_cron.write()




#!/usr/bin/env python

# import datetime
# import time
# import sys
# # sys.path.insert(0, '/home/pi/adhan/crontab')
#
# from praytimes import PrayTimes
# PT = PrayTimes()

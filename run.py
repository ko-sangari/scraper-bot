import os
import time
import schedule


print('> Scheduler initialised ...')

os.system('python3 scraper_holland2stay.py')

schedule.every(2).minutes.do(
    lambda: os.system('python3 scraper_holland2stay.py')
)

while True:
    schedule.run_pending()
    time.sleep(10)

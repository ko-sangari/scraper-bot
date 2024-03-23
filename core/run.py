import os
import time
import schedule

from core.settings import settings


print(f" > Scheduler initialized to run every {settings.SCHEDULER_TIMER} minutes ...\n")

os.system("python3 scrapers/holland2stay.py")

schedule.every(settings.SCHEDULER_TIMER).minutes.do(
    lambda: os.system("python3 scrapers/holland2stay.py")
)

while True:
    schedule.run_pending()
    time.sleep(10)

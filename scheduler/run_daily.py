import schedule
import time

from main import run_pipeline


schedule.every().day.at("08:00").do(
    run_pipeline
)

schedule.every().day.at("20:00").do(
    run_pipeline
)

print("Scheduler Running...")


while True:

    schedule.run_pending()

    time.sleep(30)
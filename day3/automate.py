import schedule
import time

def upload():
    print("upload started..")

schedule.every().minutes.do(upload)
schedule.every().hour.do(upload)
schedule.every().day.at("10:30").do(upload)
# schedule.every().seconds.do(upload)
# schedule.every(10).minutes.do(upload)
# schedule.every().hour.do(upload)
# schedule.every().day.at("10:30").do(upload)
# schedule.every(5).to(10).minutes.do(upload)
# schedule.every().monday.do(upload)
# schedule.every().wednesday.at("13:15").do(upload)
# schedule.every().minute.at(":17").do(upload)

while True:
    schedule.run_pending()
    print('*')
    time.sleep(10)
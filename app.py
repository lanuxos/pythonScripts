# python automate trading
# ep 2
# flask app

from flask import Flask
from ep2 import SignalBySymbols
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
import time

executors = {
    'default': ThreadPoolExecutor(16),
    'processpool': ProcessPoolExecutor(4)
}

def Job():
    print('Checking for singals please be patient')
    coin_list = ['BTCUSDT', 'ETHUSDT', 'BCHUSDT', 'LTCUSDT', 'DOGEUSDT']
    for c in coin_list:
        SignalBySymbols(c)

sched = BackgroundScheduler(timezone='Asia/Singapore', executors=executors)

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return 'Hello World'

@app.route("/")
def pair_signals(pairname):
    return ''

if __name__ == '__main__':
    # app.run(debug=True)
    # input('press enter to init bot')
    # schedule.run
    # sched.add_job(Job, 'interval', minute='1', id='Signal')
    while True:
        # if input('press enter to exit'):
            # sched.remove_job('Signal')
            # sched.shutdown()
            # break
        Job()
        time.sleep(10)

    print('bye...')


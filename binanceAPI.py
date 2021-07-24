# binance api
# https://www.youtube.com/watch?v=fIvXmDQOS8E&t=49s&ab_channel=UncleEngineerUncleEngineer
apiKey = 'EjFmmQoUA3hXQhKjwgFjgqf3F7YycRmFLCrEMSnzmRQbxGASVo47mU4BvDhuAxEz'
secretKey = '8RZ3YczxPqT3hFEEpqyVwNaH6hofn1DxTX6Yxvpn8I769L86dizv9p6Tub1ijpVu'
import time
from time import mktime
from datetime import datetime, timedelta
from pprint import pprint
from binance.client import Client

client = Client(apiKey, secretKey)

time_res = client.get_server_time() # milliseconds
# print('>SERVER_TIME_IN_MILLISECONDS', time_res['serverTime'])
seconds = time_res['serverTime'] / 1000
# print('>SERVER_TIME_WITH_CTIME', time.ctime(seconds))
# print('>SERVER_TIME_IN_LOCAL', time.localtime(seconds))
dt = datetime.fromtimestamp(mktime(time.localtime(seconds)))
dt = dt.strftime('%Y-%m-%d %H:%M:%S')
print('>SERVER_TIME_LOCAL_COMPUTER_TIME', dt)

info = client.get_exchange_info()
# pprint(info)

depth = client.get_order_book(symbol='BNBBTC')
# pprint(depth)

# 24 hour price change statistics.
tickers = client.get_ticker(symbol='SUSDBTC')
# pprint(tickers['askPrice'])
# askPrice - ລາຄາທີ່ຜູ້ຖືຕ້ອງການຂາຍ
# bidPrice - ລາຄາທີ່ຜູ້ຊື້ຕ້ອງການຊື້

prices = client.get_all_tickers()
# for pc in prices:
    # pprint(pc)

depth = client.get_order_book(symbol='SUSDBTC', limit=5)
# pprint(depth)

trades = client.get_recent_trades(symbol='SUSDBTC', limit=5)
# pprint(trades)

candles = client.get_klines(
    symbol='SUSDBTC', interval=Client.KLINE_INTERVAL_30MINUTE, limit=5)
# pprint(candles)



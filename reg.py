"""получить послетние твиты пользователя"""
import requests
import json
import sys
import getpass
import time
import datetime
import os
import re
import collections
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import matplotlib.finance as mfinance
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import matplotlib.pyplot as plt

def get_tweets(screen_name):
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    params = {'screen_name': screen_name, 'count': 200}
    response = requests.get(url, auth=auth, params=params)
    tweets = json.loads(response.text)
    return tweets

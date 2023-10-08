import sys
sys.path.insert(0, r"D:\ZB\git_repo\waditu\czsc")
import czsc
import pandas as pd
from pathlib import Path
from czsc.connectors.research import get_raw_bars


def test_split():
    from czsc.utils.bar_generator import *
    row = mss[(mss['market'] == '期货') & (mss['time'] == '00:00')]



def get_future_times():
    files = Path(r"D:\CZSC投研数据\期货主力").glob("*.parquet")
    times = {}
    for file in files:
        df = pd.read_parquet(file)
        times[file.stem] = sorted(list({x.strftime("%H:%M") for x in df['datetime']}))
    uni_times = sorted(list({x for y in times.values() for x in y}))

    df = pd.read_excel(r"D:\test.xlsx")
    df.to_feather(r"D:\ZB\git_repo\waditu\czsc\czsc\utils\minites_split.feather")


def test():
    bars = get_raw_bars("SQag9001", '1分钟', sdt='20230101', edt='20230801')
    # time_seq = sorted(list({x.dt.strftime("%H:%M") for x in bars}))
    # x_freq, market = czsc.check_freq_and_market(time_seq=time_seq)

    bg = czsc.BarGenerator(base_freq='1分钟', freqs=['5分钟', '15分钟', '20分钟', '30分钟', '60分钟', '日线'], max_count=1000, market="期货")
    for bar in bars:
        bg.update(bar)

    df = czsc.resample_bars(pd.DataFrame(bars), '30分钟', raw_bars=True)
    bg = czsc.BarGenerator(base_freq='30分钟', freqs=['60分钟', '日线'], max_count=1000, market="期货")
    for bar in df:
        bg.update(bar)


    df = czsc.resample_bars(pd.DataFrame(bars), '15分钟', raw_bars=True)
    bg = czsc.BarGenerator(base_freq='15分钟', freqs=['30分钟', '60分钟', '日线'], max_count=1000, market="期货")
    for bar in df:
        bg.update(bar)

    df = czsc.resample_bars(pd.DataFrame(bars), '20分钟', raw_bars=True)
    bg = czsc.BarGenerator(base_freq='20分钟', freqs=['30分钟', '60分钟', '日线'], max_count=1000, market="期货")
    for bar in df:
        bg.update(bar)

    df = czsc.resample_bars(pd.DataFrame(bars), '5分钟', raw_bars=True)
    bg = czsc.BarGenerator(base_freq='5分钟', freqs=['15分钟', '20分钟', '30分钟', '60分钟', '日线'], max_count=1000, market="期货")
    for bar in df:
        bg.update(bar)

import time
from sleepctl import SleepControl

if __name__ == '__main__':
    from random import random
    import datetime

    slp_ctl = SleepControl(interval=3)
    @slp_ctl.sleep_deco
    def test_function():
        s = random() *3
        print(f'{datetime.datetime.now().isoformat()} Sleep {s}s')
        time.sleep(s)
    while True:
        test_function()



import time
from sleepctl import SleepControl
from random import random
import datetime

# Setup Sleep Contoler
slp_ctl = SleepControl(interval=3)

# Set Decorator
@slp_ctl.interval_func
def test_function():
    # This Function must be OneShot
    # No Loop
    s = random() *4
    print(f'{datetime.datetime.now().isoformat()} Sleep {s}s')
    time.sleep(s)


if __name__ == '__main__':
    # Set Loop
    while True:
        test_function()



import time
import datetime

__author__ = 'customtea (https://github.com/customtea/)'
__version__ = '1.5.0'

class SleepControl:
    def __init__(self, interval=1):
        """Init

        Parameters
        ----------
        interval : int, optional
            interval sec, by default 1
        """
        self.interval = interval
        self.sleep_time = 0
        self.init_time = time.time()

    # with Overflow Interval Time Warning Print
    def interval_func(self, func):
        def decorator_wrapper(*args, **kwargs):
            time.sleep(self.sleep_time)
            
            func_start_time = time.time()
            correction_time = (func_start_time - self.init_time)%self.interval
            r = func(*args, **kwargs)
            func_end_time = time.time()

            calc_start_time = time.time()
            diff_time = func_end_time - func_start_time
            self.sleep_time = self.interval - diff_time - correction_time
            if self.sleep_time < 0:
                print(f"{datetime.datetime.now().isoformat()} [Warning] Processing Time ({diff_time}) is Overflowed Interval ({self.interval})")
                # print(f"Next Sleep Time Set at ({self.interval})'")
                self.sleep_time = abs(self.sleep_time) % self.interval
            calc_end_time = time.time()

            diff_time = calc_end_time - calc_start_time
            self.sleep_time -= diff_time
            return r
        return decorator_wrapper

    # no warning (MUST Complete Function within sleep interval)
    def interval_func_nowarn(self, func):
        def decorator_wrapper(*args, **kwargs):
            time.sleep(self.sleep_time)
            
            r = func(*args, **kwargs)

            calc_start_time = time.time()
            self.sleep_time = self.interval - (calc_start_time - self.init_time) % self.interval
            calc_end_time = time.time()

            self.sleep_time -=  (calc_end_time - calc_start_time)
            return r
        return decorator_wrapper

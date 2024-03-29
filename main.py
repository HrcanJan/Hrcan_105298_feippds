"""This module contains an implementation of the bakery algorithm.
"""

__author__ = "Jan Hrćan"
__email__ = "xhrcan@stuba.sk"
__license__ = "MIT"

from fei.ppds import Thread
from time import sleep

num: list[int] = [0, 0, 0, 0, 0]
inVar: list[bool] = [False, False, False, False, False]


def process(tid: int, num_runs: int):
    """Simulates a process.

    Arguments:
        tid      -- thread id
        num_runs -- number of executions of the critical section
    """
    global num, inVar
    inVar[tid] = True
    num[tid] = 1 + max(num)
    inVar[tid] = False

    for _ in range(num_runs):
        for j in range(NUM_THREADS):
            while inVar[j]:
                continue
            while (num[j] != 0) and ((num[j], j) < (num[tid], tid)):
                continue

        # execute critical section
        print(f"Process {tid} runs a complicated computation!")
        sleep(1)
    num[tid] = 0


# inspired from https://github.com/tj314/ppds-2023-cvicenia/blob/master/seminar2/04_ticket.py
if __name__ == '__main__':
    DEFAULT_NUM_RUNS = 5
    NUM_THREADS = 5
    threads = [Thread(process, i, DEFAULT_NUM_RUNS) for i in range(NUM_THREADS)]
    [t.join() for t in threads]
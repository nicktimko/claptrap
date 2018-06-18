import random


def wub(length=50):
    if length < 1:
        return ValueError('length must be positive')
    if length == 1:
        return random.choice('wW')
    if length == 2:
        return random.choice


    wubs, pad = divmod(length, 4)

    return

from time import time


presidents = [
    'George Washington',
    'John Adams',
    'Thomas Jefferson',
    'James Madison',
    'James Monroe',
    'John Quincy Adams',
    'Andrew Jackson',
    'Martin Van Buren',
    'William Henry Harrison',
    'John Tyler'
]


big = True

if not big:
    article_names = presidents
else:
    from .many_long_articles import many_long_articles
    article_names = many_long_articles


##################################################################


tick = time()


def tock():
    interval = time() - tick
    return str(round(interval, 3))

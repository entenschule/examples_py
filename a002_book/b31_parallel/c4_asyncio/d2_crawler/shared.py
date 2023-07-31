import os
from time import time


big = True

if not big:
    from .article_names import presidents, colonies
    article_names_1 = presidents
    article_names_2 = colonies
else:
    from .article_names import some_long_articles, more_long_articles
    article_names_1 = some_long_articles
    article_names_2 = more_long_articles


##################################################################


def make_download_folder(file):
    parent_path = os.path.dirname(file)
    download_path = parent_path + '/DOWNLOADS'
    try:
        os.mkdir(download_path)
    except FileExistsError:
        pass
    return download_path


##################################################################


tick = time()


def tock():
    interval = time() - tick
    return str(round(interval, 3))

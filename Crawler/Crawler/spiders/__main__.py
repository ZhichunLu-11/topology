import os
from scrapy.cmdline import execute
import time
if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    try:
        execute(
            [
                'scrapy',
                'crawl',
                'capacity_spider',
                '-L',
                'ERROR'
            ]
        )
    except SystemExit:
        pass

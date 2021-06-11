from os import sched_get_priority_min
from ssl import get_server_certificate
import scrapy
import math
import time
from scrapy.selector import Selector
from html.parser import HTMLParser
from fake_useragent import UserAgent
from scrapy.http import FormRequest
from pathlib import Path
import random
import base64
import csv
import pandas as pd


class capacity_spider(scrapy.Spider):
    name = "capacity_spider"
    channel_file_path = Path("../../../peruned_edges.csv")

    def get_scids(self):
        with open(self.channel_file_path, "r", encoding="utf-8") as f:
            channels = pd.read_csv(f)
        scids = list(channels["Unnamed: 0"])
        scids = [scid_iter[:-2] for scid_iter in scids]
        scids = list(set(scids))
        return scids

    def start_requests(self):
        scids = self.get_scids()
        url = "https://1ml.com/search"
        for scid in scids:
            formdata = {"q": scid}
            yield scrapy.FormRequest(url, formdata=formdata, meta={'scid': scid}, callback=self.parse)

    def parse(self, response):
        capacity = response.xpath('//li/div').get()[5:-10].replace(",", "")
        scid = response.meta['scid']
        with open('scid_capacity.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([scid, capacity])

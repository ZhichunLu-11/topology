import csv
from pathlib import Path

import pandas as pd
import scrapy
from fake_useragent import UserAgent


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

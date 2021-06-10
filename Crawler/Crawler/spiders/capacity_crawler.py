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
            # scid_bytes = scid.encode('ascii')
            # scid_based_64_encoded = base64.b64encode(
            #     scid_bytes).decode('ascii')
            # url = url_prefix+scid_based_64_encoded

            formdata = dict()
            formdata["q"] = "683749x371x0"

            yield scrapy.FormRequest(url, formdata=formdata, callback=self.parse)
            break

    def parse(self, response):
        capacity = int(response.xpath('//li/div').get()
                       [5:-10].replace(",", ""))

    # def parse_block(self, response):
    #     time.sleep(random.random())
    #     ua = UserAgent()
    #     if not validation(response):
    #         time.sleep(2)
    #         yield scrapy.Request(url=response.url, meta={'block': response['block']}, callback=self.parse_block, headers={'User-Agent': ua.random})
    #     block = response.meta['block']
    #     tx_num = response.selector.css('.d-flex.align-items-center')
    #     if len(tx_num) != 5:
    #         return 0
    #     tx_num = tx_num[0]
    #     tx_num = tx_num.css('::text').extract()
    #     tx_num = tx_num[1]
    #     tx_num = int(tx_num[12:-20])
    #     page = math.ceil(tx_num/50)
    #     for p in range(1, page+1):
    #         # print("block",block,"  page:",p)
    #         head = {'User-Agent': ua.random}
    #         url_page = "https://etherscan.io/txs?block=" + \
    #             str(block)+"&p="+str(p)
    #         yield scrapy.Request(url=url_page, callback=self.parse_addr_url, headers=head)

    # def parse_addr_url(self, response):
    #     time.sleep(random.random())
    #     addr_list = []
    #     ua = UserAgent()
    #     if not validation(response):
    #         time.sleep(1)
    #         yield scrapy.Request(url=response.url, callback=self.parse_addr_url, headers={'User-Agent': ua.random})
    #     for i in response.css('.far.fa-file-alt.text-secondary + span'):
    #         i = i.css('a')
    #         addr_list.append(i.css('::attr(href)').extract()[0][9:])
    #     for i in response.css('.far.fa-file-alt.text-secondary + a'):
    #         addr_list.append(i.css('::attr(href)').extract()[0][9:])
    #     for addr in addr_list:
    #         # get true code
    #         head = {'User-Agent': ua.random}
    #         url_contract = "https://etherscan.io/address/%s#code" % addr
    #         yield scrapy.Request(url=url_contract, dont_filter=True, meta={'a': addr}, callback=self.parse__contract, headers=head)
    #         # if it is not in db

    # def parse__contract(self, response):
    #     ua = UserAgent()
    #     if not validation(response):
    #         time.sleep(2)
    #         head = {'User-Agent': ua.random}
    #         yield scrapy.Request(url=response.url, dont_filter=True, meta={'a': response.meta['a']}, callback=self.parse__contract, headers=head)
    #     addr = response.meta['a']
    #     text = response.selector.css('pre#editor::text').extract()
    #     if len(text) != 0:
    #         print("111")
    #         code = text[0]
    #         code = HTMLParser().unescape(code)
    #         name = response.css('.h6.font-weight-bold.mb-0::text').extract()
    #         name = name[0]
    #         doc = ContractItem()
    #         doc['addr'] = addr
    #         doc['name'] = name
    #         doc['code'] = code
    #         yield doc

import requests
from bs4 import BeautifulSoup
import json
import re
from itertools import count
from time import sleep


# land.naver.com '부산시 사하구' 검색 후 단지 정보 크롤링
def get_list():    
    for page in count(1):
        page_url = "http://land.naver.com/search/complexSearch.nhn"
        params = {
            'complexSearchSortOption':'popularRank.asc',
            'cortarInfo':'[object Object]',
            'regionAddress':'부산광역시 사하구',
            'keywordInfo':'[object Object]',
            'flashData':'[object Object]',
            'flashMapRegionType':'region3',
            'regionType':'region2',
            'articleSizeTitle':'면적(㎡)',
            'minSize':0,
            'tradeType':'A1',
            'query':'부산시 사하구',
            'maxPrice':0,
            'resultCode':'S00',
            'isFirstSiteArticle':'true',
            'maxSize':0,
            'regionCode':2638000000,
            'isComplexRegion':'false',
            'isaleComplexCount':0,
            'complexCount':0,
            'minPrice':0,
            'complexSelectType':'all',
            'trendPrice':'all',
            'trendPriceDirectUse':'false',
            'trendPriceDirectMax':'null',
            'trendPriceDirectMin':'null',
            'stationDistanceUse':'false',
            'moveinDateUse':'false',
            'householdUse':'false',
            'page':page
            }
       
        print('################## page : {}##################'.format(page))

        r = requests.get(page_url, params=params)
        r.encoding = "utf-8"
        r = r.text
        r_dict = json.loads(r)
        
        r_list = r_dict['complexInfo']['complexList']

        for i in range(len(r_list)):
            r_dict = r_list[i]
            print(r_dict['complexTypeName'], r_dict['address'], r_dict['complexName'])

        sleep(0.5)

get_list()
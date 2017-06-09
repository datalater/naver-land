import requests
from bs4 import BeautifulSoup
import json
import re
from itertools import count
from time import sleep
import csv


# land.naver.com '부산시 사하구' 검색 후 단지 정보 크롤링


def get_list():    
    # query_text = input(">>> 검색할 행정구역을 입력하세요. ex. 부산시 사하구: ")
    
    for page in count(1):
        page_url = "http://land.naver.com/search/complexSearch.nhn"  

        pusan_dict = {
            '강서구' : 2644000000,
            '금정구' : 2641000000,
            '기장군' : 2671000000,
            '남구' : 2629000000,
            '동구' : 2617000000,
            '동래구' : 2626000000,
            '부산진구' : 2623000000,
            '북구' : 2632000000,
            '사상구' : 2653000000,
            '사하구' : 2638000000,
            '서구' : 2614000000,
            '수영구' : 2650000000,
            '연제구' : 2647000000,
            '영도구' : 2620000000,
            '중구' : 2611000000,
            '해운대구' : 2635000000,
        }

        query_text = input("부산시 내 행정구역을 입력하세요. ex. 강서구 : ")

        params = {
            'complexSearchSortOption':'popularRank.asc',
            'cortarInfo':'[object Object]',
            'regionAddress':'부산시 '+ query_text,
            'keywordInfo':'[object Object]',
            'flashData':'[object Object]',
            'flashMapRegionType':'region3',
            'regionType':'region2',
            'articleSizeTitle':'면적(㎡)',
            'minSize':0,
            'tradeType':'A1',
            'query':'부산시',
            'maxPrice':0,
            'resultCode':'S00',
            'isFirstSiteArticle':'true',
            'maxSize':0,
            'regionCode': pusandict[query_text],
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
       
        print('################## page : {} ##################'.format(page))

        r = requests.get(page_url, params=params)
        r.encoding = "utf-8"
        r = r.text
        r_dict = json.loads(r)

        # print(r_dict)
        
        if r_dict['complexInfo']['complexList']:
            r_list = r_dict['complexInfo']['complexList']

            for i in range(len(r_list)):
                r_dict = r_list[i]

                # row_list = [r_dict['complexTypeName'], r_dict['address'], r_dict['complexName'],"\n"]

                data = r_dict['complexTypeName'] + "\t" + r_dict['address'] + "\t" + r_dict['complexName'] + "\n"

                # print(r_dict['complexTypeName'], r_dict['address'], r_dict['complexName'])

                # with open('naver-land.csv', 'w', newline='') as csvfile:
                #     spamwriter = csv.writer(csvfile, delimiter=' ',
                #                             quotechar=',', quoting=csv.QUOTE_MINIMAL)
                #     # spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
                #     spamwriter.writerows([r_dict['complexTypeName'], r_dict['address'], r_dict['complexName']])
            
                with open('naver-land-'+query_text+'.txt, 'a', newline='') as f:
                    # f.write(",".join(row_list))
                    f.write(data)


            sleep(0.5)
        
        else:
            print("더 이상 자료 없음")
            break

get_list()
# -*- coding:utf-8 -*-

from spider.scrape.crawler import fetch
from spider.models.mysql import init_db

if __name__ == '__main__':
    # init_db()
    cookie = 'lastCity=101010100; _uab_collina=155621530970335108444826; __c=1557463185; __g=-; __l=l=%2Fwww.zhipin.com%2F&r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DgxrUf621vw9fIoHyze5GkyQbkfKooPVr0krhUkI9UG5QniJ9-cMmz256xREQtgDK%26wd%3D%26eqid%3Df0a5e26400010bcc000000025cd5008a; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1557303355,1557335458,1557373968,1557463185; __a=8042423.1556215310.1557373968.1557463185.131.6.12.85; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1557477740'
    print('开始抓取...')
    fetch(2, cookie)



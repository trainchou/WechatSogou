from wechatsogou import WechatSpider
import time
import re

wechats = WechatSpider()

if __name__ == '__main__':
    infos = wechats.search_gzh_info("",1)
    url=infos[0]['url']
    dict = wechats.get_gzh_article_dict(url)
    msgdict = dict['msgdict']
    articles = wechats.get_gzh_article_detail(msgdict)
    article = articles[0]
    pattern= re.compile(r"暗号“(.+)”[aA]")
    article_info = wechats.get_gzh_article_info(article)
    content_text = article_info['content']['content_text'].strip()
    match = pattern.search(content_text)
    if match:
        print(match.group(1))

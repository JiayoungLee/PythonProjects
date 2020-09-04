# !/user/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Jayoung"

'''
 gzbd 数据爬取
'''

import requests;
from bs4 import BeautifulSoup;
import re;

__wjw_region = "四川";
__wjw_domain = "http://wsjkw.sc.gov.cn";
__wjw_base_url = "/scwsjkw/gzbd01/ztwzlmgl.shtml";
__wjw_page_count = 10;


def gzbd_all_data():
    all_data = [];

    # 创建新闻列表页url 并且获取列表页的数据
    news_page_url = __wjw_domain;
    for i in range(1, __wjw_page_count + 1):
        if i == 1:
            news_page_url += __wjw_base_url;
        else:
            l = __wjw_base_url.split(".");
            l.insert(1, "_%d." % (i,));
            news_page_url += "".join(l);
        print("Visit url:"+news_page_url+"\n")
        news_list = news_page_data(news_page_url);
        print("    %s"%(news_list,));
        all_data += news_list;
        news_page_url = __wjw_domain;
    # print(all_data);
    return all_data;


# 爬取新闻列表页数据
def news_page_data(url):
    news_list = [];

    r = requests.get(url);
    r.encoding = r.apparent_encoding;

    bs = BeautifulSoup(r.text, "html.parser");
    li_list = bs.find(name="div", attrs={"class": "contMain fontSt"}).find_all(name='li');
    for li in li_list:
        child_span = li.findChildren("span", recursive=False)[0];
        child_a = li.findChildren("a", recursive=False)[0];
        # print(child_a.get_text());
        # print(child_a.get("href"));
        new_page_url = __wjw_domain + child_a.get("href");
        new_dict = new_page_data(new_page_url);
        new_dict["日期"] = child_span.get_text();
        new_dict["地区"] = __wjw_region;
        news_list.append(new_dict);

    return news_list;


# 爬取新闻页数据
def new_page_data(url):
    # 装载新闻页数据
    new_dict = {};

    # requests 获取页面内容
    r = requests.get(url);
    r.encoding = r.apparent_encoding;

    # 解析页面标签
    bs = BeautifulSoup(r.text, "html.parser");
    span_list = bs.find_all(name="span", attrs={"style": "font-size: 12pt;"});
    line = span_list[1].get_text();

    # 正则表达式提取数据 ，并装载到dict
    line_re = r'全省累计报告新型冠状病毒肺炎确诊病例(\d+)例\(其中境外输入(\d+)例\），' \
              r'累计治愈出院(\d+)例，死亡(\d+)例，目前在院隔离治疗(\d+)例，(\d+)人尚在接受医学观察。';
    # new_line_match = re.match(line_re, line);   match 会从开始位置匹配，匹配失败就不会再往下匹配了
    # search 不管开始匹配是否成功，都会匹配下去，直到结束。
    sea = re.search(line_re, line);

    # line_compile = re.compile(line_re);
    # print(new_line_math);
    if sea:
        new_dict["确诊数"] = sea.group(1);
        new_dict["境外输入数"] = sea.group(2);
        new_dict["治愈数"] = sea.group(3);
        new_dict["死亡数"] = sea.group(4);
        new_dict["隔离数"] = sea.group(5);
        new_dict["观察数"] = sea.group(6);
    return new_dict;


def requests_test(url):
    r = requests.get(url);
    r.encoding = r.apparent_encoding;
    # print(r.text);
    # print(r.status_code);
    # print(r.url);
    # print(r.headers);
    # print(r.headers['Content-Type'])
    return r.text;


def bs4_test(response_text):
    new_dict = {};
    bs = BeautifulSoup(response_text, "html.parser");
    span_list = bs.find_all(name="span", attrs={"style": "font-size: 12pt;"});
    line = span_list[1].contents[0].replace("\u2002", "");
    print(line);
    line_re = r'^截至9月3日0时，全省累计报告新型冠状病毒肺炎确诊病例(\d+)例\(其中境外输入(\d+)例\），' \
              r'累计治愈出院(\d+)例，死亡(\d+)例，目前在院隔离治疗(\d+)例，(\d+)人尚在接受医学观察。';
    new_line_math = re.match(line_re, line);
    new_dict["确诊数"] = new_line_math.group(1);
    new_dict["境外输入数"] = new_line_math.group(2);
    new_dict["治愈数"] = new_line_math.group(3);
    new_dict["死亡数"] = new_line_math.group(4);
    new_dict["隔离数"] = new_line_math.group(5);
    new_dict["观察数"] = new_line_math.group(6);


if __name__ == "__main__":
    # url = "http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/2020/9/3/fe0eb6e3101d4709a9bbd27f5a12ae78.shtml";
    url = "http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/ztwzlmgl.shtml";
    # r = requests_test(url);
    # bs4_test(r);
    # print(new_page_data(url));
    # print(news_page_data(url));
    # gzbd_all_data();

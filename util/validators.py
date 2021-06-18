# -*- coding: utf-8 -*-

import requests
from re import findall
from handler.configHandler import ConfigHandler
from handler.logHandler import LogHandler

w_log = LogHandler("validator")
conf = ConfigHandler()
validators = []

def validator(func):
    validators.append(func)
    return func


@validator
def formatValidator(proxy_obj):
    """
    检查代理格式
    :param proxy_obj:
    :return:
    """
    proxy = proxy_obj.proxy
    
    verify_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}"
    _proxy = findall(verify_regex, proxy)
    return True if len(_proxy) == 1 and _proxy[0] == proxy else False


@validator
def timeOutValidator(proxy_obj):
    """
    检测超时
    :param proxy_obj:
    :return:
    """

    proxy = proxy_obj.proxy

    proxies = {"http": "http://{proxy}".format(proxy=proxy), "https": "https://{proxy}".format(proxy=proxy)}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
               'Accept': '*/*',
               'Connection': 'keep-alive',
               'Accept-Language': 'zh-CN,zh;q=0.8'}
    try:
        Check_urls = {
            "opendota": "http://api.opendota.com/api/players/148351321/wl",
            "steam": "http://api.steampowered.com/ISteamWebAPIUtil/GetServerInfo/v0001/"
        }
        
        r = requests.get(Check_urls[proxy_obj.goal_web], headers=headers, proxies=proxies, timeout=3)

        if proxy_obj.goal_web == "opendota":
            if r.status_code == 200 and 'win' in r.text:
                return True
        elif proxy_obj.goal_web == "steam":
            if r.status_code == 200 and "servertime" in r.text:
                return True
        else:
            return False

    except Exception as e:
        pass
    return False


@validator
def customValidator(proxy_obj):
    """
    自定义validator函数，校验代理是否可用
    :param proxy_obj:
    :return:
    """

    return True

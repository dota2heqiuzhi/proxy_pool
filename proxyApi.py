# -*- coding: utf-8 -*-
# !/usr/bin/env python
import platform
from werkzeug.wrappers import Request, Response
from flask import Flask, jsonify, request

import random
from handler.proxyHandler import ProxyHandler
from handler.configHandler import ConfigHandler
from helper.proxy import Proxy

app = Flask(__name__)
conf = ConfigHandler()
proxy_handler = ProxyHandler()


@app.route('/get_all')
def get_all():
    proxies = proxy_handler.getAll()
    return jsonify([_.to_dict for _ in proxies])

# 仅自己调用，返回支持steam api的proxy，用于抓全量DOTA2对局基本数据
@app.route('/get_one')
def get_one():
    try:
        proxies = proxy_handler.getAll()
        return jsonify(random.sample([p.to_dict for p in proxies if p.goal_web == "steam"], 1))        
    except:
        return jsonify({"error": "没有可用的代理！"})

@app.route('/count')
def count():
    proxies = proxy_handler.getAll()
    return jsonify({"proxy_count": len(proxies)})

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    from werkzeug.serving import run_simple
    run_simple('localhost', 9000, app)

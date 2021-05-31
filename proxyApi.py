# -*- coding: utf-8 -*-
# !/usr/bin/env python
import platform
from werkzeug.wrappers import Request, Response
from flask import Flask, jsonify, request

from handler.proxyHandler import ProxyHandler
from handler.configHandler import ConfigHandler
from helper.proxy import Proxy

app = Flask(__name__)
conf = ConfigHandler()
proxy_handler = ProxyHandler()


@app.route('/get_all/')
def getAll():
    proxies = proxy_handler.getAll()
    return jsonify([_.to_dict for _ in proxies])

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    from werkzeug.serving import run_simple
    run_simple('localhost', 9000, app)

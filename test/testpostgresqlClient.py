if __name__ == '__main__':
    from db.dbClient import DbClient
    from helper.proxy import Proxy

    uri = 'PostgreSQL://root:1016heqiuzhI@127.0.0.1:5432/proxypool'
    db = DbClient(uri)
    proxy = Proxy('127.0.0.1:1010', goal_web = 'haha')
    db.clear()

    # print("put: ", db.put(proxy))

    print("getAll: ", db.getAll())

    # for goal_web, proxy in db.getAll().items():
    #     print("delete: ", db.delete(proxy))

    
    

    # print("get: ", db.get())

    # print("exists: ", db.exists("27.38.96.101:9797"))

    # print("exists: ", db.exists("27.38.96.101:8888"))

    # print("pop: ", db.pop())

    # print("clear: ", db.clear())

    # print("getCount", db.getCount())
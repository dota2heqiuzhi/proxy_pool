# -*- coding: utf-8 -*-
# !/usr/bin/env python

__author__ = "qiuzhihe"

import psycopg2
from psycopg2 import pool
from handler.logHandler import LogHandler

class PostgresqlClient(object):

    _pool = None

    def __init__(self, **kwargs):
        if PostgresqlClient._pool is None:
            # self.initPool(kwargs['host'], kwargs['port'])
            self.initPool(kwargs)

    @staticmethod
    def initPool(kwargs):
        PostgresqlClient._pool = psycopg2.pool.ThreadedConnectionPool( 
            1, 200, 
            user=kwargs['username'], password=kwargs['password'],
            host=kwargs['host'], port=kwargs['port'], database=kwargs['db']
        )

        try:
            conn = PostgresqlClient._pool.getconn()
            sql = """
            CREATE TABLE IF NOT EXISTS proxy(
                proxy VARCHAR(30) PRIMARY KEY,
                goal_web VARCHAR(30) NOT NULL
            )
            """
            conn.cursor().execute(sql)
            conn.commit()
            conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            exit(error)

    def put(self, proxy_obj):
        conn = PostgresqlClient._pool.getconn()
        try:
            sql = f'INSERT INTO proxy (proxy, goal_web) VALUES (%s, %s)'
            conn.cursor().execute(sql, (proxy_obj.proxy, proxy_obj.goal_web) )
            conn.commit()
        # 插入重复的proxy
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            conn.close()
        conn.close()
        return proxy_obj

    def delete(self, proxy):
        conn = PostgresqlClient._pool.getconn()
        try:
            sql = f"DELETE FROM proxy WHERE proxy = '{proxy}'"
            conn.cursor().execute(sql)
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            conn.close()
        conn.close()		
        return proxy

    def getAll(self):
        data = {}
        conn = PostgresqlClient._pool.getconn()
        cursor = conn.cursor()
        cursor.execute('SELECT goal_web, proxy  FROM proxy')
        conn.commit()
        results = cursor.fetchall()
        for i, result in enumerate(results):
            data[i] = {'goal_web': result[0], 'proxy': result[1]}
        conn.close()
        return data

    def getCount(self):
        conn = PostgresqlClient._pool.getconn()
        try:
            cursor = conn.cursor()
            sql = "select count(*) FROM proxy"
            conn.cursor().execute(sql)
            conn.commit()
            result = cursor.fetchone()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            conn.close()
        conn.close()		
        return result

    def test(self):
        log = LogHandler('postgresql_client')
        try:
            print(self.getCount())
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def clear(self):
        conn = PostgresqlClient._pool.getconn()
        try:
            sql = f"DROP TABLE IF EXISTS proxy "
            conn.cursor().execute(sql)
            conn.commit()
            sql = """
            CREATE TABLE IF NOT EXISTS proxy(
                goal_web VARCHAR(30),
                proxy VARCHAR(30),
                PRIMARY KEY (goal_web, proxy)
            )
            """
            conn.cursor().execute(sql)
            conn.commit()
            conn.close()		
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            conn.close()

    def exists(self, key):
        """
        未使用
        """
        pass
        # conn = PostgresqlClient._pool.getconn()
        # cursor = conn.cursor()
        # cursor.execute("SELECT proxy FROM %s WHERE proxy='%s'" % (self.name, key))
        # conn.commit()
        # if cursor.fetchone() is None:
        # 	conn.close()
        # 	return False
        # conn.close()
        # return True			

    def getNumber(self):
        """
        未使用
        """
        pass
        # conn = PostgresqlClient._pool.getconn()
        # cursor = conn.cursor()
        # cursor.execute("SELECT COUNT(*) FROM %s" % self.name)
        # conn.commit()
        # result = cursor.fetchone()[0]
        # conn.close()
        # return result

    def update(self, key, value):
        """
        未使用
        """
        pass

    def get(self, proxy):
        """
        未使用
        """
        pass

    def changeTable(self, name):
        # self.name = name
        """
        未使用
        """
        pass

    def pop(self):
        # """
        # 弹出一个代理, 只对raw_proxy表使用
        # :return: dict {proxy: value}
        # """
        # conn = PostgresqlClient._pool.getconn()
        # cursor = conn.cursor()
        # cursor.execute("SELECT proxy FROM %s LIMIT 0,1" % self.name)
        # conn.commit()
        # result = cursor.fetchone()
        # data = None
        # if result is not None:
        # 	self.delete(result[0])
        # 	data = {"proxy" : result[0]}
        # conn.close()
        # return data
        """
        未使用
        """
        pass

if __name__ == '__main__':
    c = PostgresqlClient(**{'host': '127.0.0.1', 'port': 5432})
    # print( c.pop() ) 
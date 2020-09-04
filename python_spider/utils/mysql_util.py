# !/user/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Jayoung"

'''
mysql util
'''

import pymysql;


def get_connect_cursor():
    conn = pymysql.connect(host="localhost", user="root", password="123", db="python", charset="utf8")
    return conn, conn.cursor();


def execute_(sql):
    conn,cur = get_connect_cursor();
    result = None;
    # 判断是否以select开头
    if sql.startswith("select"):
        result = execute_query(cur, sql);
        close_connect_cursor(conn, cur);
    else:
        result = execute_insert_update_delete(cur, sql);
        commit_(conn);
        close_connect_cursor(conn, cur);
    return result;

def execute_insert_update_delete(cursor, sql):
    result = cursor.execute(sql);
    return result;


def execute_query(cursor, sql):
    cursor.execute(sql);
    return cursor.fetchall();


def commit_(conn):
    conn.commit();


def close_connect_cursor(conn, cur):
    conn.close();
    cur.close();

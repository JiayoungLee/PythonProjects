# !/user/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Jayoung"

'''
mysql test
'''

# import pymysql;
import mysql_util;

def insert_resource():
    conn,cur = mysql_util.get_connect_cursor();
    sql = "insert into resource (resource_uri, resource_name, permission) values ('a','b','c')";
    result = mysql_util.execute_insert_update_delete(cur, sql);
    print(result);
    mysql_util.commit_(conn);
    mysql_util.close_connect_cursor(conn,cur);

    # cur = conn.cursor();
    # result = cur.execute("insert into resource (resource_uri, resource_name, permission) values ('a','b','c')")
    # print(result);
    # conn.commit();
    # cur.close();
    # conn.close();

def query_resource():
    conn,cur = mysql_util.get_connect_cursor();
    sql = "select * from resource";
    result = mysql_util.execute_query(cur, sql);
    print(result);
    mysql_util.commit_(conn);
    mysql_util.close_connect_cursor(conn,cur);

if __name__ == "__main__":
    insert_resource();
    query_resource();
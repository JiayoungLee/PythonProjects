# !/user/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Jayoung"

'''
excel util
'''

import openpyxl;


def create_excel(header, body, file_path):
    # 获取 workbook 对象
    workbook = openpyxl.Workbook();
    # 获取sheet对象
    # active_sheet = workbook.get_active_sheet(); 已过时
    active_sheet = workbook.active;
    # 数据操作
    active_sheet.append(header);
    for item in body:
        active_sheet.append(item);

    # 文件保存
    workbook.save(filename=file_path);

if __name__ == "__main__":
    l = list(range(1, 10));
    print(1[0]);

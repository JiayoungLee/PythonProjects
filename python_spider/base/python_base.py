# !/user/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Jayoung"

'''
python base demo
'''

import re;
import math;

# ==== 输入输出 ====
# name = input();
# print(name);

name = 11;
print(name);
b = "Jayoung";

print("hello world");
# 逗号间隔字符串 => 空格间隔字符串
print("hello", "world", "jayoung");

# 占位符 %后面的括号代表 元组（不可变） 单个占位符后面得跟个逗号，表示是元组
print("hello %s" % name);
print("hello %s" % (name,));
print("hello %s - %s" % (name, b));

# 数据类型
a = 11;
print("a=%s 的数据类型: %s" % (a, type(a)));

a = 11.11;
print("a=%s 的数据类型: %s" % (a, type(a)));

a = "abcde";
print("a=%s 的数据类型: %s" % (a, type(a)));

a = ["abcde", 123, 12.3];
print("a=%s 的数据类型: %s" % (a, type(a)));

# tuple 元组
a = ("scsa", 32, 33.3);
print("a=%s 的数据类型: %s" % (a, type(a)));

# dic 字典
a = {"name": "jayoung", "age": "62"};
print("a=%s 的数据类型: %s" % (a, type(a)));

a = None;
print("a=%s 的数据类型: %s" % (a, type(a)));

# a = True and False;
# a = not False;
a = 1 > 2;
print("a=%s 的数据类型: %s" % (a, type(a)));

# ==== 运算符 ====
print((2 + 44 / 12) * 3);
# 地板除----取整
print(15 // 2)
print(12 % 5)
# 乘方
print(2 ** 3)

# ==== 字符串 ====
print(u'李佳阳');
print(r'李佳阳');
print(b'a');

# ==== ASCII转换 ====
print("98-->%s; a-->%s" % (chr(98), ord('a')));
# ==== encode && decode ====
print("cdsa".encode("ascii"));
# print("中文".encode("ascii")); # ASCII只定义了127个字符，中文无法解析
print("中文".encode("utf-8"));  # 转化为byte类型
print(b'cdsa'.decode("ascii"));

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf-8"));
print("\n")

# ==== function ====
print(len("hhhh"))  # 对于str计算字符数
print(len("李佳阳"))  # 对于str计算字符数
print(len("hhhh".encode("utf-8")))  # 对于bytes计算字符数
print(len("李佳阳".encode("utf-8")))  # 对于bytes计算字符数 --- 一个中文站3个字符
b = "李佳阳"
c = "abadfkjajdlskfjaiuerjdfd";
print(b.replace("佳", " "))
print(b)

print(c.find("ja"));  # 第一次出现该字符串的下标
print(c.rfind("ja"));  # 倒数第一次出现该字符串的下标

print("  ".isspace());

# ==== 字符串格式化 ====
print("%s ---- %2d ---- %04d" % (10, 4, 3));

print("%f ---- %.2f" % (32.32325, 4245.454512));  # 保留两位小数

print("%x" % 333);  # 格式化为十六进制

print("%s%%%s" % ("3", "2"));  # 转义字符

print([1, 2, 3]);
print(list("%s" % x for x in range(2, 10)));
print("Hi {0}, 成绩提高了{1:.1f}%".format("小明", 1.234));
print("Hi {0}, 成绩提高了{1}%".format("小明", "%.1f" % 1.234));
print("=".join(["sdsac", "sdsa", "djfkd"]));  # list转化为字符串，并以引号里面的字符连接

# ==== 正则表达式 ====
# 匹配字符串
email_re = "^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$";
if re.match(email_re, "jayounglee@163.com"):
    print("ok");
else:
    print("error");

# ==== 切分字符串 ====
print("a  b c".split(" "));
print(re.split(r'\s+', "a  b c"));
print(re.split(r"[\s\,\;]+", "a,b;; c   d"));

# ==== 分组 ====
# 分组提取电话号码
match = re.match(r'^(\d{3})-(\d{3,8})$', "020-123456")
print(match.group());
print(match.group(0));  # 0就是原生的字符串
print(match.group(1));
print(match.group(2));

new_line = r'截至9月3日0时，全省累计报告新型冠状病毒肺炎确诊病例655例(其中境外输入114例），' \
           r'累计治愈出院630例，死亡3例，目前在院隔离治疗22例，926人尚在接受医学观察。';
new_line_re = r'^截至9月3日0时，全省累计报告新型冠状病毒肺炎确诊病例(\d+)例\(其中境外输入(\d+)例\），' \
              r'累计治愈出院(\d+)例，死亡(\d+)例，目前在院隔离治疗(\d+)例，(\d+)人尚在接受医学观察。$';
# 方式一
new_line_match = re.match(new_line_re, new_line);
print(new_line_match.group(0));
print(new_line_match.group(1));
print(new_line_match.group(2));
print(new_line_match.group(3));
print(new_line_match.group(4));
print(new_line_match.group(5));
print(new_line_match.group(6));
# 方式二
new_line_compile = re.compile(new_line_re);
print(re.search(new_line_compile, new_line).group(1));
print(re.search(new_line_compile, new_line).group(2));
print(re.search(new_line_compile, new_line).group(3));
print(re.search(new_line_compile, new_line).group(4));
print(re.search(new_line_compile, new_line).group(5));
print(re.search(new_line_compile, new_line).group(6));
# 方式一 与方式二 的区别
'''
match 是从头开始的
search 任何地方都可以匹配
'''

# 贪婪匹配  全部匹配
print(re.match(r'^(\d+?)(0*)$', '102300').groups());  # ('1023', '00')

# ==== list & tuple ====
# ==== list ====
l = ["jayoung", 2, 2.11, None, True];
print(l[-2]);

list2 = list(range(1, 10));
print(list2);
l.append("jayoung");
print(l);
l.insert(2, "Lee");
print(l);
l.pop();
print(l);
l.pop(2);
print(l);
l.append(list2);
print(l);
l += list2;  # 等价于 l.extend(list3);
print(l);
l[0] = "hhhh";
print(l);

# ==== 元组 tuple====
list3 = list(range(1, 10));
t = ("aaa", 12, 12.2, True, None, list3);  # tuple元组初始化了就不能变了看，但是如果它的元素中有list这类可变的元素也就变成了可变的了
print(t)
list3.pop();
print(t);
t2 = tuple(range(1, 10));
print(t2);
print(max(t2));  # 只针对于全是数字的tuple
# 元组只有一个元素的时候，后面得加一个逗号，以区别数学的括号
t3 = (1,);
print(t3);
print(tuple(list3));  # list 转化为 tuple

# ==== dict & set =====
d = {"name": "jayoung", "age": "33"};
print(d);
print(d.keys());
print(d.values());
print(d.items())
print(d.get("name"));
print(d.get("name1", "aaaa"));  # 如果娶不到值，就使用后面的默认值
d["name"] = "JayoungLee";  # 通过键赋值
d["sex"] = "女";
print(d);
d.pop("sex");  # 通过键删除
print(d);
print(len(d));

# ==== set 一组key的集合 无重复元素 无序====
s = set(["sds", True, None, 212, 22.3]);
s2 = {"sds", 212, 22.22, "cdsafdf"};
s.add("Jayoung");
print(s);
# s.pop();
s.remove("sds");  # 删除指定值  下标不是从0开始 注意和pop联用的时候，有可能出现bug
print(s);
print(type(s2));
print(s & s2);
print(s | s2);

# ==== 判断语句 ====
aa = 20;
if aa < 10:
    print("aaaa");
elif 10 <= aa < 20:
    print("bbbb");
else:
    print("cccc");

a = " a";
if a and a.strip():  # strip() 是去掉字符串首位的字符（默认为空格或换行符）
    print(a);
else:
    print("Null String");

a, b, c = 1, 2, 3;
print(a if (b > c) else c);

# ==== 循环 ====
a = list(range(10));
sum1 = 0;
for i in a:
    sum1 += i;
print("sum1: %s" % sum1);

sum1 = 0;
i = 0;
while "a":
    sum1 += 1;
    if sum1 > 10:
        break;
print("sum1: %s" % sum1);


# ==== 函数 ====
def test(a):
    a += 3;
    return a;


print(test(1));


def test_2(x, y="jayoung"):
    print(x, y);


# 可变参数
def test_3(*num):
    count = 0;
    for i in num:
        count += 1;
    return count;


# 可变关键字参数
def test_4(name, **kv):
    if "city" in kv:
        print("name:%s, city:%s" % (name, kv.get("city")));
    else:
        print("name:%s, city:%s" % (name, "Unknown"));


# 命名关键字参数  在调用该函数时，*号后面的参数名必须一致
def test_5(name, *, city):
    if not isinstance(city, (str,)):
        raise TypeError("Bad Type");
    print("name:%s, city:%s" % (name, city));

# 内置函数
print(hex(16)); #  10进制转16进制
print(float("22.2"));
print(print("djfkdjkf"));
print(sum(range(1,101)));
print(sum(list(range(101))));

if __name__ == "__main__":
    # print(test(6));

    # test_2("hello", "ljy");
    # test_2("hello");

    # print(test_3(1, 2, 3, 4));
    # print(test_3(*list(range(1, 4))));

    # test_4("Jayoung", **{"age": 33});
    # test_4("JayoungLee", **{"city": "成都"});

    # test_5("Jayoung", city="cd");
    pass;

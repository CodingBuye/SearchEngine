"""
正则表达式：
特殊字符：
1. ^ $ * ? + {2} {2,} {2,5}
2. [] [^] [a-z] .
3. \s \S \w \W
4. [\u4E00-\u9FA5] () \d
"""
import re

line = "bobby123"
regex_str = "^b.*3$"  # ^表示以它后边的字符开头开头；.表示任意字符(一个)；*表示前面的字符可以出现任意次
if re.match(regex_str, line):
    print("yes")

line1 = "booooooobby123"
regex_str1 = ".*(b.*b).*"
# 贪婪匹配，从右往左匹配
match_obj1 = re.match(regex_str1, line1)
if match_obj1:
    print(match_obj1.group(1))  # 返回的结果是：bb

line2 = "booooooobby123"
regex_str2 = ".*?(b.*?b).*"  # ?遇到一个b就停止
# 非贪婪匹配,从左开始
match_obj2 = re.match(regex_str2, line2)
if match_obj2:
    print(match_obj2.group(1))  # 返回的结果是：booooooob


line3 = "booooooobby123"
regex_str3 = ".*(b.+b).*"  # +表示前面的字符至少出现一次
match_obj3 = re.match(regex_str3, line3)
if match_obj3:
    print(match_obj3.group(1))


line4 = "booooooobby123"
regex_str4 = ".*(b.{2,}b).*"  # {2,}表示前面的字符至少出现2次
match_obj4 = re.match(regex_str4, line4)
if match_obj4:
    print(match_obj4.group(1))


line5 = "bobby123"
regex_str5 = "(bobby|bobby123)"  # |表示匹配其中一个
match_obj5 = re.match(regex_str5, line5)
if match_obj5:
    print(match_obj5.group(1))


line6 = "aoobby123"
regex_str6 = "([abcd]oobby123)"  # []表示匹配其中一个
match_obj6 = re.match(regex_str6, line6)
if match_obj6:
    print(match_obj6.group(1))


line7 = "你 好"
regex_str7 = "(你\s好)"  # \s表示匹配一个空格 \S表示除空格以外的任何一个字符都可以
match_obj7 = re.match(regex_str7, line7)
if match_obj7:
    print(match_obj7.group(1))


line8 = "study in 北京邮电大学"
regex_str8 = ".*?([\u4E00-\u9FA5]+大学)"  # 匹配汉字
match_obj8 = re.match(regex_str8, line8)
if match_obj8:
    print(match_obj8.group(1))


line8 = "XXX出生于2001年北京邮电大学"
regex_str8 = ".*?(\d+)年"  # 匹配数字
match_obj8 = re.match(regex_str8, line8)
if match_obj8:
    print(match_obj8.group(1))


line9 = ['XXX出生于2001年6月1日',
         'XXX出生于2001/6/1',
         'XXX出生于2001-6-1',
         'XXX出生于2001-06-01',
         'XXX出生于2001-06']
regex_str9 = ".*出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}|[月/-]$|$))"
for item in line9:
    match_item = re.match(regex_str9, item)
    print(match_item.group(1))

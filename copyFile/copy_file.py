# -*- coding:utf-8 -*-
# @Time    : 2022/09/01 15:02
# @Author  : wyt
# @Remark:

old_name = input('请输入要备份文件的名称：')

# 返回文件名和文件后缀
index = old_name.rfind('.')
name = old_name[:index]
postfix = old_name[index:]
# 拼接备份后的文件名
new_name = name + '-bak' + postfix
# 打开旧文件和新文件
old_file = open(old_name, 'rb')
new_file = open(new_name, 'wb')

while True:
    # 一次读1024字节，防止文件过大影响性能
    content = old_file.read(1024)
    if len(content) == 0:
        break
    new_name.write(content)
# 关闭文件
old_file.close()
new_file.close()

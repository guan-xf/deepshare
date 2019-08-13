# /usr/bin/env python
# -*- coding=utf-8 -*-

import os


def modify(file, old, new):
    with open(file, 'r', encoding='UTF-8') as f:
        with open('tmp', 'w+', encoding='UTF-8') as t:
            content = f.read()
            if old in content:
                content = content.replace(old, new)
            else:
                print('您要修改的内容不存在')
            t.write(content)
    os.remove(file)
    os.rename('tmp', file)


def word_count(content):
    count = {'num': 0, 'alpha': 0, 'space': 0, 'other': 0}
    for i in content:
        if 47 < ord(i) < 58:
            count['num'] += 1
        elif ord(i) == 32:
            count['space'] += 1
        elif 64 < ord(i) < 91 or 96 < ord(i) < 123:
            count['alpha'] += 1
        else:
            count['other'] += 1

    print('您输入的内容是%s,其中数字有%d个，字母有%d个，空格有%d个，其他有%d个' %
          (content, count['num'], count['alpha'], count['space'], count['other']))


def instance_len(instance):
    if isinstance(instance, str) or isinstance(instance, list) or isinstance(instance, tuple):
        if len(instance) > 5:
            return True
        else:
            return False
    else:
        print('输入的数据类型无法识别')


def list_count(l):
    if isinstance(l, list):
        new_list = l[:2]
        print('保留下的内容为%s' % new_list)
        return l[2:]


def fun1(instance):
    new_list = list()
    if isinstance(instance, tuple) or isinstance(instance, list):
        for i in range(len(instance)):
            if i % 2 == 1:
                new_list.append(instance[i])
    return new_list


def fun2(origin):
    new_dict = dict()
    if isinstance(origin, dict):
        for key, value in origin.items():
            if len(value) > 2:
                new_dict[key] = value[:2]
    return new_dict


if __name__ == '__main__':
    modify('test.txt', 'bbb', 'aaa')
    s = input('请输入一段任意内容：')
    word_count(s)
    print(instance_len(['a', 'b', 'c', 'd']))
    print(instance_len(('a', 'b', 'c', 'd')))
    print(instance_len('hello world'))
    print(list_count('hello world'))
    print(fun1(['a', 'b', 'c', 'd']))
    print(fun1(('a', 'b', 'c', 'd')))
    print(fun2({'a': 'hello world', 'b': ['a', 'b', 'c', 'd'], 'c': ('e', 'f', 'g')}))

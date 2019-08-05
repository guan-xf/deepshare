# /usr/bin/env python
# -*- coding: utf-8 -*-

with open('account', 'r', encoding='UTF-8') as fa, open('blacklist', 'a+', encoding='UTF-8') as fb:
    user_info = dict()
    fb.seek(0)
    blacklist = fb.read().split('\n')

    for line in fa.readlines():
        name, password, money = line.split('|')
        user_info[name] = [password, money]

    def login():
        user = input('请输入账号：').strip()
        if user in user_info and user not in blacklist:
            pass_word = input('请输入密码：').strip()
            count = 0
            while pass_word != user_info[user][0]:
                pass_word = input('密码错误，请重新输入：').strip()
                count += 1
                if count == 2:
                    print('密码输入错误超过3次，账号被锁定！')
                    fb.write(user)
                    fb.write('\n')
                    with open('account', 'r', encoding='UTF-8') as f:
                        lines = f.readlines()
                    with open('account', 'w', encoding='UTF-8') as f_new:
                        for each in lines:
                            if each.startswith(user):
                                continue
                            f_new.write(each)
                    break
            print('登录成功！')
        elif user in blacklist:
            print('该账户被锁定，不得登录！')
        else:
            print('账号不存在！')

    # def regist():
    #     user = input('请输入账号：').strip()
    #     if user in user_info:
    #         print('当前用户已注册，请登录')
    #     elif user in
    #     password = input('请输入密码：').strip()

    if __name__ == '__main__':
        login()

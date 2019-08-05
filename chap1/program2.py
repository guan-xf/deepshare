# /usr/bin/env python
# -*- coding: utf-8 -*-

with open('account', 'r+', encoding='UTF-8') as fa, open('blacklist', 'a+', encoding='UTF-8') as fb:
    user_info = dict()
    fb.seek(0)
    blacklist = fb.read().split('\n')

    for line in fa.readlines():
        name, password, money = line.split('|')
        user_info[name] = [password, money]

    def login():
        tag = True
        count_lo = 0
        user_lo = input('请输入账号：').strip()
        if user_lo in user_info:
            while tag:
                password_lo = input('请输入密码：').strip()
                if password_lo == user_info[user_lo][0]:
                    print('登录成功')
                    break
                else:
                    print('密码输入错误！')
                    count_lo += 1
                if count_lo == 3:
                    print('密码输入错误超过3次，账号被锁定！')
                    fb.write(user_lo)
                    fb.write('\n')
                    with open('account', 'r', encoding='UTF-8') as f:
                        lines = f.readlines()
                    with open('account', 'w', encoding='UTF-8') as f_new:
                        for each in lines:
                            if each.startswith(user_lo):
                                continue
                            f_new.write(each)
                    break
        elif user_lo in blacklist:
            print('该账户被锁定，不得登录！')
        else:
            print('账号不存在！')

    def register():
        tag = True
        user_re = input('请输入账号：').strip()
        if user_re in user_info:
            print('当前用户已注册，请登录')
        elif user_re in blacklist:
            print('当前用户已锁定，不得重复注册！')
        else:
            password_re = input('请输入密码：').strip()
            conf_password = input('请再次输入密码：').strip()
            count_re = 0
            while conf_password != password_re:
                password_re = input('两次输入不一致，请重新输入：').strip()
                conf_password = input('请再次输入密码：').strip()
                count_re += 1
                if count_re == 2:
                    print('密码输入错误超过3次，请重新注册')
                    break
            while tag:
                salary_str = input('请输入您的薪资：')
                try:
                    if '.' in salary_str:
                        salary = float(salary_str)
                    else:
                        salary = int(salary_str)
                    tag = False
                    register_info = user_re + '|' + password_re + '|' + str(salary)
                    fa.write(register_info)
                except ValueError:
                    print('薪资输入错误')

    if __name__ == '__main__':
        login()

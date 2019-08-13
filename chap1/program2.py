# /usr/bin/env python
# -*- coding=utf-8 -*-


def login():
    with open('account', 'r', encoding='UTF-8') as fa,\
            open('blacklist', 'a+', encoding='UTF-8') as fb:
        user_info = dict()
        fb.seek(0)
        blacklist = fb.read().split('\n')
        for line in fa.readlines():
            name, password, money = line.split('|')
            user_info[name] = [password, money]
        tag = True
        count = 0
        user = input('请输入账号：').strip()
        if user in user_info:
            while tag:
                password_input = input('请输入密码：').strip()
                if password_input == user_info[user][0]:
                    print('登录成功')
                    return user
                else:
                    print('密码输入错误！')
                    count += 1
                if count == 3:
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
        elif user in blacklist:
            print('该账户被锁定，不得登录！')
        else:
            print('账号不存在！请注册')
            register()


def register():
    with open('account', 'a+', encoding='UTF-8') as fa, \
            open('blacklist', 'r', encoding='UTF-8') as fb:
        fa.seek(0)
        user_info = dict()
        for line in fa.readlines():
            name, password, money = line.strip('\n').split('|')
            user_info[name] = [password, money]

        blacklist = fb.read().split('\n')
        tag = True
        user_input = input('请输入账号：').strip()
        if user_input in user_info:
            print('当前用户已注册，请登录')
            login()
        elif user_input in blacklist:
            print('当前用户已锁定，不得重复注册！')
        else:
            password_input = input('请输入密码：').strip()
            conf_password = input('请再次输入密码：').strip()
            count = 0
            while conf_password != password_input:
                password_input = input('两次输入不一致，请重新输入密码：').strip()
                conf_password = input('请再次输入密码：').strip()
                count += 1
                if count == 2:
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
                    register_info = user_input + '|' + password_input + '|' + str(salary)
                    fa.write('\n' + register_info)
                    print('账号注册成功！')
                except ValueError:
                    print('薪资输入错误')


def shopping(user_login = '1'):
    with open('account', 'r+', encoding='UTF-8') as fa:
        fa.seek(0)
        user_info = dict()
        for line in fa.readlines():
            name, password, money = line.strip('\n').split('|')
            user_info[name] = [password, money]
        goods_dic = {'1': {'apple': 10}, '2': {'mac': 10000}, '3': {'iphone': 8000}, '4': {'lenovo': 30000}, '5': {'chicken': 10}}
        goods_list = []
        print('*' * 20)
        for index, good in enumerate(goods_dic):
            goods_list.append(good)
        print(goods_list)
    #
#     while True:
#         choice = input('请输入需要够买的商品：').strip()
#         try:
#             number = int(input('请输入商品购买数量：'))
#         except ValueError:
#             number = int(input('输入有误，请重新输入数量：'))
#         if choice not in goods_dic.keys():
#             print('未找到对应商品，请重新输入')
#             continue
#         else:
#             cast = goods_dic[choice] * number
#             if cast <= float(user_info[user_given][1]):
#                 print('购买成功！')
#                 float(user_info[user_given][1]) - cast
#                 user_info[user_given][1] = str(float(user_info[user_given][1]) - cast)
#                 with open('account', 'r', encoding='UTF-8') as f:
#                     lines = f.readlines()
#                 with open('account', 'w', encoding='UTF-8') as f_new:
#                     for each in lines:
#                         if each.startswith(user_given):
#                             f_new.write(user_given + '|' + user_info[user_given][0] + '|' + user_info[user_given][1])
#                             continue
#                         f_new.write(each)
#             else:
#                 if_charge = input('账户余额不足!是否充值？y/n')
#                 if if_charge == 'y':
#                     charge = input('请输入要充值的金额：')
#                     try:
#                         if '.' in charge:
#                             user_info[user_given][1] = str(float(charge) + float(user_info[user_given][1]))
#
#                         else:
#                             user_info[user_given][1] = str(int(charge) + int(user_info[user_given][1]))
#
#                         with open('account', 'r', encoding='UTF-8') as f:
#                             lines = f.readlines()
#                         with open('account', 'w', encoding='UTF-8') as f_new:
#                             for each in lines:
#                                 if each.startswith(user_given):
#                                     f_new.write(
#                                         user_given + '|' + user_info[user_given][0] + '|' + user_info[user_given][1])
#                                     continue
#                                 f_new.write(each)
#                     except ValueError:
#                         print('薪资输入错误')
#
#         if_quit = input('是否继续购买其他商品？Y/N').upper()
#         if if_quit == 'N':
#             break
#         elif if_quit != 'Y':
#             print('输入错误，程序退出')
#             break


if __name__ == '__main__':
    # while True:
    #     print('请选择需要的操作'.center(20, '='))
    #     print('1.登录'.ljust(18, ' '), '2.注册')
    #     print('=' * 25)
    #     operation = input('您的选择：')
    #     if operation == '1':
    #         user = login()
    #         if user:
    #             pass
    #         else:
    #             break
    #
    #     elif operation == '2':
    #         register()
    #         continue
    #     else:
    #         print('无此选项，请重新操作！')
    #         continue
    shopping()

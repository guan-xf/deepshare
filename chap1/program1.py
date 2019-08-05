# /usr/bin/env python
# -*- coding=utf-8 -*-

menu = {
    '汽车': {
        '轿车': {
            '宝马': {
                '宝马760': {},
                '宝马M5': {},
                '宝马M3': {}
            },
            '奔驰': {
                '奔驰C180': {},
                '奔驰E260': {},
                '奔驰S600': {}
            },
            '奥迪': {
                '奥迪A4L': {},
                '奥迪A6':{}
            },
        },
        '越野车': {
            '保时捷': {
                '保时捷Macan': {},
                '保时捷Cayenne': {}
            },
            '路虎': {},
            '英菲尼迪': {}
        },
        '卡车': {},
        '公交车': {}
    },
    '飞机': {
        '战斗机': {
            '国产': {
                '歼-16': {},
                '歼-20': {},
                '歼-10': {},
            },
            '美产': {
                'F-35': {},
                'F-15': {},
                'F-22': {}
            }
        },
        '客机': {},
        '直升机': {}
    }
}
tag = True
while tag:
    menu1 = menu
    for key in menu1:
        print(key)
    choice1 = input('请输入要查看的内容（退出按q）>>>:').strip()
    if choice1 == 'q':
        tag = False
        continue
    elif choice1 not in menu1:
        print('无此选项，请重新输入')
        continue
    while tag:
        menu2 = menu1[choice1]
        for key in menu2:
            print(key)
        choice2 = input('请输入要查看的内容（退出按q，返回上一级按b）>>>：').strip()
        if choice2 == 'b':
            break
        elif choice2 == 'q':
            tag = False
            continue
        elif choice2 not in menu2:
            print('无此选项，请重新输入')
            continue
        while tag:
            menu3 = menu2[choice2]
            for key in menu3:
                print(key)
            choice3 = input('请输入要查看的内容（退出按q，返回上一级按b）>>>：').strip()
            if choice3 == 'b':
                break
            elif choice3 == 'q':
                tag = False
                continue
            elif choice3 not in menu3:
                print('无此选项，请重新输入')
                continue
            while tag:
                menu4 = menu3[choice3]
                for key in menu4:
                    print(key)
                choice4 = input('是否继续？（退出按q，返回上一级按b）>>>：').strip()
                if choice4 == 'b':
                    break
                elif choice4 == 'q':
                    tag = False
                    continue
                elif choice4 not in menu4:
                    print('无此选项，请重新输入')
                    continue
                else:
                    print('当前为末级菜单，请选择返回上一级或退出')
                    continue


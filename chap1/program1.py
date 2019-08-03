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
    choice1 = input('第一层>>>:').strip()
    if choice1 == 'b':
        break
    if choice1 == 'q':
        tag = False
        continue
    if choice1 not in menu1:
        continue
    while tag:
        menu2 = menu1[choice1]
        for key in menu2:
            print(key)
        choice2 = input('第二层>>>：').strip()
        if choice2 == 'b':
            break
        if choice2 == 'q':
            tag = False
            continue
        if choice2 not in menu2:
            continue
        while tag:
            menu3 = menu2[choice2]
            for key in menu3:
                print(key)
            choice3 = input('第三层>>>：').strip()
            if choice3 == 'b':
                break
            if choice3 == 'q':
                tag = False
                continue
            if choice3 not in menu3:
                continue
            while tag:
                menu4 = menu3[choice3]
                for key in menu4:
                    print(key)
                choice4 = input('是否继续>>>：').strip()
                if choice4 == 'b':
                    break
                if choice4 == 'q':
                    tag = False
                    continue

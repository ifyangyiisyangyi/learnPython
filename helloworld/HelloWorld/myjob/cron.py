import time

from django.core.mail import send_mail


def send_email():
    for i in range(10):
        print("发送次数 :" + str(i))
        time.sleep(3)
        res = send_mail('good afternoon my neighbour', "基友拍了拍我开始摇尾巴" + str(i), 'ifyangyiisyangyi@163.com',
                        ['122342748@qq.com'])
    print(res)

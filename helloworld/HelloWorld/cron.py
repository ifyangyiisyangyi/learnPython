from django.core.mail import send_mail

def send_email():
    res = send_mail('good afternoon my neighbour', "基友拍了拍我开始摇尾巴", '117645743@qq.com',
                    ['ifyangyiisyangyi@163.com'])
    print(res)

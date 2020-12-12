from os.path import expanduser,os
import time,subprocess
import os
print('Приуэт...')
time.sleep(2)
print('Для начала - установим все библиотеки и модули для корректной работы программы...')
time.sleep(3.5)
print('Вам ничего не придется делать, я все зделаю за вас...приятного пользования!')
time.sleep(4.3)
subprocess.call(["pip","install","requests"])
subprocess.call(["pip","install","html2text"])
subprocess.call(["pip","install","wget"])
subprocess.call(["pip","install","beautifulsoup4"])
subprocess.call(["pip","install","selenium"])
subprocess.call(["pip","install","wheel"])
subprocess.call(["pip","install","pyinstaller"])
subprocess.call(["pip","install","--upgrade","pip"])

time.sleep(5)
home= expanduser("~")
print(home)
print('SUCCESSS')
import requests,wget,html2text
time.sleep(2.5)
print('ВСЕ БИБЛЕОТЕКИ И МОДУЛИ БЫЛИ УСПЕШНО УСТАНОВЛЕНЫ!')
time.sleep(1.5)
print('А теперь ближе к делу...')
time.sleep(1.5)
while(1==1):
                print('1 - Скачать и установить скрипт с циклами')
                print('2 - Funny(Веселье)')
                print('666 - Кто меня создал...')
                
                frfr=int(input('Ваш вариант...'))
                if(frfr==1):
                                print('DOWNLOAD...')
                                time.sleep(2)
                                s='https://raw.githubusercontent.com/zizazop/wwwhackerrorandrey-zhuk-7ester4ester/main/andrey-*zhuk/4ester/www/PATRIK/pythonmycodewww.py'
                                os.makedirs(home+'/Desktop/'+'ANDREWCODE'+'/')
                                os.makedirs(home+'/Desktop/'+'ANDREWCODE'+'/ИСХОДНЫЙ-КОД-УСТАНОВЩИКА')
                                filename= wget.download(s)
                                os.rename(filename,u''+os.getcwd()+'/ANDREWCODE/'+filename)
                                s='https://raw.githubusercontent.com/zizazop/-/main/INSTALL%20XD.py'
                                filename= wget.download(s)
                                os.rename(filename,u''+os.getcwd()+'/ANDREWCODE/ИСХОДНЫЙ-КОД-УСТАНОВЩИКА'+filename)
                                time.sleep(2)
                                print('Успех! все установлено.')
                                time.sleep(1)
                                print('Пологаю вам нужно cmd?')
                                subprocess.call(['cmd'])
                                time.sleep(1.5)
                                print('GOOD')
                                time.sleep(3)
                                print('Если захочешь деталь осмотреть скрипт тогда зайди в исходный код скрипта приложеным к ранее скачаным файлам(P>S они в тойже папке:) ')
                                time.sleep(5)
                                print('А сейчас этот exe файл сам себя уничтожет:)')
                                time.sleep(2)
                                print('POKA')
                                time.sleep(8)
                                os.remove(home+'/'+'Desktop'+'/'+'INSTALATOR XD.exe')
                                
                if(frfr==666):
                                            solod=requests.get('https://vk.com/andrey47785')
                                            dikol = html2text.HTML2Text().handle(solod.text)
                                            print(dikol)
                                            time.sleep(1.5)
                                            print('....15sec')
                                            print('https://vk.com/andrey47785')
                                            time.sleep(0.5)
                                            print('https://vk.com/andrey47785')
                                            time.sleep(0.5)
                                            print('https://vk.com/andrey47785')
                                            time.sleep(0.5)
                                            print('https://vk.com/andrey47785')
                                            time.sleep(0.5)
                                            print('https://vk.com/andrey47785')
                                            time.sleep(16)
                if(frfr==2):
                                while(1==1):
                                                print('YOU SELECT FUNNY OPTIONS///')
                                                time.sleep(1)
                                                
                                                print('1 - Создание  заданое кол-во папок на рабочем столе...')
                                                time.sleep(1)
                                                print('2 - Скачать заданое кол-во картинок на рабочий стол')
                                                time.sleep(1)
                                                print('0 - EXIT')

                                                popcorn=int(input(...))
                                                
                                                if(popcorn>3)or(popcorn<1):
                                                               print('Я не понимаю...')
                                                if(popcorn==1):
                                                                print('СОЗДАЮ МНОГО ПАПОК...')
                                                                time.sleep(10)
                                                                idi=input('Как будет называтся ваша папка??')
                                                                idi1=input('А папка в этой папке?')
                                                                idi2=input('А третья папка во второй папке?')
                                                                dki=int(input('Кол-во циклов создания папок??'))  
                                                                if(dki>495):
                                                                                dki=495
                                                                                print('Принято решение добавить лишь 495 папок...')
                                                                ffff=((idi1+'/'+idi2+'/'))
                                                                ffff1=ffff*dki
                                                                os.makedirs(home+'/Desktop/'+idi+'/')
                                                                os.makedirs(home+'/Desktop/'+idi+'/'+ffff1)
                                                                time.sleep(1)
                                                                print('ВЫПОЛНЕНО!')
                                                                time.sleep(6)
                                                                print('BACK/////')
                                                if(popcorn==0):
                                                                break
                                                if(popcorn==2):
                                                                time.sleep(1.5)
                                                                print('creation photos ////....')
                                                                print('Фотографии будутт созданы на рабочем столе')
                                                                kolvo=int(input('Кол-во фоток на рабочем столе...'))
                                                                h=0
                                                                while(1==1):
                                                                                h=h+1
                                                                                sh=('https://i.ibb.co/gPjmbs1/BY-WWW-4ester-ANDREY.jpg')
                                                                                filename=wget.download(sh)
                                                                                os.rename(filename,u''+os.getcwd()+'/'+filename)
                                                                                if(h==kolvo):
                                                                                                print('COMPLETED!')
                                                                                                break


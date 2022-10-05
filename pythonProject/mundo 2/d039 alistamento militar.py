from datetime import date
idade = int(input('Em que ano você nasceu?: '))
ano = date.today().year
qanosTem = ano -idade
if qanosTem == 18:
    print('\033[7;32;40mVocê tem {} já esta na hora de se alistar ao serviço militar\033[m'.format(qanosTem))
elif qanosTem >=19:
    passou = qanosTem - 18
    print('\033[7;31;40mVocê tem {} já passou {} anos do tempo de se alistar! Vá urgentemente ao serviço militar\033[m '.format(qanosTem,passou))
else:
    falta = 18 - qanosTem
    print('\033[7;33;40mVocê tem {} é falta pouco! Você tem {} anos para se alistar\033[m  '.format(qanosTem,falta))

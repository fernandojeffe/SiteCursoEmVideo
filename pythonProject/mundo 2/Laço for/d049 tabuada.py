num = int(input('Digite a tabua de preferência: '))
tabuada = 1
for tabuada in range (10):
    print('{} x {} = {}'.format(num, tabuada+1, num * (tabuada+1)))
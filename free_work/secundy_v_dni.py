def seconds(n):
    days = (n//3600)//24
    hours = ((n//3600)%24)
    minuts = (n%3600)//60
    seconds = (n%3600)%60
    print(f'{days}:{hours}:{minuts}:{seconds}')
seconds(370000)
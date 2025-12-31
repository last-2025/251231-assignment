for i in (1, 15+1):
    if i %15 ==0:
        print('fizzbuzz')
    elif i %3 == 0:
        print('fizz')
    elif i %5 ==0:
        print('buzz')
    else:
        print(i)


###
try:
    print('try...')
    r = 10 /0
    print('result',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally')
    
    print('END')
##Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”


























































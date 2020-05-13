a , b  =  1 , 2
tổng  =  0
in ( a , end = "" )
trong khi ( a <= 4000000 - 1 ):
    nếu  một  %  2  ==  0 :
        tổng  + =  a
    a , b  =  b , a + b
    in ( a , end = "" )
in ( " \ n tổng số thuật ngữ số nguyên tố trong chuỗi:" , tổng cộng )

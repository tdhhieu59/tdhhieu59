def  Sequential_Search ( mảng , n , x ):
    cho  tôi  trong  phạm vi ( n ):
        if ( mảng [ i ] ==  x ):
            trả lại  tôi
    trở lại  - 1

mảng = []
n  = int ( đầu vào ( 'Mục bao nhieu:' ))
cho  k  trong  phạm vi ( n ):
    mục = đầu vào ( 'mục Nhap:' )
    mảng . phụ lục ( mục )
x  = input ( 'Nhap vao mục có thể hẹn giờ:' )
n =  len ( mảng )
result  =  Sequential_Search ( mảng , n , x )
nếu ( kết quả  ==  - 1 ):
    in ( "Phan tu khong co trong mang" )
khác :
    in ( "Phan tu co trong mang" , 'va co vi tri:' , kết quả )

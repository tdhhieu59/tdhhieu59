str = input ( "Nhập chuỗi:" )
dict  = {}
cho  n  trong  str :
    phím  =  dict . phím ()
    nếu  n  trong  các phím :
        ra lệnh [ n ] + =  1
    khác :
        dict [ n ] =  1
in ( dict )

nhập  datetime  dưới dạng  dt
định dạng =  '% Y-% m-% dT% H:% M:% S'
t1 =  dt . datetime . strptime ( '2008-10-12T14: 45: 52' , định dạng )
in ( 'Ngày' + str ( t1 . ngày ))
in ( 'Ngày' + str ( t1 . ngày ))
in ( 'Tháng' + str ( t1 . tháng ))
in ( 'Phút' + str ( t1 . phút ))
in ( 'Thứ hai' +  str ( t1 . giây ))

# Xác định ngày và giờ
t2 = dt . datetime . bây giờ ()
khác biệt = t2 - t1
in ( 'bao nhiêu ngày khác biệt?' +  str ( diff . ngày ))

class circle(object):
    def __init__(self, r):
        self.r=r
    def chuvi(self):
        return self.r*2*3.14
    def dientich(self):
        return self.r**2*3.14
r=int(input("nhap vao ban kinh: "))
c=circle(r)
print("chu vi hinh tron la: ",c.chuvi())
print("dien tich hinh tron la: ",c.dientich())

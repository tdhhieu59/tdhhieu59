class hinhchunhat(object):
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def dien_tich(self):
        return self.a*self.b
a=int(input("nhap chieu dai: "))
b=int(input("nhap chieu rong: "))
c=hinhchunhat(a,b)
print("dien tich hinh chư nhat la: ",c.dien_tich())

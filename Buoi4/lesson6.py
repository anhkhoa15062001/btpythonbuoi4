print("Chuyen chuoi hoa thanh Chu Thuong va Nguoc lai")
def hoathuong(line):
    x = ""
    for i in line:
        if i.islower():
            x+=i.upper()
        else:
            x+=i.lower()
    print(x)
line=input("Nhap chuoi: ")
hoathuong(line)


s = input("Nhap cau cua ban: ")
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isdigit():
        d["UPPER CASE"]+=1
    elif c.isalpha():
            d["LOWER CASE"]+=1
    else:
         pass
print("chu hoa:",d["UPPER CASE"])
print("chu thuong",d["LOWER CASE"])

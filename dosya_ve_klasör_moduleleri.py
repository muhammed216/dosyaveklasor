import os
os.getcwd()
os.listdir()
dosyalar = os.listdir()
for eleman in dosyalar:
    print(eleman)
    
print(os.getcwd())

os.mkdir('C:\\Users\\Namiq\\Desktop\\dosya ve klasör\\deneme')

print(os.listdir())
yeni_dosya = os.open('yeni_dosya.txt', os.O_RDWR|os.O_CREAT)
os.write(yeni_dosya, "Merhaba dunya!".encode())
os.close(yeni_dosya)
yeni_dosya = os.open('yeni_dosya.txt', os.O_RDONLY)
os.read(yeni_dosya)

icerik = os.read(yeni_dosya,5)
print(icerik)
os.close(yeni_dosya)
os.mkdir("deneme_yeni")
print(os.listdir())










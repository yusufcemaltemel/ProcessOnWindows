import os
import datetime
#mkdir , chdir , listdir , makedirs , rmdir , removedirs , remove (for files) , rename , stat (info about directory)

def create_directory():
    try:
        option_cr = str(input("Oluşturacağınız Dosyanın Adını Giriniz : "))
        option2 = input(f"{option_cr} Adlı Klasörün Oluşturulacağı Path Yolunu Giriniz : ")
        path = os.path.join(option2) #kalıp path yolu. Birdaha birdaha yazmamak için
        os.chdir(path)
        os.mkdir(option)
        show_dir = os.listdir(path)
        when = os.stat(option).st_mtime
        when_ = datetime.datetime.fromtimestamp(when)
        view = """
        {} Adlı Dosyanın Oluşturulma Tarihi : {}
        {} Adlı Dosyanın Oluşturulduğu Mevcut Klasördeki İçerikler : {}
        """.format(option,when_,option,show_dir)
        print(view)
    except FileExistsError:
        print("Dosya Zaten Var")
    except FileNotFoundError:
        print("Dosya Bulunamadı")

def rename_directory():
    option____ = str(input("İsmini Değiştireceğiniz Dosyanın Adını Eksiksiz Giriniz : "))
    option2 = str(input("Değiştirilecek İsmi Giriniz : "))
    os.rename(option____,option2)

def delete_directory():
    try:
        option_dl = str(input("Silinecek Dosyanın Adını Giriniz : "))
        os.rmdir(option)
        print(f"{option_dl} Adlı Dosyanız Başarıyla Silindi")
    except FileNotFoundError:
        print("Dosya Bulunamadı.")

def show_directory():
    option_ = str(input("İçindeki İçerikleri Görüntülemek İstediğiniz Klasörün Uzantısını Giriniz : "))
    show_dir = os.listdir(option_)
    for j in show_dir:
        if os.path.isfile(j):
            print(f"Dosya Adı : {j}")
        else:
            print(f"Klasör Adı : {j}")

#Kendi başına kullanılabilinir
def show_create_time_of_dir():
    option__ = str(input("Oluşturulma Tarihine Bakacağınız Dosyanın Adını Giriniz"))
    option2 = str(input(f"{option__} Adlı Dosyanın Bulunduğu Dosya Uzantısını Giriniz : "))
    when = os.stat(option2).st_mtime #time of create
    time_ = datetime.datetime.fromtimestamp(when)
    print(time_)

def delete_file():
    try:
        option___ = str(input("Silmek İstediğiniz Dosyanın Uzantısını Giriniz : "))
        transmission_path = os.path.join(option___)
        os.remove(transmission_path)
        print(f"{option} Adlı Dosyanız Başarıyla Silindi.")
    except FileNotFoundError:
        print("Dosya Bulunamadı.")

def show_cwd():
    cwd = os.getcwd()
    print(f"Mevcut Çalıştığınız Dizin : {cwd}")

def change_dir():
    option_ch = str(input("Geçiş Yapmak İstediğniz Dizinin Path Yolunuz Giriniz : "))
    os.chdir(option_ch)

head = """
            Dosya İşlemleri Uygulamasına Hoş Geldiniz
        
        1) Klasör Oluştur
        2) Klasörü Yeniden Adlandır
        3) Klasörü Sil
        4) Klasör İçeriğini Görüntüle
        5) Klasörün Oluşturulma Tarihine Bak
        6) Dosya Sil
        7) Mevcut Dizini 
        8) Dizini Değiştir
        9) Çıkış
"""

while True:
    print(head)
    option = str(input("Gerçekleştimek İstediğiniz İşlemin Numarasını Giriniz : "))
    if option == "1":
        create_directory()
    elif option == "2":
        rename_directory()
    elif option == "3":
        delete_directory()
    elif option == "4":
        show_directory()
    elif option == "5":
        show_create_time_of_dir()
    elif option == "6":
        delete_file()
    elif option == "7":
        show_cwd()
    elif option == "8":
        change_dir()
    elif option == "9":
        print("Çıkış Yapılıyor...")
        quit()
    else:
        print("Hatalı Seçim Yaptınız")
        input("Tekrar Denemek İçin Herhangi Bir Tuşa Basınız")
    input('Yeniden İşlem Yapmak İçin "Enter" Tuşuna Basınız.')
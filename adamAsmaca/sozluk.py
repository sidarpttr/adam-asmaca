import random

def sozluge_ekle(kelime):
    with open("./sozluk.txt","r+") as sozluk:
        veri = sozluk.readlines()
        if f"{kelime}\n" in veri:
            print("zaten var")
        else:
            sozluk.write(f"{kelime}\n")

def sozlukten_sil(kelime):
    with open("./sozluk.txt","r") as sozluk:
        veri = sozluk.readlines()
        if f"{kelime}\n" in veri:
            veri.remove(f"{kelime}\n")
        else:
            print("kelime bulunamadi")
    with open("./sozluk.txt","w") as sozluk:
        sozluk.writelines(veri)

def sozlukten_cek():
    with open("./sozluk.txt","r") as sozluk:
        veri = sozluk.readlines()
        return random.choice(veri).strip("\n")

if __name__ == "__main__":
    pass
import sozluk

dar_agaci = ["▂▂▂▂▂",
             "▌   ",
             "▌   ",
             "▌ ",
             "▌   ",
             "▌  "]

adam =      ["",
            "|",
            "0",
             "( | )",
             "|",
             r"/ \ "]

def yanlis_hamle():
    global ciz, dar_agaci, adam
    ciz = [i for i in dar_agaci]
    hata = 1
    def adam_as():
        nonlocal hata
        ciz[hata] += adam[hata]
        hata += 1 if hata < 6 else 0
        return 1 if hata >= 6 else 0
    return adam_as 

while True:
    rastgele_kelime = sozluk.sozlukten_cek()
    kelime = ["_ " for _ in rastgele_kelime]    # kelimedeki harf sayısı kadar "_" koyuyo
    yanlis = yanlis_hamle() # yanlış sayacı
    tahminler = []  #adı üstünde tahminler işte

    while True:
        if tahminler:
            print("\nyanlis tahminlerin:    ",*tahminler)  

        for i in ciz:   # adamı çizer
            print(i)

        print("\n",*kelime)
        tahmin = input("\ntahmin: ")
        
        if len(tahmin) == 1 and tahmin in rastgele_kelime:   # eğer bir harf ve tahmin doğruysa 
            if rastgele_kelime.count(tahmin) == 1:   # kelimede o harften bir tane varsa
                kelime[rastgele_kelime.index(tahmin)] = tahmin.upper()

            elif rastgele_kelime.count(tahmin) > 1: # kelimede o harften birden fazla varsa
                for index, h in enumerate(rastgele_kelime):
                    if h == tahmin:
                        kelime[index] = tahmin.upper()

        if "_ " not in kelime or tahmin == rastgele_kelime :    #kazanma durumu
            print("".center(30,"-"))
            print(f"\n>> {rastgele_kelime.upper()}")
            print("helal, kazandin!")
            break

        elif tahmin not in rastgele_kelime: #yanlış tahmin
            print(f"{tahmin.upper()}, kelimede yok.")
            tahminler.append(tahmin.upper())
            
            if yanlis() == 1:   #kaybetme durumu
                print("".center(30,"-"))
                for i in ciz:
                    print(i)
                print("adam öldü a. kaybettin.")
                print(rastgele_kelime.upper())
                break
        print("".center(30,"-"))



    sorgu = input("\n\n(t)amam mi, (d)evam mi?  ")
    if sorgu == "t":
        print("allah'a emanetsin cano.")
        break
    elif sorgu == "d":
        continue
    else:
        print("anlamadim ne demeye calisiyon, ben gidiyom.\n")
        break
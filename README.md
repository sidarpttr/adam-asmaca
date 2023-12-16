# Adam Asmaca

Bu Python projesi, klasik bir "Adam Asmaca" oyununu içeriyor. Kullanıcının oluşturduğu sölükten rastgele seçilen kelimeleri tahmin etmekten ibaret.

## Nasıl Oynanır

- Her oyun başında rastgele bir kelime seçilir ve bu kelimenin harf sayısı kadar alt çizgi görüntülenir.
- Kullanıcı, harf tahminleri yapar ve yanlış tahminlerle oluşturulan "adamı" tamamlamadan doğru tahminlerle kelimeleri bulmaya çalışır.
- Her yanlış tahminle birlikte "adam" resmi oluşturulur. Eğer "adam" tamamlanırsa, oyun kaybedilir.
- Kelimeler **sozluk.txt** dosyasından rastgele çekilir. Bu dosyaya kelime ekleme ve silme yapılabilir.

## Dosyalar

- **sozluk.txt**: Oyunun kullanacağı kelime havuzunu içeren metin dosyasıdır. İstediğiniz kelimeleri ekleyebilir veya silebilirsiniz.

## Kullanım
1. Projeyi bilgisayarınıza klonlayın.
2. **sozluk.txt** dosyasına kendi kelimelerinizi ekleyebilir veya silebilirsiniz.
3. Oyunu başlatın
   ```bash
   python main.py

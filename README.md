# Python Core Mastery

Bu depo, Python'ı temelden başlayarak güvenilir yazılım geliştirme ve ileri mühendislik yargısına doğru öğrenmek için kullanılır.

## Öğrenme yaklaşımı

- Her aşamada önce kavramı açıkla, sonra örnek üzerinde tahmin yap, kodu çalıştır ve sonucu anlat.
- Bir yeterlilik kapısı tamamlanmadan yeni aşamaya geçme.
- Öğrenme alıştırmalarını küçük ve tek amaçlı tut.
- DreamAI ve agent sistemleri için gerekli web, veri, güvenlik ve sistem konularını Python temellerinden sonra sırayla ekle.

## Depo düzeni

- `src/`: Python öğrenme örnekleri. Mevcut `01_syntax_basics` içeriği korunur.
- `tests/`: İleride örnekler ve projeler için otomatik testler.
- `projects/`: Birden çok kavramı birleştiren, aşamalı projeler.
- `study-materials/`: Bu bilgisayarda tutulan HTML dersleri ve görsel notlar. `.gitignore` nedeniyle GitHub'a gönderilmez.

## Yerel çalışma

Python kurulumunu doğrulamak için terminalde:

```powershell
python --version
```

Bir Python dosyasını çalıştırmak için:

```powershell
python path\to\file.py
```

Komutları VS Code veya Cursor içindeki terminalde çalıştırabilirsin. Aynı anda tek bir editör kullanmak başlangıçta daha az dikkat dağıtır.

## Git'e gönderilecekler

Kaynak kod, testler, README ve yapılandırmalar Git'te tutulur. Yerel eğitim HTML'leri, SVG ders görselleri, sanal ortamlar, önbellekler ve sır içeren `.env` dosyaları dışarıda kalır. `.env.example` paylaşılabilir; içine gerçek anahtar veya parola koyma.

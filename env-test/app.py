import os

# "RENK" adındaki ortam değişkenini oku.
# Eğer dışarıdan bir renk verilmezse varsayılan olarak "Renksiz" olsun.
gelen_renk = os.getenv('RENK', 'Renksiz')
kullanici = os.getenv('KULLANICI', 'Misafir')

print(f"Merhaba {kullanici}!")
print(f"Benim şu anki rengim: {gelen_renk}")
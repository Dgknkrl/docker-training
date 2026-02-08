FROM python:3.9-alpine

# 1. Yeni bir grup ve kullanıcı oluştur (Şifresiz, sistem kullanıcısı)
# -S: System user (Sistem kullanıcısı)
# -G: Gruba ekle
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# 2. Çalışma klasörünü ayarla
WORKDIR /app

# 3. Dosyaları kopyala (Sahipliğini 'appuser'a vererek!)
# Eğer bunu yapmazsan dosyalar root'un olur, appuser okuyamaz/yazamaz.
COPY --chown=appuser:appgroup . .

# --- KRİTİK NOKTA ---
# 4. Root'tan çık, normal kullanıcıya geç
USER appuser

# 5. İspat için kim olduğumuzu yazdıralım
CMD ["whoami"]
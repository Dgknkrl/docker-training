# 1. Taban İmaj: Dünyanın en hafif web sunucusu (Alpine tabanlı Nginx)
FROM nginx:alpine

# 2. Etiketleme: Bu imajın sorumlusu kim? (Opsiyonel ama iyi pratik)
LABEL maintainer="kiralidogukan@gmail.com"

# 3. Kopyalama: Hazırladığımız HTML dosyasını, Nginx'in sunum klasörüne at
COPY index.html /usr/share/nginx/html/index.html

# 4. Bilgilendirme: Bu container 80 portunu kullanır (Dokümantasyon amaçlı)
EXPOSE 80

# 5. Başlat: Nginx'i ön planda çalıştır (Daemon off)
CMD ["nginx", "-g", "daemon off;"]
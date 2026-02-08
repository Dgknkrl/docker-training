# --- AŞAMA 1: Mutfak (Builder) ---
# Buraya "builder" takma adını veriyoruz
FROM golang:1.21 AS builder
WORKDIR /app
COPY . .
# Yemeği pişir (Derle)
RUN go build -o uygulamam main.go

# --- AŞAMA 2: Servis (Production) ---
# Tertemiz, küçücük bir işletim sistemi (Alpine)
FROM alpine:latest
WORKDIR /root/
# Sadece pişen yemeği (uygulamam dosyasını) 1. aşamadan kopyala
# Tencereleri (Go derleyicisi, kaynak kodlar) geride bırak
COPY --from=builder /app/uygulamam .

CMD ["./uygulamam"]
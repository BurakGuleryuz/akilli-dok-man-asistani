import os #klasör yollarını birleştirmek
import shutil #dosyayı diske kopyalamak
from fastapi import FastAPI,UploadFile,File,HTTPException #düzenli hata fırlatmak için
from schemas import SoruIstegi, DokumanKayit
app=FastAPI(title="Akıllı Doküman Asistanı API")

@app.get("/")
def ana_sayfa():
    return {"mesaj":"Sistem Aktif! başarıyla tammalandı."}

@app.get("/saglik-kontrolu")
def health_check():
    return {"durum":"OK","version":"1.0.0"}
 
@app.get("/hakkinda")
def hakkinda():   
    return {"mesaj":"Bu bir akıllı doküman asistanıdır.","yazar":"Burak Güleryüz"}

@app.post("/soru-sor")
def soru_sor(istek: SoruIstegi):
    # Gelen veri Pydantic süzgecinden geçtiyse buraya ulaşır
    cevap_tipi="Detaylı analiz" if istek.detayli_cevap  else "Kısa Özet"
    return{
            "Durum":"Başarılı",
            "hedef_doküman": istek.dokuman_id,
            "soru": istek.soru,
            "mod":cevap_tipi

          }
@app.post("/dokuman-ekle")
def dokuman_ekle(istek: DokumanKayit):
    
    return{
        "Durum":"Başarılı",
        "doküman başlığı": istek.baslik,
        "sayfa sayısı": istek.sayfa_sayisi
    }
KLASOR_YOLU = "yuklenen_dokumanlar"
@app.post("/dokuman-yukle", status_code=201)
def dokuman_yukle(dosya: UploadFile = File(...)):
    # Klasör yoksa oluştur    
# 1. Güvenlik Kontrolü: Dosya uzantısı .pdf mi?
    if not dosya.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Sadece PDF dosyaları yüklenebilir."
        )
    # 2. Klasör yoksa oluştur (Garanti adım)
    os.makedirs(KLASOR_YOLU, exist_ok=True)
    # 2. Dosyanın kaydedileceği tam yolu oluştur (örn: yuklenen_dokumanlar/sozlesme.pdf)
    kayit_yolu=os.path.join(KLASOR_YOLU, dosya.filename)

    # 3. Gelen dosyayı diskteki klasöre kaydet
    with open(kayit_yolu,"wb" ) as hedef_dosya:
        shutil.copyfileobj(dosya.file,hedef_dosya)
    return{
           "Durum":"Dosya başarıyla yüklendi",
           "dosya_adı": dosya.filename,
           "icerik_tipi": dosya.content_type,
           "kayit_yeri": kayit_yolu
      }





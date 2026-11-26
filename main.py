from fastapi import FastAPI
from schemas import SoruIstegi
from schemas import DokumanKayit
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



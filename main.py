from fastapi import FastAPI
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
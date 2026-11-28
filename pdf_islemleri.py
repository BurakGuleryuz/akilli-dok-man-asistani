from pypdf import PdfReader

def pdf_metin_cikar(dosya_yolu: str) -> str:
    """Verilen yoldaki PDF dosyasının tüm sayfalarındaki metni okur ve birleştirir."""
    okuyucu = PdfReader(dosya_yolu)
    tam_metin =""

    for sayfa_no,sayfa in enumerate(okuyucu.pages):
        sayfa_metni = sayfa.extract_text()
        if sayfa_metni:
            tam_metin += f"\n--- Sayfa {sayfa_no + 1} ---\n {sayfa_metni}" 

    return tam_metin.strip()
def metni_parcala(metin: str,parca_boyutu: int=500,cakisma: int=50 ) -> list[str]:

    """Uzun metni, anlam bütünlüğünü korumak için belirli bir çakışma payıyla parçalara böler."""   

    parcalar=[]
    baslangic=0
    metin_uzunlugu=len(metin)

    while baslangic < metin_uzunlugu:
        bitis=baslangic+ parca_boyutu
        parca=metin[baslangic:bitis]
        parcalar.append(parca)
        # Bir sonraki parça, önceki parçanın son 'cakisma' karakteri kadar gerisinden başlar
        baslangic+=parca_boyutu - cakisma
    return parcalar



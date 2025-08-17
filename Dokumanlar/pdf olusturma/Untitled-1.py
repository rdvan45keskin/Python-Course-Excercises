from fpdf import FPDF

class ImprovedCV(FPDF):
    def header(self):
        self.set_font('DejaVu', 'B', 16)  # Yeni yazı tipini kullan
        self.set_text_color(0, 0, 0)
        self.cell(0, 10, 'Rıdvan Keskin - Özgeçmiş', border=False, ln=True, align='C')
        self.ln(10)

# PDF oluştur
pdf = ImprovedCV()

# Yazı tipi ekleme (Bu kısım add_page'den önce olmalı)
pdf.add_font('DejaVu', '', 'C:/Users/Rıdvan Keskin/Documents/dersler/btk/python/Dokumanlar/pdf olusturma/dejavu-fonts-ttf-2.37/ttf/DejaVuSans.ttf', uni=True)
pdf.add_font('DejaVu', 'B', 'C:/Users/Rıdvan Keskin/Documents/dersler/btk/python/Dokumanlar/pdf olusturma/dejavu-fonts-ttf-2.37/ttf/DejaVuSans-Bold.ttf', uni=True)

pdf.add_page()

# Arka plan
pdf.set_fill_color(240, 240, 240)
pdf.rect(0, 0, 210, 297, style='F')  # A4 boyutu

# Profil Fotoğrafı
photo_path = "C:/Users/Rıdvan Keskin/Documents/dersler/btk/python/Dokumanlar/pdf olusturma/resim.jpg"
try:
    pdf.image(photo_path, x=10, y=20, w=40, h=50)
except Exception as e:
    print(f"Fotoğraf eklenemedi: {e}")

# Kişisel Bilgiler
pdf.set_xy(60, 20)
pdf.set_font('DejaVu', '', 12)
pdf.set_text_color(0, 0, 0)
pdf.multi_cell(0, 8, "Ad: Rıdvan Keskin\nLinkedIn: https://www.linkedin.com/in/rdvan45keskin/\nGitHub: https://www.github.com/rdvan45keskin/")

# Bölüm Ekleme Fonksiyonu
def add_section(title, content, y_position):
    pdf.set_y(y_position)
    pdf.set_fill_color(200, 200, 200)
    pdf.set_font('DejaVu', 'B', 12)
    pdf.cell(0, 10, title, ln=True, fill=True, border=0)

    pdf.set_font('DejaVu', '', 11)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(0, 8, content)

# İçerik Ekle
add_section("Eğitim", "- Mehmet Akif Ersoy Üniversitesi, Bilgi Sistemleri ve Teknolojileri, 3. Sınıf", 80)
add_section("Teknik Beceriler", "- İleri seviye Java\n- İleri seviye Flutter\n- Python, SQL, HTML, CSS", 110)
add_section("Projeler", "- Öğrenci Takip Sistemi (Flutter)\n- Alışveriş Sistemi (Java & Spring Boot)\n- YouTube ve Google Arama Arayüzü (PyQt5 ve Selenium)", 150)
add_section("İlgi Alanları", "- Yapay Zeka\n- Veri Analizi\n- Web Geliştirme", 190)

# PDF'i Kaydet
final_output_path = "C:/Users/Rıdvan Keskin/Documents/dersler/btk/python/Dokumanlar/pdf olusturma/Ridvan_Keskin_Improved_CV.pdf"
pdf.output(final_output_path)

print(f"CV başarıyla oluşturuldu: {final_output_path}")

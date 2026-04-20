from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
import socket
import requests

class IPYakalamaSistemi(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Başlık
        self.label_baslik = Label(
            text="SPYWARER93 IP TAKİP SİSTEMİ", 
            font_size='24sp', 
            size_hint_y=None, 
            height=50,
            color=(0, 1, 0, 1) # Yeşil (Hacker stili)
        )
        self.layout.add_widget(self.label_baslik)

        # Bilgi Ekranı
        self.scroll = ScrollView()
        self.label_info = Label(
            text="Sistem Hazır...\nButona basarak verileri çekebilirsiniz.", 
            halign='center', 
            valign='middle',
            size_hint_y=None
        )
        self.label_info.bind(texture_size=self.label_info.setter('size'))
        self.scroll.add_widget(self.label_info)
        self.layout.add_widget(self.scroll)

        # Yakalama Butonu
        self.btn = Button(
            text="IP VE AĞ VERİLERİNİ YAKALA",
            size_hint_y=None,
            height='50dp',
            background_color=(0, 0.5, 0, 1)
        )
        self.btn.bind(on_press=self.ip_yakala)
        self.layout.add_widget(self.btn)

        return self.layout

    def ip_yakala(self, instance):
        try:
            # 1. Yerel IP (Cihazın Ağdaki Adresi)
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            yerel_ip = s.getsockname()[0]
            s.close()

            # 2. Dış IP ve Detaylar (İnternetteki Görünür Adres)
            response = requests.get('https://ipapi.co/json/').json()
            dis_ip = response.get('ip', 'Bilinmiyor')
            sehir = response.get('city', 'Bilinmiyor')
            ulke = response.get('country_name', 'Bilinmiyor')
            isp = response.get('org', 'Bilinmiyor')

            sonuc = (
                f"--- SİSTEM VERİLERİ YAKALANDI ---\n\n"
                f"Cihaz Yerel IP: {yerel_ip}\n"
                f"İnternet Dış IP: {dis_ip}\n"
                f"Konum: {sehir} / {ulke}\n"
                f"Servis Sağlayıcı: {isp}\n"
                f"---------------------------------"
            )
            self.label_info.text = sonuc
            
        except Exception as e:
            self.label_info.text = f"Hata Oluştu: {str(e)}\nİnternet bağlantınızı kontrol edin."

if __name__ == "__main__":
    IPYakalamaSistemi().run()

# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import random
area = "pengecekan area melalui aplikasi dan website InterNetQ, pilih cek area"
daftar= "Pendaftaran melalui website atau aplikasi mobile, pilih paket dan daftar"
paket="tersedia paket internet 10 mb, 20 mb 50 mb"

pertanyaan = {
"apakah area saya tercover?": ["BOT: silahkan  {0}".format(area),
                                "BOT: anda bisa melakukan {0}".format(area),
                                "BOT: untuk area dapat di lakukan {0}".format(area)],
"bagaimana cara mendaftar INterNetQ?": ["BOT:silahkan lakukan {0}".format(daftar),
                                        "BOT:untuk berlangganan {0}".format(daftar)],
"Apa saja paket internet?": ["BOT:Terdapat beberapa pilihan {0}".format(paket),
                            "BOT:terdapat beberapa {0}!  ?".format(paket),
                            "BOT:untuk paket ada pilihan {0}!".format(paket)],
"": ["Apakah anda masih online?",
    "Apakah sudah cukup jelas?"],
"default": ["Saya CS bot InterNetQ, ada yang bisa di bantu?"] 
}


def balas(jawaban):
    if jawaban in pertanyaan:
     jawaban_bot = random.choice(pertanyaan[jawaban])
    else:
     jawaban_bot = random.choice(pertanyaan["default"])
    return jawaban_bot

def cek(teks_pertanyaan):
 if "area" in teks_pertanyaan:
  klien_tanya = "apakah area saya tercover?"
 elif "daftar" in teks_pertanyaan:
  klien_tanya = "bagaimana cara mendaftar INterNetQ?"
 elif "paket" in teks_pertanyaan:
  klien_tanya = "Apa saja paket internet?"
 else:
  klien_tanya = ""
 return klien_tanya

def kirim_balasan(jawaban):
 print((jawaban))
 balasan = balas(jawaban)
 print((balasan))

print("Selamat datang di Layanan chatbot InterNetQ")
print("Silahkan ajukan pertanyaan terkait layanan area, pendaftaran, paket internet")
print("BOT: Siapa nama anda?")
user_name = input()
print(f"BOT: Halo {user_name }. Saya CS bot InterNetQ, ada yang bisa di bantu?\n1. Area\n2. Daftar\n3. Paket")

while 1:
   input_pertanyaan = input()
   cek_teks = cek(input_pertanyaan.lower())
   kirim_balasan(cek_teks)
   if input_pertanyaan == "exit" or input_pertanyaan == "stop" or input_pertanyaan == "sudah":
       print("sampai jumpa saya akhiri terimakasih")
       break
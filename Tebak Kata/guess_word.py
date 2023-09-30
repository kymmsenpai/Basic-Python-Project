import random

border = '-----------------------------------------------------'
judul = ''' _____    _           _      _   __      _        
|_   _|  | |         | |    | | / /     | |       
  | | ___| |__   __ _| | __ | |/ /  __ _| |_ __ _ 
  | |/ _ \ '_ \ / _` | |/ / |    \ / _` | __/ _` |
  | |  __/ |_) | (_| |   <  | |\  \ (_| | || (_| |
  \_/\___|_.__/ \__,_|_|\_\ \_| \_/\__,_|\__\__,_|
'''
nyawa = 9

def play():
		print(border)
		print(judul)

		# menanyakan user apakah mau main lagi atau tidak
		def restrat():
				print(border)
				jawaban = input('mau main lagi? (y/n) : ')
				if jawaban.lower() == 'y':
					global nyawa
					nyawa = 9
					return main_lagi()
				else:
					print(border)
					print('Terimakasih')
					print(border)
					exit()
		
		def main_lagi():
			katakata = ['mutlak',
									'benar',
									'terserap',
									'menonjolkan',
									'aktivis',
									'sebenarnya',
									'aktualitas',
									'remaja',
									'mempengaruhi',
									'terpengaruh',
									'udara',
									'waspada',
									'sepanjangwaktu',
									'mengalegorisasikan',
									'persekutuan',
									'aliansi',
									'kiasan',
									'sindiran',
									'baik',
									'samasekali',
									'memperkuat',
									'analisis',
									'semu',
									'tampaknya',
									'penampilan',
									'menangkap',
									'menilai',
									'penilaian',
									'anggapan',
									'astronomis',
									'sikap',
									'rata-rata',
									'sadar',
									'kesadaran',
									'bayi',
									'padadasarnya',
									'tongkat',
									'kepercayaan',
									'keyakinan',
									'besar',
									'darah',
									'berbasisluas',
									'tanpahenti',
									'pusat',
									'bersertifikat',
									'nyanyian',
									'klaim',
									'rahasia',
									'memikirkan',
									'tanggungjawab',
									'komentar',
									'komentator',
									'lengkap',
									'samasekali',
									'memahami',
									'terpadu',
									'curhat',
									'dugaan',
									'hatinurani',
									'kesadaran',
									'besar',
									'sangat']

			# mengambil perhuruf dari kata yang diambil secara acak
			kata = random.choice(katakata)
			kumpulan_huruf = []
			tebak = []
			for perkumpulan_huruf in kata:
					kumpulan_huruf.append(perkumpulan_huruf)
			# memberikan output tanda tanya untuk ditebak oleh user
			for rahasia in range(len(kumpulan_huruf)):
					tebak.append('?')

			# memasukkan input tebakan user berupa kumpulan_huruf
			def masukan():
					print(border)
					user = input('masukan huruf : ')
					main(user.lower())

			# mencocokan inputan user dengan kata yang telah ditentukan
			def main(input_pemain):
					global nyawa 
					# jika pemain benar menebak maka program akan mengganti tanda tanya dengan huruf yang dimasukkan user
					if input_pemain in kumpulan_huruf:
							for i in range(len(kumpulan_huruf)):
									if kumpulan_huruf[i] == input_pemain:
											tebak.pop(i)
											tebak.insert(i,input_pemain)
							print(''.join(tebak))
							if tebak == kumpulan_huruf:
									print(border)
									print('Kamu menang!!')
									return restrat()
							else:
									return masukan()
					# jika pemain salah menebak maka nyawa akan dikurangi satu 
					else:
							nyawa -= 1
							print(f'Nyawa Anda tinggal {nyawa}')
							if nyawa != 0:
									return masukan()
							else:
									print(border)
									print('Kamu kalah')
									print(f'kata yang sebenarnya adalah : {"".join(kumpulan_huruf)}')
									return restrat()
			
			# meminta input user pertama kali
			masukan()
		
		main_lagi()

if __name__ == '__main__':
	play()


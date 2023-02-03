print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("                                                                   Quizz Games!!!")
print("\n")
print("\n")
print("                                          helooo!, selamat datang di quizz game yang saya buat")
print("                                                                       enjoy!")
print("\n")
print("\n")

#disini tempat untuk melabeli nama dari jawaban tersebut 
#jika ingin memasukan kolom jawaban, maka ketik input lalu masukan pertanyaan

nama = input("Siapa nama anda? ")
if nama=="Admin":
	print("Identified user = 0")
elif nama == "Bima":
     print(f"Hemlooooooooooooo {nama}")
#kamu bisa memanggil jawaban yang telah kamu labeli, dengan cara ketik f sebelum kutip dan menggunakan {}
#dan menulis nama label di dalam {}
elif nama == "dian":
    print("halo diannn!, selamat mencoba yaa!")
else:
	 print(f"Haloo {nama}, semoga beruntung dalam mengerjakan quizz ini!")
#disini if memiliki arti (jika jawabannya merupakan yang ditulis, maka munculkan sesuai yang ditulis)
#elif merupakan sama seperti if, namun if hanya bisa digunakan sekali, maka selanjutnya menggunakan elif
#else memiliki arti jika jawabannya tidak ada yang sesuai di if dan elif, maka munculkan yang sudah ditulis di command else
print("\n")
print("\n")
print("\n")
score = 0
print("                                                  Quiz!")
print("\n")
print("\n")
print("Quiz: Apa nama ibukota dari perancis?")
answer = input("masukan jawabanmu: ")

if answer.lower() == "paris":
    print("Benar! Ibukota dari perancis adalah paris.")
    score += 1
#fungsi .lower() untuk mengubah jawabanmu menjadi huruf kecil semua, karena biasanya jawabannya sama
#tetapi dianggap salah karena tidak sesuai dengan jawaban di command
else:
    print("Salah. Jawabannya adalah paris.")
    score -= 0
print("\n")
print("\n")
print("\n")

print("Patung Sphinx kebanyakan terdapat di negara")
answer = input("masukan jawabanmu: ")

if answer.lower() == "mesir":
    print("Benar! Patung sphinx terletak di daerah mesir.")
    score += 1
else:
    print("Salah. Jawabannya adalah mesir.")
    score -= 0
print("\n")
print("\n")
print("\n")
print("Orang yang bertugas membuat peta disebut sebagai…")
answer = input("masukan jawabanmu: ")

if answer.lower() == "kartografer":
    print("Benar! Orang yang membuat peta disebut kartografer.")
    print(f"Wah! jago juga kamu {nama}")
    score += 1

else:
    print("Salah. kartografer.")
    score -= 0
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("Your score:", score, "out of 10")
print(f"keren juga lo {nama}")
print("\n")
print("\n")






print(".__________________________.")
print("|                          |")
print("|Welcome to the Quest Game!|")
print("|        made by :         |")
print("|         myself           |")
print("|                          |")
print("|__________________________|")
print("                            ")
print("                            ")
print("                            ")
print("                            ")
print("Selamat datang di quest game ini, semoga enjoy!! ")
print("                            ")
print("                            ")
print("                            ")
print("                            ")


nama = input("Siapa nama anda? ")
if nama=="Admin":
	print("Identified user = 0")
elif nama == "Bima":
     print(f"Hemlooooooooooooo {nama}")
else:
	 print(f"haloo!{nama}, goodluck dalam mengerjakan game ini ")
print("\n")
print("\n")
print("\n")


# print(f"Terima kasih {nama}")
# Set the initial location
print(f"Selamat datang wahai seorang bijak bernama {nama}")
print("Pada suatu hari kamu sedang mengembara, namun karena kamu salah membaca peta, kamu tersesat ke arah hutan \n kamu mulai sadar kamu salah membaca peta saat kamu sudah berada di dalam hutan yang luas")
print("lalu kamu terhenti sebentar, dan berfikir")
print("\n")
print("\n")
print("\n")
location = "forest"

# Set the initial inventory
inventory = []

while True:
    # Give the player information about their current location

    if location == "forest":
        print("kamu berada di hutan yang dalam. lalu kamu melihat sepetak jalan ke arah kiri dan kanan.")
        print("Dan didalam tasmu, terdapat:", inventory)
        choice = input(f"jalan mana yang akan kamu pilih {nama}? (kiri/kanan) ")
        if choice == "kiri":
            location = "cave"
        elif choice == "kanan":
            location = "river"
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
    elif location == "cave":
        print("saat kamu menelusuri jalan di bagian kanan, kamu menemukan gua dan langsung memasukinya")
        print("kamu mengecek kembali tas mu, di dalam tas mu, terdapat:", inventory)
        print("saat kamu menjelajahi goa tersebut, kamu menemukan senter tergeletak")
        print("\n")
        choice = input("apa kamu ingin mengambil senter itu? (ya/tidak) ")
        if choice == "ya":
            inventory.append("flashlight")

        elif choice == "tidak":
            print("You continue on without the flashlight.")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
         

    elif location == "river":
        print ("saat menyusuri jalan ini, kamu menemukan sebuah sungai. Namun airnya terlalu dalam untuk kamu berenang, \n sehingga kamu perlu mencari perahu kecil.")
        print("\n")
        print("malam hari pun tiba, kamu masih mecari perahu, kamu membutuhkan senter agar dapat terus mencari")
        print("kmu melihat ke dalam tasmu, didalamnya terdapat:", inventory)
        print("lalu kamu tidak sengaja menemukan senter di dekat sungai")
        choice = input("apakah kamu akan mengambilnya? (ya/tidak) ")
        if choice == "ya":
            inventory.append("flashlight")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
        elif choice == "tidak":
            print("You continue on without the flashlight.")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
        if "flashlight" in inventory:
            print("kamu menemukan kapal saat sedang mencari.")
            inventory.append("boat")
        choice = input("apakah kamu ingin menyebrangi sungai ini? (ya/tidak) ")
        if choice == "ya":
            if "boat" in inventory:
                print("Selamat! ternyata di daerah seberang ini merupakan tujuan awalmu.")
                location = "other_side"
                break
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
        elif choice == "no":
            print("You decide to go back the way you came.")
            location = "forest"

        else:
            print("Without a boat, you are unable to cross the river.")
        
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")

print("Congratulations, you have completed the quest!")
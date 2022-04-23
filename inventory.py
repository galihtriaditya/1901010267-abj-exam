while True:
    lanjut=input("Input data inventory baru (Ya/Tidak)?")
    if lanjut == "ya" or lanjut == "Ya":
        file = open ("db-inventory.txt", "a")
        print("*"*45)
        x = input("Nama Perangkat : ")
        y = input("Lokasi : ")
        print("-"*45)
        file.write("Nama perangkat : "+x+", Lokasi : "+y+"\n")
        file.close()
    elif lanjut == "tidak" or lanjut == "Tidak":
        file = open ("db-inventory.txt", "r")
        print("*"*45)
        for perangkat in file:
            perangkat = perangkat.strip()
            print(perangkat)
        break

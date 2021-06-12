import time

print("Silahkan Masukkan Kartu ")

time.sleep(1)
sandi = 1234

pin=(input("Masukkan Pin anda "))

balance=200000

if sandi==sandi:
    while True:

        print("""MENU PENARIKAN CEPAT
            1==saldo
            2==tarik saldo
            3==setoran kredit
            4==exit
            """
            )
        
        try:
             option = int(input("Silahkan Pilih Menu "))
        except:
            print("Silahkan Masukkan Menu yang benar ")

        if option==1:
             print(f"Saldo anda saat ini adalah {balance} ")

        elif option==2:
            withdraw_amount=int(input("Silahkan masukkan jumlah penarikan "))
            balance = balance - withdraw_amount

            print(f"{withdraw_amount} adalah debit dari akun anda ")
            print(f"Saldo anda saat ini adalah {balance}" )

        elif option==3:
            deposit_amount = int(input("Silahkan masukkan jumlah setoran "))
            balance = balance + deposit_amount

            print(f"{deposit_amount} adalah kredit di akun anda ")
            print(f"Saldo anda saat ini adalah {balance} ")
            
        elif option==4:
            break

else:
    print("Pin anda salah, harap coba lagi")
    
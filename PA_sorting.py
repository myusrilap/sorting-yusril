import random, os, time

list_kosong = []
for i in range(10):
    list_kosong.append(random.randint(1, 100))

def menu():
    print("Angka acak:", list_kosong)
    print("")
    print('''Program sorting Arjulio
1. shell sort
2. quick sort
3. Acak angka
4. Keluar''')
    while True:
            a1 = (input("input pilihan sort apa yang ingin dilakukan(1/2/3): "))
            if a1 =="1":
                shell()
            elif a1 == "2":
                quick()
            elif a1 == "3":
                os.system('cls')
                list_kosong.clear()
                for i in range(10):
                    list_kosong.append(random.randint(1, 100))
                menu()
            elif a1 == "4":
                print("Terima kasih")
                break
            else:
                print("Inputan salah, mohon input ulang pilihan anda")
                time.sleep(2)
                os.system('cls')
                menu()
    
def shell():
    def shell(list_kosong):
        n = len (list_kosong)
        gap = n // 2

        while gap > 0:
            for i in range (gap, n):
                temp = list_kosong[i]
                j=i
                while j >= gap and list_kosong [j-gap] > temp:
                    list_kosong[j] = list_kosong[j-gap]
                    j -= gap

                list_kosong [j] = temp
            gap //= 2
        return list_kosong
    print("")
    print ("Sesudah di sort:", shell(list_kosong))

def quick():
    def quick(list_kosong):
        if len(list_kosong) <= 1:
            return list_kosong
        else:
            pivot = list_kosong[0]
            left = [x for x in list_kosong[1:] if x <= pivot]
            right = [x for x in list_kosong[1:] if x > pivot]
            return quick(left) + [pivot] + quick(right)
    result = quick(list_kosong)
    print("")
    print(f"sesudah di sort {result}")

menu()


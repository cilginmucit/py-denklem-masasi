import os

def coz(denklem: str):
    step1p1,step1p2 =  denklem.split(" = ")
    step2p1,step2p2 =  step1p1.split(" "),step1p2.split(" ")
    
    def step2p2master(n:list)-> list:
        i= 0

        while set(["*","/"]) & set(n) or len(n) <=i:
            if not set(["*","/"]) & set(n):
                break
            if len(n) <= i:
                i= 0
            
            if n[i] == "*" :
                n[i] = str(float(n[i-1]) * float(n[i+1]))
                n.pop(i+1)
                n.pop(i-1)
            elif  n[i] == "/" :
                n[i] = str(float(n[i-1]) / float(n[i+1]))
                n.pop(i+1)
                n.pop(i-1)

            i = i+1

        i= 0

        while set(["+","-"]) & set(n) or len(n) <=i:
            if not set(["+","-"]) & set(n):
                break
            if len(n) <= i:
                i= 0
            
            if n[i] == "-" :
                n[i] = str(float(n[i-1]) - float(n[i+1]))
                n.pop(i+1)
                n.pop(i-1)
            elif n[i] == "+" :
                n[i] = str(float(n[i-1]) + float(n[i+1]))
                n.pop(i+1)
                n.pop(i-1)
            i = i+1

        i= 0
        return n
    
    def step2p1master(n:list)-> list:
        i=1
        while set(["(",")"]) & set(n):
            
            if n[-i] == "(":

                x = i
                while True:
                    if n[-x] == ")":
                        break
                    x = x - 1 


                n[-i :-x+1] = step2p2master(n[-i +1:-x])

                i=1

            i = i+1
        return step2p2master(n)

    return float(step2p1master(step2p1)[0])

def x():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''Bu proje Bartu Ustaoğlu tarafından yapılmıştır.
İşlemler Toplama çıkartma bölme ve çarpma (bide parantez) ile sınırlıdır.
Herhangi bir işlem işaretinden önce ve sonra boşluk bırakılmalı(parantez dahil) 
not: Eğer işlemle başlayacaksanız işlemden önce Boşluğa gerek yoktur.(Mesela aşağıdaki örnekte olduğu gibi ilk "parantezden" önce bir boşluk yok.)
örnek doğru kulanım:( 1 + 1 ) * ( 1 - 8 ) / 3 

''')

if __name__ == "__main__":
    while True:
        denklem = ""
        x()
        while True:
            denklem = input("Denklem giriniz: \n\t")
    
            if not denklem == "":
                break
            else:
                x()
    
    
        x()
    
        try: 
            print("Denklem giriniz:\n\t",denklem," = ","{:g}".format(coz(denklem + " = ")),sep="")
            
        except: 
            print("Ya boşluk bırakmayı unuttunuz ya fazla boşluk bıraktınız ya da verdiyiniz denklem zazla karışıktı\n ")
        finally:
            input("\nDevam etmek için herhangi bir tuşa basın...")

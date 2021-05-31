import tkinter as tk
from tkinter import messagebox 
from tkinter import StringVar
from tkinter import *


window = tk.Tk()

class keluar:
    def keluar():
        
        
        exit(0)




def book():
    step = 1
    if len(stringnama.get()) == 0:
        messagebox.showerror("Error!!!","BELUM MENGISI NAMA ANDA")
        step = 0
    if len(stringalamat.get()) == 0:
        messagebox.showerror("Error!!!","BELUM MENGISI ALAMAT ANDA")
        step = 0
    if len(stringpekerjaan.get()) == 0:
        messagebox.showerror("Error!!!","BELUM MENGISI PEKERJAAN ANDA")
        step = 0
    if len(stringnomortelepon.get()) == 0:
        messagebox.showerror("Error!!!","BELUM MENGISI NOMOR TELEPON ANDA")
        step = 0
    if tujuan.get() == 0:
        messagebox.showerror("Eror!!!","BELUM MEMILIH JENIS MOBIL")
    if verifikasi.get() == 0:
        messagebox.showerror("EROR!!!","PASTIKAN TERLEBIH DAHULU SEBELUM MEMBELI")
    else:
        while step == 1:
            if tujuan.get()==1:
                harga="450.000.000"
                jenis="FORTUNER"
                
            elif tujuan.get()==2:
                harga="300.000.000"
                jenis="INNOVA"
                
            elif tujuan.get()==3:
                harga="180.000.000"
                jenis="AVANZA "
              
            elif tujuan.get()==4:
                harga="130.000.000"  
                jenis="AGYA "

            elif tujuan.get()==5:
                harga="200.000.000"  
                jenis="RUSH"
            
            elif tujuan.get()==6:
                harga="120.000.000"  
                jenis="CAYLA"
           
            elif tujuan.get()==7:
                harga="190.000.000"
                jenis="TERIOS"
                
            elif tujuan.get()==8:
                harga="165.000.000"
                jenis="XENIA "
              
            elif tujuan.get()==9:
                harga="140.000.000"  
                jenis="AYLA "

            elif tujuan.get()==10:
                harga="205.000.000"  
                jenis="SIRION"
           
            elif tujuan.get()==11:
                harga="150.000.000"  
                jenis="SIGRA"
           
            elif tujuan.get()==12:
                harga="240.000.000"  
                jenis="LUXIO"
               
            hasil =  "Terima kasih " + stringnama.get() + " telah membeli mobil " + jenis + " dengan harga Rp" + harga +  " Jangan lupa membayar pajak " 
            messagebox.showinfo("SHOWROOM PEMBELIAN MOBIL BEKAS DAIYOT", hasil)
            step =0



#Tampilan  
window.title("SHOWROOM PEMBELIAN MOBIL BEKAS DAIYOT ")
window.geometry("1500x700")
window.configure(bg="#5A6868")



#label
label1 = tk.Label(bg="blue", text ="SHOWROOM PEMBELIAN MOBIL BEKAS DAIYOT").place(x=150, y=10)
label2 = tk.Label(bg="red", text ="Pilih Mobil Yang Ingin Anda Beli\t:").place(x=10, y=170)
label3 = tk.Label(text = "nama").place(x=45, y=50)
label4 = tk.Label(text = "alamat").place(x=45, y=80)
label5 = tk.Label(text = "pekerjaan").place(x=45, y=110)
label6 = tk.Label(text = "nomor telepon").place(x=45, y=140)

#JENIS
tujuan  = IntVar()
button1 = Checkbutton(window, bg="#F04A3A", text="FORTUNER ", variable=tujuan, onvalue=1, offvalue=0).place(x=10, y=200)
button2 = Checkbutton(window, bg="#F05A3A", text="INNOVA ", variable=tujuan, onvalue=2, offvalue=0).place(x=10, y=220)  
button3 = Checkbutton(window, bg="#F05A3A", text="AVANZA ", variable=tujuan, onvalue=3, offvalue=0).place(x=10, y=240)  
button4 = Checkbutton(window, bg="#F05A3A", text="AGYA ", variable=tujuan, onvalue=4, offvalue=0).place(x=10, y=260)  
button5 = Checkbutton(window, bg="#F05A3A", text="RUSH ", variable=tujuan, onvalue=5, offvalue=0).place(x=10, y=280) 
button6 = Checkbutton(window, bg="#F05A3A", text="CAYLA", variable=tujuan, onvalue=6, offvalue=0).place(x=10, y=300) 
button7 = Checkbutton(window, bg="#F05A3A", text="TERIOS ", variable=tujuan, onvalue=7, offvalue=0).place(x=410, y=200)  
button8 = Checkbutton(window, bg="#F05A3A", text="XENIA ", variable=tujuan, onvalue=8, offvalue=0).place(x=410, y=220)  
button9 = Checkbutton(window, bg="#F05A3A", text="AYLA ", variable=tujuan, onvalue=9, offvalue=0).place(x=410, y=240)  
button10 = Checkbutton(window, bg="#F05A3A", text="SIRION ", variable=tujuan, onvalue=10, offvalue=0).place(x=410, y=260)  
button11 = Checkbutton(window, bg="#F05A3A", text="SIGRA ", variable=tujuan, onvalue=11, offvalue=0).place(x=410, y=280) 
button12 = Checkbutton(window, bg="#F05A3A", text="LUXIO", variable=tujuan, onvalue=12, offvalue=0).place(x=410, y=300) 

#VERIF
verifikasi = IntVar()
button1 = Checkbutton(window, bg="#F04A3A", text="Verifikasi", variable=verifikasi, onvalue=1, offvalue=0).place(x=10, y=380)


    

#NAMA 
stringnama = StringVar()
NAMA = Entry(width = 20, textvariable=stringnama).place(x = 250, y = 50) 

#ALAMAT
stringalamat = StringVar()
ALAMAT = Entry(width = 20, textvariable=stringalamat).place(x = 250, y = 80)

#PEKERJAAN
stringpekerjaan= StringVar()
PEKERJAAN = Entry(width = 20, textvariable=stringpekerjaan).place(x = 250, y = 110)

#NOMOR TELEPON
stringnomortelepon = StringVar()
NOMORTELEPON = Entry(width = 20, textvariable=stringnomortelepon).place(x = 250, y = 140)

#BUTTON
button1 = Button(window, bg="yellow", command = book, text="PESAN").place(x=100,y=450)
exitbutton = Button(window, bg="yellow", command = exit, text="KELUAR").place(x=200,y=450)



window.mainloop()

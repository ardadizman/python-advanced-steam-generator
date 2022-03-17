import random
import time
import os
import sys
import subprocess
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from tkinter import messagebox

while True:
    premiumaccount = 0

    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')


    nickfile = open("dtbsnick.dbf", "r")
    list_of_nicks = []
    for linenick in nickfile:
        stripped_line1 = linenick.strip()
        line_list1 = stripped_line1.split()
        list_of_nicks.append(line_list1)

    nickfile.close()

    keysfile = open("dtbsgen.dbf", "r")
    list_of_lists = []
    for line in keysfile:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists.append(line_list)

    keysfile.close()


    def non_premium():
        while 1:
            print(random.choice(list_of_lists))
            time.sleep(5)


    def premium():
        while 1:
            print(random.choice(list_of_lists))
            time.sleep(1)


    def startgen():
        cls()
        print('Premium Key Satın Almak İçin "1" Tuşlayınız.')
        premiumkey = input('Premium Key: ')
        if premiumkey == 'f4k1rs4v4r':
            print("Premium Key Girişi Başarılı!")
            time.sleep(1.5)
            cls()
            premium()
        elif premiumkey == '1':
            print("Premium Key = 2TL")
            time.sleep(0.3)
            print("Discord Üzerinden Satın Alınabilir.")
            time.sleep(3)
            cls()
            non_premium()
        else:
            print("Premium Key Yanlış!")
            time.sleep(1.5)
            cls()
            non_premium()


    def startnickgen():
        # noinspection PyGlobalUndefined
        global otodinleme
        global premiumaccount
        cls()
        premiumkey = input('Premium Key: ')
        if premiumkey == 'f4k1rs4v4r':
            print("Premium Key Girişi Başarılı!")
            premiumaccount = 1
            time.sleep(1.5)
            cls()
            seslidinleme = input("Otomatik Nicknameleri Dinlemek İster Misiniz ? (y/n)")
            if seslidinleme == 'y':
                print("Otomatik Dinleme Sistemi Açıldı!")
                otodinleme = 1
            elif seslidinleme == 'n':
                print("Otomatik Dinleme Sistemi Kapatıldı!")
                otodinleme = 0
            else:
                print("Incorrect Input, Try Again.")
                otodinleme = 0
            cls()
        else:
            print("Premium Key Yanlış!")
            premiumaccount = 0
            time.sleep(1.5)
            cls()
        while 1:
            if premiumaccount == 0:
                print(random.choice(list_of_nicks))
                time.sleep(3)
            elif premiumaccount == 1:
                if otodinleme == 0:
                    print(random.choice(list_of_nicks))
                    time.sleep(0.5)
                elif otodinleme == 1:
                    outputtext = (str(random.choice(list_of_nicks)))
                    print(outputtext)
                    time.sleep(0.75)


    def creditspage():
        cls()
        print('Program Developer: Arda Dizman \nProgram Version: Alpha v1.0 \n\nIt is legal because the program randomly generates these steam codes. \n\n\n\nAll licenses and rights of our program have been taken.\n\n\nAll of the income from premium purchases will either be returned to you as a gift or donated for your information.')
        time.sleep(5)
        cls()


    def mainguiapp():
        cls()
        print('Şuanlık PBE Test Kapalıdır.')

        root = tk.Tk()

        canvas = tk.Canvas(root, width=800, height=200)
        canvas.grid(columnspan=3, rowspan=3)

        #logo
        logo = Image.open('steamlogo.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(image=logo)
        logo_label.image = logo
        logo_label.grid(column=1, row=0)

        #instructions
        instructions = tk.Label(root,  text="Kapalı Herkese Açık Beta Test Alanı!", font=" Haleway 14")
        instructions.grid(columnspan=3, column=0, row=5)

        def  open_File():
            browse_text.set("loading...")
            file = askopenfile(parent=root, mode='rb', title='Choose a file', filetype=[("Dbf file", "*.dbf")])
            if file:
                print("PBE Kapalıdır! Sürümünüzü Kontrol Ediniz!")
                messagebox.showinfo("PBE Test", "Şuanlık PBE Test Kapalıdır.")
                browse_text.set("Browse  ")
            else:
                browse_text.set("Browse")


        #browse button
        browse_text = tk.StringVar()
        browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_File(), font="Haleway", bg="#28bebe", fg="white", height=2, width=15)
        browse_text.set("Browse")
        browse_btn.grid(column=1, row=3)
        canvas = tk.Canvas(root, width=800, height=150)
        canvas.grid(columnspan=3)

        root.title('PBE App')

        root.mainloop()
    def start():
        cls()
        print('1: Steam Random Key Generator')
        print('2: Steam Nickname Generator')
        print('3: Credits')
        print('4: PBE App')
        choice = int(input("Your choice (1/2/3): "))
        if choice == 1:
            startgen()
        elif choice == 2:
            startnickgen()
        elif choice == 3:
            creditspage()
        elif choice == 4:
            mainguiapp()
        else:
            print('Incorrect Input, Try Again.')
            time.sleep(1)
            cls()
            subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])


    while 1:
        start()

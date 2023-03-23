import os
import tkinter as tk

WIDTH = 200
HEIGHT = 100
root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

def ZPPR3033_ASM():
    ZPPR3033_ASM = os.system('start sapshcut.exe -guiparm="165.244.245.200 00" -user=c002102 -pw=whflq11+ -system=R3P -language=KO -client=100 \
                        -command="*zppr3033 P_WERKS=3204; S_DISPO-LOW=CN*; S_PROCD-LOW=ASM; S_SPMON-LOW=2023.01"')
    ZPPR3033_ASM.pack()

def ZPPR3033_INJ():
    ZPPR3033_INJ = os.system('start sapshcut.exe -guiparm="165.244.245.200 00" -user=c002102 -pw=whflq11+ -system=R3P -language=KO -client=100 \
                        -command="*zppr3033 P_WERKS=3204; S_DISPO-LOW=CN*; S_PROCD-LOW=INJ; S_SPMON-LOW=2023.01"')
    ZPPR3033_INJ.pack()

def ZPPR3033_PRE():
    ZPPR3033_PRE = os.system('start sapshcut.exe -guiparm="165.244.245.200 00" -user=c002102 -pw=whflq11+ -system=R3P -language=KO -client=100 \
                        -command="*zppr3033 P_WERKS=3204; S_DISPO-LOW=CN*; S_PROCD-LOW=PRE; S_SPMON-LOW=2023.01"')
    ZPPR3033_PRE.pack()

def ZPPR3033_INM():
    ZPPR3033_INM = os.system('start sapshcut.exe -guiparm="165.244.245.200 00" -user=c002102 -pw=whflq11+ -system=R3P -language=KO -client=100 \
                        -command="*zppr3033 P_WERKS=3204; S_DISPO-LOW=CN*; S_PROCD-LOW=INM; S_SPMON-LOW=2023.01"')
    ZPPR3033_INM.pack()

button1 = tk.Button(root, text="생산실적_조립", command=ZPPR3033_ASM)
button1.pack()

button2 = tk.Button(root, text="생산실적_코킹", command=ZPPR3033_INJ)
button2.pack()

button3 = tk.Button(root, text="생산실적_프레스", command=ZPPR3033_PRE)
button3.pack()

button4 = tk.Button(root, text="생산실적_사출", command=ZPPR3033_INM)
button4.pack()

root.mainloop()
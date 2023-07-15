minute = ["Ein","Zwei","Drei","Vier","Funf","Sechs","Sieben","Acht","Neun","Zehn","Elf","Zwolf","Dreizehn","Vierzehn","Funfzehn","Sechzehn","Siebzehn","Achtzehn","Neunzehn","Zwanzig","Ein und Zwanzig","Zwei und Zwanzig","Drei und Zwanzig","Vier und Zwanzig","Funf und Zwanzig","Sechs und Zwanzig","Sieben und Zwanzig","Acht und Zwanzig","Neun und Zwanzig","Dreizig","Ein und Dreizig","Zwei und Dreizig","Drei und Dreizig","Vier und Dreizig","Funf und Dreizig","Sechs und Dreizig","Sieben und Dreizig","Acht und Dreizig","Neun und Dreizig","Vierzig","Ein und Vierzig","Zwei und Vierzig","Drei und Vierzig","Vier und Vierzig","Funf und Vierzig","Sechs und Vierzig","Sieben und Vierzig","Acht und Vierzig","Neun und Vierzig","Funfzig","Ein und Funzig","Zwei und Funzig","Drei und Funzig","Vier und Funzig","Funf und Funzig","Sechs und Funzig","Sieben und Funzig","Acht und Funzig","Neun und Funzig","Sechzig"]
hour = ["Ein","Zwei","Drei","Vier","Funf","Sechs","Sieben","Acht","Neun","Zehn","Elf","Zwolf","Eins"]
time = input("What's the time : ")
AM_PM = input("AM or PM? ")
daynighttime = ""

hours = int(time.split(":")[0])
minutes = int(time.split(":")[1])

if AM_PM == "AM":
    daynighttime = " in dem Morgen"
else:
    daynighttime = " in dem Nacht"


if minutes == 0:
    print(hour[hours-1]+" Uhr"+daynighttime)
if minutes == 15:
    print("Viertel nach "+hour[hours-1]+daynighttime)
if minutes == 30:
    print("Halb "+ hour[hours]+daynighttime)
if minutes == 45:
    print("Viertel vor "+hour[hours]+daynighttime)

if minutes > 0 and minutes < 30 and minutes != 15:
    print(minute[minutes-1], "Minuten nach", hour[hours-1] + daynighttime)

if minutes <= 59 and minutes > 30 and minutes != 45:
    print(minute[(60-minutes)-1], "Minuten vor", hour[hours] + daynighttime)
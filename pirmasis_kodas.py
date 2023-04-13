## Uzduotis: Nustatyti pilnametyste arba lyti
print()
vardas = input("Iveskite savo varda: ")
amzius = input("Iveskite savo amziu:")
amzius = int(amzius)
vardas = vardas.upper()
choice = input("pasirinkite ar norite suzinoti lyti (L) ar amziaus statusa (A)")
vardo_galas = vardas[-1]


if choice == "A" and amzius < 18:
    bus_pilnametis = 18 - amzius
    print(f"{vardas} yra nepilanmetis.\nPilnamtystes sulauks uz {bus_pilnametis} metu") 
elif choice == "A" and amzius >= 18 and amzius <= 65:
    bus_pensijoje = 65 - amzius
    print(f"{vardas} yra pilanmetis\npensijoje bus uz {bus_pensijoje} metu")
elif choice == "A" and amzius > 65:
    print(f"{vardas} yra pensijoje")
elif choice == "L" and vardo_galas == "s":
    print(f"{vardas} yra vyras")
elif choice == "L" and vardo_galas != "s":
    print(f"{vardas} yra moteris")
else:
    print("Neteisingai ivesta")

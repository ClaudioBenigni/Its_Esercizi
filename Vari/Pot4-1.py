import math

def calculateCharges(ore):
    if ore > 24:
        print("Non puoi parcheggiare per più di 24 ore")
        return 0
    else:
        if ore <= 3:
            costo = 2.00
        else:
            costo = 2.00 + (math.floor(ore) - 3) * 0.50
            if costo > 10:
                costo = 10.00
        return round(costo, 2)

ore_parcheggio = [1.5, 4.0, 5.5, 24.0]

# Intestazione tabella
print(f"{'Car':<5}{'Hours':>10}{'Charge':>15}")

# Variabili totali
total_hours = 0
total_charge = 0

# Corpo tabella
for i, ore in enumerate(ore_parcheggio, start=1):
    charge = calculateCharges(ore)
    total_hours += ore
    total_charge += charge
    print(f"{i:<5}{ore:>10.1f}{charge:>12.2f} $")

# Riga totale
print(f"{'TOTAL':<5}{total_hours:>10.1f}{total_charge:>12.2f} $")

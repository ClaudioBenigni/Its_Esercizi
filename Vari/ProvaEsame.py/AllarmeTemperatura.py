#Verifica Allarme Temperatura – PUNTI 1
#Scrivi una funzione:
#check_temperature_alarm(temp_sensor: float, smoke_sensor: bool, gas_sensor: bool) -> str
#L’allarme si attiva se temp_sensor > 50 e almeno uno tra smoke_sensor o gas_sensor è True.
#Ritorna "Allarme attivato" o "Nessun allarme".

def check_temperature_alarm(temp_sensor: float, smoke_sensor: bool, gas_sensor: bool) -> str: 

    if temp_sensor > 50 and smoke_sensor==True:
        print("Allarme attivato")
    
    elif temp_sensor > 50 and gas_sensor==True:
        print(f"Allarme attivato")
    
    else:
        print(f"Nessun allarme")
    
check_temperature_alarm(70,True,True)
check_temperature_alarm(40,True,True)
check_temperature_alarm(40,False,False)
check_temperature_alarm(60,False,True)
check_temperature_alarm(60,False,False)
    

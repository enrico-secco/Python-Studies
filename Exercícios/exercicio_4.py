# lê temperatura em Fahrenheit e responde em celsius

def TempCelsius(temp_fahrenheit):
    temp_celsius = (5*(temp_fahrenheit - 32)) / 9
    return temp_celsius

print(TempCelsius(64))
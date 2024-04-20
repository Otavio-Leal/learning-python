def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def convert_temp(temp_in_F, temp_in_C):
    if temp_in_F:
        temp = celsius_to_fahrenheit(temp_in_F)
        print(temp)
    else:
        temp = fahrenheit_to_celsius(temp_in_C)
        print(temp)

    
convert_temp(75, False)

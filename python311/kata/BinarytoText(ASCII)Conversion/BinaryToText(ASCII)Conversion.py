def binary_to_string(binary):

    input_string=int(binary, 2);
    
    Total_bytes= (input_string.bit_length() +7) // 8

    input_array = input_string.to_bytes(Total_bytes, "big")
    
    ASCII_value=input_array.decode()
    
    print(ASCII_value)
    
binary_to_string('0100100001100101011011000110110001101111') #Hallo


#Funktion schreiben die ein String in eine Liste von Strings umwandelt die alle 8 zeichen/bit lang sind

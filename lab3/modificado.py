with open("rockyou.txt", "rb") as file:
    lines = file.readlines()


with open("rockyou_mod.dic", "w") as modified_file:
    for line in lines:
       
        line = line.decode("latin-1")
       
        if line[0].isalpha():
           
            modified_password = line[0].upper() + line[1:]
          
            modified_password = modified_password.strip() + "0\n"
            modified_file.write(modified_password)


print("Cantidad de contraseñas en el diccionario modificado:", len(lines))

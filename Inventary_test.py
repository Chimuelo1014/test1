def menu():#In this function, the main menu is executed and the option of the action to be performed is saved.
    option = input("---------Inventario---------\n1 Añadir producto\n2 Consultar producto\n3 Actualiza producto \n4 Eliminar producto \n5 Total Inventario\n6 Salir\n---------------------------\n : ")    
    if option.isdigit():
        return int(option)
    else :
        print("Ingrese un numero del menu valido")
        return menu()
    
def add_product(inventary,name,price,amount): #This function receives the inventory, the name of the product, its price and its units, and checks if it is already in the inventory and if not, adds it.
    if name in inventary :
        print("El produto ya se encuentra en el inventario!")
    else :
        inventary[name] = (price,amount)
        print("Producto añadido exitosamente!")

def check_int(massage,case) :#This function is responsible for checking that what the user entered is actually an integer in order to cast it and add it to the product value.
    entry = check_str(massage,case)
    if entry.isdigit():
        return int(entry)
    else :
        print("Dato ingresado invalido!")
        return check_int(massage,case)

def check_float(massage,case) :#This function receives a message that will be what will be asked to the user and a case, to automate what is asked to the user and before casting it is checked that an empty value has not been entered.
    entry = check_str(massage,case)
    entry1 = entry.replace(",","") 
    entry12 = entry1.replace(".","") 
    if entry12.isdigit():
        entry = entry.replace(",",".")
        entry = float(entry)
        if entry == 0 :
            print("¡El precio no puede ser 0!")
            return check_float(massage,case)
        else:
            return entry
    else :
        print("¡dato ingresado invalido!")
        return check_float(massage,case) 
    

def check_str(massage,case):#This function checks that the entered value is not empty.


    entry = input(massage).strip()
    if entry == "":
        print(case," no puede estar vacio!")
        return check_str(massage,case)
    else :
        return entry

def check_choose(choose) : #This function is responsible for returning a boolean value, true if entered and false if entered
    if choose == "Y" or choose == "y" or choose == "n" or choose == "N" :
            if choose == "Y" or choose == "y":
                return True
            else: return False
                
    else:
        print("Ingrese una opcion valida Y/N")
        return inicial() 
    
    

def check_choose_int(choose1): #This function is used to validate what number of repetitions will be done at the beginning
    choose1 = check_int("¿Cuantos productos iniciales quiere ingresar? : ","")
    if choose1<5 :
        print("¡Deben ser almenos 5!")
        return check_choose_int(choose1)
    else : return choose1
                    
                    

def inicial():#This function is responsible for ordering the 5 initial products
    choose = check_str("¿Quiere ingresar datos iniciales al programa?: Y/N ","")
    
    choose1 = check_choose(choose)
    
    if choose1 :
        choose2 = check_choose_int(choose1) 
        
        counter = 0
        while len(inventary) < choose2 :
            counter +=1
            name = check_str(f"Ingrese el nombre del producto {counter} : ","Nombre").strip().lower()
            price = check_float(f"Ingrese el precio del prodcuto {counter} : ","precio")
            amount = check_int(f"Ingrese las unidades disponibles del producto {counter} : ","unidades")
            if price is not None and amount is not None and name is not None:
                add_product(inventary,name,price,amount)
    else :
        return 
        
def consult_product(inventary,name):#This function receives the inventory and the name to search for, if it is in the inventory it searches for all the matches and saves them in a list and then prints it.
    found = []
    # values = inventary.get(name)
    if name in inventary :
        for keys,values in inventary.items() :
            if name in keys :
                found.append((keys,values))
                print(f"{keys} | Price: {values[0]} | Amount: {values[1]}")
                
    else :
        print("Producto no encontrado.")
  
def update_price(inventary,name,new_price,new_amount=0):#In this function you are asked if you want to change the available units to make it much more dynamic.
    if name in inventary:
        if new_amount == 0 :
            amount = inventary[name][1]
            inventary[name] = (new_price,amount)
            print("Precio actualizado con exito")
        else :
            if name in inventary:
                
                inventary[name] = (new_price,new_amount)
                print("Precio y unidades actualizadas con exito")
            else :
                print("El procutos no se encuentra en el inventario")
    else :
        print("El producto no se encuentra en el inventario")   

def delete_product(inventary):#In this function we first print the products with 0 units available, so that the user can later enter the one they want to delete.
    noamount = []
    print("Esta es la lista de los productos sin unidades\n-------------------------")
    
    for keys,values in inventary.items() :
        if values[1] == 0 :
            noamount.append((keys,values)) 
            print(f"{keys} | precio: {values[0]} | unidades: {values[1]}")
    
    delete = check_str("-----------------------------\n¿que producto desea eliminar?\nIngrese el nombre del producto: ","El nombre")
    if delete not in inventary :
        print("El producto no se eencuentra en el inventario")
        return delete_product(inventary)
    
    del inventary[delete]
    print("El producto fue eliminado con exito")

def total_inventary(inventary):#Here we multiply the quantity of each key by the price and then with an accumulator we add everything up.
    sum=0
    for key in inventary:
        sum=sum+(inventary[key][0])*(inventary[key][1])
    print("El total del inventario es de: $",sum)
    
    
    
    
inventary = {}                       

inicial()

while True :
    option = menu()
    if option == 1 :
        name = check_str("Ingrese el nombre del producto: ","Nombre").strip().lower()
        price = check_float("Ingrese el precio del prodcuto: ","precio")
        amount = check_int("Ingrese las unidades disponibles del producto: ","unidades")
        if price is not None and amount is not None and name is not None:
            add_product(inventary,name,price,amount)
            
    elif option == 2 :
        name = input("Ingrese el nombre del producto a buscar: ").strip().lower()
        consult_product(inventary,name)
        
    elif option == 3 :
        name = check_str("Nombre del producto a actualizar: ","Nombre").strip().lower()
        choose = check_str("¿Quiere actualizar las unidades disponibles?: Y/N ","")
    
        choose1 = check_choose(choose)
        if choose1 :
            new_amount = check_int("Ingrese la nueva cantidad: ","Precio") 
            new_price = check_float("Nuevo precio: ","Precio") 
            if new_price is not None:
                update_price(inventary, name, new_price,new_amount)
            
        else: 
            new_price = check_str("Nuevo precio: ","Precio") 
        
            if new_price is not None:
                update_price(inventary, name, new_price)
        
    elif option == 4 :
        delete_product(inventary)
            
    elif option == 5 :
        total_inventary(inventary)
    elif option == 6 :
        print("Adios")
        break 

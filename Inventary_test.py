def menu():#En esta función se ejecuta el menú principal y se guarda la opción de la acción a realizar.
    option = input("---------Inventario---------\n1 Añadir producto\n2 Consultar producto\n3 Actualiza producto \n4 Eliminar producto \n5 Total Inventario\n6 Salir\n---------------------------\n : ")    
    if option.isdigit():
        return int(option)
    else :
        print("Ingrese un numero del menu valido")
        return menu()
    
def add_product(inventary,name,price,amount): #Esta función recibe el inventario, el nombre del producto, su precio y sus unidades, y verifica si ya está en el inventario y si no, lo agrega.
    if name in inventary :
        print("El produto ya se encuentra en el inventario!")
    else :
        inventary[name] = (price,amount)
        print("Producto añadido exitosamente!")

def check_int(massage,case) :#Esta función se encarga de verificar que lo ingresado por el usuario sea realmente un número entero para poder convertirlo y agregarlo al valor del producto.
    entry = check_str(massage,case)
    if entry.isdigit():
        return int(entry)
    else :
        print("Dato ingresado invalido!")
        return check_int(massage,case)

def check_float(massage,case) :#Esta función recibe un mensaje que será lo que se le preguntará al usuario y un caso, para automatizar lo que se le pregunta al usuario y antes de realizar el cast se revisa que no se haya ingresado un valor vacío.
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
    

def check_str(massage,case):#Esta función verifica que el valor ingresado no esté vacío.


    entry = input(massage).strip()
    if entry == "":
        print(case," no puede estar vacio!")
        return check_str(massage,case)
    else :
        return entry

def check_choose(choose) : #Esta función es responsable de devolver un valor booleano, verdadero si se ingresa y falso si se ingresa
    if choose == "Y" or choose == "y" or choose == "n" or choose == "N" :
            if choose == "Y" or choose == "y":
                return True
            else: return False
                
    else:
        print("Ingrese una opcion valida Y/N")
        return inicial() 
    
    

def check_choose_int(choose1): #Esta función se utiliza para validar qué número de repeticiones se realizarán al inicio.
    choose1 = check_int("¿Cuantos productos iniciales quiere ingresar? : ","")
    if choose1<5 :
        print("¡Deben ser almenos 5!")
        return check_choose_int(choose1)
    else : return choose1
                    
                    

def inicial():#Esta función es responsable de ordenar los 5 productos iniciales.
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
        
def consult_product(inventary,name):#Esta función recibe el inventario y el nombre a buscar, si esta en el inventario busca todas las coincidencias y las guarda en una lista para luego imprimirla.
    found = []
    # values = inventary.get(name)
    if name in inventary :
        for keys,values in inventary.items() :
            if name in keys :
                found.append((keys,values))
                print(f"{keys} | Price: {values[0]} | Amount: {values[1]}")
                
    else :
        print("Producto no encontrado.")
  
def update_price(inventary,name,new_price,new_amount=0):#En esta función se te pregunta si quieres cambiar las unidades disponibles para hacerla mucho más dinámica.
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

def delete_product(inventary):#En esta función primero imprimimos los productos con 0 unidades disponibles, para que posteriormente el usuario pueda introducir el que desea eliminar.
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

def total_inventary(inventary):#Aquí multiplicamos la cantidad de cada clave por el precio y luego con un acumulador sumamos todo.
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

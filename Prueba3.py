generos = ["Ficción","No Ficción","Ciencia"] 
inventario = {"libros 1": {"autor": "Autor 1", "genero": "No Ficción", "Valor": 10, "stock": 20},
            "libro 2": {"autor": "Autor 2", "genero": "No Ficción", "Valor": 15, "stock" : 15},
            "libro 3": {"autor": "Autor 3", "genero": "Ciencia", "Valor": 20, "stock" : 10}}

def registrar_libro():
    titulo = input("INGRESE EL TITULO DEL LIBRO: ")
    autor = input("INGRESE EL NOMBRE DEL AUTOR: ")
    genero = input("INGRESE EL GENERO DEL LIBRO: ")
    valor = float(input("INGRESE EL VALOR DEL LIBRO: "))
    if titulo and autor and genero and valor:
        inventario[titulo] = {"autor": autor, "genero": genero, "valor": valor, "stock": 0}
        print("LIBRO REGISTRADO EXITOSAMENTE!! ")
    else:
        print("TODOS LOS DATOS DEBEN ESTAR REGISTRADOS CORRECTAMENTE, POR FAVIR INTETE NUEVAMENTE")

def listar_libros():
    print("LISTA DE LIBROS REGISTRADOS: ")
    for titulo, detalles in inventario.items():
        print(f"Titulo: {'titulo'}, Autor: {detalles['autor']}, Genero: {detalles['genero']},  Valor: {detalles['valor']}")
        
def registrar_venta():
    titulo = input("INGRESE EL TITULO DEL LIBRO VENDIDO: ")
    if titulo in inventario:
        cantidad = int(input("INGRESE LA CANTIDAD VENDIDA: "))
        valor_unitario = inventario[titulo]["valor"]
        if cantidad <= inventario[titulo]["stock"]:
            valor_final =cantidad * valor_unitario
            inventario[titulo]["stock"] -= cantidad
            print(f"VENTA EXITOSA. VALOR TOTAL: {valor_final}")
        else:
            print("ERROR! EXCEDE LA CANTIDAD DEL STOCK DISPONIBLE.")
    else:
        print("ERROR!! EL LIBRO NO EXISTE EN EL INVENTARIO ")
 
def imprimir_reporte_de_ventas():
    opcion == input("SELECCIONE UNA OPCION - 'TODOS' PARA IMPRIMIR TODAS LAS VENTAS O 'GENERO' PARA IMPRIMIR POR GENERO: ")
    if opcion == "todos":
        print("IMPRIMIR REPORTE DE TODAS LAS VENTAS")
    elif opcion in generos:
        print("IMPRIMRI REPORTE DE VENTAS DEL GENERO {opcion}")
    else: 
        print("OPCIÓN INVÁLIDA.")
try:
    while True:
        print("\n--- Menú ---" )
        print("[1] Registrar libro")
        print("[2] Listar todos los libros")
        print("[3] Registrar venta")
        print("[4] Imprimir reporte de ventas")
        print("[5] Generar txt")
        print("[6] Salir del Programa")

        opcion = int(input("INGRESE UNA DE LAS OPCIONES "))

        if opcion == 1:
            registrar_libro()

        elif opcion == 2:
            listar_libros()

        elif opcion == 3:
            registrar_venta()

        elif opcion == 4:
            imprimir_reporte_de_ventas()
        
        elif opcion == 5:
            print("Generando archivo txt con registro de ventas")

        elif opcion == 6 : 
            print("Salir de progtama!!")
            break
        else:
            print("OPCIÓN INVÁLIDA. POR FAVOR SELECCIONE UNA DE LAS OPCIONES DISPONIBLES. ")
except ValueError:
    print("INGRESE UNA OPCION DISPONIBLE!")
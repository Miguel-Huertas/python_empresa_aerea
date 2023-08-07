# menu obciones
class menu():
	
	def __init__(self, registro, ordenar,salir ):
		
		self.registro = registro
		self.ordenar = ordenar 
		self.salir = salir
    # menu
	def registro():

		opcion=int(input("\n Digite opcion deseada: \n\n 1. Registrar datos clientes \n 2. Imprimir lista clientes \n 3. Ordenar la lista de clientes por identificación \n 4. Consulta de clientes por país de origen \n 5. Salir  \n"))
		
		return opcion


# arreglo
import numpy as np

#   registro clientes 		
class registro():
	
    def __init__(self):
        self.identificacion = 0
        self.nombre = ""
        self.pais_origen = ""
        self.pais_destino = ""
    #registra datos 
    def registrar(self):
        self.identificacion=int(input("Digute su identificación: "))
        self.nombre=input("Digite su nombre: ")
        self.pais_origen=input("Digite país origen: ")
        self.pais_destino=input("Digite país destino: ")
    #imprime datos 
    def imprime(self):
        print(' --------------------- \n Identificacion: {} \n nombre: {} \n país origen: {} \n país destino: {} \n --------------------- '.format(self.identificacion,self.nombre,self.pais_origen,self.pais_destino))

arr=np.empty((10,),dtype = np.object_)
# segun obcion el codigo se repite       

def correr_codigo ():   
    print("\n'HOLA'")
    op=0
    i=0
    while op<=4:
        # llamamos a la clase menu y al metodo  
        op=menu.registro()
        if op==1:
            arr[i]=registro() # llama a la clase
            arr[i].registrar() # llama al metodo
            i+=1

        elif op==2:
             # inprime el arreglo dato por dato
            a=0
            while a < i:
                arr[a].imprime()
                a+=1
        elif op == 3:
            # ordena por numero de documento 
            for l in range(i-1):
                for m in range(i-1):
                    if (arr[m].identificacion > arr[m+1].identificacion):
                        
                        tem = arr[m]
                        arr[m] = arr[m + 1]
                        arr[m + 1] = tem
            a=0
            while a < i:
                arr[a].imprime()
                a+=1             
        elif op == 4:
            # consultar por pais de origen
            l=0
            while l< i:
                print("\nPaices registrados: \n")
                #se crea lista para guardar los paides de orige de cada cliente
                r=[]
                for d in range(i):
                    P=(arr[d].pais_origen)
                    r.append(P)
                    d+=1
                # se crea lista  sin repetir 2 y mas veses el mismo pais    
                a=[]
                for m in r:
                    if m not in a:
                        a.append(m)
                # se realiza el menu de los paices registrados 
                q=1
                for g in a:
                    print(q,". ",g)
                    q+=1
                print(q,". Salir ")
                elec=int(input("\nDigite numero del pais a consultar: \n"))
                # segun el pais seleccionado se imprime los clientes de origen en ese pais 
                for w in range(len(a)):
                    if elec== w+1:
                        for n in range(i):
                            if a[elec-1]== arr[n].pais_origen:
                                arr[n].imprime()
                    # salida de obcion consultar por pais de origen
                if elec < 1 or elec > q:
                    print("*********************\n* OPCION INCORRECTA *\n********************* \n \nDigite una opcion valida ") 
                elif elec == q:
                    l=i

        elif op==5:
             # salida del codigo 
            op=5       

correr_codigo()
print("GRACIAS POR ULILIZAR EL COGIGO \n ¡HASTA PRONTO! ")

#INTRODUCCION A LA PROGRAMACION 
#Luis Miguel Huertas Montaña 
#Grupo: 301304_93

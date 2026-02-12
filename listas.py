ef double (arr):
  return [x*2 for x in arr]
  
def maximum (arr):
  return max (arr)

def average (arr): 
  if not arr: 
    return 0
  return sum(arr)/ len (arr)

def main():
    # Lista de prueba
    datos = [2, 4, 6, 8]
    
    # Ejecución y resultados breves
    print("Doble:", double(datos))
    print("Máximo:", maximum(datos))
    print("Promedio:", average(datos))

if __name__ == "__main__":
    main()

  

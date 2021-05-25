def outfit(city_name):
    if city_name == 'Medellin' or 'Medellín':
        return f" El valor total del producto es {(product_quant*product_value_unit)-(product_quant*product_value_unit)*0.05}"


if __name__ == '__main__':
    i = ''
    while i != 'Y':

        # Product characteristics 
        product_name = input("Nombre del producto: ")
        product_quant = int(input("Cantidad que llevará: "))
        product_value_unit = int(input("Valor por unidad"))
        product_city = input("Nombre de la ciudad de venta: ")
        # Confirmation
        i = input("Escribe Y para confirmar los datos o cualquier letra si quieres reiniciar: ")

    j = outfit(product_city)
    if j:
        print(j)
    else:
        print(f" El valor total del producto es {product_quant*product_value_unit} en la ciudad de {product_city}")
        






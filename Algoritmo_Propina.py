try:
    entrada_1 = input("\nCual es la factura total de hoy?: $")
    entrada_2 = input("\nCuanto porcentaje quiere usar para propina?: %")

    valor_entrada_1 = float(entrada_1)
    valor_entrada_2 = float(entrada_2)
    porcentaje = valor_entrada_1 * valor_entrada_2 / 100
    total_entrada = porcentaje + valor_entrada_1
    string_entrada = str(total_entrada)
    
    print("\nEl total a pagar contando la propina es de $" + string_entrada + '\n')

except ValueError:
    print("ERROR!!! \nINGRESE CORRECTAMENTE LOS DATOS")


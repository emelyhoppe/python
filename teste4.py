mes = input("Digite um mês: ")
if mes in("dezembro", "janeiro", "fevereiro"):
    estacao = "Verão"
    
elif mes in ("março", "abril", "maio"):
    estacao = "Outono"
    
elif mes in ("junho", "julho", "agosto"):
    estacao = "Inverno"
    
elif mes in ("setembro", "outubro", "novembro"):
    estacao = "Primavera"
print(f"A estação do seu mês é: {estacao}.")
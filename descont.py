#ESCOLHER O PRECO   
preco = float(input("Qual o valor desse produto?\n"))

#CALCULO DO DESCONTO
desconto = preco * 5 / 100
preco_final = preco - desconto
print("O valor com desconto fica {:.2}".format(preco_final))
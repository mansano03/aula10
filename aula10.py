def comparar_par_impar(num1, num2):
    
    resultado_num1 = "par" if num1 % 2 == 0 else "ímpar"
    resultado_num2 = "par" if num2 % 2 == 0 else "ímpar"

   
    if resultado_num1 == resultado_num2:
        return f"Ambos os números são {resultado_num1}s."
    else:
        return f"Um número é {resultado_num1} e o outro é {resultado_num2}."


print(comparar_par_impar(4, 7)) 
print(comparar_par_impar(6, 2))  


#2
def multiplicar_tres_numeros(num1, num2, num3):
    
    resultado = num1 * num2 * num3
    return resultado


print(multiplicar_tres_numeros(2, 3, 4))

#3
def elevar_numero(base, expoente):
    
    resultado = base ** expoente
    return resultado


print(elevar_numero(2, 3))


#4
def verificar_idade():
    
    idade = input("Digite sua idade: ")

    
    if idade == "18 anos":
        print("Você tem 18 anos! Bem-vindo à maioridade!")
    else:
        print("Você não tem 18 anos ainda.")


verificar_idade()

#5
from datetime import datetime

def calcular_idade(data_nascimento):
    
    hoje = datetime.today()
    
    
    idade = hoje.year - data_nascimento.year
    
    
    if hoje.month < data_nascimento.month or (hoje.month == data_nascimento.month and hoje.day < data_nascimento.day):
        idade -= 1 
    
    return idade


ano = int(input("Digite o ano de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
dia = int(input("Digite o dia de nascimento: "))


data_nascimento = datetime(ano, mes, dia)


idade = calcular_idade(data_nascimento)
print(f"Sua idade é: {idade} anos.")


#6
def verifica_copa_1999():
    
    copa_1999_campeao = "Estados Unidos"
    
    if copa_1999_campeao == "Brasil":
        return "Sim, o Brasil ganhou a Copa do Mundo de 1999."
    else:
        return "Não, o Brasil não ganhou a Copa do Mundo de 1999."


resultado = verifica_copa_1999()
print(resultado)

#7
def exibir_menu():
    print("Bem-vindo ao nosso Restaurante!")
    print("Escolha uma das opções abaixo:")
    print("1. Salada - R$ 15,00")
    print("2. Macarronada - R$ 20,00")
    print("3. Sanduíche - R$ 12,00")
    print("4. Sorvete - R$ 8,00")
    print("0. Finalizar pedido")

def calcular_total(pedido):
    total = 0
    for item in pedido:
        if item == 1:
            total += 15.00  
        elif item == 2:
            total += 20.00  
        elif item == 3:
            total += 12.00  
        elif item == 4:
            total += 8.00  
    return total

def sistema_restaurante():
    pedido = []
    
    while True:
        exibir_menu()
        try:
            escolha = int(input("Digite o número do item que você deseja ou 0 para finalizar: "))
            
            if escolha == 0:
                break
            elif escolha in [1, 2, 3, 4]:
                pedido.append(escolha)
                print("Item adicionado ao seu pedido!")
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")
    
    if pedido:
        print("\nSeu pedido foi:")
        print(f"Items escolhidos: {', '.join(map(str, pedido))}")
        total = calcular_total(pedido)
        print(f"Total do seu pedido: R$ {total:.2f}")
    else:
        print("\nVocê não fez nenhum pedido.")
        

sistema_restaurante()


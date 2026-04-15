resposta = 'S'
print("--- Sistema de Cálculo de Vendas ---")

while resposta != 'N':
    entrada = float(input("\nDigite o valor da venda: R$ "))
    
    if entrada > 1000:
        desconto = entrada * 0.10
        valor_final = entrada - desconto
        print(f"\nValor original: R$ {entrada:.2f}")
        print(f"DESCONTO APLICADO (10%): R$ {desconto:.2f}")
        print(f"Total a pagar: R$ {valor_final:.2f}")
    else:
            print("Sem desconto aplicado (venda abaixo de R$ 1.000,00)")
            
    resposta = input("Deseja informar novas vendas? (S/N): ").upper().strip()

print("\nPrograma finalizado com sucesso!")
LOJA = "Python Express"

BRINDES = ("Adesivos", "Caneca", "Camiseta")

def calculo_venda(valor_bruto: float):

    if valor_bruto <= 0:
        raise ValueError("O valor deve ser maior que zero!!")
    
    if valor_bruto > 1000:
        desconto = valor_bruto*0.1

    else :
        desconto = valor_bruto*0.05

    total= valor_bruto - desconto

    return total, desconto

def ger_brindes(cliente: list, valor_total: float):

    if valor_total > 1000:
        cliente.append(BRINDES[1])
    elif valor_total >= 500:
        cliente.append(BRINDES[0])

def main ():
    try:
        historico_vendas = []

        vendas = "s"

        while vendas == "s":

            valor_input= input("Registre o valor da venda:")
            venda = float(valor_input)

            brinde_cliente = []

            total, desconto= calculo_venda(venda)

            ger_brindes(brinde_cliente, total)

            aux_dic = {
                "total": total,
                "desc": desconto,
                "brindes": brinde_cliente
            }

            historico_vendas.append(aux_dic)

            print(f"--- {LOJA} ---")
            print(f"\nValor Total: R$ {total:.2f}")
            print(f"\nPARABÉNS!! Você economizou R$ {desconto:.2f} na sua compra!")
            print(f"Você ganhou de brindes: {', '.join(brinde_cliente if brinde_cliente else "Nenhum")}")

            continuar = input("Deseja cadastrar um novo produto? (s/n)").lower()

            vendas = str(continuar)

            while vendas not in ["s", "n"]:
                print("Resposta inválida! Tente novamente! \n -----------------")

                continuar = input("Deseja cadastrar um novo produto? (s/n)").lower()
                vendas = str(continuar)

        faturamento = 0

        for i in historico_vendas:
            faturamento += i["total"]

        print(f"--- {LOJA} ---")
        print(f"\nValor Total de vendas: R$ {faturamento:.2f}")
        print(f"\nVendas feitas: {len(historico_vendas)} na sua compra!")

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
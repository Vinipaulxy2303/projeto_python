import tkinter as tk
def cadastro():
    janela = tk.Tk()
    janela.title("Cadastro de Entregas")

    tk.Label(janela, text="Código:").pack()
    campo_codigo = tk.Entry(janela)
    campo_codigo.pack()

    def salvar():
        codigo = campo_codigo.get()
        print("Código digitado:", codigo)

    tk.Button(janela, text="Salvar", command=salvar).pack()

    janela.mainloop()
        
    entregas=[]
    timer=1
    codigo= []
    for i in range(4):
        sistema= True
        codigos=int(input("Me de um codigo: "))
        if timer > 1:
            while sistema == True:
                if codigos in codigo:
                    print("Repetido!")
                    codigos=int(input("Me de um codigo: "))
                else:
                    sistema = False
                    codigo.append(codigos) 
        else:
            codigo.append(codigos)      
        nome_ou_descrição_do_destinatário=str(input("Qual o nome : "))
        região_de_origem =str(input("Qual a região de origem: "))
        região_de_destinada =str(input("Qual é o destino final: "))
        peso_da_carga =float(input("QUal é o peso da carga: "))
        valor_da_mercadoria =float(input("Qual é o valor de mercado: "))
        prioridade =int(input("Qual a sua prioridade: "))
        distância =float(input("Qual a distancia total: "))
        status =str(input("QUal é o status: "))
        sistema2 = False
        while sistema2 == False:
            if status != "Disponivel" and status != "Indisponivel":
                print("Status incorretos ")
                status =str(input("QUal é o status: "))
            else:
                sistema2 = True
                if status == "Disponivel" :
                    verificacao = True
                elif status == "Indisponivel":
                    verificacao = False
        custo_estimado_da_entrega =float(input("Qual é o valor estimado para a entrega: "))
        print("==============================")
        opcao=input("Digite Qualquer coisa!")
        timer += 1
        entrega={"Codigo": codigos ,"nome ou descrição do destinatário" : nome_ou_descrição_do_destinatário ,"região de origem": região_de_origem,"região de destinada": região_de_destinada,"peso da carga": peso_da_carga,"valor da mercadoria": valor_da_mercadoria,"prioridade":prioridade,"distância": distância,"status": status,"custo estimado da entrega":custo_estimado_da_entrega}
        entregas.append(entrega)
        return verificacao , entregas

cadastro()
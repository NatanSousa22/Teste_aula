while True:
    print("\nEscolha uma opção:")
    print("1: Contar caracteres")
    print("2: Contar palavras")
    print("0: Sair")

    opcao = input("Digite o número da opção: ")

    if opcao == "0":
        print("Saindo do programa. Valeu, falou!")
        break
    elif opcao in ("1", "2"):
        texto_usuario = input("Digite o texto: ")

        if opcao == "1":
            print(f"O texto tem {len(texto_usuario)} caracteres.")
        elif opcao == "2":
            print(f"O texto tem {len(texto_usuario.split())} palavras.")
    else:
        print("Essa opção não é válida. Tente novamente uma das opções avaliadas.")
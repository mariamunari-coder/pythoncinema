#PYTHON CINEMA
catalogo = ['Interestrelar', 'O Poderoso Chefão', 'A Lista de Schindler', 'Hulk']

while True:
    print('\n' + '=' * 30)
    print('🎬 Catálogo de Filmes ')
    print('=' * 30)
    print('1. Listar todos os filmes')
    print('2. Buscar por título')
    print('3. Adicionar filme')
    print('0. Sair')
    
    opcao = input("\nEscolha uma opção: ")
    if opcao == '1':
        print('\nLista de Filmes')
        for filme in sorted(catalogo):
            print(f'• {filme}')
    elif opcao == '2':
        busca = input('Digite o nome ou parte do filme: ').lower()
        encontrados = []
        for filme in catalogo:
            if busca in filme.lower():
                encontrados.append(filme)
        if encontrados:
            print('\nResultados:')
            for item in encontrados:
                print(f"-> {item}")
        else:
            print('Nenhum filme encontrado')
    elif opcao == '3':
        novo_filme = input('Nome do filme: ').strip()
        if novo_filme == "":
            print('erro')
        else:
            catalogo.append(novo_filme)
            print(f"'{novo_filme}' adicionado com sucesso!")
    elif opcao == '0':
        print("Saindo do Sistema. Até logo!")
        break
    else:
        print('erro')

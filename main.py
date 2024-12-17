import csv
import os

arquivo_csv = 'agenda.csv'

def exibir_menu():
    print("\nMenu:")
    print("1. Criar contato")
    print("2. Listar contatos")
    print("3. Atualizar contato")
    print("4. Deletar contato")
    print("5. Baixar contatos (CSV)")
    print("6. Sair")

def criar_contato():
    nome = input("Nome do contato: ").strip()
    telefone = input("Telefone do contato: ").strip()
    email = input("E-mail do contato: ").strip()

    if not nome or not telefone or not email:
        print("Todos os campos são obrigatórios!")
        return

    with open(arquivo_csv, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, telefone, email])

    print("Contato criado!")

def listar_contatos():
    if os.path.exists(arquivo_csv):
        with open(arquivo_csv, 'r') as file:
            reader = csv.reader(file)
            print("\nContatos:")
            for row in reader:
                print(f"Nome: {row[0]}, Telefone: {row[1]}, E-mail: {row[2]}")
    else:
        print("Nenhum contato encontrado.")

def atualizar_contato():
    nome_atualizar = input("Nome do contato a atualizar: ").strip()
    encontrado = False
    contatos = []

    if os.path.exists(arquivo_csv):
        with open(arquivo_csv, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == nome_atualizar:
                    telefone = input("Novo telefone: ").strip()
                    email = input("Novo e-mail: ").strip()
                    contatos.append([nome_atualizar, telefone, email])
                    encontrado = True
                else:
                    contatos.append(row)

        if encontrado:
            with open(arquivo_csv, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(contatos)
            print("Contato atualizado!")
        else:
            print("Contato não encontrado.")

def deletar_contato():
    nome_deletar = input("Nome do contato a deletar: ").strip()
    encontrado = False
    contatos = []

    if os.path.exists(arquivo_csv):
        with open(arquivo_csv, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == nome_deletar:
                    encontrado = True
                else:
                    contatos.append(row)

        if encontrado:
            confirmar = input(f"Tem certeza que deseja deletar o contato '{nome_deletar}'? (s/n): ").strip().lower()
            if confirmar == 's':
                with open(arquivo_csv, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(contatos)
                print("Contato deletado!")
            else:
                print("Ação de deletar contato cancelada.")
        else:
            print("Contato não encontrado.")

def baixar_contatos():
    if os.path.exists(arquivo_csv):
        with open(arquivo_csv, 'r') as file:
            reader = csv.reader(file)
            with open('agenda_export.csv', 'w', newline='') as export_file:
                writer = csv.writer(export_file)
                for row in reader:
                    writer.writerow(row)
        print("Contatos exportados para 'agenda_export.csv'.")
    else:
        print("Nenhum contato encontrado.")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            criar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            atualizar_contato()
        elif opcao == "4":
            deletar_contato()
        elif opcao == "5":
            baixar_contatos()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

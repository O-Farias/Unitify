from app.converters import convert_temperature, convert_length
import os

def clear_console():
    """
    Limpa o terminal para manter o menu organizado.
    """
    os.system("cls" if os.name == "nt" else "clear")

def main():
    while True:
        clear_console()
        print("=" * 30)
        print("🌟 Bem-vindo ao Conversor de Unidades! 🌟")
        print("=" * 30)

        print("\nEscolha o tipo de conversão:")
        print("1. Converter Temperatura")
        print("2. Converter Comprimento")
        print("3. Sair")
        print("=" * 30)

        option = input("Digite a opção desejada (1/2/3): ").strip()

        if option == "1":
            handle_temperature_conversion()
        elif option == "2":
            handle_length_conversion()
        elif option == "3":
            print("\n✨ Obrigado por usar o Conversor de Unidades! Até a próxima! ✨")
            break
        else:
            print("\n⚠️ Opção inválida. Tente novamente.")
            input("Pressione ENTER para voltar ao menu...")

def handle_temperature_conversion():
    clear_console()
    print("=" * 30)
    print("🌡️ Conversão de Temperatura 🌡️")
    print("=" * 30)
    print("1. Celsius")
    print("2. Fahrenheit")
    print("=" * 30)

    from_unit = input("Escolha a unidade de origem (1/2): ").strip()
    to_unit = input("Escolha a unidade de destino (1/2): ").strip()
    value = input("Digite o valor: ").strip()

    unit_map = {"1": "celsius", "2": "fahrenheit"}

    try:
        value = float(value)
        result = convert_temperature(unit_map[from_unit], unit_map[to_unit], value)
        print(f"\n✅ Resultado: {value} {unit_map[from_unit]} equivalem a {result} {unit_map[to_unit]}")
    except KeyError:
        print("\n⚠️ Erro: Opção de unidade inválida.")
    except ValueError:
        print("\n⚠️ Erro: Valor inválido. Digite um número válido.")

    input("\nPressione ENTER para voltar ao menu...")

def handle_length_conversion():
    clear_console()
    print("=" * 30)
    print("📏 Conversão de Comprimento 📏")
    print("=" * 30)
    print("1. Metros")
    print("2. Quilômetros")
    print("=" * 30)

    from_unit = input("Escolha a unidade de origem (1/2): ").strip()
    to_unit = input("Escolha a unidade de destino (1/2): ").strip()
    value = input("Digite o valor: ").strip()

    unit_map = {"1": "meters", "2": "kilometers"}

    try:
        value = float(value)
        result = convert_length(unit_map[from_unit], unit_map[to_unit], value)
        print(f"\n✅ Resultado: {value} {unit_map[from_unit]} equivalem a {result} {unit_map[to_unit]}")
    except KeyError:
        print("\n⚠️ Erro: Opção de unidade inválida.")
    except ValueError:
        print("\n⚠️ Erro: Valor inválido. Digite um número válido.")

    input("\nPressione ENTER para voltar ao menu...")

if __name__ == "__main__":
    main()

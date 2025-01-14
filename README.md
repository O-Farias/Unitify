# **Unitify** 🌍🔄  
> Um conversor de unidades simples e funcional, desenvolvido em Python.

---

## **Sobre o Projeto**
O **Unitify** é uma aplicação em Python com foco no **backend**, projetada para facilitar a conversão de unidades como:
- **Temperatura**: Celsius ↔ Fahrenheit.
- **Comprimento**: Metros ↔ Quilômetros.

O sistema é completamente interativo via terminal, garantindo uma experiência fluida e intuitiva para o usuário.

---

## **Funcionalidades**
- Conversão de temperatura entre:
  - Celsius ↔ Fahrenheit.
- Conversão de comprimento entre:
  - Metros ↔ Quilômetros.
- Menu interativo no terminal.

---

## **Pré-requisitos**
Antes de começar, você precisará ter instalado em sua máquina:
- **Python 3.8+**

---

## **Como Rodar o Projeto**

### **1. Clone o Repositório**
```bash
git clone https://github.com/O-Farias/unitify.git
cd unitify
```

### **2. Crie um Ambiente Virtual**
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### **3. Instale as Dependências**
```bash
pip install -r requirements.txt
```

### **4. Rode o Projeto**
```bash
python app/main.py
```

## **Como Usar**

Ao rodar o projeto, você verá o seguinte menu interativo no terminal:

```plaintext
🌍 Unitify 🌍
1. Converter Temperatura
2. Converter Comprimento
3. Sair
Escolha uma opção:
```

## **Exemplo de Uso**

1. Escolha a opção 1 para converter temperatura.
2. Informe a unidade de origem (ex.: Celsius).
3. Informe a unidade de destino (ex.: Fahrenheit).
4. Digite o valor que deseja converter.
5. Receba o resultado instantaneamente no terminal.

## **Tecnologias Utilizadas**

- **Python 3.10**
- **FastAPI** - Framework web para APIs (caso necessário no futuro).
- **Testes Automatizados** - Implementados com `unittest`.
 
## **Licença**

Esse projeto está sob a licença **MIT**.

# 🔎 Analisador de CPF

O **Analisador de CPF** é uma aplicação simples desenvolvida com o objetivo de verificar se um CPF brasileiro é válido ou não, utilizando o cálculo dos dígitos verificadores.

---

## 🧠 Como funciona?

O CPF (Cadastro de Pessoa Física) possui 11 dígitos, sendo os dois últimos **dígitos verificadores**. A aplicação realiza os seguintes passos:

1. Remove caracteres especiais (`.` e `-`)
2. Verifica se há 11 dígitos numéricos
3. Calcula os dois dígitos verificadores conforme a fórmula oficial da Receita Federal
4. Compara os dígitos calculados com os dois últimos do CPF fornecido

Se tudo estiver correto, o CPF é considerado **válido**.

---

## ✅ Exemplo de uso

```txt
Entrada: 123.456.789-09  
Saída: {'valido': False, 'regiao': None}

Entrada: 529.982.247-25  
Saída: {'valido': True, 'regiao': '7) ES e RJ'}
````

---

## 🛠️ Tecnologias utilizadas

* Linguagem: Python
* Lógica baseada na validação matemática dos dígitos do CPF

---

## 📦 Como usar

1. Clone o repositório:

```bash
git clone https://github.com/Boyuridod/AnalisadorDeCPF.git
```

2. Acesse a pasta:

```bash
cd AnalisadorDeCPF
```

3. Execute o código:

```bash
python AnalisadorDeCPF.py
```

---

## 📚 Referências

* [A matemática dos CPFs – Clube da Matemática OBMEP](https://clubes.obmep.org.br/blog/a-matematica-nos-documentos-a-matematica-dos-cpfs/)
* [Vídeo explicativo no YouTube – canal Super Simples](https://youtu.be/15Bw0duulMQ)

---

## 👨‍💻 Autor

* **Yuri Duarte**

---

## 📄 Licença

Este projeto tem fins **educacionais**.
Sinta-se à vontade para estudar e adaptar, mas evite simplesmente copiar — entender o funcionamento é a melhor forma de aprender! 🚀

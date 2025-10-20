# Orçamento de Aluguel R.M

## Descrição do Projeto

Este projeto é uma aplicação em **Python orientada a objetos** para calcular orçamentos de aluguel de imóveis.  
Ele foi desenvolvido para atender às necessidades de uma imobiliária fictícia R.M, permitindo gerar orçamentos mensais considerando diferentes tipos de imóveis, número de quartos, vagas de garagem, descontos e o contrato imobiliário.

O sistema também gera automaticamente um arquivo CSV com **12 parcelas do aluguel**, facilitando o controle e registro dos valores.

---

## Funcionalidades

- Cálculo do aluguel mensal baseado no tipo de imóvel:
  - Apartamento (1 ou 2 quartos)  
  - Casa (1 ou 2 quartos)  
  - Estúdio
- Aplicação de valores adicionais:
  - Quartos extras (quando aplicável)
  - Vagas de garagem
  - Desconto de 5% para apartamentos sem crianças
- Contrato imobiliário fixo (R$ 2.000,00) parcelado em até 5 vezes
- Geração automática de arquivo CSV com 12 parcelas do aluguel
- Relatório completo exibido no terminal
- Arquivo CSV gerado com **nome único** usando timestamp, evitando sobrescrita

---

## Estrutura do Projeto

- `main.py` → Arquivo principal com todas as classes e lógica do programa:
  - **Classe `Imovel`**: calcula o valor do aluguel mensal de acordo com o tipo de imóvel, quartos, garagem e desconto.  
  - **Classe `Contrato`**: define o contrato imobiliário e permite calcular o valor de cada parcela do contrato.  
  - **Classe `Orcamento`**: centraliza o orçamento, gera relatório no terminal e arquivo CSV com as parcelas do aluguel.

---

## Como Executar

1. Clone o repositório:

git clone https://github.com/FrankM1randa/orcamento_aluguel.git
Entre na pasta do projeto:


cd orcamento_aluguel
Execute o programa:

python main.py
Siga as instruções no terminal para inserir:

Nome do cliente

Tipo de imóvel

Número de quartos

Número de vagas de garagem

Presença de crianças (para apartamentos)

O programa exibirá o relatório no terminal e gerará um arquivo CSV com 12 parcelas do aluguel.
Exemplo de arquivo gerado: orcamento_20251020_181530.csv

Exemplo de Saída
=== ORÇAMENTO GERADO ===
Cliente: João Silva
Aluguel mensal: R$ 1.155,00
Contrato imobiliário: R$ 2.000,00 em até 5x de R$ 400,00
Arquivo 'orcamento_20251020_181530.csv' gerado com sucesso!
Arquivo CSV:

Parcela,Valor (R$)
1,R$ 1.155,00
2,R$ 1.155,00
...
12,R$ 1.155,00


Requisitos
Python 3.7 ou superior

Biblioteca padrão (csv, datetime)

Próximos Passos / Melhorias

Adicionar interface gráfica (Tkinter ou Flask Web)

Permitir customização do valor do contrato

Salvar histórico de orçamentos em um banco de dados

Gerar relatórios gráficos das parcelas e contratos

Autor
Frank Miranda
GitHub: https://github.com/FrankM1randa

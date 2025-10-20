import csv
from datetime import datetime

class Imovel:
    def __init__(self, tipo, quartos=1, garagem=0, possui_criancas=True):
        self.tipo = tipo.lower()
        self.quartos = quartos
        self.garagem = garagem
        self.possui_criancas = possui_criancas

    def calcular_aluguel(self):
        valor_base = 0
        if self.tipo == 'apartamento':
            valor_base = 700
            if self.quartos == 2:
                valor_base += 200
            if not self.possui_criancas:
                valor_base *= 0.95
        elif self.tipo == 'casa':
            valor_base = 900
            if self.quartos == 2:
                valor_base += 250
        elif self.tipo == 'estudio':
            valor_base = 1200
            valor_base += 250
            if self.garagem > 2:
                valor_base += (self.garagem - 2) * 60
        else:
            print("Tipo de imóvel inválido.")
            return None

        if self.tipo in ['apartamento', 'casa'] and self.garagem >= 1:
            valor_base += 300

        return valor_base


class Contrato:
    def __init__(self, valor_total=2000, parcelas=5):
        self.valor_total = valor_total
        self.parcelas = parcelas

    def valor_parcela(self):
        return round(self.valor_total / self.parcelas, 2)


class Orcamento:
    def __init__(self, cliente, imovel, contrato):
        self.cliente = cliente
        self.imovel = imovel
        self.contrato = contrato
        self.aluguel_mensal = self.imovel.calcular_aluguel()

    def gerar_csv(self):
        # Criar nome único para cada execução usando timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"orcamento_{timestamp}.csv"

        with open(nome_arquivo, 'w', newline='') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerow(['Parcela', 'Valor (R$)'])
            for i in range(1, 13):
                valor_formatado = f"R$ {self.aluguel_mensal:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
                writer.writerow([i, valor_formatado])
        print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")

    def exibir_relatorio(self):
        print("\n=== ORÇAMENTO GERADO ===")
        print(f"Cliente: {self.cliente}")
        print(f"Aluguel mensal: R$ {self.aluguel_mensal:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
        print(f"Contrato imobiliário: R$ {self.contrato.valor_total:,.2f} em até {self.contrato.parcelas}x de R$ {self.contrato.valor_parcela():,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))


def main():
    print("=== Orçamento de Aluguel R.M ===")
    cliente = input("Nome do cliente: ")
    tipo_imovel = input("Tipo de imóvel (Apartamento/Casa/Estudio): ").strip()
    
    quartos = 1
    if tipo_imovel.lower() in ['apartamento', 'casa']:
        quartos = int(input("Número de quartos (1 ou 2): "))
    
    garagem = 0
    if tipo_imovel.lower() in ['apartamento', 'casa', 'estudio']:
        garagem = int(input("Número de vagas de garagem: "))
    
    possui_criancas = True
    if tipo_imovel.lower() == 'apartamento':
        resposta = input("Possui crianças? (sim/não): ").strip().lower()
        possui_criancas = True if resposta == 'sim' else False

    imovel = Imovel(tipo_imovel, quartos, garagem, possui_criancas)
    contrato = Contrato()
    orcamento = Orcamento(cliente, imovel, contrato)
    
    orcamento.exibir_relatorio()
    orcamento.gerar_csv()


if __name__ == "__main__":
    main()

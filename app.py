class CalculadoraConsumo:
    def __init__(self, tarifa: float = 0.75, dias: int = 30):
        self._tarifa = tarifa
        self._dias = dias

    def _obter_float(self, mensagem):
        while True:
            try:
                valor = float(input(mensagem).strip().replace(",", ".")
                              )
                if valor > 0:
                    return valor
                print(" ❌ Informe um valor maior que zero.")
            except ValueError:
                print(" ❌ Valor inválido. Use apenas números.")

    def _calcular_consumo(self, potencia, horas):
        return (potencia * horas * self._dias) / 1000

    def _obter_nome(self) -> str:
        while True:
            nome = input("Nome do aparelho: ").strip()
            if nome:
                return nome
            print(" ❌ Informe um nome para o aparelho.")
    
    def executar(self):
        print("🔢⚡Calculadora de Consumo Elétrico ⚡🔢\n")

        while True:
            nome = self._obter_nome()
            potencia = self._obter_float("Potência (W): ")
            horas = self._obter_float("Horas por dia: ")

            consumo = self._calcular_consumo(potencia, horas)
            custo = float(consumo) * self._tarifa

            print("================ \nResultado: ")
            print(f"    Aparelho: {nome}")
            print(f"    Consumo: {consumo:.2f} kWh/mês".replace(".", ","))
            print(f"    Custo: R$ {custo:.2f}/mês".replace(".", ","))

            if input("Calcular outro? (s/n): ").strip().lower() != "s":
                print("\nEncerrado.")
                break


if __name__ == "__main__":
    CalculadoraConsumo().executar()
# :zap: Calculadora de Consumo Elétrico

> Estime o consumo mensal de energia elétrica dos seus aparelhos e descubra quanto custam na conta de luz.

---

## Sobre

Programa em **Python** que calcula o consumo mensal de qualquer aparelho doméstico a partir do nome, potência (W) e horas de uso diário.

---

## Implementação

O consumo mensal é calculado com base na potência, horas de uso e número de dias:
```python
def _calcular_consumo(self, potencia, horas):
    return (potencia * horas * self._dias) / 1000
```

O custo é obtido multiplicando o consumo pela tarifa:
```python
custo = float(consumo) * self._tarifa
```

A tarifa padrão é **R$ 0,75/kWh** (média ANEEL). Pode ser alterada diretamente no código.
```python
def __init__(self, tarifa: float = 0.75, dias: int = 30):
    self._tarifa = tarifa
```

---

## Como executar
```bash
git clone https://github.com/sart-mercyy/calculadora-consumo-eletrico.git
cd calculadora-consumo-eletrico
python app.py
```

---

## Exemplo de uso
```
🔢⚡Calculadora de Consumo Elétrico ⚡🔢

Nome do aparelho: Geladeira
Potência (W): 100 
Horas por dia: 24
================ 
Resultado:
    Aparelho: Geladeira
    Consumo: 72,00 kWh/mês
    Custo: R$ 54,00/mês
Calcular outro? (s/n):
```
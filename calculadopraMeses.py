# Defina o número de dias em cada mês
dias_por_mes = {
    "janeiro": 31,
    "fevereiro": 28, # 29 em um ano bissexto
    "março": 31,
    "abril": 30,
    "maio": 31,
    "junho": 30,
    "julho": 31,
    "agosto": 31,
    "setembro": 30,
    "outubro": 31,
    "novembro": 30,
    "dezembro": 31,
}

# Número de horas em um dia
horas_por_dia = 24

def calcular_horas_mes(mes):
    if mes in dias_por_mes:
        dias = dias_por_mes[mes]
        horas = dias * horas_por_dia
        return horas
    else:
        return 0

# Solicita ao usuário o nome dos dois meses
mes1 = input("Digite o nome do primeiro mês: ").lower()
mes2 = input("Digite o nome do segundo mês: ").lower()

horas_mes1 = calcular_horas_mes(mes1)
horas_mes2 = calcular_horas_mes(mes2)

if horas_mes1 > 0 and horas_mes2 > 0:
    total_horas = horas_mes1 + horas_mes2
    print(f"Total de horas entre {mes1.capitalize()} e {mes2.capitalize()} em um ano: {total_horas} horas.")
else:
    print("Mês inválido. Certifique-se de digitar o nome do mês corretamente.")

# Pergunta ao usuário se deseja calcular o total de horas em um ano
calcular_ano = input("Deseja calcular o total de horas entre esses dois meses em 1 ano? (Sim/Não): ").strip().lower()

if calcular_ano == "sim":
    total_horas_ano = (horas_mes1 + horas_mes2) * 12 # Multiplicando por 12 para um ano completo
    print(f"Total de horas entre {mes1.capitalize()} e {mes2.capitalize()} em 1 ano: {total_horas_ano} horas.")

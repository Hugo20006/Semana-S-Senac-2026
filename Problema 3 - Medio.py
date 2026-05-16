peso = float(("Digite o seu peso corporal: "))

#constantes
capacidade_por_copo = 250
ml_por_kg = 15

#funções
 calcular_agua (peso, ml_por_kg):
    return peso * ml_por_kg

def calcular_copos (agua_total, capacidade_por_copo):
    return int(agua_total // capacidade_por_copo + (agua_total % capacidade_por_copo > 0))

#processo
agua_total = calcular_agua(peso, ml_por_kg)
copos_necessario = calcular_copos(agua_total, capacidade_por_copo)

#saída
(f"Seu peso é: {peso:.2f} kg")
print("Meta diária {agua_total:.2f} ml")
print(f"Quantidade necessária:{copos_necessario} copos de 250 ml")
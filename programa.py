faturamento_diario = [/* valores carregados */]

# Filtrando apenas dias com faturamento
dias_com_faturamento = [valor for valor in faturamento_diario if valor > 0]

# Menor valor de faturamento
menor_valor = min(dias_com_faturamento)

# Maior valor de faturamento
maior_valor = max(dias_com_faturamento)

# Cálculo da média anual, ignorando os dias sem faturamento
media_anual = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Contagem dos dias em que o faturamento foi superior à média
dias_acima_da_media = len([valor for valor in dias_com_faturamento if valor > media_anual])

print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Dias com faturamento superior à média: {dias_acima_da_media}")

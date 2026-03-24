import pandas as pd

caixa_inicial = 5000.00

dados_transacoes = [
    {"data": "2025-10-05", "tipo": "Receita", "categoria": "Mensalidade", "descricao": "Mensalidades - Lote 1", "valor": 3500.00},
    {"data": "2025-10-10", "tipo": "Despesa", "categoria": "Custo Fixo", "descricao": "Aluguel do estúdio", "valor": -2000.00},
    {"data": "2025-11-12", "tipo": "Despesa", "categoria": "Figurino", "descricao": "Materiais figurino Boneco de Neve", "valor": -450.00},
    {"data": "2025-11-18", "tipo": "Despesa", "categoria": "Figurino", "descricao": "Costureira figurino Grinch", "valor": -600.00},
    {"data": "2025-12-05", "tipo": "Receita", "categoria": "Evento", "descricao": "Ingressos Festival de Fim de Ano", "valor": 6500.00},
    {"data": "2025-12-15", "tipo": "Despesa", "categoria": "Repasse", "descricao": "Repasse professores convidados", "valor": -1500.00},
    {"data": "2026-01-10", "tipo": "Despesa", "categoria": "Custo Fixo", "descricao": "Aluguel do estúdio", "valor": -2000.00},
    {"data": "2026-01-15", "tipo": "Receita", "categoria": "Matrícula", "descricao": "Novas matrículas - Turmas de Férias", "valor": 1200.00},
    {"data": "2026-02-10", "tipo": "Despesa", "categoria": "Manutenção", "descricao": "Manutenção dos espelhos", "valor": -800.00},
    {"data": "2026-02-28", "tipo": "Despesa", "categoria": "Cancelamento", "descricao": "Estorno de matrícula", "valor": -150.00},
    {"data": "2026-03-05", "tipo": "Receita", "categoria": "Mensalidade", "descricao": "Mensalidades - Lote 1", "valor": 3200.00},
    {"data": "2026-03-20", "tipo": "Despesa", "categoria": "Marketing", "descricao": "Anúncios redes sociais", "valor": -300.00}
]

def carregar_dados():
    df = pd.DataFrame(dados_transacoes)
    df['data'] = pd.to_datetime(df['data'])
    return df
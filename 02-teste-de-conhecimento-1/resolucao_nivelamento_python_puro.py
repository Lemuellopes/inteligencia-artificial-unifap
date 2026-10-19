"""
Teste de Nivelamento - Inteligência Artificial
Centro Universitário Paraíso (UniFAP) - 2026.2
Aluno: Lemuel Lopes Sousa

Resolução das questões práticas (1 a 6) em Python puro: sem Pandas, sem NumPy.
Apenas o módulo `math` é utilizado, como permitido no enunciado.

Execute com:  python resolucao_nivelamento_python_puro.py
"""

import math


# ---------------------------------------------------------------------------
# Dados de exemplo
# ---------------------------------------------------------------------------

NOTAS = [
    {"id": 1, "nome": "Ana", "nota": 8.5, "horas_estudo": 6.0, "turno": "manhã"},
    {"id": 2, "nome": "Bruno", "nota": None, "horas_estudo": 3.5, "turno": "noite"},
    {"id": 3, "nome": "Carla", "nota": 9.0, "horas_estudo": 7.5, "turno": "manhã"},
    {"id": 4, "nome": "Diego", "nota": 6.0, "horas_estudo": 2.0, "turno": "noite"},
    {"id": 5, "nome": "Elisa", "nota": None, "horas_estudo": 5.0, "turno": "tarde"},
    {"id": 6, "nome": "Felipe", "nota": 7.5, "horas_estudo": 4.0, "turno": "tarde"},
]

PRESENCAS = [
    {"id": 1, "presenca": 92.0},
    {"id": 2, "presenca": 70.0},
    {"id": 3, "presenca": 75.0},
    {"id": 4, "presenca": 88.5},
    {"id": 6, "presenca": 60.0},
    {"id": 7, "presenca": 100.0},  # não existe em NOTAS: some no inner join
]


# ---------------------------------------------------------------------------
# Questão 1 - Inner join manual + filtro de presença >= 75
# ---------------------------------------------------------------------------

def questao_1_manipular_dados(notas, presencas, chave="id", campo_presenca="presenca", minimo=75.0):
    """Junta as duas listas pela `chave` (inner join) e mantém só quem tem presença >= minimo.

    1. Monta um dicionário {chave: registro_de_presenca} para buscar em O(1).
    2. Percorre as notas; se a chave existir nas presenças, une os dois dicionários.
    3. Registros que existem em apenas uma das listas ficam de fora (inner join).
    """
    presenca_por_chave = {}
    for registro in presencas:
        presenca_por_chave[registro[chave]] = registro

    resultado = []
    for aluno in notas:
        registro_presenca = presenca_por_chave.get(aluno[chave])
        if registro_presenca is None:
            continue  # sem correspondência: fora do inner join
        if registro_presenca[campo_presenca] >= minimo:
            unido = dict(aluno)
            unido.update(registro_presenca)
            resultado.append(unido)
    return resultado


# ---------------------------------------------------------------------------
# Questão 2 - Média aritmética e desvio padrão amostral
# ---------------------------------------------------------------------------

def questao_2_estatistica(dados, campo="horas_estudo"):
    """Retorna (media, desvio_padrao_amostral) do `campo`.

    média  = soma(x) / n
    desvio = raiz( soma((x - média)^2) / (n - 1) )   <- n - 1: correção de Bessel (amostral)
    """
    valores = [registro[campo] for registro in dados if registro[campo] is not None]
    n = len(valores)
    if n == 0:
        return None, None

    soma = 0.0
    for valor in valores:
        soma += valor
    media = soma / n

    if n < 2:
        return media, 0.0

    soma_quadrados = 0.0
    for valor in valores:
        soma_quadrados += (valor - media) ** 2
    desvio = math.sqrt(soma_quadrados / (n - 1))
    return media, desvio


# ---------------------------------------------------------------------------
# Questão 3 - Divisão treino/teste com slicing
# ---------------------------------------------------------------------------

def questao_3_divisao_manual(dados, proporcao_treino=0.8):
    """Divide a lista em treino e teste usando slicing.

    O ponto de corte é int(len * proporção): os primeiros elementos vão para o treino
    e o restante para o teste. A lista original não é alterada.
    """
    corte = int(len(dados) * proporcao_treino)
    treino = dados[:corte]
    teste = dados[corte:]
    return treino, teste


# ---------------------------------------------------------------------------
# Questão 4 - Substituir notas ausentes (None) pela média das válidas
# ---------------------------------------------------------------------------

def questao_4_dados_nulos(dados, campo="nota"):
    """Substitui `None` no `campo` pela média aritmética dos valores válidos.

    Primeiro calcula a média só com os valores presentes; depois preenche os ausentes.
    Trabalha sobre cópias para não modificar a lista original.
    """
    soma = 0.0
    quantidade = 0
    for registro in dados:
        if registro[campo] is not None:
            soma += registro[campo]
            quantidade += 1
    media = soma / quantidade if quantidade > 0 else 0.0

    resultado = []
    for registro in dados:
        novo = dict(registro)
        if novo[campo] is None:
            novo[campo] = media
        resultado.append(novo)
    return resultado


# ---------------------------------------------------------------------------
# Questão 5 - Erro Quadrático Médio (MSE) com laço
# ---------------------------------------------------------------------------

def questao_5_calculo_erro(previsoes, reais):
    """MSE = (1/n) * soma( (real - previsto)^2 ), calculado com um laço."""
    if len(previsoes) != len(reais):
        raise ValueError("Previsões e valores reais precisam ter o mesmo tamanho.")
    if len(reais) == 0:
        return 0.0

    soma_erros = 0.0
    for previsto, real in zip(previsoes, reais):
        soma_erros += (real - previsto) ** 2
    return soma_erros / len(reais)


# ---------------------------------------------------------------------------
# Questão 6 - Média de horas de estudo por turno (agrupamento manual)
# ---------------------------------------------------------------------------

def questao_6_agrupamento(dados, campo_grupo="turno", campo_valor="horas_estudo"):
    """Agrupa com dicionários: acumula soma e contagem por turno e depois divide."""
    soma_por_grupo = {}
    contagem_por_grupo = {}
    for registro in dados:
        grupo = registro[campo_grupo]
        soma_por_grupo[grupo] = soma_por_grupo.get(grupo, 0.0) + registro[campo_valor]
        contagem_por_grupo[grupo] = contagem_por_grupo.get(grupo, 0) + 1

    medias = {}
    for grupo in soma_por_grupo:
        medias[grupo] = soma_por_grupo[grupo] / contagem_por_grupo[grupo]
    return medias


# ---------------------------------------------------------------------------
# Questões teóricas
# ---------------------------------------------------------------------------

RESPOSTA_QUESTAO_7 = "B"
# [x**2 for x in range(5) if x % 2 != 0]
# range(5) = 0, 1, 2, 3, 4 -> o filtro mantém só os ímpares: 1 e 3 -> ao quadrado: [1, 9]

RESPOSTA_QUESTAO_8 = "B"
# Inner Join: o resultado contém apenas os registros cuja chave existe nas duas estruturas.
# (Left Join mantém tudo da esquerda; Full Outer mantém tudo; Cross Join faz todas as combinações.)


# ---------------------------------------------------------------------------
# Execução e verificação
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("Questão 1 - Inner join com presença >= 75:")
    juntos = questao_1_manipular_dados(NOTAS, PRESENCAS)
    for aluno in juntos:
        print(f"  id={aluno['id']} {aluno['nome']}: presença {aluno['presenca']}%")
    assert [a["id"] for a in juntos] == [1, 3, 4]

    media, desvio = questao_2_estatistica(NOTAS)
    print(f"\nQuestão 2 - Horas de estudo: média = {media:.4f}, desvio padrão amostral = {desvio:.4f}")
    assert abs(media - 4.6667) < 1e-3 and abs(desvio - 1.9408) < 1e-3

    treino, teste = questao_3_divisao_manual(NOTAS, 0.8)
    print(f"\nQuestão 3 - Treino: {len(treino)} registros | Teste: {len(teste)} registros")
    assert len(treino) == 4 and len(teste) == 2 and treino + teste == NOTAS

    preenchidos = questao_4_dados_nulos(NOTAS)
    print("\nQuestão 4 - Notas após preencher ausentes com a média das válidas:")
    for aluno in preenchidos:
        print(f"  {aluno['nome']}: {aluno['nota']:.2f}")
    assert preenchidos[1]["nota"] == 7.75 and NOTAS[1]["nota"] is None

    mse = questao_5_calculo_erro([2.5, 0.0, 2.0, 8.0], [3.0, -0.5, 2.0, 7.0])
    print(f"\nQuestão 5 - MSE = {mse}")
    assert mse == 0.375

    medias_turno = questao_6_agrupamento(NOTAS)
    print("\nQuestão 6 - Média de horas de estudo por turno:")
    for turno, valor in medias_turno.items():
        print(f"  {turno}: {valor:.2f} h")
    assert medias_turno == {"manhã": 6.75, "noite": 2.75, "tarde": 4.5}

    print(f"\nQuestão 7 - Alternativa {RESPOSTA_QUESTAO_7}: {[x**2 for x in range(5) if x % 2 != 0]}")
    print(f"Questão 8 - Alternativa {RESPOSTA_QUESTAO_8}: Inner Join")
    print("\nTodas as verificações passaram.")

"""
Este script calcula a média de notas de alunos, verifica se foram reprovados, e
gera um relatório dos alunos reprovados.

Funções:
    calcular_media(notas) -> float
        Calcula a média de uma lista de notas.

    verificar_reprovado(media) -> bool
        Verifica se a média é inferior a 6, indicando reprovação.

    relatorio(lista_alunos) -> None
        Imprime um relatório de alunos reprovados.

Uso:
    O script processa uma lista de dicionários contendo dados dos alunos, calcula
    a média de suas notas, verifica a reprovação, e imprime o relatório dos
    reprovados.

Exemplo:
    alunos = [{"nome": "Maria", "matricula": 26, "notas": [8, 7, 5, 9], "media": [], "resultado": []},
              {"nome": "Ana", "matricula": 101, "notas": [9, 9, 8, 9], "media": [], "resultado": []}]
    for aluno in alunos:
        media_aluno = calcular_media(aluno["notas"])
        aluno["media"] = media_aluno
        resultado = verificar_reprovado(media_aluno)
        if resultado:
            aluno["resultado"] = "REPROVADO"
        else:
            aluno["resultado"] = "APROVADO"
    relatorio(alunos)
"""
def calcular_media(notas):
      """
    Calcula a média das notas fornecidas.

    Parâmetros:
    notas (list[float]): Lista de notas dos 4 bimestres de um aluno.

    Retorna:
    float: A média das notas.

    Exemplo:
    >>> calcular_media([8, 7, 5, 9])
    7.25
    """
    media = sum(notas) / len(notas)
    return media

def verificar_reprovado(media):
      """
    Verifica se a média das notas é inferior a 6, indicando reprovação.

    Parâmetros:
    media (float): A média das notas de um aluno.

    Retorna:
    bool: True se a média for menor que 6, False caso contrário.

    Exemplo:
    >>> verificar_reprovado(5.5)
    True
    >>> verificar_reprovado(7.0)
    False
    """
    reprovado = media < 6
    return reprovado


def relatorio(lista_alunos):
       """
    Imprime um relatório com detalhes dos alunos reprovados.

    Parâmetros:
    lista_alunos (list[dict]): Lista de dicionários contendo os dados dos alunos,
        cada dicionário deve conter as chaves 'nome', 'matricula', 'media', e 'resultado'.

    Retorna:
    None: Esta função não retorna nenhum valor. Ela imprime o relatório dos alunos
        reprovados na tela.

    Exemplo:
    >>> alunos = [
    ...     {"nome": "Maria", "matricula": 26, "media": 7.25, "resultado": "APROVADO"},
    ...     {"nome": "João", "matricula": 13, "media": 5.25, "resultado": "REPROVADO"}
    ... ]
    >>> relatorio(alunos)
    Aluno Reprovado: João
    Matrícula: 13
    Média Final: 5.25
    """
    for aluno in lista_alunos:
        if aluno["resultado"] == "REPROVADO":
            print(f'Aluno Reprovado: {aluno["nome"]}\nMatricula: {aluno["matricula"]}\nMédia Final: {aluno["media"]:.2f}')


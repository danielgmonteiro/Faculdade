def calcular_media(notas):
    """
    Calcula a média das notas de um aluno.
    
    Parâmetros:
    notas (list): Lista com as notas dos 4 bimestres de um aluno.
    
    Retorna:
    float: Média das notas.
    """
    return sum(notas) / len(notas)

def verificar_reprovacao(media):
    """
    Verifica se o aluno foi reprovado com base na média.
    
    Parâmetros:
    media (float): Média das notas de um aluno.
    
    Retorna:
    bool: True se a média for inferior a 6, indicando reprovação. Caso contrário, False.
    """
    return media < 6

def gerar_saida_reprovados(alunos, reprovados):
    """
    Gera a saída com os dados dos alunos reprovados.
    
    Parâmetros:
    alunos (dict): Dicionário contendo os dados dos alunos.
    reprovados (list): Lista com os números de matrícula dos alunos reprovados.
    
    Retorna:
    list: Lista de strings com a mensagem de reprovação para cada aluno reprovado.
    """
    saida = []
    for matricula in reprovados:
        aluno = alunos[matricula]
        saida.append(f'Aluno Reprovado: {aluno["nome"]} – Matrícula: {matricula} – Média Final: {aluno["media"]:.2f}')
    return saida
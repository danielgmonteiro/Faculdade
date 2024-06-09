from operacoes import  calcular_media, verificar_reprovado, relatorio

# Lista de alunos com suas notas
alunos = [{"nome": "Maria", "matricula": 26, "notas": [8, 7, 5, 9], "media": [], "resultado": []},
          {"nome": "Ana", "matricula": 101, "notas": [9, 9, 8, 9], "media": [], "resultado": []},
          {"nome": "João", "matricula": 13, "notas": [6, 5, 5, 5], "media": [], "resultado": []},
          {"nome": "Ágatha", "matricula": 37, "notas": [8, 6, 7.5, 9], "media": [], "resultado": []},
          {"nome": "Joaquim", "matricula": 72, "notas": [6, 6, 5.5, 7], "media": [], "resultado": []},
          {"nome": "Félix", "matricula": 5, "notas": [10, 8, 8, 8], "media": [], "resultado": []}]

# Processamento das médias e resultados
for aluno in alunos:
    media_aluno = calcular_media(aluno["notas"])
    aluno["media"] = media_aluno
    resultado = verificar_reprovado(media_aluno)
    if resultado == True:
        aluno["resultado"] = "REPROVADO"
    else:
        aluno["resultado"] = "APROVADO"

# Geração do relatório de alunos reprovados
relatorio(alunos)
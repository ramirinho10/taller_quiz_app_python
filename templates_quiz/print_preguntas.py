import preguntas as p
from shuffle import shuffle_alt


def print_pregunta(enunciado, alternativas):
    # Imprimir enunciado y alternativas
    ###############################################################
    print(f'{enunciado[0]} \n')
    letras = ['A', 'B', 'C', 'D']
    for letra, alternativa in zip(letras, alternativas):
        print(f'{letra}. {alternativa[0]}')
    ###############################################################


if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'], pregunta['alternativas'])
    # pregunta = p.pool_preguntas.get('avanzadas').get('pregunta-2') # Pide especificamente la pregunta 2
    # print_pregunta(pregunta.get('enunciado'), shuffle.shuffle_alt(pregunta))
    # pregunta = p.pool_preguntas['avanzadas']['pregunta_2']
    # print_pregunta(pregunta['enunciado'], shuffle_alt['pregunta'])

    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4
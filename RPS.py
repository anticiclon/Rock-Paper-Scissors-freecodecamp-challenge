# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    ideal_guess = {"P": "S", "R": "P", "S": "R"}
    if len(opponent_history) < 10:
        guess = "P"
    else:
        aux = buscador(opponent_history, 4)
        if aux == "nada":
            aux = max(set(opponent_history), key = opponent_history.count)
        guess = ideal_guess[aux]
    opponent_history.append(prev_play)
    return guess


def buscador(historial, n):
    lista = []
    ultimos = historial[-n:]
    contador = 0
    while contador != len(historial):
        for i in range(len(historial)-len(ultimos)+1):
            # print(max(range(len(historial)-len(ultimos)+1)))
            for j in range(len(ultimos)):
                if historial[i+j] != ultimos[j]:
                    break
            else:
                if i+len(ultimos)+1 < len(historial):
                    # if i+len(ultimos)+1 > len(historial):
                    #     print(i+len(ultimos)+1)
                    lista.append(historial[i+len(ultimos)+1])
                else:
                    contador = i+len(ultimos)
    if len(lista) != 0:
        resultado = max(set(lista), key = lista.count)
    else:
        resultado = "nada"
    return resultado

    
    
    





import random as r
import re
natureza = [
    "arvore", "floresta", "rio", "montanha", "mar", "cachoeira",
    "deserto", "oceano", "lago", "praia", "pedra", "vento",
    "chuva", "sol", "luz", "nuvem", "neve", "gelo", "areia",
    "fogo", "terra", "planeta", "estrela", "cometa", "espaco",
    "flora", "fauna", "paisagem", "animais", "ecosistema",
    "clima", "ambiente", "savana", "selva", "campo", "lagarto",
    "inseto", "ar", "vida", "bioma", "regiao", "habitat", "musgo",
    "folha", "galho", "fruto", "raiz", "luz"
]
tecnologia = [
    "computador", "servidor", "rede", "internet", "nuvem", "processador", "memoria", "banco", "dados", "disco",
    "programacao", "software", "hardware", "codigo", "linguagem", "inteligencia", "maquina", "interface", "sistema", "firewall",
    "virus", "malware", "seguranca", "criptografia", "algoritmo", "rede", "neural", "autoaprendizado", "blockchain", "token",
    "bitcoin", "criptomoeda", "virtualizacao", "navegador", "html", "css", "javascript", "python", "java", "ciberseguranca",
    "engenharia", "circuito", "robotica", "sensor", "drone", "conexao", "wifi", "bluetooth", "ciberataque", "backup",
    "servidor", "armazenamento", "inteligencia", "analise", "processo", "computacao", "digital", "imagem", "processamento", "video",
    "streaming", "codificacao", "linguagem", "dados", "big", "internet", "cabo", "fibra", "satellite", "modem",
    "banda", "sinal", "frequencia", "transmissor", "receptor", "antena", "digitalizacao", "pixel", "resolucao", "grafico",
    "modelo", "design", "inovacao", "inteligente", "confiabilidade", "desempenho", "confianca", "chatbot", "assitente", "virtual",
    "biometria", "hardware", "software", "monitor", "teclado", "mouse", "tela", "celular", "rede", "tablet"
]
alimentos = [
    "arroz", "feijao", "batata", "tomate", "alface", "cebola", "alho", "cenoura", "beterraba", "pimentao",
    "maca", "banana", "uva", "pera", "manga", "laranja", "morango", "abacaxi", "abacate", "kiwi",
    "melancia", "melao", "caju", "cereja", "figo", "caqui", "mamao", "pinha", "amora", "framboesa",
    "limao", "lima", "mandioca", "inhame", "carne", "frango", "peixe", "ovo", "leite", "queijo",
    "iogurte", "manteiga", "nata", "creme", "margarina", "azeite", "oleo", "mel", "pao", "massa",
    "macarrao", "biscoito", "bolo", "chocolate", "sorvete", "bala", "pipoca", "cafe", "cha", "refrigerante",
    "suco", "agua", "vinho", "cerveja", "vodka", "cachaca", "gin", "rum", "champanhe", "camarao",
    "siri", "lagosta", "lula", "ostra", "marisco", "bacalhau", "atum", "sardinha", "anchova", "caranguejo",
    "churrasco", "costela", "picanha", "hamburguer", "pizza", "lasanha", "salada", "sopa", "caldo", "frango",
    "risoto", "omelete", "torta", "creme", "pure", "musse", "pate", "doce", "bife", "farofa"
]
esportes = [
    "futebol", "basquete", "volei", "tenis", "natacao", "atletismo", "ciclismo", "surf", "skate", "boxe",
    "judo", "karate", "capoeira", "kungfu", "muaythai", "jiujitsu", "handebol", "rugby", "golfe", "baseball",
    "beisebol", "esgrima", "ginastica", "trampolim", "hockey", "remo", "vela", "motocross", "automobilismo", "aviacao",
    "snowboard", "esqui", "patinacao", "tobogan", "mergulho", "kitesurf", "arco", "canoagem", "bocha", "cricket",
    "polo", "futsal", "kickboxing", "corrida", "escalada", "paraquedismo", "luta", "bike", "levantamento", "caminhada",
    "maratona", "triatlo", "pentatlo", "dardos", "pesca", "snooker", "bilhar", "poker", "tiro",
    "corrida", "aventura", "ciclismo", "urbano", "turismo", "rafting", "bungee", "salto", "ginastica", "olimpico",
    "taekwondo", "vitoria", "derrota", "jogador", "tecnico", "craque", "arbitro", "juiz", "luta", "campeonato",
    "maratona", "circuito", "velocidade", "revezamento", "concentracao", "saude", "educacao", "foco", "dedicacao", "resistencia",
    "triunfo", "titulos", "ouro", "prata", "bronze", "recorde", "vencer", "comemorar", "treinamento", "estrategia"
]
emocoes = [
    "alegria", "tristeza", "raiva", "medo", "surpresa", "nojo", "esperanca", "angustia", "ansiedade", "amor",
    "odio", "frustracao", "satisfacao", "decepcao", "contentamento", "orgulho", "vergonha", "culpa", "compaixao", "simpatia",
    "empatia", "solidao", "felicidade", "gratidao", "preocupacao", "tranquilidade", "paz", "alivio", "nervosismo", "ciumes",
    "pena", "admiracao", "fascinacao", "surpresa", "choque", "ira", "zangado", "curiosidade", "saudade", "timidez",
    "introspecao", "culpa" ]
animais = [
    "cachorro", "gato", "cavalo", "vaca", "boi", "leao", "tigre", 
    "onca", "elefante", "lobo", "coelho", "raposa", "porco", "urso", 
    "morcego", "veado", "camelo", "galinha", "galo", 
    "pato", "papagaio", "coruja", "pombo", "arara", "aguia", "falcao", 
    "tartaruga", "crocodilo", "jacare", "cobra", "sapo", "rato", 
    "golfinho", "baleia", "tubarao", "polvo",
    "caranguejo", "lagosta", "camarao", "abelha", "formiga", "aranha",
    "borboleta", "mosquito", "besouro", "cavalo-marinho"
]


temas = [natureza, tecnologia, alimentos, emocoes, esportes, animais]
chances, vitorias, derrotas = 7,0,0
# Definição Inicial:
tema = r.choice(temas)
palavraEscolhida = r.choice(tema)
tamanhoPalavra  =  list("_" * len(palavraEscolhida))
tentativas = []
if palavraEscolhida in natureza:
    temaSTR = 'Natureza'
elif palavraEscolhida in tecnologia:
    temaSTR = 'Tecnologia'
elif palavraEscolhida in alimentos:
    temaSTR = 'Alimentos'
elif palavraEscolhida in emocoes:
    temaSTR = 'Emocões'
elif palavraEscolhida in esportes:
    temaSTR = 'Esportes'
elif palavraEscolhida in animais:
    temaSTR = 'Animais'
# Loop Principal:
while True:
    # Jogo inicia aqui:
    print(f'O tema é: {temaSTR}')
    print(f'Quantidade de letras: {len(palavraEscolhida)}')
    print(f'Chances: {chances}')
    print(f'Vitórias: {vitorias}')
    print(f'Derrotas: {derrotas}')
    tamanhoPalavra = ''.join(tamanhoPalavra)
    print(tamanhoPalavra)
    tamanhoPalavra = list(tamanhoPalavra)
    print(f'Tentativas: {', '.join(tentativas)}')
    letraDigitada = input().lower()
    # Verifica se a letra é válida:
    if re.match("^[a-zA-Z]+$", letraDigitada):
        # Agora é os paranaué doido lá:
        if 1 == len(letraDigitada):
            if letraDigitada not in tentativas:
                tentativas.append(letraDigitada)
            else:
                print('Você já tentou essa letra')
                if letraDigitada not in palavraEscolhida:
                    chances += 1
            if letraDigitada in palavraEscolhida:
                letras = [i for i, letra in enumerate(palavraEscolhida) if letra == letraDigitada]
                for letra in letras:
                    tamanhoPalavra[letra] = letraDigitada
            else:
                chances -= 1
                # Verifica se o úsuario venceu:
            if '_' not in tamanhoPalavra:
                print(palavraEscolhida)
                print(f'Vitória, a palavra era {palavraEscolhida}')
                tema = r.choice(temas)
                palavraEscolhida = r.choice(tema)
                tamanhoPalavra  =  list("_" * len(palavraEscolhida))
                tentativas = []
                if palavraEscolhida in natureza:
                    temaSTR = 'natureza'.capitalize()
                elif palavraEscolhida in tecnologia:
                    temaSTR = 'tecnologia'.capitalize()
                elif palavraEscolhida in alimentos:
                    temaSTR = 'alimentos'.capitalize()
                elif palavraEscolhida in emocoes:
                    temaSTR = 'emocões'.capitalize()
                elif palavraEscolhida in esportes:
                    temaSTR = 'esportes'.capitalize()
                elif palavraEscolhida in animais:
                    temaSTR = 'Animais'
                tamanhoPalavra  =  list("_" * len(palavraEscolhida))
                chances = 7
                tentativas = []
                vitorias+=1
            elif chances == 0:
                print(palavraEscolhida)
                print(f'Derrota, a palavra era {palavraEscolhida}')
                tema = r.choice(temas)
                palavraEscolhida = r.choice(tema)
                tamanhoPalavra  =  list("_" * len(palavraEscolhida))
                tentativas = []
                if palavraEscolhida in natureza:
                    temaSTR = 'natureza'.capitalize()
                elif palavraEscolhida in tecnologia:
                    temaSTR = 'tecnologia'.capitalize()
                elif palavraEscolhida in alimentos:
                    temaSTR = 'alimentos'.capitalize()
                elif palavraEscolhida in emocoes:
                    temaSTR = 'emocões'.capitalize()
                elif palavraEscolhida in esportes:
                    temaSTR = 'esportes'.capitalize()
                elif palavraEscolhida in animais:
                    temaSTR = 'Animais'

                derrotas+=1
        elif len(letraDigitada) == 0:
            print('Você não digitou nada')
        else:
            print('Não se pode tentar mais de uma letra de uma só vez')
    else:
        print('Caractere inválido: (a-z apenas)!!!!!!!!!!!!!!!!!!!!!!!!!')    
class Jogo:
    def __init__(self, nome, horario, ligas):
        self.nome = nome
        self.horario = horario
        self.ligas = ligas

def carregar_jogos():
    # Aqui seria o scraping ou API real
    return [
        Jogo("Flamengo vs Palmeiras", "20:00", "Serie A"),
        Jogo("Barcelona vs Real Madrid", "22:00", "La Liga"),
    ]

def gerar_mensagem(jogo):
    return f"🧠 Análise: {jogo.nome}\nSugestão: +1.5 golos\nOdd: 1.70\nConfiança: 82%"
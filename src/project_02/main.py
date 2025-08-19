import requests
from datetime import datetime

def checa_status_github():
    resposta = requests.get("https://api.github.com")
    return {
        "codigo_status": resposta.status_code,
        "tempo_resposta_ms": resposta.elapsed.total_seconds() * 1000,
        "verificado_em": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == "__main__":
    github_info = checa_status_github()
    print(f"[{github_info['verificado_em']}] STATUS_PROJETO_API | Código: {github_info['codigo_status']} - Tempo: {github_info['tempo_resposta_ms']:.2f} ms")

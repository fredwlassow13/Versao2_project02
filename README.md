# Project 02

Projeto simples em **Python** que consulta a API do GitHub e retorna o status.  
Ideal para testar conectividade de uma API externa e monitorar tempos de resposta.

## 🚀 Funcionalidade
- Consulta o status da API do GitHub e retorna:
  - status_code: codigo HTTP da resposta
  - response_time_ms: tempo de resposta em milissegundos
  - checked_at: timestamp do momento da verificação

- Tratamento de falhas de rede, retornando status_code='error' quando não é possivel conectar.
- suporte a parsing de respostas padronizadas via modulo parsers.py

## 📂 Estrutura do Projeto
````
|---- src/
| |---- project_02/
| |---- __init__.py
| | |---- main.py
| | |---- cache.py
| | |---- github_client.py
| | |---- parsers.py
| | |---- latency_checker.py
| | |---- __init__.py
|---- tests/
| |---- test_main.py
| |---- cache.py
| |---- github_client.py
| |---- parsers.py
| |---- latency_checker.py
| |---- __init__.py
|---- .gitignore
|---- requirements.txt
````
## Instalação
````
git clone <https://github.com/fredwlassow13/Versao2_project02.git>
cd <Versao2_project02>
pip install -r requirements.txt
````
## 📌 Testes
- Testes automatizados com pytest cobrindo cache, parsing e requests mockados.
````
PYTHONPATH=src pytest -v
````

## ⚙️ Alterações
- Apenas o **status do GitHub** foi modificado.  
- Nova funcionalidade: captura o **tempo de resposta** em milissegundos.  
- Adicionada a chave **`checked_at`**, registrando o horário exato em que a API foi checada.

## ✅ Bugs Arrumados
- Corrigida a URL que tinha `"/)` no final (sintaxe inválida).  
- Corrigido `strfime` → agora está `strftime`.  
- Corrigido `if name == "main":` → agora está `if __name__ == "__main__":`.

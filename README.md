# Project 02

Projeto simples em **Python** que consulta a API do GitHub e retorna o status.  
Ideal para testar conectividade de uma API externa.

## 🚀 Funcionalidade
- Consulta o endpoint oficial da API do GitHub.  
- Exibe o código de status da resposta (`200` = OK, `503` = indisponível).  
- Pode ser executado localmente ou integrado em pipelines de **CI/CD**.  

## 📂 Estrutura do Projeto
````
|---- src/
| |---- project_02/
| |---- main.py
|---- tests/
| |---- test_main.py
|---- .gitignore
|---- requirements.txt
````

## ⚙️ Alterações
- Somente o status do GitHub
- **Nova funcionalidade:** Pega a resposta em ms de tempo
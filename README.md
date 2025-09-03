# Project 02
Projeto simples em Python que consulta a API do GitHub e retorna o status.  
Ideal para testar conectividade de uma API externa.

## 🚀 Funcionalidade
- Consulta o endpoint oficial da API do GitHub.  
- Exibe o código de status da resposta (200 = OK, 503 = indisponível).  
- Pode ser executado localmente ou integrado em pipelines de CI/CD.

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
- Apenas o **status do GitHub** foi modificado.  
- Nova funcionalidade: captura o **tempo de resposta** em milissegundos.  
- Adicionada a chave **`checked_at`**, registrando o horário exato em que a API foi checada.

## ✅ Bugs Arrumados
- Corrigida a URL que tinha `"/)` no final (sintaxe inválida).  
- Corrigido `strfime` → agora está `strftime`.  
- Corrigido `if name == "main":` → agora está `if __name__ == "__main__":`.

# Ballon Controll 🎈

## **🛠 Projeto em contrução!!**

**Ballon Controll** é um sistema simples para gerenciar a entrega de balões em maratonas de programação.  
O objetivo é que cada vez que uma equipe resolve um problema, um balão correspondente seja adicionado e possa ser confirmado pelos entregadores.

---

## 📝 Funcionalidades

- Criar equipes e cadastrar os balões a serem entregues.  
- Lista de balões pendentes e entregues em tempo real.  
- Painel separado para **Emissor** e **Entregadores**.  
- Atualização instantânea via WebSocket (Socket.IO).  
- Layout bonito e responsivo usando **Bootstrap** + CSS customizado.  

---

## 🛠 Tecnologias usadas

- Python 3  
- Flask  
- Socket.IO  
- Bootstrap 5 via CDN  
- CSS customizado  

---

## 🚀 Como rodar o projeto

1. Clone este repositório:
```bash
git clone https://github.com/SEU_USUARIO/ballon_controll.git
cd ballon_controll
```
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
```
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```
3. Instale as dependências:
```
pip install -r requirements.txt
```
4. Rode o servidor Flask:
```
python app.py
```
5. Acesse o painel no navegador:
```
Emissor: http://127.0.0.1:5000/
Entregador: http://127.0.0.1:5000/delivery
```
Observações:
  - Este projeto foi desenvolvido para uso local, sem necessidade de banco de dados.
  - Atualizações em tempo real são feitas usando Socket.IO, então todos os painéis conectados refletem as mudanças instantaneamente.

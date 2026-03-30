# Lioris

Lioris é uma plataforma web de compartilhamento e descoberta de imagens inspirada no Pinterest.
O projeto permite que usuários publiquem imagens, organizem ideias e explorem conteúdos de outros usuários.

## Sobre o projeto

O objetivo do Lioris é criar um ambiente simples e intuitivo para compartilhar inspirações visuais.
O projeto foi desenvolvido como prática de desenvolvimento web utilizando Python e Flask.

## Funcionalidades

* Upload de imagens
* Visualização de posts em formato de feed
* Sistema de usuários
* Organização de conteúdo visual
* Interface simples e responsiva

## Tecnologias utilizadas

* Python
* Flask
* Flask-SQLAlchemy
* SQLite
* HTML5
* CSS3

## Como rodar o projeto

1. Clone o repositório

git clone https://github.com/itscavalari-sudo/Lioris

2. Entre na pasta do projeto

Lioris

3. Crie um ambiente virtual

python -m venv venv

4. Ative o ambiente virtual

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

5. Instale as dependências

pip install -r requirements.txt

6. Rode a aplicação

python main.py

7. Abra no navegador

http://127.0.0.1:5000

## Estrutura do projeto

lioris/
│
├── models.py            # Modelos do banco de dados
├── routes.py            # Rotas
├── forms.py             # Arquivo de forms
├── templates/           # Arquivos HTML  
├── static/              
      └── css            # Arquivo CSS
      └── fotos_posts    # Imagens
      └── fotos_site     # Imagens do site
      
main.py                  # Aplicação principal Flask
criarbanco.py            # Criar o banco de dados

## Melhorias futuras

* Sistema de curtidas
* Sistema de comentários
* Pesquisa de imagens
* Sistema de seguidores
* Upload otimizado de imagens
* Deploy online

## Licença

Este projeto foi criado para fins educacionais.

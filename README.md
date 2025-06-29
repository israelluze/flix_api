# flix-api

API para gerenciamento de filmes, gêneros, atores, reviews e autenticação, construída com Django e Django REST Framework.

## Funcionalidades

- Cadastro, listagem, atualização e remoção de filmes
- Gerenciamento de gêneros e atores
- Sistema de reviews para filmes
- Autenticação de usuários (JWT)
- Permissões e grupos de usuários

## Estrutura do Projeto

```
.
├── actors/
├── app/
├── authenticate/
├── genres/
├── movies/
├── reviews/
├── db.sqlite3
├── manage.py
├── requirements.txt
```

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/flix-api.git
   cd flix-api
   ```

2. Crie um ambiente virtual e ative:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4. Aplique as migrações:
   ```sh
   python manage.py migrate
   ```

5. Crie um superusuário:
   ```sh
   python manage.py createsuperuser
   ```

6. Rode o servidor:
   ```sh
   python manage.py runserver
   ```

## Endpoints Principais

- `/api/movies/` - CRUD de filmes
- `/api/genres/` - CRUD de gêneros
- `/api/actors/` - CRUD de atores
- `/api/reviews/` - CRUD de reviews
- `/api/auth/` - Autenticação (login, refresh de token)

## Autenticação

A autenticação é feita via JWT. Utilize o endpoint de login para obter o token e envie no header das requisições autenticadas:

```
Authorization: Bearer <seu_token>
```

## Requisitos

- Python 3.10+
- Django 5.2.2
- Django REST Framework 3.16.0
- djangorestframework-simplejwt 5.5.0

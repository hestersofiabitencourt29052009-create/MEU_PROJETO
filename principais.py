As arquiteturas :
 
Frontend
  ↓
Flask (Interface Web)
  ↓
FastAPI (API REST)
  ↓
Services
  ↓
Repositories
  ↓
PostgreSQL
 
Base da estrutura do projeto
 
project/
│
├── app/
│   ├── api/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── repositories/
│   ├── auth/
│   ├── core/
│   └── templates/
│
├── tests/
│
├── migrations/
│
├── docker/
│
├── main.py
│
├── requirements.txt
│
└── .env
 
Base usada e estruturada
 
configurar PostgreSQL
Instale:
pip install psycopg2-binary
código usado para o terminal ter base de como o código deve ser usado
Criar banco:
CREATE DATABASE crud_system;
Configurar SQLAlchemy
Ultilizados o uso de if como principal função de variável como por exemplo em descontos ou em lista principalmente
 
Criar conexão:
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
DATABASE_URL = "postgresql://postgres:123456@localhost/crud_system"
 
engine = create_engine(DATABASE_URL)
 
SessionLocal = sessionmaker(
   autocommit=False,
   autoflush=False,
   bind=engine
)
 
Criar modelo de usuário
Exemplo:
from sqlalchemy import Column, Integer, String, Boolean
 
class User(Base):
   __tablename__ = "users"
 
   id = Column(Integer, primary_key=True)
   name = Column(String)
   email = Column(String, unique=True)
   password = Column(String)
 
   is_admin = Column(Boolean, default=False)
Observe a regra de negócio:
 Email único
unique=True
— Implementar autenticação JWT
Instalar:
pip install python-jose passlib[bcrypt] 
Hash de senha:
pwd_context.hash(password)
Login:
POST /login
Retorna:
{
 "access_token": "jwt_token",
 "token_type": "bearer"
}
Requisito atendido:
 JWT com expiração
Passo 6 — Criar CRUD
Por exemplo, uma entidade chamada Produto.
Modelo:
class Product(Base):
   __tablename__ = "products"

   id = Column(Integer, primary_key=True)
   name = Column(String)
   price = Column(Float)
Endpoints:
POST    /products
GET     /products
GET     /products/{id}
PUT     /products/{id}
DELETE  /products/{id}
Atende:
 RF03 CRUD
 
Passo 7 — Implementar permissões
Somente administradores podem excluir.
Exemplo:
if not current_user.is_admin:
   raise HTTPException(
       status_code=403,
       detail="Acesso negado"
   )
Atende:
 RF05 Controle de Permissões
 
Passo 8 — Busca e paginação
Exemplo:
GET /products?page=1&limit=10
Código:
query.offset((page-1)*limit).limit(limit)
Busca:
GET /products?search=notebook
Atende:
 RF04 Busca e Paginação
 
Passo 9 — Documentação automática
Uma vantagem do FastAPI.
Ao executar:
uvicorn main:app --reload
Acesse:
http://localhost:8000/docs
Swagger será gerado automaticamente.
Atende:
 RF07
 
Passo 10 — Logs
Instalar:
pip install loguru
Exemplo:
from loguru import logger

logger.info("Usuário logado")
logger.error("Erro ao cadastrar")
Atende:
 RF08
 RNF07 Observabilidade
 
Passo 11 — Testes
Instalar:
pip install pytest
Exemplo:
def test_login():
   response = client.post("/login")

   assert response.status_code == 200
Atende:
Testes automatizados
 
Passo 12 — Docker
Criar:
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
Executar:
docker build -t crud-system .

docker run -p 8000:8000 crud-system
 
Passo 13 — Deploy
Opções citadas no documento:
• AWS
• Render
• Railway
Fluxo profissional:
GitHub
  ↓
CI/CD
  ↓
AWS
 
O que normalmente será avaliado
Se esse projeto for para portfólio ou entrevista, o recrutador geralmente verifica:
Item

Peso

Arquitetura em camadas

⭐⭐⭐⭐⭐

JWT

⭐⭐⭐⭐⭐

SQLAlchemy

⭐⭐⭐⭐⭐

PostgreSQL

⭐⭐⭐⭐⭐

FastAPI

⭐⭐⭐⭐⭐

Docker

⭐⭐⭐⭐

Testes

⭐⭐⭐⭐

AWS

⭐⭐⭐⭐

Logs

⭐⭐⭐

Clean Architecture

⭐⭐⭐⭐⭐

Ordem ideal de desenvolvimento
1. Configurar projeto
2. PostgreSQL
3. SQLAlchemy
4. Model User
5. Cadastro
6. Login JWT
7. CRUD Produto
8. Permissões Admin
9. Busca e Paginação
10. Testes
11. Docker
12. Deploy AWS
Seguindo essa sequência,  conseguimos entregar exatamente o que o documento pede e ainda montar um projeto bastante alinhado com vagas de Backend Python Júnior/Pleno.
Parte superior do formulário

Baseado no pensamento
Parte inferior do formulário

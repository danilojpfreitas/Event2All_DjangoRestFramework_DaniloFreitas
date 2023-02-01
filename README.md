# Event2All_DjangoRestFramework_DaniloFreitas

---

API em desenvolvimento com Django Rest Framework, os endpoints do projeto Event2All que foram realizados anteriormente com TypeOrm estão sendo reconstruídos. 

Os endpoints podem ser usados localmente (ambiente de desenvolviemnto), cujo a sua documentação é gerada pelo Insomnia Button.

<p align="center">
<a href="https://insomnia.rest/run/?label=API%20Event2All%20-%20Django%20Rest%20Framework%20-%20Danilo%20Freitas&uri=https%3A%2F%2Fraw.githubusercontent.com%2Fdanilojpfreitas%2FEvent2All_DjangoRestFramework_DaniloFreitas%2Fmain%2FInsomnia%2FInsomnia_2023-02-01.json" target="_blank"><img src="https://insomnia.rest/images/run.svg" alt="Run in Insomnia"></a>
</p>

---
## Como usar a API:
  - Após clonar o repositório:
      1) Criar o ambiente virtual: `python3 -m venv ./venv`
      2) Ativar o ambiente virtual: `source venv/bin/activate`
      3) Baixar as dependências: `pip install -r requirements.txt`
      4) Realizar as migrations: `python manage.py makemigrations` + `python manage.py migrate`
      5) Popular o User do Banco de Dados: `python seeds.py` (Opcional)
  - Determinar o usuário para gerar o token pela rota `/auth`, pelo comando: `python manage.py createsuperuser` 
  - Comando para executar o banco de dados: `python manage.py runserver`
  - Após rodar a API, por meio da rota `auth/` gerar o token (access) pelo usuário criado 
  
---
## :memo: Funcionalidades criadas até o momento: 

1. Auth (JWT);
2. User (Completo);
3. Event (Completo);
4. Quotation (Completo);
5. Guest (Completo);
6. ToDoList (Completo).

---


## :page_with_curl: Documentação

1) Insomnia

  A documentação da API encontra-se em `/docs/Doc_Insomnia`.
  Todas as informações da documentação da API podem ser vistas ao clicar em `Run in Insomnia` neste README.   

2) Swagger

Após rodar localmente a API é possível acessar a documentação pelo Swagger, pela seguitne rota: `swagger/`


Obs.: A API necessita de alguns ajustes, futuramente será realizado o deploy (Fev/23)


---


## :keyboard: Desenvolvedor participante
 
[<sub>Danilo Freitas</sub>](https://github.com/danilojpfreitas)  

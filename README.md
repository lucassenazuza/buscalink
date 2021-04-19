
![logobuscalinks](https://user-images.githubusercontent.com/4533305/115165600-f3b84880-a084-11eb-9309-1b206ad5c4d0.png)


# BuscaLinks

O Site **Buscalinks** permite que links sejam buscados pelo engine do google, através
da biblioteca [Google Search](https://pypi.org/project/googlesearch-python/) . O Sistema foi desenvolvido usando o Framework [Flask](https://flask.palletsprojects.com/en/1.1.x/)  Foi usado um banco
[SQLite](https://www.sqlite.org/index.html) para armazenar os dados. O deploy da aplicação foi feito pelo [Heroku](https://www.heroku.com)

Link Aplicação: https://buscalinks.herokuapp.com/



# Estrutura de Arquivos
   O Projeto Foi todo desenvolvido usando o Padrão de Projeto MVC( Model View Controller). No diretório **Models**, temos as entidades da aplicação; Na pasta templates temos nossa **View**, constiuindo da parte visual da aplicação. Na pasta controllers temos o **Controller** da aplicação, onde as requisições do *front-end* são direcionadas e tratadas. Na pasta services, temos algumas implementações da lógica das regras de negócio.

├── app.py <br>
├── banco.db <br>
├── config.py <br>
├── controllers <br>
├── models <br>
├── Procfile <br>
├── __pycache__ <br>
├── requirements.txt <br>
├── services <br>
├── static <br>
├── templates <br>
└── venv <br>

# Funcionamento e Teste do Sistema
A Seguir serão mostradas as telas do Sistema, e seu funcionamento. O Sistema pode ser acessado pelo link: https://buscalinks.herokuapp.com/

- No página principal, é possível realizar as buscas por links com palavras chaves. Para realizar a busca, o usuário deve digitar algum nome e clicar ***Buscar***. Caso o usuário clique ***Buscar***  com o campo em branco a validação do formulário vão indicar que o campos precisa ser preenchido.

![image](https://user-images.githubusercontent.com/4533305/115165867-6d9d0180-a086-11eb-92c4-6501ac3d852f.png)
 - Feito a busca, a aplicação irá retornar até 10 links relacionados a palavra-chave digitada. Abaixo, temos que o usuário digitou "Busca Teste" na barra de pesquisa, e aplicação retornou links relacionados. Todos Esses links são salvos no banco de dados, estando atrelado a palavra chave de pesquisa. Nesse ponto o usuário pode voltar para página principal, ou listar todas palavras chaves já buscadas(*Listar Todos*), ou acessa a estatística de palavras mais buscadas, além da quantidade de pesquisas já feitas e a quantidade de links salvos.

![image](https://user-images.githubusercontent.com/4533305/115165883-84dbef00-a086-11eb-88a8-3767f64b4f5f.png)
- Acessando a o link *Listar Todos*, a aplicação lista todos os links já buscados, e as palavras chaves associadas. O usuário pode também excluir os respectivos links, clicando o botão *Excluir*. Ao clicar no mesmo, o registro do Link é removido do banco de dados.

![image](https://user-images.githubusercontent.com/4533305/115165895-97562880-a086-11eb-8a84-2a1f1ec9200e.png)
- Acessando a o link *Estatísticas*, a aplicação nos mostra quantas palavras-chave já foram procuradas, quantos links estão salvos no Banco de Dados, e qual foi o termo mais procurado. Na busca do termo mais procurado, a aplicação não diferencia maísculo de minúsculo.

![image](https://user-images.githubusercontent.com/4533305/115165902-a2a95400-a086-11eb-952e-e2d4524f0b66.png)

# Banco de Dados

Para a aplicação BuscaLinks, foi usado um banco de dados relacional **SQLite**. O Banco de dados possui duas tabelas, uma para todos elementos que são buscados(**element**) e outra de todos links salvos(**link**).  

![image](https://user-images.githubusercontent.com/4533305/115166431-7216e980-a089-11eb-835f-e5d48041c105.png)

# Deploy da Aplicação

Foi feito o deplay da aplicação no Heroku, para isso foi usado o [ Guinicorn](https://gunicorn.org/) e toda api API do Heroku para subir a aplicação.
```
web: gunicorn app:app
```


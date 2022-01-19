# Mini Projeto Django - Cadastro de Produtos
Projeto realizado aplicando melhorias e customizações no projeto Django2 do curso [Programação Web com Python e Django Framework: Essencial](https://www.udemy.com/course/programacao-web-com-django-framework-do-basico-ao-avancado/) realizado pela Geek University.

Propósito do Projeto: apenas aplicar conhecimetos adquiridos durante o curso para manipulação dos arquivos base do Django, e criando uma aplicação útil para divulgação de produtos.


# Publicação no Heroku
A aplicação pode ser vista online no domínio: https://django2-gustaoliv.herokuapp.com/

**Obs**: Para acessar a página de cadastro de produtos é necessário estar logado. O Heroku apaga as imagens feitas upload após alguns minutos, só as estáticas permanecem :/

## Como publicar:

1. Login:
```
    heroku login 
```

2. Verificação da versão do Python:
```
python -V
```
3. Criação de um arquivo runtime.txt com a versão do Python referente:
    
    Ex: *python-3.10.1*

4. Criação de um arquivo Procfile para configuração de execução no Heroku
    
    Conteúdo: *web: gunicorn django2.wsgi --log-file -*

5. Adicionar arquivos ao git
   
6. Criação do projeto no Heroku:
```
heroku create django2-gustaoliv --buildpack heroku/python
```
7. Enviar os arquivos para o Heroku
```
git push heroku master
```

8. Fazendo o migrate das tabelas para o heroku:
```
heroku run python manage.py migrate
```

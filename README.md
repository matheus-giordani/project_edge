# Projeto backend edge


## Objetivo do projeto
> Criar uma API para gerenciar (CRUD) um conjunto de dispositivos pertencentes a um usuário, que podem estar localizados em um local específico de sua
casa.

## Descrição do projeto
> Um usuário tem pelo menos um nome completo e e-mail, enquanto cada dispositivo tem um nome, marca, modelo. Um ou mais usuários podem gerenciar um ou
mais dispositivos.

## stacks
> Projeto utilza a liguagem python com o uso do framework web Django Rest framework e para realizar o deploy da aplicaçao foi utilzado uma instância Ec2 com uma maquina Linux e utiliza o banco postgres que está no Rds








## Modelo ER
![](https://github.com/matheus-giordani/base_image/blob/main/teste%20-%20public%20(1).png)



## Abordagem para resolução dos problemas
> O unico ponto que gostaria de comentar é sobre a relação de n pra n (muitos para muitos) entres os usuarios e os dispositivos acredito que foi o ponto que gera um pouco de duvida de como pensar na arquitetura e resolvi usar o conceito, de banco de dados relacional, entidade associativa entre as tabelas peaple e devices utilizando uma tabela intermediaria devices_control com as chaves primarias de ambas isso pode ser visto no modelo ER disponibilizado acima


## Instalação
> Não há necessidade de instalação nem nenhum processo para rodar a aplicação, pois o deploy foi feito no ec2

## Testes
[![Run in Insomnia}](https://insomnia.rest/images/run.svg)](https://insomnia.rest/run/?label=edge%20API&uri=https%3A%2F%2Fraw.githubusercontent.com%2Fmatheus-giordani%2Fbase_image%2F065423ae3595dd3af677c455e1141a5abdb6f0fc%2FInsomnia_2022-10-01.json)

> [Swagger](http://54.91.16.211:8000/documentation/)

>[Portal Admin](http://54.91.16.211:8000/admin/) username: admin senha: admin



> [API](http://54.91.16.211:8000/)




 








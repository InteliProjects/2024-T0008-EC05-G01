---
title: Artefato - Documentação
sidebar_position: 2
---


## Integração

&emsp;A integração entre frontend e backend é fundamental para o desenvolvimento de aplicações web modernas, eficientes e que também ofereçam uma experiência de usuário suave e intuitiva. Essa integração permite que as informações sejam consistentes e atualizadas, melhorando a performance da aplicação e facilitando a manutenção e o desenvolvimento contínuo.

&emsp;Ao analisar as atualizações que ocorreram na Sprint 5 do projeto, é possível dizer que houve tanto a integração geral do sistema e de novas rotas, quanto a implementação de novas tecnologias para a entrega final do projeto.

### Novas tecnologias

&emsp;A integração do projeto foi feita tendo em vista os conceitos mais importantes tanto do frontend quanto do backend. Estes conceitos já foram explicados nas documentações das últimas Sprints. Com isso, novas tecnologias foram implementadas no projeto, para melhorar a qualidade da solução, sendo eles o HTMX e o JavaScript

&emsp;O HTMX é uma ferramenta que se destaca na integração entre frontend e backend por sua capacidade de enriquecer páginas HTML com funcionalidades dinâmicas, e foi por conta desse motivo que ele foi implementado na solução do projeto. Ele permite atualizar partes específicas de uma página web de forma assíncrona, o que significa que é possível modificar o conteúdo da página ou parte dela sem ter que recarregar toda a página, proporcionando uma experiência de usuário mais fluida e responsiva.

&emsp;Já o JavaScript foi escolhido, pois é uma ferramenta popular para a integração entre frontend e backend, em que num estágio final de projeto foi essencial para o grupo concluir a integração das telas dentro do prazo de entrega.

### Novas rotas

&emsp;Ao dar ênfase às novas rotas na solução, é possível dizer que elas foram essenciais para a construção e o funcionamento das páginas web. Segue abaixo a documentação de novas rotas:

---

#### Rotas relacionadas ao reabastecimento do armazem

- **GET /reabastecimento**: Retorna a tela de reabastecimento do armazem
- **POST /item**: Adiciona um novo item (interação com o banco de dados)

&emsp;Exemplo de corpo de requisição para adicionar um item no armazém:

```json
{
	"nome": "Fentanyl",
	"quantidade": 123,
}
```

---

#### Rotas relacionadas ao auxiliar
- **GET /edit**: Retorna a edição de um kit na tabela de kits.
- **POST /fila**: Adiciona um novo kit à fila de kits
&emsp;Exemplo de corpo de requisição para adicionar ou atualizar um medicamento:
```json
{
    "nome": "Kit-1",
}
```
---

#### Rotas relacionadas a tela do kit
- **GET /telaKit/\{Nome}**: Retorna a tela de um kit.
- **POST /kits**: Adiciona um novo kit à tela de kits.
- **GET /kit?kit=\{Nome}**: Retorna a edição de um kit na tela de kits.

&emsp;Exemplo de corpo de requisição para adicionar ou atualizar um medicamento:
```json
{
    
    "nome": "Kit-1", "medicamentos": [{"nome": "Fentanyl", "quantidade": 3, "altura": 10, "pos": {"x": 229.84, "y": 177.75, "z": -40.0, "r": 0.0}}, {"nome": "Paracetamol", "quantidade": 0, "altura": 5.35, "pos": {"x": 15.42, "y": 264.77, "z": -40.0, "r": 0.0}}]

}
```
---

&emsp;Também é importante reforçar que as características da comunicação dos dados através das requisições HTTP existentes na solução, destacadas na anteriormente na documentação da Sprint 4, seguem com um mesmo princípio. O frontend comunica com o backend através de requisições HTTP para realizar operações CRUD, enquanto o backend fornece endpoints para essas ações, o que permite a manipulação dos dados.

&emsp;Dessa forma, é possível apresentar os principais elementos da arquitetura geral do projeto, junto com a integração frontend e backend, em que residem um sistema coeso e eficiente, o que foi crucial para o desenvolvimento desta aplicação web. Também, as novas rotas representaram novas possibilidades para a solução, o que resultou em um projeto com uma maior qualidade.

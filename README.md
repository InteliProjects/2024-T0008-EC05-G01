# Inteli - Instituto de Tecnologia e Liderança 

<p align="center">
<a href= "https://www.inteli.edu.br/"><img src="documentation\docusaurus-documentation\static\img\inteli.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width=40% height=40%></a>
</p>

<br>

# Arm

<figure>
  <figcaption style="text-align: center;"></figcaption>
  <img src="documentation\docusaurus-documentation\static\img\logo_arm.png" />
  <figcaption style="text-align: center;">Fonte: Autoria própria.</figcaption>
</figure>

## 🟣 GitHub Pages

&emsp; A documentação do projeto pode ser acessada pelo GitHub Pages, através do seguinte link:
<a href="https://inteli-college.github.io/2024-T0008-EC05-G01/">Link do GitHub Pages</a>

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/breno-santos-0843131b8/">Breno Santos</a>
- <a href="https://www.linkedin.com/in/eduardo-henrique-dos-santos-8b24451b8/">Eduardo Henrique</a>
- <a href="https://www.linkedin.com/in/gabrielle-mitoso-6253a219b/">Gabrielle Mitoso</a> 
- <a href="https://www.linkedin.com/in/gustavo-widman/">Gustavo Widman</a> 
- <a href="https://www.linkedin.com/in/isabelle-beatriz-vasquez-oliveira-55a19626a/">Isabelle Vasquez</a> 
- <a href="https://www.linkedin.com/in/naruto/">Ivan Ferreira</a>
- <a href="https://www.linkedin.com/in/luiz-fernando-villaça-leão-930568271/">Luiz Fernando</a>
- <a href="https://www.linkedin.com/in/marco-antonio-rizzi-620b56257/">Marco Rizzi</a>

## 📜 Descrição

&emsp;A solução proposta aborda o desafio apresentado pelo Hospital Sírio Libanês, visando reduzir o tempo de montagem de kits, como o carrinho de emergência cardiorespiratório e outros destinados a procedimentos como endoscopia. O principal obstáculo identificado reside no tempo dedicado à montagem desses kits, que demanda a verificação e reposição de todos os medicamentos ausentes, seguido pela bipagem e nova reposição. A necessidade de uma montagem precisa em todos os kits é crucial, permitindo que os profissionais envolvidos acessem os medicamentos de forma rápida e eficiente durante situações de emergência, sem a necessidade de verificação adicional.

&emsp;Diante desse cenário, a solução proposta pelo grupo ARM consiste na implementação de um braço robótico para auxiliar os profissionais de farmácia na montagem dos kits, com o objetivo de reduzir o tempo despendido e proporcionar uma montagem mais precisa. O robô será equipado com uma interface que permitirá aos profissionais inserir os medicamentos faltantes no kit, além de oferecer a opção de escolher entre diversos layouts para diferentes tipos de kits. Caso não haja um layout predefinido, a interface gráfica possibilitará que o profissional defina a disposição dos medicamentos na montagem.

&emsp;Por fim, a solução implementará um sistema de armazenamento que registrará os medicamentos retirados e colocados em cada kit em um banco de dados. Isso permitirá a identificação precisa do lote em caso de erro, proporcionando uma gestão mais segura e eficiente. A solução não apenas agiliza o processo de montagem, mas também fortalece a segurança e a precisão no manuseio de medicamentos, atendendo às necessidades críticas do ambiente hospitalar.

## 📁 Estrutura de pastas

```
.
├───.github
│   └───workflows
├───documentation
│   └───docusaurus-documentation
│       ├───blog
│       ├───docs
│       │   └───sprints
│       │       ├───Sprint 1
│       │       ├───Sprint 2
│       │       ├───Sprint 3
│       │       ├───Sprint 4
│       │       └───Sprint 5
│       ├───src
│       │   ├───components
│       │   │   └───HomepageFeatures
│       │   ├───css
│       │   └───pages
│       └───static
│           └───img
│               ├───doc_component
│               ├───frontend
│               ├───integrantes
│               ├───mockup
│               └───wireframe
├───src
│    ├───classes
│    ├───commands
│    │   └───templates
│    ├───conexaoHTTP
│    │   └───embarcado
│    ├───lib
│    │   └───pydobot
│    │       └───enums
│    ├───novo_backend
│    │   ├───classes
│    │   ├───database
│    │   │   └───archives
│    │   │       └───qrcode
│    │   ├───modules
│    │   │   ├───api
│    │   │   │   ├───classes
│    │   │   │   └───routes
│    │   │   ├───qrcode
│    │   │   └───robot
│    │   │       ├───classes
│    │   │       ├───lib
│    │   │       │   └───pydobot
│    │   │       │       └───enums
│    │   │       └───utils
│    │   ├───static
│    │   │   ├───css
│    │   │   ├───img
│    │   │   └───scripts
│    │   └───templates
│    └───utils
└───README.md
```

&emsp;&emsp;Dentre os arquivos e pastas presentes na raiz do projeto, define-se:

- <b>.github</b>: nesta pasta há o arquivo de deploy do repositório, que faz a documentação do projeto ser exibida no GitHub Pages

- <b>documentation</b>: aqui estão todos os documentos do projeto, incluindo a documentação das Sprints e as imagens utilizadas. Futuramente o manual de instruções será adicionado

- <b>src</b>: pasta com todos os códigos e base de dados utilizados no projeto

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto 

## 🔧 Instalação

Para iniciar a documentação do projeto, faça upload do repositório no computador ou notebook. Abra o Prompt de Comando e digite ```cd .\documentation\docusaurus-documentation``` para entrar na pasta da documentação.
Digite ```npm i``` para instalar todas dependências e aguarde enquanto a instalação é feita.
Para concluir, digite ```npm start``` para iniciar a documentação, e aguarde até a página ser carregada.

## 🗃 Histórico de lançamentos

* Versão 4.0 - 11/04/2024
    * Interface navegável;
    * Interface frontend e backend do sistema;
    * Hardware periférico com o sistema do robô;
   
* Versão 3.0 - 01/04/2024
    * Telas e mockup;
    * Periféricos.

* Versão 2.0 - 01/03/2024
    * Mapeamento do Fluxo de Utilização da Solução;
    * Sistema de Automação.

* Versão 1.0 - 16/02/2024
    * Entendimento do Negócio;
    * UX Research;
    * Proposta de Arquitetura do Sistema.

## 📋 Licença/License

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/Inteli-College/2024-T0008-EC05-G01">Arm</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/InteliProjects">Inteli</a>, <a property="dct:title" rel="cc:attributionURL" href="https://www.linkedin.com/in/breno-santos-0843131b8/">Breno Santos</a>, <a property="dct:title" rel="cc:attributionURL" href="https://www.linkedin.com/in/eduardo-henrique-dos-santos-8b24451b8/">Eduardo Henrique</a>, <a property="dct:title" rel="cc:attributionURL" href="https://www.linkedin.com/in/gabrielle-mitoso-6253a219b/">Gabrielle Mitoso</a>, <a property="dct:title" rel="cc:attributionURL" href="https://www.linkedin.com/in/gustavo-widman/">Gustavo Widman</a>, <a property="dct:title" rel="cc:attributionURL" href="https://www.linkedin.com/in/isabelle-beatriz-vasquez-oliveira-55a19626a/">Isabelle Vasquez</a>, <a property="dct:title" rel="cc:attributionURL" href="https://www.linkedin.com/in/naruto/">Ivan Ferreira</a>, <a property="dct:title" rel="cc:attributionURL" href="https://www.linkedin.com/in/luiz-fernando-villaça-leão-930568271/">Luiz Fernando Villaça Leão</a>, <a property="dct:title" rel="cc:attributionURL" href="https://www.linkedin.com/in/marco-antonio-rizzi-620b56257/">Marco Rizzi</a> is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

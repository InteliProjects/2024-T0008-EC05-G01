---
title: Artefato - Interface Navegável
sidebar_position: 1
---
## Mockup

&emsp;Um mockup de alta fidelidade é uma representação visual detalhada e próxima do produto final, utilizado para apresentar o visual e a experiência do usuário antes da implementação. Este tipo de mockup praticamente representa o visual definitivo da solução, permitindo avaliações precisas e feedback concreto antes da produção final. Suas vantagens incluem economia de tempo, facilitação da comunicação entre equipes e stakeholders, e a capacidade de identificar e corrigir problemas visualmente antes da implementação. Neste documento, evidenciaremos nosso processo de desenvolvimento da interface do usuário.

<div style={{ textAlign: 'center', padding: "0px" }}>
    <p style={{ margin: '15px', fontWeight: 'bold' }}>Para acessar e interagir com o Mockup desenvolvido <a href="https://www.figma.com/proto/73gPLi62HNx6Pj0WL5cGoJ/Arm-Group?page-id=28%3A42&type=design&node-id=279-350&viewport=-179%2C-169%2C0.07&t=dj4G99KuIqo1uJGd-1&scaling=scale-down&starting-point-node-id=279%3A350&show-proto-sidebar=1&mode=design" target="_blank">Clique aqui</a></p>
</div>

### Telas desenvolvidas
A seguir, serão detalhadas as funcionalidades e características de cada tela, fornecendo uma visão abrangente do fluxo de interação e das principais áreas de interesse do projeto.

<p style={{fontSize: '130%', fontWeight: 'bold' }}>Tela incial</p>
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 01 - Tela Inicial
    ![image](/img/mockup/TelaInicial.png)
    Fonte: Elaborado pelos próprios autores
</div>

&emsp;Esta será a primeira tela apresentada ao usuário ao iniciar a aplicação. Seu principal objetivo é direcionar os dois tipos de usuários para suas respectivas áreas. O usuário farmacêutico será direcionado para sua área ao clicar no botão 'Farmacologista', enquanto o auxiliar de farmácia selecionará a opção 'Auxiliar de Farmácia'. A navegação é projetada de forma simples para garantir uma experiência sem complicações para o usuário.

---

<p style={{fontSize: '160%', fontWeight: 'bold' }}>Fluxo: Farmacêutico</p>

O fluxo do farmacêutico representa a totalidade da interface à qual o usuário terá acesso ao selecionar a opção "Farmacologista" na página inicial.

<p style={{fontSize: '130%', fontWeight: 'bold' }}>Tela principal - Farmacêutico</p>
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 02 - Tela Principal - Farmacologista
    ![image](/img/mockup/TelaPrincipal.png)
    Fonte: Elaborado pelos próprios autores
</div>

&emsp;Esta tela é a primeira que o usuário do perfil farmacêutico encontrará após selecionar sua área. Os kits de emergência são apresentados em uma disposição organizada, em formato de matriz, com botões representando cada modelo disponível. Ao clicar em um kit específico, o farmacêutico será redirecionado para outra tela com informações detalhadas sobre o kit selecionado.


&emsp;Além disso, um header é visível na tela, contendo uma barra de pesquisa para facilitar a localização de kits desejados. Há também a opção de criar um novo modelo de kit, acessível através do botão 'Novo kit'

<p style={{fontSize: '130%', fontWeight: 'bold' }}>Tela do Kit - Farmacêutico</p>
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 03 - Tela do Kit - Farmacologista
    ![image](/img/mockup/TeladoKit.png)
    Fonte: Elaborado pelos próprios autores
</div>
&emsp;Após selecionar um dos modelos de kit na tela principal, o farmacêutico será redirecionado para esta tela. Aqui, ele poderá visualizar todos os itens presentes no kit, juntamente com suas quantidades. Além disso, há a opção de editar o kit caso seja identificada alguma inconformidade. Para isso, basta selecionar o botão 'Editar Kit' no header.

&emsp;Se não houver necessidade de alterações, o usuário pode retornar à tela principal utilizando o botão 'Voltar', também presente no header.

<p style={{fontSize: '130%', fontWeight: 'bold' }}>Tela de Edição de Kit - Farmacêutico</p>
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 04 - Tela Edição de Kit - Farmacologista
    ![image](/img/mockup/EdiçãodeKit.png)
    Fonte: Elaborado pelos próprios autores
</div>

&emsp;Após selecionar a opção 'Editar Kit', o usuário será redirecionado para esta tela. Embora seja muito semelhante à tela anterior, aqui é possível editar todos os itens presentes no kit. Para isso, basta clicar nos itens desejados, que estão disponíveis em uma lista.

&emsp;Caso seja necessário adicionar um novo item ao kit, o usuário pode clicar no botão com o símbolo de '+'.

&emsp;Após finalizar as modificações, o usuário pode salvar suas mudanças ao clicar em 'Concluir Edição', botão contido no header. No entanto, caso deseje cancelar suas alterações, basta clicar em 'Cancelar'.

<p style={{fontSize: '130%', fontWeight: 'bold' }}>Tela de Novo Kit - Farmacêutico</p>
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 05 - Tela de Novo Kit - Farmacologista
    ![image](/img/mockup/NovoKit.png)
    Fonte: Elaborado pelos próprios autores
</div>
&emsp;Esta tela é idêntica à tela de edição de kit, exceto pelo fato de que nenhum item está pré-registrado para edição. Portanto, todos os itens devem ser adicionados pelo usuário. O processo de adição de itens é realizado clicando no botão com o símbolo de '+'.

&emsp;Após selecionar os itens desejados para o novo kit, o usuário pode salvar suas mudanças ao clicar em 'Concluir Edição', botão presente no header. Se o usuário preferir cancelar a criação do novo kit, basta clicar em 'Cancelar'.

---

<p style={{fontSize: '160%', fontWeight: 'bold' }}>Fluxo: Auxiliar</p>

O fluxo do auxiliar representa a totalidade da interface à qual o usuário terá acesso ao selecionar a opção "Auxiliar de Farmácia" na página inicial.

<p style={{fontSize: '130%', fontWeight: 'bold' }}>Tela Principal - Auxiliar</p>
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 06 - Tela Principal - Auxiliar
    ![image](/img/mockup/TelaPrincipal2.png)
    Fonte: Elaborado pelos próprios autores
</div>
&emsp;Esta tela será a primeira vista pelo usuário que selecionar a área de Auxiliar de Farmácia. Assim como na tela principal do Farmacêutico, o usuário poderá visualizar todos os modelos de kits existentes. No entanto, há uma pequena diferença: ao lado dos botões dos kits, há um pequeno botão com o símbolo de '+'. Esse botão está relacionado à funcionalidade exclusiva desta tela, a 'Fila de Espera dos Kits'. Ao clicar neste botão, o usuário pode adicionar mais kits à fila de espera, bem como removê-los.

&emsp;Além disso, na parte superior da tela, o usuário pode acessar o armazém clicando no botão 'Armazém'.

<p style={{fontSize: '130%', fontWeight: 'bold' }}>Tela do Kit - Auxiliar</p>
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 07 - Tela do Kit - Auxiliar
    ![image](/img/mockup/TeladoKit2.png)
    Fonte: Elaborado pelos próprios autores
</div>
&emsp;Esta tela é idêntica à tela de detalhes do kit para o farmacêutico, com a exceção de que não possui a opção 'Editar Kit'. Apenas os farmacêuticos têm autorização para realizar tais ações, tornando esta tela exclusivamente para visualização dos itens do kit pelo auxiliar de farmácia.

<p style={{fontSize: '130%', fontWeight: 'bold' }}>Armazém - Auxiliar</p>
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 08 - Armazém - Auxiliar
    ![image](/img/mockup/Armazem.png)
    Fonte: Elaborado pelos próprios autores
</div>

&emsp;Esta tela é muito semelhante à tela de detalhes do kit. No entanto, em vez de exibir os itens de um kit de emergência, ela mostra os itens disponíveis no armazém. O botão de edição do kit é substituído por um botão 'Reabastecido', utilizado para enviar ao sistema a informação de que o estoque foi reabastecido com sucesso.

---
 
 ### Especificações dos componentes utilizados
&emsp;Nesta seção, você encontrará informações detalhadas sobre os principais componentes utilizados para a idealização do nosso mockup e, consequentemente, para o desenvolvimento da nossa interface. Aqui, exploraremos os elementos-chave que compõem a estrutura visual e funcionalidade do projeto.
 <div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 09 - Componentes em destaque
    ![image](/img/doc_component/component1.png)
</div>
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    ![image](/img/doc_component/component2.png)
</div>
<div style={{width: '40%', margin: '0 auto', textAlign: 'center'}}>
    ![image](/img/doc_component/component3.png)
    Fonte: Elaborado pelos próprios autores
</div>

&emsp;Nesta seção, detalharemos cada elemento destacado anteriormente, descrevendo sua função, aparência e características gerais. A seguir, você encontrará uma análise minuciosa dos componentes que compõem nosso wireframe, permitindo uma compreensão abrangente de sua implementação e interação na interface.

<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 10 - Explicação de componentes
    ![image](/img/doc_component/componentExplanation.png)
    Fonte: Elaborado pelos próprios autores
</div>

---

### Observação

Se você deseja obter um entendimento mais profundo de como as telas do mockup foram implementadas na solução real, você pode acessar o Artefato "Backend e Frontend". Isso lhe proporcionará acesso a informações mais específicas, como quais rotas são chamadas dependendo da interação do usuário com a plataforma, entre outros detalhes relevantes.
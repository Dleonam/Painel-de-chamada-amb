# Painel-de-chamada-amb
Projeto básico de painel de chamadas focado para 'amb' com input de nome e seleção de salas já pré-configuradas no banco.

FUNCIONALIDADE:

Temos um programa feito em Python, ele é o responsável pela parte de input de dados no banco e de fazer a interface gráfica do usuário Nº1, que estará alimentando a base.

A base usada aqui foi a SQLite;

A terceira e última parte do projeto e composta por 3 outras linguagens de programação que fazem a parte visual, sonora e de buscar as informações que foram inputadas ao banco anteriormente.
   Essa parte, então, foi desenvolvida em CSS,PHP,JS e HTML 

Para usar o projeto é bem simples, basta você configurar um SV com apache e php onde rodará a interface do usuário 2 que será aquele que estará na sala de espera, esperando ser chamado pelo profissional,

Essa e a tela do programa em que o profissional que fará a chamada fara input do nome da pessoa!
![image](https://github.com/user-attachments/assets/05206b52-0dce-4813-ba38-30a019a2f0d4)

! É importante freezar que dentro do código-fonte desse programa a também a parte de especificar o caminho do banco de dados, que devera ser o mesmo colocado no php posteriormente!
![image](https://github.com/user-attachments/assets/e813aa2d-d01b-47b5-baf4-de22bea661ee)

Após essas mudanças no código Python, iremos para a configuração da parte visual que ficará para o público. 

Nessa parte, você colocará a pasta painel-de-chamadas-cliente. Dentro da pasta htdocs do sem apache, após isso iremos editar o PHP para ele conectar ao mesmo banco de dados que você setou lá no código em Python. 

![image](https://github.com/user-attachments/assets/476e9331-70c9-49dc-8306-a7b75f41dffd)
A FUNÇAO DO PHP AQUI É SINCRONIZAR COM A CONEXÃO DO BANCO. 

No meu caso, somente joguei os aquivos na pasta Htdocs, mas vocês, por boas práticas e organização, coloquem em uma pasta separando os arquivos já pré-existentes do apache.

![image](https://github.com/user-attachments/assets/ddec6383-40b9-4d74-80d7-a6455f29734e)

temos então dentro da pasta os aquivos JS 'responsável pela parte sonora, quando e gerado um novo dado no banco nas colunas de (paciente)'

No HTML temos a parte visual da página somente. E separado dela temos o CSS que fara a estilização das nossas escritas e dos nossos dados, um bom exemplo que eu posso usar de comparação aqui e como se fosse um BI  puxando dados e te apresentando na tela de forma bonita. 
mas com a função de não te dar gráficos e sim chamadas de nomes.

Por fim teremos o resultado impresso em formato web, da nossa exibição de chamadas que poderá ficar em uma tela de TV Smart na sala de espera ou em uma tela de PC com boas proporções, escolhi o formato web da parte do cliente, pois foi o método mais fácil e com melhor desempenho e compatível com diversos locais que encontrei

![image](https://github.com/user-attachments/assets/6a20af6e-37bc-4756-b149-66acc33cb252)


esse projeto visa uma melhoria no meu local de trabalho, estou postando aqui para obter feedback e ajuda com melhorias e para aqueles que também, assim como eu lá no início, procurava um painel de chamadas simples e prático e tive que acabar recorrendo em construí-lo.

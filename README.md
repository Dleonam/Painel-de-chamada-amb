# Painel-de-chamada-amb
Projeto basico que painel de chamadas mais focado para 'amb' com input de nome e seleção de salar ja pre-configuradas  no banco.

FUNCIONALIDADE:

Temos um programa feito em python, ele é o responsavel pela parte de input de dados no banco e de fazer a interface grafica do usuario Nº1, que estara alimentando a base

A base usada aqui foi a SQLite;

A terceira e ultima parte do projeto e composta por 3 outras liguagens de programação que fazer a parte vizual, sonora e de buscar as infs que foram inputadas ao banco anteriormente
   Essa parte entao ela foi desenvolvida em CSS,PHP,JS e HTML 

Para usar o projeto e bem simples basta vc configurar um SV com apache e php onde rodara a interface do usuario 2 que sera aquele que estara na sala de espera, esperando ser chamado pelo profissional,

Essa e a tela do programa em que o profissional que fara a chamada fara input do nome da pessoa!
![image](https://github.com/user-attachments/assets/05206b52-0dce-4813-ba38-30a019a2f0d4)

! importante freezar que dentro do codigo fonte desse programa a tambem a parte de expecificar o caminho do banco de dados, que devera ser o mesmo colocado no php posteriormente!
![image](https://github.com/user-attachments/assets/e813aa2d-d01b-47b5-baf4-de22bea661ee)

Apos essas mudanças no codigo python iremos para a configuraçao da parte vizual que ficara para o publico 

Nessa parte voce colocara a pasta painel-de-chamadas-cliente. dentro da pasta htdocs do sem  apach, apos isso iremos editar o  PHP para ele conectar ao mesmo banco de dados que voce setou la no codigo em python 

![image](https://github.com/user-attachments/assets/476e9331-70c9-49dc-8306-a7b75f41dffd)
A FUNÇAO DO PHP AQUI E BASICAMENTE A CONEXÃO DO BANCO 

no meu caso somente joguei os aquivos na pasta Htdocs, mas vcs por boas pratigas e organização coloquem dentro de uma pasta seprando os arquivos  ja pre existentes do apach

![image](https://github.com/user-attachments/assets/ddec6383-40b9-4d74-80d7-a6455f29734e)

temos entao dentro da pasta os aquivos JS  'responsavel pela parte sonora, quando e gerado um novo dado no banco nas colunas de (paciente)'

No html temos a parte visual da pagina somente. separados dela temos o CSS que fara a estilização das nossas escritas e dos nossos dados, um bom exemplo que eu posso usar de comparação aqui e como se fosse um BI  puxando dados e te apresentando na tela de forma bonita 
mas com a funçao de nao te dar graficos e sim chamadas de nomes.

Por fim teremos o resultado impresso em formato web, da nossa exibiçao de chamadas que podera ficar em uma tela de TV smart na sala de espera ou em uma tela de PC com boas proporçoes, escolhi o formato web da parte do cliente, pois foi o metodo mais facil e com melhor desempenho e compativel com diversos locais que encontrei

![image](https://github.com/user-attachments/assets/6a20af6e-37bc-4756-b149-66acc33cb252)


esse projeto visa uma melhoria no meu local de trabalho, estou postanto aqui com a finalidade de obter feedback e ajuda com melhorias e tambem para aqueles que tambem assim como eu  la no inicio procurava um painel de chamadas simples e pratico e tive que acabar recorrendo em construilo.







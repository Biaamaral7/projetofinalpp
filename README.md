# projetofinalpp

# Descrição do Projeto
Código em Python que simula um sistema de Proof of Work (PoW) com comunicação entre nós, incluindo diferentes estados (aceitando, rejeitando, propondo) e simulação de mineração/validação de blocos. A implementação também inclui um nó coordenador, nós participantes, lógica de falha e recuperação, e logs detalhados para acompanhamento do processo de consenso.

# Instruções de configuração de ambiente
O código foi executado e testado no ambiente do Visual Studio Code, e requer a instalação do Python, que pode ser encontrada no link: https://www.python.org/downloads/
Para executar o código, rodar o seguinte comando no terminal: python pow.py

# Explicação das fases do algoritmo
Temos uma classe que representa o nó, dentro dessa classe declaramos o id de cada nó, o nó coordenador, o estado desses nós, histórico dos blocos validados, os logs de cada ação e o estado de falha.
O método mine_block simula a mineração de um bloco, buscando um nonce válido.
O método validate_block valida um bloco com base no prefixo do hash.
O método propose_block propõe um bloco para os outros nós.
O método communicate_with_node tenta realizar a comunicação com o nó.
O método simulate_failure, simula uma chance de falha de 20%.
O método recover simula a recuperação do nó.
O método start_simulation inicia a simulação, na simulação, o nó coordenador gera o primeiro bloco, em seguida os nós começam a minerar seus blocos, é então simulada uma falha e recuperação de nós participantes, estabelecendo-se 10% de chance de recuperação, cada nó tenta minerar ou validar, o nó coordenador propõe os blocos e por fim são exibidos os logs de cada nó.

# Falhas simuladas e recuperação
O log pode exibir 'Node [id] failed', isso significa que o nó  de [id] falhou de alguma forma, e esse nó se encontra momentaneamente fora de operação.
O log também pode exibir 'Node [id] failed. Node [id] recovered', significando o nó de [id] falhou, porém se recuperou e está funcionando novamente, pronto para continuar minerando e validando blocos.


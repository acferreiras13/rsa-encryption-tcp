# Sistema de Comunicação Segura com Criptografia RSA

# Descrição
Este projeto implementa um sistema de comunicação entre cliente e servidor, utilizando criptografia RSA para garantir a segurança na troca de mensagens. O sistema utiliza o protocolo TCP para comunicação em rede e garante que apenas o destinatário correto possa ler as mensagens, mantendo a privacidade das informações.

# O que é RSA?
RSA (Rivest-Shamir-Adleman) é um algoritmo de criptografia assimétrica amplamente utilizado para proteger dados na comunicação digital. Ele utiliza um par de chaves: uma chave pública para criptografar a mensagem e uma chave privada para descriptografá-la. O algoritmo se baseia na dificuldade de fatoração de grandes números primos, o que torna a criptografia extremamente segura.

Chave pública (e, n): Utilizada para criptografar a mensagem.

Chave privada (d, n): Utilizada para descriptografar a mensagem.

A segurança do RSA se baseia no fato de que, mesmo conhecendo a chave pública, é computacionalmente difícil calcular a chave privada.

# O que é TCP?
TCP (Transmission Control Protocol) é um protocolo de comunicação confiável que garante a entrega de dados entre um cliente e um servidor em uma rede. Ele garante que os pacotes de dados cheguem corretamente ao destino e na ordem certa, fazendo com que a comunicação entre o cliente e o servidor seja segura e confiável.

# Funcionalidade
O sistema de comunicação possui dois componentes principais:

Cliente: Envia mensagens criptografadas para o servidor, recebe respostas criptografadas e as descriptografa usando sua chave privada.

Servidor: Recebe as mensagens criptografadas do cliente, as descriptografa com sua chave privada, realiza um processamento (no caso, converte a mensagem para maiúsculas) e envia a resposta de volta ao cliente de forma criptografada.

# Fluxo de Comunicação:
Troca de Chaves:
O cliente gera um par de chaves públicas e privadas RSA e envia sua chave pública para o servidor.
O servidor também gera seu par de chaves e envia sua chave pública de volta para o cliente.

Criptografia de Mensagens:
O cliente envia uma mensagem digitada, que é criptografada utilizando a chave pública do servidor.
O servidor recebe a mensagem criptografada, a descriptografa com sua chave privada, transforma a mensagem para maiúsculas e a criptografa novamente com a chave pública do cliente.

Descriptografando Respostas:
O cliente recebe a mensagem criptografada do servidor e a descriptografa com sua chave privada, exibindo a resposta processada.

# Como Funciona o Código
Client:
- O client gera suas chaves pública e privada.
- Conecta-se ao servidor através de um socket TCP (porta 1300).
- Envia sua chave pública ao servidor.
- Recebe a chave pública do servidor.
- Solicita ao usuário que digite uma mensagem e a criptografa utilizando a chave pública do servidor.
- Envia a mensagem criptografada ao servidor.
- Recebe a resposta criptografada do servidor, descriptografa com sua chave privada e exibe o resultado.
- Fecha a conexão.

Server:
- O servidor gera suas chaves pública e privada.
- Configura um servidor TCP na porta 1300 e aguarda a conexão do cliente.
- Quando o cliente se conecta, o servidor recebe a chave pública do cliente.
- Envia sua própria chave pública ao cliente.
- Recebe a mensagem criptografada do cliente e a descriptografa com sua chave privada.
- Processa a mensagem (transformando-a em maiúsculas).
- Recrypografa a resposta com a chave pública do cliente e envia de volta.
- Fecha a conexão.
  
# Como Utilizar

Pré-requisitos:

- Python 3.x instalado no seu sistema.
- Rede local ou um servidor que possa ser acessado via IP.

Passos:
1. Clone o repositório.
2. Execute o código do servidor:
3. Execute o código do cliente em outro terminal:
4. O cliente pedirá para você digitar uma mensagem.
5. Após enviar, você verá a mensagem criptografada sendo exibida no terminal do cliente.
6. O servidor processará a mensagem, transformando-a para maiúsculas, e responderá de forma criptografada.
7. O cliente irá descriptografar a resposta e mostrar no terminal.

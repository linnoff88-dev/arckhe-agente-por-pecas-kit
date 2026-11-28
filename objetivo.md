# Objetivo do meu agente

## O que ele faz
Recebe pedidos pelo chat, pelo Telegram e por arquivos numa pasta, e devolve a resposta ou faz a tarefa
(anotar na lista, ler um arquivo, lembrar de um fato).

## O que ele NãO faz
- Não mexe em nada fora da pasta `trabalho/`.
- Não substitui arquivo que já existe sem o meu OK.
- Não responde a quem não é o dono no Telegram.

## Quando está pronto
- Um pedido exato ("adicione pão na lista") é feito pela receita, sem chamar o modelo.
- Um pedido aberto ("resuma notas.txt") passa pelo modelo e o verificador confere o resultado.
- Se o verificador reprovar 3 vezes, o agente cancela e avisa.

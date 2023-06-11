# Projeto Python Discord Bot

## Sumário 📚

- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Descrição](#descrição)
- [Execução 1](#execução-1)
- [Execução 2](#execução-2)
- [Hospedagem](#hospedagem)
- [Licença](#licença)

## Tecnologias Utilizadas

![Licença](https://img.shields.io/badge/Licença-MIT-blue)
[![Python](https://img.shields.io/badge/Python-Programming-blue?logo=python&logoColor=white)](https://www.python.org/)
[![PyCharm](https://img.shields.io/badge/PyCharm-IDE-green?logo=pycharm&logoColor=white)](https://www.jetbrains.com/pycharm/)

## Descrição 📝

Projeto de fins pessoais e didáticos com a finalidade de facilitar e ajudar a mim e aos meus colegas. Com este bot, conseguimos automatizar a ação de buscar nossas classificações e as classificações dos nossos adversários em nosso jogo (Valorant). Além disso, o bot é capaz de fornecer opiniões sobre os membros do nosso servidor, compartilhar curiosidades, sortear jogadores individuais ou duplas e muito mais. Estamos trabalhando para organizar e aprimorar esse projeto, tornando-o útil para mim e meus amigos, para facilitar e melhorar nossas experiências durante nossas jogatinas.

## Execução 1 ⚙

Este bot é um script em Python que utiliza a biblioteca Selenium para automatizar a captura de screenshots das classificações de jogadores no jogo Valorant. Com esse bot, eu e meus colegas podemos obter essas informações de forma mais fácil e eficiente.

O objetivo principal do bot que criei é facilitar o processo de obtenção das classificações dos jogadores. Ele acessa o site tracker.gg e navega até os perfis dos jogadores especificados em uma lista. Em seguida, simula as ações de rolagem da página para garantir que todas as informações estejam carregadas.

Após isso, o bot cria pastas individuais para cada jogador e captura um screenshot da página atual. Esses screenshots são salvos nas respectivas pastas com o nome do jogador e a data atual. Assim, temos um registro das classificações de cada jogador em um determinado momento.

Esse bot é uma maneira eficiente e conveniente de automatizar a obtenção das classificações no jogo Valorant, tornando o processo mais ágil e facilitando a organização dessas informações para mim e meus amigos.

## Execução 2 ⚙

Este bot está diretamente ligado ao bot de capturas de tela. Ele é responsável por interagir através de comandos com um servidor do Discord. Alguns desses comandos são:

- $sorteio: Responsável por sortear um jogador ou duplas, útil para organização dos times.
- $curiosidades: Útil para a distração, gerando curiosidades sobre cada membro do servidor do Discord.
- $opinião: Dá uma opinião polêmica, de forma brincalhona, sobre cada membro.
- $chance: Gera uma porcentagem útil para saber a chance de algo dar certo ou errado.
- !buscar: Útil para buscar informações sobre nossos adversários no Valorant.
- $rank: Busca as capturas de tela salvas pelo outro bot no GitHub.
- $rank_nome_do_membro. Também é possível buscar o rank individual dos membros do servidor usando 

## Hospedagem 🌐

O bot foi hospedado usando os serviços da:
https://discloudbot.com

## Licença 🔒

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.

© 2023 Viniciuszile. Todos os direitos reservados.

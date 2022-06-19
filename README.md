# Tarefa de programação UFRJ Analytica



> Este projeto faz parte do desafio de programação do processo seletivo da UFRJ Analytica

A tarefa tem como objetivo construir uma API com duas rotas. As duas rotas da API estão descritas abaixo

### POST /age

Essa rota responde uma requisição POST que contenha um body com a seguinte estrutura:

```
{
    name: "Nome Sobrenome",
    birthdate: yyyy-mm-dd,
    date: YYYY-MM-DD
}
```

Com um JSON com a seguinte estrutura:

```
{
    quote: "Olá, Nome Sobrenome! Você tem X anos e em DD/MM/YYYY você terá Y anos.",
    ageNow: X,
    ageThen: Y
}
```

## GET /album-info

Essa rota responde uma requisição GET que contenha, obrigatoriamente, o seguinte parâmetro de query

```
artist=NOME-DO-ARTISTA
```

Com um JSON com a seguinte estrutura:

```
{
    artist: "NOME-DO-ARTISTA",
    latest-album: "NOME-DO-ALBUM",
    album-year: 2022,
    album-tracks: {
        1: "MUSICA 1"
        2: "MUSICA 2"
        3: "MUSICA 3"
    }
}
```

Esta requisição irá retornar o último album lançado pelo artista buscado utilizando a [API do AudioDB](https://www.theaudiodb.com/api_guide.php).

## Usando a API

Para usar a API localmente, siga estas etapas:

```
git clone https://github.com/joaopedrofreire/ufrj-analytica-p3.git
cd ufrj-analytica-p3
pip install -r requirements.txt
python api.py
```
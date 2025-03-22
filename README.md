# BinDecConverter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**BinDecConverter** é uma aplicação web interativa desenvolvida em Flask que permite converter números entre os sistemas decimal e binário. O projeto foi criado com foco na didática, oferecendo explicações claras e passo a passo de como as conversões são realizadas. Além disso, inclui funcionalidades divertidas, como um Easter Egg e áudios que tornam a experiência mais envolvente.

## Funcionalidades Principais

- **Conversão Decimal para Binário**:
  - Exibe as divisões sucessivas por 2 em cascata.
  - Mostra uma tabela final com os valores das potências de 2 correspondentes a cada bit.

- **Conversão Binário para Decimal**:
  - Apresenta a soma horizontal detalhada dos valores posicionais.
  - Gera uma tabela final com os bits e seus respectivos valores decimais.

- **Easter Egg**:
  - Ao digitar `13` (decimal) ou `1101` (binário), um áudio especial será reproduzido.

- **Áudio Interativo**:
  - Ao passar o mouse sobre a tabela final, um áudio complementar (`audio2.mp3`) é acionado.

- **Interface Didática**:
  - Explicações passo a passo para facilitar o entendimento.
  - Potências exibidas no formato sobrescrito (ex.: 2³).

## Requisitos

- Python 3.x
- Flask (pip install flask)
- Um navegador moderno (Chrome, Firefox, Edge, etc.)

## Como Executar o Projeto

1. Clone este repositório:
```bash
   git clone https://github.com/seu-usuario/BinDecConverter.git
   cd BinDecConverter
```
2. Instale as dependências:
```bash
   pip install -r requirements.txt
```
3. Execute o servidor Flask:
```bash
   python app.py
```

4. Acesse a aplicação no navegador:
   http://127.0.0.1:5000

## Estrutura do Projeto

BinDecConverter/
│
├── app.py               # Código principal do Flask
├── templates/           # Arquivos HTML renderizados pelo Flask
│   └── index.html       # Página principal da aplicação
├── static/              # Arquivos estáticos (CSS, áudios, etc.)
│   ├── audio.mp3        # Áudio do Easter Egg
│   └── audio2.mp3       # Áudio interativo para tabelas finais
└── README.md            # Este arquivo

## Licença

Este projeto está licenciado sob a **Licença MIT**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contribuições

Contribuições são bem-vindas! Se você encontrar bugs ou quiser adicionar novas funcionalidades, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Autor

Desenvolvido por [Argeu](https://github.com/Gegeu-sp).
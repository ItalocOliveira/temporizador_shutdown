# Temporizador de Shutdown

Este script em Python cria um temporizador que desliga o computador após um período de tempo especificado pelo usuário. O temporizador é definido em minutos e conta regressivamente até atingir zero, momento em que o comando de desligamento é executado.

## Funcionamento

- Solicita ao usuário a quantidade de minutos para o temporizador.
- Converte os minutos em segundos para contagem regressiva.
- Exibe uma contagem regressiva em tempo real no formato `MM:SS`.
- Desliga o computador automaticamente ao término da contagem regressiva.

## Dependências

- `time` (módulo padrão do Python)
- `os` (módulo padrão do Python)

## Como Usar

1. Certifique-se de ter Python instalado em seu computador.
2. Copie o código abaixo para um arquivo Python (ex: `temporizador_shutdown.py`).
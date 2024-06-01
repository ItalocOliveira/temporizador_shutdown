# Temporizador de Shutdown

Este código em Python cria um temporizador que desliga o computador após um período de tempo especificado pelo usuário. O usuário pode definir o temporizador em horas, minutos ou segundos, e a contagem regressiva será exibida em tempo real no formato `HH:MM:SS`.

## Funcionamento

- Solicita ao usuário a quantidade de tempo para o temporizador, que pode ser em horas, minutos ou segundos.
- Converte o tempo fornecido em segundos para a contagem regressiva.
- Exibe uma contagem regressiva em tempo real no formato `HH:MM:SS`.
- Desliga o computador automaticamente ao término da contagem regressiva.

## Dependências

- `time` (módulo padrão do Python)
- `os` (módulo padrão do Python)

## Como Usar

1. Certifique-se de ter Python instalado em seu computador.
2. Copie o código para um arquivo Python (ex: `temporizador_shutdown.py`).
3. Execute o script no terminal ou prompt de comando.
4. Digite o tempo desejado para o temporizador no formato apropriado:
    - Para horas: `h X` (ex: `h 1` para 1 hora)
    - Para minutos: `m X` (ex: `m 30` para 30 minutos)
    - Para segundos: `s X` (ex: `s 120` para 120 segundos)

5. O temporizador começará a contagem regressiva e exibirá o tempo restante no formato `HH:MM:SS`.
6. Quando o tempo se esgotar, o computador será desligado automaticamente.

## Observações

- Este código é destinado para sistemas operacionais Windows. Para outros sistemas operacionais, o comando de desligamento pode precisar ser ajustado.
- Use com cuidado.

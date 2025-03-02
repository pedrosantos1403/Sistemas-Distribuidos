﻿# Sistemas-Distribuidos

## Requisitos Mínimos

Para implementar e executar o sistema de torrent simples, é necessário ter o seguinte ambiente configurado:

### Software Necessário
- **Python 3.8+** (Recomendado)
- **Pip** (Gerenciador de pacotes do Python)
- **Bibliotecas Python:**
  - Flask
  - Requests
  - Threading (Módulo padrão do Python)

### Instalação das Dependências
Instale as bibliotecas necessárias com o comando:
```bash
pip install flask requests
```

## Tutorial de Implementação

### 1. Criar o Tracker (Servidor)
O Tracker é um servidor que coordena os peers. Crie um arquivo semelhante ao arquivo `tracker.py` deste repositório.

Para iniciar o tracker, execute o comando:
```bash
python tracker.py
```

### 2. Criar um Peer
Cada peer se conecta ao tracker e compartilha partes do arquivo. Crie um arquivo semelhante ao arquivo `peer.py` deste repositório.

Em seguida, ajuste a variável `TRACKER_URL_EXTERNAL` com o valor de IP da máquina que está executando o tracker.

```bash
TRACKER_URL_EXTERNAL = "http://IP_MAQUINA_TRACKER:5000"
```

Execute um ou mais peers e uma outra máquina dentro da mesma rede local:
```bash
python peer.py
```




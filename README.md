# Algoritmo de Autogerenciamento de Processos

Este repositório contém um algoritmo de autogerenciamento de processos que visa executar uma rotina de processamento por exatamente 60 segundos. O código utiliza conceitos de threads, ajuste de prioridade (`nice`) e monitoramento de processos para alcançar este objetivo.

## Descrição

O algoritmo é composto por três funções principais:

1. **gerador_processo(iteracoes)**: Esta função simula a execução de um processo, ajustando sua prioridade utilizando o valor de `nice`. A função calcula o tempo de execução e imprime o resultado.

2. **gerenciador_processos()**: Esta função monitora o tempo de execução do processo gerado e ajusta o valor de `nice` e o número de iterações com base no tempo objetivo de 60 segundos. Se o tempo de execução for maior que o objetivo, a prioridade é reduzida e o número de iterações é diminuído. Se o tempo de execução for menor que o objetivo, a prioridade é aumentada e o número de iterações é incrementado.

3. **executar_processos(iteracoes)**: Esta função gerencia a execução dos processos em threads. Ele cria duas threads: uma para o gerador de processos e outra para o gerenciador de processos. O loop continua até que o tempo de execução esteja dentro da margem aceitável de 60 segundos.

## Como Utilizar

Para executar o algoritmo, basta rodar o script `atividade1.py`. Certifique-se de que você tem as permissões necessárias para alterar a prioridade dos processos utilizando `os.nice()`.

```sh
python atividade1.py
```

## Exemplo de Saída

```
[Rápido] Tempo de execução: 55.23
Novo nice: 3
Acabou! 60.01 no nice: 3 iteracoes: 1000001000
```

## Requisitos

- Python 3.x

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests com melhorias e correções.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Este algoritmo foi desenvolvido como parte de um estudo sobre gerenciamento de processos e otimização de recursos em sistemas operacionais.

# Algoritmo Simplex 
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

## Conteúdos

<p align="center">
    <a href="#apresentação">Apresentação</a> •
    <a href="#introdução">Introdução</a> • 
    <a href="#implementar-o-algoritmo-simplex">Metodologia</a> •
    <a href="#aplicação">Aplicação</a> •
    <a href="#conclusão">Conclusão</a> •
    <a href="#bibliotecas">Bibliotecas</a> •
    <a href="#execução-do-projeto">Execução do projeto</a> •
    <a href="#autor">Autor</a>
</p>

---

## Apresentação

Este projeto foi desenvolvido como parte de um estudo sobre algoritmos de otimização para resolver problemas de programação linear. O foco principal é a implementação do **Algoritmo Simplex**, um método amplamente utilizado em otimização linear para encontrar a melhor solução possível, minimizando uma função objetivo sujeita a um conjunto de restrições lineares.

---

## Introdução

A programação linear é uma técnica matemática para a otimização de uma função linear sujeita a restrições lineares. É amplamente utilizada em diversas áreas como economia, engenharia, transporte, entre outras. O **Algoritmo Simplex** é uma das metodologias mais eficientes para resolver esses problemas.

O objetivo deste projeto é implementar o Algoritmo Simplex em Python e demonstrar sua aplicação através de exemplos práticos. A escolha do Python se deve à sua simplicidade e às bibliotecas disponíveis que facilitam a manipulação de matrizes e a implementação de algoritmos matemáticos.

---

## Metodologia

A implementação do método Simplex segue os seguintes passos:

1. **Leitura do arquivo**: Leitura dos coeficientes da função objetivo, das restrições e dos valores do lado direito das equações.
2. **Configuração da Tabela Simplex**: Criação e inicialização da tabela Simplex com os coeficientes lidos.
3. **Iteração Simplex**: Realização das iterações do Simplex até encontrar a solução ótima ou determinar que o problema é ilimitado.
4. **Resultado**: Exibição dos valores das variáveis de decisão e do valor da função objetivo na solução ótima.

---

## Aplicação

O código é composto por três funções principais:

1. **read_file(file)**:
    - Lê o arquivo de entrada e separa as variáveis usadas no método Simplex.
    - Exemplo de formato de arquivo:
    ```
    3 2
    3 2 1
    2 1 4
    1 1 2
    ```

2. **simplex(c, A, b)**:
    - Executa o algoritmo Simplex para encontrar a solução ótima.
    - Imprime a tabela Simplex a cada iteração, mostrando o progresso do algoritmo.

3. **main**:
    - Ponto de entrada do programa, que lê o arquivo especificado e chama a função simplex.

## Conclusão

O Algoritmo Simplex é uma ferramenta poderosa para resolver problemas de otimização linear. Sua implementação em Python demonstra a eficiência e a aplicabilidade do método para diversos tipos de problemas práticos. A simplicidade do código e a robustez da biblioteca NumPy facilitam o desenvolvimento e a experimentação com diferentes cenários de problemas.

---

## Bibliotecas

As seguintes bibliotecas foram utilizadas no desenvolvimento deste projeto:

- [NumPy](https://numpy.org/): Para manipulação de matrizes e operações matemáticas.

---

## Execução do projeto

Para executar o projeto, siga os passos abaixo:

1. Clone o repositório:
   ```sh
   git clone https://github.com/PedroLouback/Simplex-Algorithm
   ```
2. Navegue até o diretório do projeto:
   ```sh
   cd simplex-algorithm/src/
   ```
3. Instale as depedências:
    ```sh
   pip install numpy pandas
   ```
4. Execute o script principal:
    ```sh
   python3 simplex.py ../file/input.txt 
   ```

## Autor

Desenvolvido por [Pedro Henrique Louback Campos](https://github.com/PedroLouback)

---
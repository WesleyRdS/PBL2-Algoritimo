# README

## Introdução
Este é um software desenvolvido para auxiliar na coleta de dados do censo demográfico do IBGE de forma automatizada. O software foi projetado para importar informações sobre regiões do país, estados e municípios, cadastrar técnicos e validar suas matrículas. Além disso, ele permite visualizar várias estatísticas importantes derivadas dos dados coletados.

## Funcionalidades Principais
1. **Importação de Dados**: O software permite importar informações sobre regiões, estados e municípios a partir de arquivos de texto.
2. **Cadastro de Técnicos**: Os técnicos podem ser cadastrados no sistema, e suas matrículas são validadas.
3. **Visualização de Estatísticas**:
   - Número de domicílios utilizados para a coleta.
   - Número de domicílios particulares pagos, ainda pagando e alugados.
   - Quantidade de domicílios por cidade com e sem banheiro.
   - Forma mais comum de abastecimento de água por cidade.
   - Percentual de domicílios por cidade sem energia elétrica.
   - Participação na entrevista por cor ou raça.
   - Região com o maior número de municípios pesquisados.
4. **Utilização de Arquivos de Texto**: O software utiliza arquivos de texto para a manipulação e validação dos dados. A função `open()` do Python é empregada para importar e manipular esses arquivos.
5. **Estrutura de Dados**: Apesar de se considerar o uso de dicionários como a melhor estrutura de dados, o programa utiliza matrizes, implementadas como listas encadeadas, devido à facilidade de implementação.
6. **Validação de Dados**: Os dados são validados comparando os arquivos de regiões, técnicos e o exemplo de pesquisa fornecido.
7. **Cálculos Estatísticos**: Para calcular estatísticas, é utilizado um loop `for` para percorrer as posições desejadas na lista, adicionando valores a uma variável que conta a frequência absoluta. Percentuais são calculados levando em consideração a quantidade de repetições e o total de dados do tipo relevante.
8. **Interação com o Usuário**: O usuário interage com o sistema por meio de um menu intuitivo, implementado em um loop `while`.

## Execução do Software
Para executar o software, basta seguir estas etapas:
1. Clone este repositório em sua máquina local.
2. Certifique-se de ter Python instalado em sua máquina.
3. Execute o arquivo principal do programa.
4. Siga as instruções do menu para interagir com o sistema e acessar as estatísticas desejadas.


## Autor
Este software foi desenvolvido por [Wesley Ramos]. 



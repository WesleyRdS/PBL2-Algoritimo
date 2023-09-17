#Funções que importam os arquivos txt e transforma em lista.
#Ultizando o contador 'index' do 'for' para ir indo de termo em termo removendo a quebra de linha
#Usando o ";" do arquivo para criar listas
def abrir_arquivoT():
    try:
        leituraT = open('tecnicosIBGE.txt','r')
        textoT = leituraT.readlines()
        for index in range(len(textoT)):
            textoT[index] = textoT[index].rstrip('\n')
            textoT[index] = textoT[index].split(';')
            
        return textoT
    except:
        print("O arquivo é invalido")
        
def abrir_arquivoE():
    try:
        leituraE = open('exemploPesquisa.txt','r')
        textoE = leituraE.readlines()
        for index in range(len(textoE)):
            textoE[index] = textoE[index].rstrip('\n')
            textoE[index] = textoE[index].split(';') 
        return textoE
    except:
        print("O arquivo é invalido")
        
def abrir_arquivoR():
    try:
        leituraR = open('regioes.txt','r',encoding= "UTF-8")
        textoR = leituraR.readlines()
        for index in range(len(textoR)):
            textoR[index] = textoR[index].rstrip('\n')
            textoR[index] = textoR[index].split(';')
        return textoR
    except:
        print("O arquivo é invalido")

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#validação do tecnico
def validarT():
    try:
        validT = abrir_arquivoT()
        validE = abrir_arquivoE()
        
        for index in range(len(validT)):        #O contador index percorrera toda a "matriz"(lista dentro de lista) do arquivo exemplo
            for indice in range(len(validE)):   #O contador indice percorrera toda a "matriz"(lista dentro de lista) do arquivo tecnicos
                if validE[indice][0] == validT[index][0]: #depois ele comparara o valor  que esta na posição equivalente ao contador do primeiro for que é referente a primeira listas e na segunda lista procurar na posição 0 do arquivo exemplo com o valor de cado posição do arquivo tecnico e repetira o laço sempre adicionando 1 quando os valores encontrados forem iguais
                    cont = 1   
        if cont == 1:   #se ao final o contador dentro da condição for igual ao tamanho total do arquivo menos 1 que é equivalente a primeira linha descritiva ele considerara aquela residencia se não descartara 
            return 1
    except:
        print("Dados invalidos")
    
 #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

 # bloco referente a domicilios       
def contar_domicilios(): #função para contar domicilios
    try:
        contdom = abrir_arquivoE() #atribuindo a "matriz" da pesquisa a uma variavel
        dom = 0
        for j in range (len(contdom)): # fazendo um contador percorrer toda a lista e ir adicionando 1 a cada linha para saber o numero de domicilios pesquisados 
            dom+=1
        return dom - 1 # desconsiderando a primeira linha referente as perguntas da pesquisa e retornando o valor
    except:
        print("Dados invalidos")

def domicilio_particular_pago(): #função para checar os domiciolios particulares ja pagos
    try:
        domParticularP = abrir_arquivoE()
        domPaticularPago = 0
        for cont in range(len(domParticularP)): 
            if domParticularP[cont][5] == '1': #se a variavel referente a posição do contador do for na lista externa e da posição 5 na lista interna for igual a 1 ele adiciona 1 ao contador de domiciolios particulares pagos. OBS: o 1 ta entre aspas pq o python reconhece as informações do arquivo como string.
                domPaticularPago += 1
        return domPaticularPago #retornando o valor
    except:
        print("Dados invalidos")

def domicilio_particular_pagando(): #função para checar os domiciolios particulares ainda não quitados 
    try:
        domParticularPA = abrir_arquivoE()
        domParticularPagando = 0
        for cont in range(len(domParticularPA)):
            if domParticularPA[cont][5] == '2': #se a variavel referente a posição do contador do for na lista externa e da posição 5 na lista interna for igual a 2 ele adiciona 1 ao contador de domiciolios particulares pagos. OBS: o 2 ta entre aspas pq o python reconhece as informações do arquivo como string.
                domParticularPagando += 1
        return domParticularPagando
    except:
        print("Dados invalidos")

def domicilio_particular_aluguel(): #função para checar os domiciolios particulares pagando aluguel
    try:
        domParticularA = abrir_arquivoE()
        domParticularAluguel = 0
        for cont in range(len(domParticularA)):
            if domParticularA[cont][5] == '3': #se a variavel referente a posição do contador do for na lista externa e da posição 5 na lista interna for igual a 3 ele adiciona 1 ao contador de domiciolios particulares pagos. OBS: o 3 ta entre aspas pq o python reconhece as informações do arquivo como string.
                domParticularAluguel += 1
        return domParticularAluguel
    except:
        print("Dados invalidos")

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#função para identificar cidades iguais para contagem de banheiros 
def banheiro_cidade():
    try:
        city = abrir_arquivoR()
        questionario = abrir_arquivoE()
        contar = 0
        result = 0
        result2 = 0
        lista_banheiro = []
        for flag in range(len(city)):
            for check in range(len(questionario)):
                if city[flag][2] in questionario[check][1]:#Comparando se os codigos IBGE são iguais pra checar cidade 
                    if questionario[check][5] != '0' and questionario[check][5]!= '-': #conferindo se as respostas são validas 
                        #bloco responsavel por transformar as strings das perguntas em inteiros e somar o numero de banheiros
                        if questionario[check][5] == '1':
                            num = 1
                            contar += num
                        elif questionario[check][5] == '2':
                            num = 2
                            contar += num
                        elif questionario[check][5] == '3':
                            num = 3
                            contar += num
                        elif questionario[check][5] == '4':
                            num = 4
                            contar += num
                        elif questionario[check][5] == '5':
                            num = 5
                            contar += num
                        elif questionario[check][5] == '6':
                            num = 6
                            contar += num
                        elif questionario[check][5] == '7':
                            num = 7
                            contar += num
                        elif questionario[check][5] == '8':
                            num = 8
                            contar += num
                        else:
                            num = 9
                            contar +=num
                        result = city[flag][1], contar # Pega a cida e o valor final do numero de banheiros da cidade
                    else :
                        result2 += 1 #numero de casas sem banheiros da cidade
                    lista_banheiro.append(result)
                    lista_banheiro.append(result2)
        return lista_banheiro #retornando a cidade o numero de banheiros da cidade e o numero de casas sem banheiros na cidade respctivamente 
    except:
        print("Dados invalidos")

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#função pra checar o abastecimento de agua;
def abastecimento_agua():
    try:
        city = abrir_arquivoR()
        questionario = abrir_arquivoE()
        contando1 = 0
        contando2 = 0
        contando3 = 0
        contando4 = 0
        contando5 = 0
        contando6 = 0
        contando7 = 0
        contando8 = 0
        contando9 = 0
        contando10 = 0
        lista_agua = []
        re = 0
        resposta = 0
        for flag in range(len(city)):
            for check in range(len(questionario)):
                if city[flag][2] in questionario[check][1]:#Comparando se os codigos IBGE são iguais pra checar cidade 
                    if questionario[check][9] != '0' and questionario[check][9]!= '-': #conferindo se as respostas são validas 
                        #bloco responsavel por transformar as strings das perguntas em inteiros e somar as resposta
                        if questionario[check][9] == '1':
                            nume = 1
                            contando1 += nume
                        elif questionario[check][9] == '2':
                            nume = 2
                            contando2 += nume
                        elif questionario[check][9] == '3':
                            nume = 3
                            contando3 += nume
                        elif questionario[check][9] == '4':
                            nume = 4
                            contando4 += nume
                        elif questionario[check][9] == '5':
                            nume = 5
                            contando5 += nume
                        elif questionario[check][9] == '6':
                            nume = 6
                            contando6 += nume
                        elif questionario[check][9] == '7':
                            nume = 7
                            contando7 += nume
                        elif questionario[check][9] == '8':
                            nume = 8
                            contando8 += nume
                        elif questionario[check][9] == '9':
                            nume = 9
                            contando9 += nume
                        elif  questionario[check][9] == '10':
                            nume = 10
                            contando10 += nume
                        else:
                            print("Resposta invalida")
                        #bloco que checa a fomar mais comum de abastecimento
                        if contando1 > contando2 and contando1 > contando3 and contando1 > contando4 and contando1 > contando5 and contando1 > contando6 and contando1 > contando7 and contando1 > contando8 and contando1 > contando9 and contando1 > contando10:
                            re = 1
                        elif contando2 > contando1 and contando2 > contando3 and contando2 > contando4 and contando2 > contando5 and contando2 > contando6 and contando2 > contando7 and contando2 > contando8 and contando2 > contando9 and contando2 > contando10:
                            re = 2
                        elif contando3 > contando1 and contando3 > contando2 and contando3 > contando4 and contando3 > contando5 and contando3 > contando6 and contando3 > contando7 and contando3 > contando8 and contando3 > contando9 and contando3 > contando10:
                            re = 3
                        elif contando4 > contando1 and contando4 > contando2 and contando4 > contando3 and contando4 > contando5 and contando4 > contando6 and contando4 > contando7 and contando4 > contando8 and contando4 > contando9 and contando4 > contando10:
                            re = 4
                        elif contando5 > contando1 and contando5 > contando2 and contando5 > contando3 and contando5 > contando4 and contando5 > contando6 and contando5 > contando7 and contando5 > contando8 and contando5 > contando9 and contando5 > contando10:
                            re = 5
                        elif contando6 > contando1 and contando6 > contando2 and contando6 > contando3 and contando6 > contando4 and contando6 > contando5 and contando6 > contando7 and contando6 > contando8 and contando6 > contando9 and contando6 > contando10:
                            re = 6
                        elif contando7 > contando1 and contando7 > contando2 and contando7 > contando3 and contando7 > contando4 and contando7 > contando5 and contando7 > contando6 and contando7 > contando8 and contando7 > contando9 and contando7 > contando10:
                            re = 7
                        elif contando8 > contando1 and contando8 > contando2 and contando8 > contando3 and contando8 > contando4 and contando8 > contando5 and contando8 > contando6 and contando8 > contando7 and contando8 > contando9 and contando8 > contando10:
                            re = 8
                        elif contando9 > contando1 and contando9 > contando2 and contando9 > contando3 and contando9 > contando4 and contando9 > contando5 and contando9 > contando6 and contando9 > contando7 and contando9 > contando8 and contando9 > contando10:
                            re = 9
                        elif contando10 > contando1 and contando10 > contando2 and contando10 > contando3 and contando10 > contando4 and contando10 > contando5 and contando10 > contando6 and contando10 > contando7 and contando10 > contando8 and contando10 > contando9:
                            re = 10
                        else:
                            print('resposta invelida')
                    resposta = city[flag][1], re
                    lista_agua.append(resposta)
        return lista_agua
    except:
        print("Dados invalidos")
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def energia():
    try:
        city = abrir_arquivoR()
        questionario = abrir_arquivoE()
        SemEnergia = 0
        Total = 0
        percentual = 0
        Resultado = 0
        lista_energia = []
        for flag in range(len(city)):
            for check in range(len(questionario)):
                if city[flag][2] in questionario[check][1]:#Comparando se os codigos IBGE são iguais pra checar cidade 
                    if questionario[check][11] != '0' and questionario[check][11]!= '-': #conferindo se as respostas são validas 
                        if questionario[check][11] == '3':
                            SemEnergia += 1 #conta domicilios sem energia 
                    Total += 1
                    percentual = (SemEnergia*100)/Total #calcula a porcentagem
                    Resultado = city[flag][1], round(percentual,2)
                    lista_energia.append(Resultado)
                    

        return lista_energia 
    except:
        print("Dados invalidos")

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#função para checar etinia 
def etnia():
    try:
        pesq = abrir_arquivoE()
        branca = 0
        preta = 0
        amarela = 0
        parda = 0 
        indigina = 0
        pessoas = 0
        porcent_branca = 0
        porcent_preta = 0
        porcent_amarela = 0
        porcent_parda = 0 
        porcent_indigina = 0
        Porcent_Total = 0
        for load in range (len(pesq)):
            if pesq[load][18] != '0' and pesq[load][18]!= '-':
                #bloco que pega as respostas e faz os acrescimos 
                if pesq[load][18] == '1':
                    branca += 1
                elif pesq[load][18] == '2':
                    preta += 1
                elif pesq[load][18] == '3':
                    amarela += 1
                elif pesq[load][18] == '4':
                    parda += 1
                elif pesq[load][18] == '5':
                    indigina +=1 
            pessoas+=1 #variavel que pega todas as respostas
        #bloco que calcula o percentual por etnia
        porcent_branca = (branca*100)/pessoas
        porcent_preta = (preta*100)/pessoas
        porcent_amarela = (amarela*100)/pessoas
        porcent_parda = (parda*100)/pessoas
        porcent_indigina = (indigina*100)/pessoas
        Porcent_Total = round(porcent_branca,2),round(porcent_preta,2),round(porcent_amarela,2),round(porcent_parda,2),round(porcent_indigina,2)
        return Porcent_Total
    except:
        print("Dados invalidos")
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#validar região
def regioes():
    try:
        R = abrir_arquivoR()
        E = abrir_arquivoE()
        cont_Nordeste =0
        cont_Sudeste = 0
        cont_Norte = 0
        cont_Sul = 0
        cont_CE = 0
        for index in range(len(E)):        #O contador index percorrera toda a "matriz"(lista dentro de lista) do arquivo exemplo
            for indice in range(len(R)):   #O contador indice percorrera toda a "matriz"(lista dentro de lista) do arquivo regioes
                if E[index][1] in R[indice][2]:#procurando codigo ibge do arquivo exemplo no arquivo regioes se encontar procurar a sigla do estado e validara a informação;
                    #localizando região do estado e contando quantas pesquisas daquela região tem no questionarios;
                    if R[indice][3] == 'MA' or R[indice][3] == 'PI' or R[indice][3] == 'CE' or R[indice][3] == 'RN' or R[indice][3] == 'PE' or R[indice][3] == 'PB' or R[indice][3] == 'SE' or R[indice][3] == 'AL'or R[indice][3] == 'BA':
                        cont_Nordeste+=1
                    elif R[indice][3] == 'AM' or R[indice][3] == 'RR' or R[indice][3] == 'AP' or R[indice][3] == 'PA' or R[indice][3] == 'TO' or R[indice][3] == 'RO' or R[indice][3] == 'AC':
                        cont_Norte+=1
                    elif R[indice][3] == 'MT' or R[indice][3] == 'MS' or R[indice][3] == 'GO':
                        cont_CE+=1
                    elif R[indice][3] == 'SP' or R[indice][3] == 'RJ' or R[indice][3] == 'ES' or R[indice][3] == 'MG':
                        cont_Sudeste+=1
                    elif R[indice][3] == 'PR' or R[indice][3] == 'RS' or R[indice][3] == 'SC':
                        cont_Sul+=1
                    else:
                        print("Regiao invalida")
            #checando qual região tem o maior numero de pesquisas;
            if cont_Nordeste > cont_CE and cont_Nordeste > cont_Norte and cont_Nordeste > cont_Sudeste and cont_Nordeste > cont_Sul:
                return "Nordeste"
            elif cont_CE > cont_Nordeste and cont_CE > cont_Norte and cont_CE > cont_Sudeste and cont_CE > cont_Sul:
                return "Centro-Oeste"
            elif cont_Norte > cont_CE and cont_Norte > cont_Nordeste and cont_Norte > cont_Sudeste and cont_Norte > cont_Sul:
                return "Norte"
            elif cont_Sudeste > cont_Nordeste and cont_Sudeste > cont_Norte and cont_Sudeste > cont_CE and cont_Sudeste > cont_Sul:
                return "Sudeste"
            elif cont_Sul > cont_Nordeste and cont_Sul > cont_Norte and cont_Sul > cont_Sudeste and cont_Sul > cont_CE:
                return "Centro-Oeste"
    except:
        print("Dados invalidos")
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def main():
    VT = validarT() #função validar tecnicos(VT)
    CD = contar_domicilios() #função que conta os domicilio(CD)
    DPPndo = domicilio_particular_pagando() #função dos domicilios particulares não quitados
    DPP = domicilio_particular_pago() #função dos domicilios particulares pagos
    DPA = domicilio_particular_aluguel() #função dos domicilios particulares alugados 
    BC = banheiro_cidade() #função dos banheiros por cidade
    AG = abastecimento_agua() #função que checa o abastecimento de agua por cidade 
    ENER = energia() #função que checa a energia eletrica por cidade
    COR = etnia() #função que checa a etnia 
    reg = regioes() #função que checa as regiões
    loop = True

    if VT == 1:
        print("\n                  Sistema para o Censo Demográfico de 2020 \n                (Acesso exclusivo para tecnicos cadastrados)\n\n")
        x = int(input("\nDigite 1 para exibir todas as informações de vez;\n\nDigite 2 para selecionar uma de cada vez;\n\nSelecionar opção: "))
        if x == 1:
            print('\nNúmeros de domicílios utilizados para a coleta: {}'.format(CD))
            print('\nNúmero de domicílios particulares que já estão pagos: {}\n Domicílios particulars que ainda estão pagando: {}\n Domicílios particulares alugados: {}'.format(DPP,DPPndo,DPA))
            print('\nCidade e quantidade de banheiro respectivamente: {}'.format(BC))
            print('\nForma mais comum de abastecimento de agua(cidade/quantidade, respectivamente): {}'.format(AG))
            print('\nCidade e percentual de domicilio que ainda não possue energia elétrica respectivamente: {}'.format(ENER))
            print('\nO percentual de moradores que participaram da entrevista por cor ou raça: {}'.format(COR))
            print('\nA região com maior número de municípiospesquisados: {}'.format(reg))
        elif x == 2:
            while loop == True:
                selecionar = int(input("Digite a opção que deseja: Para exibir números de domicílios utilizados para a coleta digite 1;\n\nPara exibir números de domicílios particulares que já estão pagos digite 2\n\nPara exibir a cidade e quantidade de banheiro respectivamente digite 3\n\nPara exibir a forma mais comum de abastecimento de agua digite 4\n\nPara exibir a cidade e percentual de domicilio que ainda não possue energia elétrica digite 5\n\nPara exibir o percentual de moradores que participaram da entrevista por cor ou raça digite 6\n\nPara exibir a região com maior número de municípios pesquisados digite 7\n\nSelecionar opção: \n\n"))
                if selecionar == 1:
                    print('Números de domicílios utilizados para a coleta: {}'.format(CD))
                elif selecionar == 2:
                    print('Número de domicílios particulares que já estão pagos: {}\n Domicílios particulars que ainda estão pagando: {}\n Domicílios particulares alugados: {}'.format(DPP,DPPndo,DPA))
                elif selecionar == 3:
                    print('Cidade e quantidade de banheiro respectivamente: {}'.format(BC))
                elif selecionar == 4:
                    print('Forma mais comum de abastecimento de agua(cidade/quantidade, respectivamente): {}'.format(AG))
                elif selecionar == 5:
                    print('Cidade e percentual de domicilio que ainda não possue energia elétrica respectivamente: {}'.format(ENER))
                elif selecionar == 6:
                    print('O percentual de moradores que participaram da entrevista por cor ou raça: {}'.format(COR))
                elif selecionar == 7:
                    print('A região com maior número de municípiospesquisados: {}'.format(reg))
                else:
                    print("Opção invalida")
                sair = int(input("Digite 0 para sair: "))
                if sair == 0:
                    break
            
    return main()

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

print(main())
input()
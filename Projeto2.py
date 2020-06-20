 """   ////////////////////////////////////////////////////////////////////////////
      /////            Between The Math & Science - The Game                 /////
     /////                          Version: 1.1                            /////
    /////                          Daniel Kauffman                         /////
   /////                           Lucas Garcia                           /////
  /////                            Matheus Chang                         /////
 /////                             Rodrigo Limongi                      /////
////////////////////////////////////////////////////////////////////////////"""



from tkinter import *
import random
import os

# Inicialização da tela inicial e título da aba
inicial = Tk()
inicial.title("Between The Math & Science - The Game")
# fim da inicialização

pontos = 0
fechar = 1
dificuldade = ''

# Ajuste de tela
windowWidth = inicial.winfo_reqwidth()
windowHeight = inicial.winfo_reqheight()
positionRight = int(inicial.winfo_screenwidth()/7 - windowWidth/3)
positionDown = int(inicial.winfo_screenheight()/4 - windowHeight/2)
# Seta as dimensões da tela
inicial.geometry("900x700+{}+{}".format(positionRight+300, positionDown))
# Fim do ajuste de tela

# Randomização das perguntas
lista_perguntas_inicial = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
random.shuffle(lista_perguntas_inicial)
lista_perguntas = []
y = 0
z = 0

# Nivel de dificuldade
lista_perguntasFacil = [2,3,5,8,11,13,15]
random.shuffle(lista_perguntasFacil)
lista_perguntasMedio = [1,9,12,14,16,18,20]
random.shuffle(lista_perguntasMedio)
lista_perguntasDificil = [4,6,7,10,17,19]
random.shuffle(lista_perguntasDificil)


# Concatenar listas e escolher dificuldade
def concatenador(lista_dificuldade, lista_perguntas_inicial):
  for k in lista_perguntas_inicial:
    if k in lista_dificuldade:
        pass
    else:
        lista_dificuldade.append(k)
  global lista_perguntas
  lista_perguntas = lista_dificuldade


# Gabarito
lista_respostas = [1.4,2.1,3.1,4.1,5.4,6.3,7.4,8.3,9.5,10.2,11.1,12.3,13.4,14.5,15.2,16.5,17.2,18.3,19.5,20.2]

# Dicionários
perguntas = {1: "Qual é a fórmula da elipse?", #Médio
             2: "Qual é o delta dessa função de 2º grau?\n x² - 5x + 6 = 0", #Facil
             3: "Qual Lei de Newton representa a Lei da Inércia?", #Facil
             4: "Qual é o volume de um cilindro com raio de 2 metros e\naltura  de 10 metros? Considere π = 3,14.", #Dificil
             5: "Qual sufixo representa a presença de\nligações duplas em um hidrocarboneto?", #Facil
             6: "Como se dá a relação entre a resistência e a corrente elétrica?", #Dificil
             7: "Qual é o valor da constante que representa a\nvelocidade da luz no vácuo?", #Dificil
             8: "Quantas senhas com 4 algarismos diferentes podemos\nescrever com os algarismos 1, 2, 3, a, b, c, !, @, # ?", #Facil
             9: "Um móvel parte de repouso e desenvolve uma aceleração\nconstante de 3 m/s² durante 4 segundos.\nO deslocamento desse móvel foi de:", #Media
             10: "Qual das propriedades periódicas a seguir representa\ntendência de um átomo a atrair elétrons para si?", #Dificil
             11: "O césio-137 tem uma meia vida igual a 30 anos. Caso \ntenhamos 48 g desse elemento, após passarem-se 120 anos,\nquanto de massa teremos dele?", #Facil
             12: "Dos elementos da tabela periódica apresentados a\nseguir qual deles possui 3 elétrons na camada de valência?", #Media
             13: "Qual dos seguintes cientistas foi responsável pelo modelo\ndo átomo apelidado de ‘pudim com passas’?", #Facil
             14: "Qual dos ácidos a seguir é o menos volátil?", #media
             15: "Entre a água, o vinagre, o gás oxigênio e o sal de cozinha,\nqual deles é uma substância simples?", #Facil
             16: "Resolva a seguinte inequação: \n 3(1 - 2x) < 2(x + 1) + x  7:", #Media
             17: "Faça a conversão de 2 * 10⁵ ml para metros cúbicos,\nresultado é igual a:", #Dificl
             18: "Calcule a diferença da área dos dois círculos,\nonde primeiro possui 35 cm de raio e o segundo 25 cm", #Media
             19: "Determine a frequência com um comprimento de onda igual\n a 1 m, sabendo que a velocidade do som no ar é igual a 340 m/s.", #dificil
             20: "Considerando um gás ideal, tendo somente 1 mol,\nsob um temperatura de 273 K e uma pressão de 1 atm,\nqual é o seu volume?\n\nConsidere R = 0,082 atm*L/mol*K"} #media

alternativas = {1.1: "x² + y²/3 = 0",
                1.2: "x³/a + y²/2 = 1",
                1.3: "x²/a = -y³/b",
                1.4: "x²/a² + y²/b² = 1", #correta 1 d)
                1.5: "x² - a²/3y² = 0",
                2.1: "1", #correta 2 a)
                2.2: "0",
                2.3: "4",
                2.4: "16",
                2.5: "38",
                3.1: "1° Lei", #correta 3 a)
                3.2: "2° Lei",
                3.3: "3° Lei",
                3.4: "4° Lei",
                3.5: "5° Lei",
                4.1: "125,6 m³", #correta 4 a)
                4.2: "123,8 m³", 
                4.3: "75,3  m³",
                4.4: "79,7  m³",
                4.5: "78,8  m³",
                5.1: "ano",
                5.2: "diano",
                5.3: "ino",
                5.4: "eno", #correta 5 d)
                5.5: "dieno",
                6.1: "A corrente e a resistência são diretamente proporcionais.",
                6.2: "A corrente e a resistência não se relacionam.",
                6.3: "A corrente e a resistência são inversamente proporcionais.", #correta 6 c)
                6.4: "A corrente e a resistência sempre possuem o mesmo valor.",
                6.5: "Nenhuma das alternativas acima está correta.",
                7.1: "2 x 10⁶ m/s",
                7.2: "3 x 10⁷ m/s",
                7.3: "2 x 10⁸ km/s",
                7.4: "3 x 10⁵ km/s", #correta 7 d)
                7.5: "2 x 10⁶ km/s",
                8.1: "2048",
                8.2: "4124",
                8.3: "3024", #correta 8 c)
                8.4: "1890",
                8.5: "1024",
                9.1: "18 m",
                9.2: "22 m",
                9.3: "30 m", 
                9.4: "12 m",
                9.5: "24 m", #correta 9 e)
                10.1: "Eletroafinidade",
                10.2: "Eletronegatividade", #correta 10 b)
                10.3: "Eletropositividade",
                10.4: "Potencial de Ionização",
                10.5: "Eletroneutralidade",
                11.1: "3  g", #correta 11 a)
                11.2: "12 g",
                11.3: "6 g",
                11.4: "24 g",
                11.5: "48 g",
                12.1: "Potássio (K)",
                12.2: "Fósforo (P)",
                12.3: "Nihônio (Nh)", # correta 12 c)
                12.4: "Ferro (Fe)",
                12.5: "Sódio (Na)",
                13.1: "Chadwick",
                13.2: "Dalton",
                13.3: "Rutherford",
                13.4: "Thomson", #correta 13 d)
                13.5: "Newton",
                14.1: "NaCl",
                14.2: "HF",
                14.3: "HI",
                14.4: "H₂SO₃",
                14.5: "H₂SO₄", #correta 14 e)
                15.1: "Água",
                15.2: "Gás oxigênio", #correta 15 b)
                15.3: "Vinagre", 
                15.4: "Sódio",
                15.5: "Sal de cozinha",
                16.1: "x < 9/8",
                16.2: "x > 3/2",
                16.3: "x < 7/3",
                16.4: "x < 2/7",
                16.5: "x > 8/9", #correta 16 e)
                17.1: "0,002",
                17.2: "0,02", #correta 17 b)
                17.3: "0,0002",
                17.4: "0,2",
                17.5: "0,00002",
                18.1: "100π cm²",
                18.2: "300π cm²",
                18.3: "600π cm²", #correta 18 c)
                18.4: "900π cm²",
                18.5: "1200π cm²",
                19.1: "10 Hz",
                19.2: "25 Hz",
                19.3: "15 Hz",
                19.4: "30 Hz",
                19.5: "20 Hz", #correta 19 e)
                20.1: "2,24 L",
                20.2: "22,4 L", #correta 20 b)
                20.3: "224 L",
                20.4: "224,4 L",
                20.5: "24,2 L"}

explic = {1: "A fórmula correta da elipse é x²/a² + y²/b² = 1" ,
          2: "A fórmula para calcular o delta é b² - 4*a*c\n Dessa forma, (-5²) - 4*1*6 = 25 - 24 = 1" ,
          3: "A Lei correspondente a lei da inércia é a 1º Lei.\nEsta lei diz que todo corpo permanece emseu estado de repouso ou\nem movimento retilíneo e uniforme caso as forças que atuem sobre ele se anulem.",
          4: "A fórmula do volume do clindro é V = π*R²*h.\n Dessa forma, conta ficaria V = 3.14*2²*10 = 125,6m³.",
          5: "De acordo com a IUPAC, o sufixo 'eno' representa a presença de\nligação dupla no hidrocarboneto",
          6: "De acordo com a fórmula da 1º Lei de Ohm:\nU = r*i\nPode-se comprovar matematicamente que a resistência elétrica e a\ncorrentelétrica são grandezas inversamentes proporcionais.",
          7: "A alternativa que representa corretamente a velocidade da luz vácuo é a\nd) 3 x 10^5 km/s\nque equivale, em metros posegundo, à 3 x 10^8 m/s .",
          8: "Como a questão pedia 4 algarismos diferentes, o número de possibilidades\ndeveria ser diminuído em 1 para cada novalgarismo.\nComo são 10 algarismos no total, a contficará: 9*8*7*6 = 3024.",
          9: "A função da posição no Movimento Uniforme Variado é:\nDeltaS = v0 * t + a * t²/2\nDessa forma, 0 * 3 + 3 * 4²/2 = 2 metros.",
          10: "A eletronegatividade é um propriedade que faz com que molécula\natraia elétrons adjacentes para si numa ligação químiccovalente.",
          11: "A cada vez que o tempo de meia vida passa,\na massa de um elemento divide por 2, então após 120 anos,\na massa divide por quatro vezes (já que 120/30=4), resultando em 3 gramas de césio-137",
          12: "A resposta correta é o elemento nihônio, pois ele pertence família 3A,\ne os que estão nessa família possuem 3 elétrons na camada de valência.",
          13: "Thomson foi responsável pela ideia de um átomo ser positivo\ncom partículas negativas nele,fazendo com que o modelo se parecesse com um pudim\ncom passas, dando origem ao apelido.",
          14: "H2SO4, o ácido sulfúrico, é o ácido menos volátil\npor ser considerado como um ácido fixo.",
          15: "O gás oxigênio é uma substância simples por ser formado por\ndois átomos do mesmo elemento químico, o oxigênio.",
          16: "Calculamos a inequação, fazemos a distribuição\n3 - 6x < 2x + + x - 7 até o seu resultado final x > 8/9",
          17: "Para calcularmos, dividimos o valor por 1e+6",
          18: "Para calcularmos a diferença, primeiros utilizamos a fórmula área que é\nA = π · r²\nentão subtraímos o valor do círculo grande com o menor e obtemos o resultado 600π cm²",
          19: "Utilizamos a fórmula f = v ÷ λ, assim substituindo os\nvalores chegando ao resultado.",
          20: "Por ser um gás ideal conseguimos usar a equação de Clapeyron que é\np*V = n*R*T\nentão substituindo os valores na equação fica 1*V = 1*0,082*273, assim V = 22,4 L." }
# Fim dos Dicionários


# Funções iniciais: identificação, jogar, regras e sair

def identificação():
    identificar = Tk()
    identificar.title('Identificação do Jogador - Between The Math and Science')

    identificar.geometry("900x700+{}+{}".format(positionRight+300, positionDown))

    def dados():
      global usuario
      usuario = nome.get()

      erroNome = Label(identificar, text='Digite um nome', font=('Arial', 14))
      erroNome.place(relx=0.5, rely=0.22, anchor=N)
      
      if usuario != '':
        erroNome['text'] = 'Nome armazenado'
        erroNome['bg'] = 'green'

    def botaoFacil():
      global dificuldade
      dificuldade = 'facil'
      dificuldadeMedia['bg'] = 'white'
      dificuldadeDificil['bg'] = 'white'
      dificuldadeFacil['bg'] = 'green'

    def botaoMedio():
      global dificuldade
      dificuldade = 'medio'
      dificuldadeDificil['bg'] = 'white'
      dificuldadeFacil['bg'] = 'white'
      dificuldadeMedia['bg'] = 'orange'

    def botaoDificil():
      global dificuldade
      dificuldade = 'dificil'
      dificuldadeMedia['bg'] = 'white'
      dificuldadeFacil['bg'] = 'white'
      dificuldadeDificil['bg'] = 'red'

    def botaoJogar():
      if dificuldade != '' and usuario != '':
        identificar.destroy()
        if dificuldade == 'facil':
          concatenador(lista_perguntasFacil, lista_perguntas_inicial)
        elif dificuldade == 'medio':
          concatenador(lista_perguntasMedio, lista_perguntas_inicial)
        else:
          concatenador(lista_perguntasDificil, lista_perguntas_inicial)
      else:
        dados()
        erroDificuldade = Label(identificar, text='Selecione uma dificuldade por favor.', font=('Arial, 14'))
        erroDificuldade.place(relx=0.5, rely=0.95, anchor=S)

    tituloUsuario = Label(identificar, text = 'Escreva seu nome abaixo', font=('Gothic', 32, "bold"), fg = 'green')
    nome = Entry(identificar, width=30, font=('Arial', 20))
    confirmarNome = Button(identificar, width=15, text = 'Confirmar', font=(16), command=dados)
    textDificuldade = Label(identificar, text = 'Selecione a dificuldade do Quiz:', font=('Gothic', 32, "bold"), fg = 'black')

    dificuldadeFacil = Button(identificar, text = 'Dificuldade Fácil', width=20, font=('Arial', 18), command=botaoFacil)
    dificuldadeMedia = Button(identificar, text = 'Dificuldade Média', width=20, font=('Arial', 18), command=botaoMedio)
    dificuldadeDificil = Button(identificar, text = 'Dificuldade Difícil', width=20, font=('Arial', 18), command=botaoDificil)
    comecarJogo = Button(identificar, text = 'JOGAR', width=20, font=('Arial', 22, 'bold'), command=botaoJogar)

    tituloUsuario.place(relx=0.5, rely=0, anchor=N)
    nome.place(relx=0.5, rely=0.1, anchor=N)
    confirmarNome.place(relx=0.5, rely=0.16, anchor=N)
    textDificuldade.place(relx = 0.5, rely = 0.3, anchor=CENTER)

    dificuldadeFacil.place(relx=0.5, rely=0.5, anchor=S)
    dificuldadeMedia.place(relx=0.5, rely=0.58, anchor=S)
    dificuldadeDificil.place(relx=0.5, rely=0.66, anchor=S)
    comecarJogo.place(relx=0.5, rely=0.9, anchor=S)

    identificar.mainloop()


def getGame():
    global z, fechar

    # Fecha a tela inicial ou da pergunta anterior
    if fechar == 1:
      inicial.destroy()
      identificação()
      if dificuldade == '' or usuario == '':
        exit()

    # Inicialização da tela das regras e título da aba
    jogo = Tk()
    jogo.title("Perguntas - Between The Math and Science")
    # fim da inicialização

    # Ajuste de tela
    jogo.geometry("900x700+{}+{}".format(positionRight+300, positionDown))
    # fim do ajuste de tela

    def verificação(y,z):
      global pontos
      if (x+y) in lista_respostas:
        pontos += 1
        jogo.destroy()
        if pontos == 20:
          feedback(x)
        else:
          getGame()
      else:
        jogo.destroy()
        feedback(x)


    def y_alt1():
        y = 0.1
        verificação(y,z)


    def y_alt2():
        y = 0.2
        verificação(y,z)


    def y_alt3():
        y = 0.3
        verificação(y,z)

        
    def y_alt4():
        y = 0.4
        verificação(y,z)
    
    def y_alt5():
        y = 0.5
        verificação(y,z)
        


    # Alternativas
    x = lista_perguntas[z]
    y = 0.1
    z += 1

    # Fechar apenas a janela de jogo em diante
    fechar += 1
    
    perguntaQ = Label(jogo, text=perguntas[x], fg = 'black', font=('Arial', 20))

    letraA = Label(jogo,
                  text='a)',
                  font=('Arial', 16, 'bold'))

    alt1 = Button(jogo,
                  text=alternativas[x+y],
                  width=50,
                  height=2,
                  font=('Arial', 12),
                  command = y_alt1)

    y += 0.1

    letraB = Label(jogo,
                  text='b)',
                  font=('Arial', 16, 'bold'))

    alt2 = Button(jogo,
                  text=alternativas[x+y],
                  width=50,
                  height=2,
                  font=('Arial', 12),
                  command=y_alt2)

    y += 0.1

    letraC = Label(jogo,
                  text='c)',
                  font=('Arial', 16, 'bold'))

    alt3 = Button(jogo,
                  text=alternativas[x+y],
                  width=50,
                  height=2,
                  font=('Arial', 12),
                  command=y_alt3)

    y += 0.1

    letraD = Label(jogo,
                  text='d)',
                  font=('Arial', 16, 'bold'))

    alt4 = Button(jogo,
                  text=alternativas[x+y],
                  width=50,
                  height=2,
                  font=('Arial', 12),
                  command=y_alt4)

    y += 0.1

    letraE = Label(jogo,
                  text='e)',
                  font=('Arial', 16, 'bold'))

    alt5 = Button(jogo,
                  text=alternativas[x+y],
                  width=50,
                  height=2,
                  font=('Arial', 12),
                  command=y_alt5)

    
    pontuacao = Label(jogo, text='Pontuação:', font=('Arial', 16))
    pontuacaonum = Label(jogo, text=pontos, font=('Arial', 16), fg='#006600')
    pontuacao.place(relx=0.9, rely=0.7, anchor=CENTER)
    pontuacaonum.place(relx=0.97, rely=0.7, anchor=CENTER)


    alt1.place(relx = 0.05, rely = 0.4, anchor = W)
    letraA.place(relx = 0, rely = 0.4, anchor = W)
    alt2.place(relx = 0.05, rely = 0.5, anchor = W)
    letraB.place(relx = 0, rely = 0.5, anchor = W)
    alt3.place(relx = 0.05, rely = 0.6, anchor = W)
    letraC.place(relx = 0, rely = 0.6, anchor = W)
    alt4.place(relx = 0.05, rely = 0.7, anchor = W)
    letraD.place(relx = 0, rely = 0.7, anchor = W)
    alt5.place(relx = 0.05, rely = 0.8, anchor = W)
    letraE.place(relx = 0, rely = 0.8, anchor = W)
    perguntaQ.place(relx = 0.5, rely = 0, anchor = N)


    # Repetição da janela do jogo
    jogo.mainloop()


def getQuit():
    # Fecha a tela inicial
    inicial.destroy()
    # Fecha o código
    exit()


def fbquit():
    fb.destroy()
    exit()


def fbrestart():
    os.execl(sys.executable, sys.executable, * sys.argv)
    

def feedback(x):
    global fb
    # Inicializa a janela de feedback e renomeia
    fb = Tk()
    fb.title("Feedback - Between The Math and Science")
    
    # Dimensiona a janela de feedback
    fb.geometry("900x700+{}+{}".format(positionRight+300, positionDown))

    tituloFeed = Label(fb, text="VOCÊ ERROU", font=('Gothic', 32, "bold"), fg = 'red')
    justificativa = Label(fb, text = 'Justificativa:', font=('Arial', 23, "bold"), fg = 'black')
    resposta = Label(fb, text=explic[x], fg = 'black', font=('Arial', 18))
    tituloFeed.place(relx=0.5,rely=0,anchor=N)
    
    # Texto de feedback
    if pontos == 0:
      textofbprimario = "Noob"
      textofbsecundario = "Você tem muito a melhorar, estude mais!"
    elif pontos > 0 and pontos < 6:
      textofbprimario = "Novice"
      textofbsecundario = "Poderia ter sido melhor..."
    elif pontos > 5 and pontos < 11:
      textofbprimario = "Median"
      textofbsecundario = "Você tem potencial! Continue praticando."
    elif pontos > 10 and pontos < 16:
      textofbprimario = "Expert!"
      textofbsecundario = "Nada mal... Quero ver fazer melhor."
    elif pontos > 15 and pontos < 20:
      textofbprimario = "Professional!"
      textofbsecundario = "Você sabe das coisas."
    elif pontos == 20:
      tituloFeed['text'] = 'VOCÊ VENCEU!'
      tituloFeed['fg'] = '#66ff66'
      tituloFeed['font'] = ('Gothic', 72, "bold")
      tituloFeed.place(relx=0.5, rely=0.18, anchor=N)
      resposta['text'] = ''
      justificativa['text'] = ''
      textofbprimario = "Masterpiece!"
      textofbsecundario = "Você acertou tudo!!"
    else:
      pass


    # Textos 
    mensagemfb = Label(fb, text='%s, sua pontuação foi:' % usuario, font=('Gothic', 20, "bold"))
    pontuacao = Label(fb, text=pontos, font=('Gothic', 42, "bold"), fg = "#330000")
    textosfeedbackpri = Label(fb, text=textofbprimario, font=('Gothic', 52, "bold"), fg = '#b30000')
    textosfeedbacksec = Label(fb, text=textofbsecundario, font=('Gothic', 18, "bold"))
    nada = Label(fb, text='', width= 0, height=8)
    sair = Button(fb, text='SAIR', width=20, font=('Arial', 18, 'bold'), fg = '#b30000', command=fbquit)
    again = Button(fb, text='JOGAR NOVAMENTE', width=20, font=('Arial', 18, 'bold'), fg = '#006600', command=fbrestart)


    # Posicionamento dos Labels
    justificativa.place(relx=0, rely=0.15, anchor=W)
    resposta.grid(row=30, column=0)
    nada.grid(row=0, column=0)
    mensagemfb.place(relx= 0.5, rely= 0.5, anchor=S)
    pontuacao.place(relx = 0.5, rely= 0.6, anchor=S)
    textosfeedbackpri.place(relx=0.5,rely=0.75, anchor=S)
    textosfeedbacksec.place(relx=0.5,rely=0.80, anchor=S)
    sair.place(relx=0.3, rely=0.95, anchor=S)
    again.place(relx=0.7, rely=0.95, anchor=S)
    
# fim das funções


# Título do Jogo na janela inicial (adicionar cores)
titulo = Label(inicial, width=30, text='Between The Math & Science',
               font=('Gothic', '28', 'bold'))
titulo.place(relx=0.5, rely=0, anchor=N)


# Botões Tela Inicial
jogar = Button(inicial, text='INICIAR', width=20, height=2, font=('Arial', 22), fg='green', command=getGame)
sair = Button(inicial, text='SAIR', width=20, font=('Arial', 18, 'bold'), command=getQuit)
# Fim dos botões

# Labels de texto
preGame = Label(inicial,
                text='Leia as regras abaixo e\ninicie o quiz quando estiver pronto',
                font=('Consolas', 12))

rules = Label(inicial,
              text='Este Quiz possui 20 (vinte) questões sobre o tema exatas,\n'
              'você deve marcar a alternativa que julgar correta e seguir para a próxima questão.\n'
              'Caso você erre a questão, o jogo terminará e aparecerá uma explicação do resultado correto.\n'
              'No final do Quiz você receberá um feedback dos seus acertos.',
              width=800,
              bg = 'black',
              fg = '#FACA2F',
              font=('Times', 14))


# Localizações dos botões
jogar.place(relx=0.5, rely=0.2, anchor=N)
preGame.place(relx=0.5, rely=0.38, anchor=N)
rules.place(relx=0.5, rely=0.55, anchor=CENTER)
sair.place(relx=0.5, rely=0.8, anchor=S)
# fim das localizações


# Repetição da janela inicial
inicial.mainloop()
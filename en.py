perguntas = {1: "What is the equation for an ellipse??", #medium
             2: "Find the Discriminant:\n x² - 5x + 6 = 0", #easy
             3: "Which Newton's Law is the Law of Inertia?", #easy
             4: "What's the volume of a cylinder with a radius of 2 meters\n and height of 10m? Consider π = 3.14", #hard
             5: "Which suffix represents the\nDouble bond in a hydrocarbon?", #easy
             6: "How does the relationship between resistance and electric current take place?", #hard
             7: "What's the constant value of the\nspeed of light in vacuum?", #hard
             8: "How many passwords with 4 different digits\ncan we write with the following digits 1, 2, 3, a, b, c, !, @, # ?", #easy
             9: "An object in resting position starts moving constantly \n 3 m/s² durante 4 segundos.\nO deslocamento desse móvel foi de:", #medium
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
                3.1: "First Law", #correta 3 a)
                3.2: "Second Law",
                3.3: "Third Law",
                3.4: "Fourth Law",
                3.5: "Fifth Law",
                4.1: "125,6 m³", #correta 4 a)
                4.2: "123,8 m³", 
                4.3: "75,3  m³",
                4.4: "79,7  m³",
                4.5: "78,8  m³",
                5.1: "an",
                5.2: "dien",
                5.3: "in",
                5.4: "en", #correta 5 d)
                5.5: "diin",
                6.1: "The electric current and resistance are directly proportional.",
                6.2: "The electric current and resistance do not relate.",
                6.3: "The electric current and resistance are inversely proportional.", #correta 6 c)
                6.4: "The electric current and resistance always have the same value.",
                6.5: "None of the options are correct.",
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
                10.1: "Electro-affinity",
                10.2: "Electronegativity", #correta 10 b)
                10.3: "Electropositivity",
                10.4: "Ionization Potential",
                10.5: "Electroneutrality",
                11.1: "3  g", #correta 11 a)
                11.2: "12 g",
                11.3: "6 g",
                11.4: "24 g",
                11.5: "48 g",
                12.1: "Potassium (K)",
                12.2: "Phosphor (P)",
                12.3: "Nihonium (Nh)", # correta 12 c)
                12.4: "Iron (Fe)",
                12.5: "Sodium (Na)",
                13.1: "Chadwick", #rip
                13.2: "Dalton",
                13.3: "Rutherford",
                13.4: "Thomson", #correta 13 d)
                13.5: "Newton",
                14.1: "NaCl",
                14.2: "HF",
                14.3: "HI",
                14.4: "H₂SO₃",
                14.5: "H₂SO₄", #correta 14 e)
                15.1: "Water",
                15.2: "Oxigen Gas", #correta 15 b)
                15.3: "Vinegar salse", 
                15.4: "Sodium",
                15.5: "Salt",
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
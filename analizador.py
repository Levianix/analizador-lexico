from pprint import pprint
import ply.lex as lex

# resultado del analisis
resultado_lexema = []

reservada = (
    # Palabras Reservadas
    'INCLUDE',
    'USING',
    'NAMESPACE',
    'STD',
    'COUT',
    'CIN',
   'GET',
   'CADENA',
  'RETURN',
   'VOID',
    'INT',
    'ENDL',
)
tokens = reservada + (
    'IDENTIFICADOR',
    'ENTERO',
    'REAL',
    'ASIGNAR',

    'POSITIVO',
    'NEGATIVO',
    'MULT',
    'DIV',
    'POTENCIA',
    'MODULO',

   'MINUSMINUS',
   'PLUSPLUS',

    #Condiones
   'SI',
    'SINO',
    #Ciclos
   'MIENTRAS',
   'PARA',
    #logica
    'AND',
    'OR',
    'NOT',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORQUE',
    'MAYORIGUAL',
    'OPERELA',
    'DISTINTO',
    # Symbolos
    'NUMERAL',

    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'LLAIZQ',
    'LLADER',
    
    # Otros
    'PUNTOCOMA',
    'COMA',
    'COMDOB',
    'MAYORDER', #>>
    'MAYORIZQ', #<<
)

# Reglas de Expresiones Regualres para token de Contexto simple

t_POSITIVO = r'\+'
t_NEGATIVO = r'-'
t_MINUSMINUS = r'\-\-'
# t_PUNTO = r'\.'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'(\*{2} | \^)'

t_ASIGNAR = r'='
# Expresiones Logicas
t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PUNTOCOMA = ';'
t_COMA = r','
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'{'
t_LLADER = r'}'
t_COMDOB = r'\"'



def t_INCLUDE(t):
    r'include'
    return t

def t_USING(t):
    r'using'
    return t

def t_NAMESPACE(t):
    r'namespace'
    return t

def t_STD(t):
    r'std'
    return t

def t_COUT(t):
    r'cout'
    return t

def t_CIN(t):
    r'cin'
    return t

def t_GET(t):
    r'get'
    return t

def t_ENDL(t):
    r'endl'
    return t

def t_SINO(t):
    r'else'
    return t

def t_SI(t):
    r'if'
    return t

def t_RETURN(t):
   r'return'
   return t

def t_VOID(t):
   r'void'
   return t

def t_MIENTRAS(t):
    r'while'
    return t

def t_PARA(t):
    r'for'
    return t

def t_REAL(t):
    r'\d+[.]\d+'
    t.value = float(t.value)
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t

def t_CADENA(t):
   r'\"?(\w+ \ *\w*\d* \ *)\"?'
   return t

def t_NUMERAL(t):
    r'\#'
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_MENORIGUAL(t):
    r'<='
    return t

def t_MAYORIGUAL(t):
    r'>='
    return t

def t_OPERELA(t):
    r'=='
    return t

def t_MAYORDER(t):
    r'<<'
    return t

def t_MAYORIZQ(t):
    r'>>'
    return t

def t_DISTINTO(t):
    r'!='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    print("Comentario de multiple linea")

def t_comments_ONELine(t):
     r'\/\/(.)*\n'
     t.lexer.lineno += 1
     print("Comentario de una linea")
t_ignore =' \t'

def t_error(t):
    global resultado_lexema
    estado = "** Token no valido Valor {:6}".format(str(t.value))
    resultado_lexema.append(estado)
    t.lexer.skip(1)

# Prueba de ingreso
def prueba(data):
    global resultado_lexema
    auxI=" "
    auxX=" "
    auxP=" "
    auxMe=" "
    auxX2=" "
    auxPa=" "

    i=0

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        estado = "Tipo {:16} Valor {:5}".format(str(tok.type) ,str(tok.value))
        #print("tok.value: ",tok.value)

        # ENTERO
        if i<=1:
            if isinstance(tok.value, int):
                #cambiar estados después
                print("\t\t\tEstados 0->18->19")

        # FLOAT
            elif isinstance(tok.value, float):
                print("\t\t\tEstados 0->18->19->18")


        if i==0:
            auxI=tok.value
        elif i==1:
            auxX=tok.value
        elif i==2:
            auxP=tok.value
        elif i==3:
            auxMe=tok.value
        elif i==4:
            auxX2=tok.value
        elif i==5:
            auxPa=tok.value
        #print(tok.value)

        resultado_lexema.append(estado)
        print("i: ",i)
        i+=1

    #"""
    print("auxI: ",auxI)
    print("auxX: ",auxX)
    print("auxP: ",auxP)
    print("auxP: ",auxMe)
    print("auxP: ",auxX2)
    print("auxP: ",auxPa)
    #"""

    # INT X;
    if (auxI=="int" and isinstance(auxX, str) and auxP==";"):
        print("\t\t\tEstados 0->1->2->3->4->5")

    # FLOAT X;
    elif (auxI=="float" and isinstance(auxX, str) and auxP==";"):
        print("\t\t\tEstados 0->6->7->8->9->10")

    # CHAR X;
    elif (auxI=="char" and isinstance(auxX, str) and auxP==";"):
        print("\t\t\tEstados 0->15->16->17->18->19->20")

    # ENTERO SIN SIGNO???

    # IF(x7<x8)
    elif (auxI=="if" and auxX=="(" and isinstance(auxP, str) and auxMe=="<" and isinstance(auxX2, str) and auxPa==")"):
        print("\t\t\tEstados 0->28->29->30->31")

    # IF(x7>x8)
        
    
    # IF(x7<=x8)


    # IF(x7>=x8)


    # IF(x==y)


    # IF(x!=y)


    # IF(999<9)
    elif (auxI=="if" and auxX=="(" and isinstance(auxP, int) and auxMe=="<" and isinstance(auxX2, int) and auxPa==")"):
        print("\t\t\tEstados 0->22->23->24->32->33->37->38")

    
    return resultado_lexema

 # instanciamos el analizador lexico
analizador = lex.lex()

def printall(the_list, level):
    for x in the_list:
        if isinstance(x, list):
            printall(x, level=level + 1)
        else:
            for tab_stop in range(level):
                print("\t", end='')
        print(x)

if __name__ == '__main__':
    while True:
        data = input("ingrese: ")
        prueba(data)
        #print(str(resultado_lexema))
        printall(resultado_lexema, 3) 



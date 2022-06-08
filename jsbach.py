if __name__ is not None and "." in __name__:
    from .jsbachParser import jsbachParser
    from .jsbachVisitor import jsbachVisitor
else:
    from jsbachParser import jsbachParser
    from jsbachVisitor import jsbachVisitor

import sys
import subprocess
from antlr4 import *
from jsbachLexer import jsbachLexer
from jsbachParser import jsbachParser


class Note:
    '''
    La classe nota representa la nota musical d'un piano. Tenim notes des de el
    A0 fins al C8, que tenen un enter assignat que va des de l'1 fins als 52
    ambos inclosos.

    També defineix les operacions entre notes. En qualsevol operació aritmètica
    que provoqui sortí d'aquest rang provocarà una excepció, ja que fora
    d'aquest rang és una nota no valida.

    Attributs:
        NameNotes: Un diccionari amb la constant entera que representa una nota
        NoteStr: La representació d'una nota en format de string.
        NoteInt: La representació d'una nota en format d'enter.
    '''

    def __init__(self, note: str) -> None:
        '''
        Constructora de la classe Note. Construeix una nota a partir de la
        representació d'una nota en format string.

        Args:
            note: Nota en format de string.
        '''
        self.__NameNotes = {}
        self.genNameNotes()
        self.__NoteStr = note
        self.__NoteInt = self.__NameNotes[self.__NoteStr]

    @classmethod
    def getNoteByInt(cls, num: int):
        '''
        Retorna una Nota donat un enter.

        Args:
            num: Nota en format d'enter.
        '''
        num %= 53
        if num == 0:
            num = 1
        NoteStr = cls.noteIntToStr(num % 52)
        return Note(NoteStr)

    def genNameNotes(self) -> None:
        '''
        genNameNotes() genera el mapa que estableix quin enter correspon a
        cada nota. El diccionari te la següent forma:
            {'A0': 1, 'B0': 2, 'C1': 3 ..., 'B7': 51, 'C8': 52}
        '''
        NameNotes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

        num = 1
        for i in range(0, 9):
            for n in NameNotes:
                note = ""
                if i == 0:
                    if 'A' == n or 'B' == n:
                        note = n + str(i)
                        self.__NameNotes[note] = num
                        num += 1
                elif i == 8:
                    if 'C' == n:
                        note = n + str(i)
                        self.__NameNotes[note] = num
                        num += 1
                else:
                    note = n + str(i)
                    self.__NameNotes[note] = num
                    num += 1

    # Sobrecarga de operadores aritmeticos
    def __add__(self, n2):
        '''
        Defineix la suma entre dues notes o entre una nota i altra tipus de
        dada. Si el resultat dona un valor fora del rang [1, 52] llança una
        excepció.

        Args:
            n2: El segon terme a operar.
        Raise:
            Llança una excepció si l'operació dona un resultat fora del rang
            [1, 52].
        '''
        sum_note = 0
        if isinstance(n2, Note):
            sum_note = self.__NoteInt + n2.__NoteInt
        else:
            sum_note = self.__NoteInt + n2

        NoteStr = self.noteIntToStr(sum_note)
        if sum_note > 52:
            raise Exception('Suma fora de rang' + str(sum_note) + ')')
        return Note(NoteStr)

    def __sub__(self, n2):
        '''
        Defineix la resta entre dues notes o entre una nota i altra tipus de
        dada. Si el resultat dona un valor fora del rang [1, 52] llança una
        excepció.

        Args:
            n2: El segon terme a operar.
        Raise:
            Llança una excepció si l'operació dona un resultat fora del rang
            [1, 52].
        '''
        sub_note = 0
        if isinstance(n2, Note):
            sub_note = self.__NoteInt - n2.__NoteInt
        else:
            sub_note = self.__NoteInt - n2

        NoteStr = self.noteIntToStr(sub_note)
        if sub_note < 1:
            raise Exception('Resta fora de rang' + str(sub_note) + ')')
        return Note(NoteStr)

    def __truediv__(self, n2):
        '''
        Defineix la divisió entre dues notes o entre una nota i altra tipus de
        dada. Si el resultat dona un valor fora del rang [1, 52] llança una
        excepció.

        Args:
            n2: El segon terme a operar.
        Raise:
            Llança una excepció si l'operació dona un resultat fora del rang
            [1, 52].
        '''
        div_note = 0
        if isinstance(n2, Note):
            div_note = int(self.__NoteInt / n2.__NoteInt)
        else:
            div_note = int(self.__NoteInt / n2)

        NoteStr = self.noteIntToStr(div_note)
        if div_note < 1:
            raise Exception('Divisió fora de rang' + str(div_note) + ')')
        return Note(NoteStr)

    def __mul__(self, n2):
        '''
        Defineix la multiplicació entre dues notes o entre una nota i altra
        tipus de dada. Si el resultat dona un valor fora del rang [1, 52]
        llança una excepció.

        Args:
            n2: El segon terme a operar.
        Raise:
            Llança una excepció si l'operació dona un resultat fora del rang
            [1, 52].
        '''
        mul_note = 0
        if isinstance(n2, Note):
            mul_note = self.__NoteInt * n2.__NoteInt
        else:
            mul_note = self.__NoteInt * n2

        NoteStr = self.noteIntToStr(mul_note)
        if mul_note > 52:
            raise Exception('Multiplicació fora de rang' + str(mul_note) + ')')
        return Note(NoteStr)

    def __mod__(self, n2):
        '''
        Defineix el mòdul entre dues notes o entre una nota i altra tipus de
        dada. Si el resultat dona un valor fora del rang [1, 52] llança una
        excepció.

        Args:
            n2: El segon terme a operar.
        Raise:
            Llança una excepció si l'operació dona un resultat fora del rang
            [1, 52].
        '''
        mod_note = 0
        if isinstance(n2, Note):
            mod_note = self.__NoteInt % n2.__NoteInt
        else:
            mod_note = self.__NoteInt % n2

        NoteStr = self.noteIntToStr(mod_note)
        if mod_note < 1:
            raise Exception('Multiplicació fora de rang' + str(mod_note) + ')')
        return Note(NoteStr)

    # Sobrecarga de operadores booleanos
    def __lt__(self, n2) -> bool:
        '''
        Defineix el operador '<' entre dues notes o entre una nota i altra
        tipus de dada.

        Args:
            n2: El segon terme a avaluar.
        '''
        if isinstance(n2, Note):
            return self.__NoteInt < n2.__NoteInt
        else:
            return self.__NoteInt < n2

    def __gt__(self, n2) -> bool:
        '''
        Defineix el operador '>' entre dues notes o entre una nota i altra
        tipus de dada.

        Args:
            n2: El segon terme a avaluar.
        '''
        if isinstance(n2, Note):
            return self.__NoteInt > n2.__NoteInt
        else:
            return self.__NoteInt > n2

    def __le__(self, n2) -> bool:
        '''
        Defineix el operador '<=' entre dues notes o entre una nota i altra
        tipus de dada.

        Args:
            n2: El segon terme a avaluar.
        '''
        if isinstance(n2, Note):
            return self.__NoteInt <= n2.__NoteInt
        else:
            return self.__NoteInt <= n2

    def __ge__(self, n2) -> bool:
        '''
        Defineix el operador '>=' entre dues notes o entre una nota i altra
        tipus de dada.

        Args:
            n2: El segon terme a avaluar.
        '''
        if isinstance(n2, Note):
            return self.__NoteInt >= n2.__NoteInt
        else:
            return self.__NoteInt >= n2

    def __eq__(self, n2) -> bool:
        '''
        Defineix el operador '==' entre dues notes o entre una nota i altra
        tipus de dada.

        Args:
            n2: El segon terme a avaluar.
        '''
        if isinstance(n2, Note):
            return self.__NoteInt == n2.__NoteInt
        else:
            return self.__NoteInt == n2

    def __ne__(self, n2) -> bool:
        '''
        Defineix el operador '!=' entre dues notes o entre una nota i altra
        tipus de dada.

        Args:
            n2: El segon terme a avaluar.
        '''
        if isinstance(n2, Note):
            return self.__NoteInt != n2.__NoteInt
        else:
            return self.__NoteInt != n2

    # Definición de la representación de una Nota en str()
    def __repr__(self) -> str:
        '''
        Retorna la representació en forma de string d'una Nota.
        '''
        return self.__NoteStr

    def noteIntToStr(self, idNote: int) -> str:
        '''
        Transforma la representació d'una Nota en format d'enter en format
        de string.

        Args:
            idNote: La representació d'una Nota en format d'enter.
        '''
        for n in self.__NameNotes:
            if self.__NameNotes[n] == idNote:
                return n

    def getNoteInt(self) -> int:
        '''
        Retorna la representació d'una Nota en format d'enter.
        '''
        return self.__NoteInt

    def getNoteInLilyFormat(self) -> str:
        '''
        Retorna la Nota en format apte per LilyPond.
        '''
        Oct = {'0': ",,,", '1': ",,",
               '2': ",", '3': "",
               '4': "'", '5': "''",
               '6': "'''", '7': "''''",
               '8': "'''''"}
        return self.__NoteStr[0].lower() + Oct[self.__NoteStr[1]]


class SheetMusic:
    '''
    La classe SheetMusic representa una partitura on una partitura es un
    conjunt de Note.

    Atributs:
        Sheet: El conjunt de notes que forma la partitura.
        Tempo: El tempo de la partitura.
    '''

    def __init__(self) -> None:
        '''
        La constructora d'un SheetMusic. Construeix una partitura buida.
        '''
        self.__sheet = list()
        self.__tempo = 120

    def __repr__(self) -> str:
        '''
        Retorna la representació d'una partitura en format de string.
        '''
        return str(self.__sheet)

    def addNote(self, note: Note) -> None:
        '''
        Afegeix una nota al final de la partitura.

        Args:
            note: La nota que volem afegir.
        '''
        self.__sheet.append(note)

    def genFiles(self, nameFile: str) -> None:
        '''
        Genera els fitxers PDF, MIDI, MP3 i WAV. Aquests fitxers corresponen a
        la partitura i a la representació en piano d'aquesta mateixa.
        Els fitxers es generen a través de programes com LilyPond (crea la
        partitura i l'arxiu midi), timidity (converteix de midi a wav) i
        ffmepg (converteix de wav a mp3).
        Els arxius es generen amb el nom de nameFile.

        Args:
            nameFile: El nom dels arxius.
        '''
        fileLily = open("./" + nameFile + ".lily", "w")
        fileLily.write('\u005Cscore {\n')
        fileLily.write('    \u005Cabsolute {\n')
        fileLily.write('        \u005Ctempo 4 = ' + str(self.__tempo))
        fileLily.write('\n        ')
        for note in self.__sheet:
            noteLily = note.getNoteInLilyFormat()
            fileLily.write(noteLily + ' ')
        fileLily.write('\n    }\n    \u005Clayout { }\n')
        fileLily.write('    \u005Cmidi { }\n}')

        fileLily.close()

        # Generamos el archivo .pdf y .midi
        subprocess.run(['lilypond', nameFile + '.lily'])
        # Generamos el archivo .wav
        subprocess.run(['timidity',
                        '-Ow',
                        '-o',
                        nameFile + '.wav',
                        nameFile + '.midi'])
        # Generamos el archivo .mp3
        subprocess.run(['ffmpeg',
                        '-i',
                        nameFile + '.wav',
                        '-codec:a',
                        'libmp3lame',
                        '-qscale:a',
                        '2',
                        nameFile + '.mp3'])


class Function:
    '''
    La classe Function representa una funció que no retorna cap valor. Una
    funció té el seu nom, el nom dels seus paràmetres, si en té, i el
    nombre de paràmetres. També conte el seu codi i la seva pròpia
    taula de símbols.

    Atributs:
        nameFunc (str): Nom de la funció.
        params (list): Conjunt de noms dels paràmetres de la funció.
        numParams (int): El nombre de paràmetres de la funció.
        code (jsbachParser.InstructionsContext): El codi associat al cos de la
        funció.
        SimbolTable (dict): La taula de símbols associada a la funció.
    '''

    def __init__(self,
                 nameFunc: str,
                 params: list,
                 code: jsbachParser.InstructionsContext,
                 ts: dict) -> None:
        '''
        Constructor de la classe Function. Construeix una funció amb nom,
        codi, paràmetres i una taula de símbols.

        Args:
            nameFunc: El nom de la funció.
            params: El conjunt de paràmetres de la funció.
            code: El codi associat a la funció.
            ts: La taula de símbols associada a la funció.
        '''
        self.__nameFunc = nameFunc
        self.__params = params[:]
        self.__numParams = len(params)
        self.__code = code
        self.__SimbolTable = ts

    def __repr__(self) -> str:
        '''
        Retorna la representació de una funció en format de string.
        '''
        func_str = 'Name Function: ' + self.__nameFunc + '\nParameters: '
        func_str = func_str + str(self.__params)
        func_str = func_str + '\nSimbol Table: ' + str(self.__SimbolTable)
        return func_str + '\n\n'

    def isVariable(self, var: str) -> bool:
        '''
        isVariable() ens indica si el nom de variable var correspon a una
        variable que existeix a la taula de símbols, és a dir, que ha sigut
        declarada en l'àmbit de visibilitat de la funció.
        Retorna cert si la variable existeix, en cas contrari retorna fals.

        Args:
            var: El nom de la variable.
        '''
        return var in self.__SimbolTable

    def setParameters(self, params: list) -> None:
        '''
        Estableix un nou conjunt de paràmetres per a la funció.

        Args:
            params: El nou conjunt de paràmetres.
        '''
        self.__params = params.copy()
        self.__numParams = len(self.__params)

    def setVariable(self, var_name: str) -> None:
        '''
        Afegeix o modifica una variable sense valor a la taula de símbols
        de la funció.

        Args:
            var_name: El nom de la variable.
        '''
        self.__SimbolTable[var_name] = 0

    def setVariableWithVal(self, var_name: str, var_val: int) -> None:
        '''
        Afegeix o modifica una variable amb valor var_val a la taula de
        símbols de la funció.

        Args:
            var_name: El nom de la variable.
            var_val: El valor de la variable.
        '''
        self.__SimbolTable[var_name] = var_val

    def getNumberParameters(self) -> int:
        '''
        Retorna el nombre de paràmetres de la funció.
        '''
        return self.__numParams

    def getCode(self) -> jsbachParser.InstructionsContext:
        '''
        Retorna el codi associat al cos de la funció.
        '''
        return self.__code

    def getNameFunction(self) -> str:
        '''
        Retorna el nom de la funció.
        '''
        return self.__nameFunc

    def getParameterByIndex(self, i: int) -> str:
        '''
        Retorna el nom del paràmetre i-èsim de la funció.

        Args:
            i: Indica el paràmetre i-èsim a consultar.
        '''
        return self.__params[i]

    def getVariableByName(self, var: str) -> int:
        '''
        Retorna el valor d'una variable donat el nom de la variable.

        Args:
            var: El nom de la variable a consultar.
        '''
        return self.__SimbolTable[var]

    def getCopySimbolTable(self) -> dict:
        '''
        Retorna una còpia de la taula de símbols.
        '''
        return self.__SimbolTable.copy()

    def getCopyParameters(self) -> list:
        '''
        Retorna una còpia del conjunt de paràmetres.
        '''
        return self.__params.copy()


class Functions:
    '''
    La classe Functions representa un conjunt de funcions.

    Atributs:
        functions (list): El conjunt de funcions.
    '''

    def __init__(self) -> None:
        '''
        Constructora de la classe Functions. Construeix un conjunt de
        funcions buit.
        '''
        self.__funcions = list()

    def __repr__(self) -> str:
        '''
        Retorna la representació d'un conjunt de funcions en format de
        string.
        '''
        func_name = str()
        for func in self.__funcions:
            func_name = func_name + str(func)
        return func_name

    def isFunctionByName(self, func_name: str) -> bool:
        '''
        Indica si existeix, en el conjunt de funcions, una funció amb
        nom == func_name.

        Args:
            func_name: El nom de la funció.
        '''
        for func in self.__funcions:
            if func.getNameFunction() == func_name:
                return True
        return False

    def modifyFunctionByName(self, func_name: str, new_func: Function) -> None:
        '''
        Modifica la funció amb nom func_name amb la nova funció new_func.

        Args:
            func_name: El nom de la funció.
            new_func: La nova funció.
        '''
        for func in self.__funcions:
            if func.getNameFunction() == func_name:
                func = new_func

    def getFunctionByName(self, func_name: str) -> Function:
        '''
        Retorna la funció amb nom func_name.

        Args:
            func_name: El nom de la funció a consultar.
        '''
        for func in self.__funcions:
            if func.getNameFunction() == func_name:
                return func

    def addFunction(self, func: Function) -> None:
        '''
        Afegeix una nova funció al conjunt de funcions.

        Args:
            func: La funció a afegir.
        '''
        self.__funcions.append(func)


class Stack:
    '''
    La classe Stack representa una pila d'execució, és a dir, una pila de
    funcions que s'estan executant.

    Atributs:
        stack (list): La pila en qüestió.
    '''

    def __init__(self) -> None:
        '''
        La constructora de la classe Stack. Construeix una pila buida.
        '''
        self.__stack = list()

    def __repr__(self) -> str:
        '''
        Retorna la representació de la pila en format de string.
        '''
        stack_str = str()
        for func in self.__stack:
            stack_str = stack_str + str(func)
        return stack_str

    def getTop(self) -> Function:
        '''
        Retorna la cima de la pila.
        '''
        return self.__stack[0]

    def add(self, func: Function) -> None:
        '''
        Afegeix una nova funció a la cima de la pila.

        Args:
            func: La nova funció a afegir.
        '''
        name = func.getNameFunction()
        params = func.getCopyParameters()
        code = func.getCode()
        ts = func.getCopySimbolTable()
        new_func = Function(name, params, code, ts)
        self.__stack.insert(0, new_func)

    def remove(self) -> None:
        '''
        Elimina la funció que es troba a la cima de la pila.
        '''
        self.__stack.pop(0)

    def modTop(self, new_top: Function) -> None:
        '''
        Modifica la funció que es troba en la cima de la pila.

        Args:
            new_top: La nova funció.
        '''
        self.__stack[0] = new_top


class JSBach(jsbachVisitor):
    '''
    La classe JSBach és l'encarregada d'avaluar i executar totes les
    expressions i instruccions del llenguatge JSBach. Aquesta classe hereta
    els seus mètodes de la classe jsbachVisitor generada a través de la
    gramàtica especificada a jsbach.g4 i generada amb Antlr4.

    Cada funció de la classe JSBach visita un tipus d'expressió, definició
    o instrucció definida a la gramàtica de tal manera que avalua i executa.

    Atributs:
        functions (Functions): El conjunt de funcions definides en un programa
        en JSBach.
        stack (Stack): La pila d'execució.
        default (bool): Indica si executem el mètode 'Main' o un mètode
        especificat per l'usuari.
        procName (str): El nom de la funció especificada per l'usuari.
        params (str): El paràmetres especificats per l'usuari.
        sheet (SheetMusic): La partitura associada a l'execució del
        programa en JSBach.
    '''

    def __init__(self, default: bool, ProcName: str, params: list):
        '''
        Constructor de la classe JSBach. Construeix l'entorn d'execució
        d'un programa en JSBach amb un conjunt de funcions buit, una pila
        buida, una partitura buida.

        Args:
            default: Indica si hem d'executar el mètode 'Main' o no.
            ProcName: El nom de la funció a executar especificada per
            l'usuari.
            params: El valor del paràmetres especificats per l'usuari.
        '''
        super().__init__()
        self.__funcions = Functions()
        self.__stack = Stack()
        self.__default = default
        self.__procName = ProcName
        self.__params = params
        self.__sheet = SheetMusic()

    def visitRoot(self, ctx: jsbachParser.RootContext):
        '''
        visitRoot() visita l'arrel del programa en JSBach, és a dir, és el
        que veu quines funcions hi ha definides en el programa que esta
        executant. Aquesta funció s'encarrega de definir les funcions i
        executar la funció que pertoca, en el cas que default sigui
        cert s'executarà el 'Main' si aquest existeix. En cas contrari
        executarà la funció especificada a self.__procName si aquesta
        existeix.

        Args:
            ctx: El context relacionat amb l'arrel.
        Raise:
            Llança una excepció en cas que no existeixi un mètode Main.
            Llança una excepció en cas que no existeixi el mètode especificat.
            Llança una excepció en cas que el nombre de paràmetres no
            coincideixi.
        '''
        self.visitChildren(ctx)
        # Si no especificamos ningun metodo ejecutamos Main si existe
        if self.__default:
            if self.__funcions.isFunctionByName('Main'):
                func = self.__funcions.getFunctionByName('Main')
                self.__stack.add(func)
                res = self.visitInstructions(func.getCode())
                self.__sheet.genFiles('Main')
                return res
            else:
                raise Exception('No existeix el procediment Main')
        else:
            if self.__funcions.isFunctionByName(self.__procName):
                f = self.__funcions.getFunctionByName(self.__procName)
                n = f.getNumberParameters()
                # Comprobamos si el numero de parametros pasado es correcto
                if len(self.__params) == n:
                    for i in range(0, len(self.__params)):
                        val = self.__params[i]
                        var = f.getParameterByIndex(i)
                        f.setVariableWithVal(var, val)
                    self.__stack.add(f)
                    codi = f.getCode()
                    res = self.visitInstructions(codi)
                    self.__sheet.genFiles(self.__procName)
                    return res
                else:
                    raise Exception('El nombre de parametres no es correcte')
            else:
                raise Exception('No existeix el metode ' + self.__procName)

    def visitProcDef(self, ctx: jsbachParser.ProcDefContext):
        '''
        visitProcDef() visita les definicions de les funcions i les emmagatzema
        en el conjunt de funcions. Guardem el nom, el codi, el nom de
        paràmetres i la taula de símbols buida.

        Args:
            ctx: Context relacionat amb la definició d'una funció.
        Raise:
            Llança una excepció en cas que es defineix dos paràmetres amb
            el mateix nom.
        '''
        children = list(ctx.getChildren())
        ProcName = children[0].getText()
        if self.__funcions.isFunctionByName(ProcName):
            raise Exception('Procediment ja definit')
        else:
            code = children[len(children) - 2]
            params = []
            func = Function(ProcName, params, code, dict())
            for i in range(1, len(children) - 3):
                param = children[i].getText()
                if param in params:
                    raise Exception('Nom de parametre repetit')
                else:
                    params.append(param)
                    func.setVariable(param)
            func.setParameters(params)
            self.__funcions.addFunction(func)

    def visitProc(self, ctx: jsbachParser.ProcContext):
        '''
        visitProc() visita les crides a les funcions i executa les funcions,
        si no existeix la funció es llança una excepció, en cas contrari es
        posa en la pila d'execució el procediment cridat.

        Args:
            ctx: Context relacionat amb l'execució d'una funció.
        Raise:
            Llança una excepció en cas que el paràmetre no existeixi.
            Llança una excepció en cas que el nombre de paràmetres no
            existeixi.
        '''
        children = list(ctx.getChildren())
        procName = children[0].getText()
        # Comprobamos si existe la función, si no existe lanzamos una excepcion
        if self.__funcions.isFunctionByName(procName):
            f = self.__funcions.getFunctionByName(procName)
            n = f.getNumberParameters()
            if len(children) - 1 == n:
                for i in range(1, len(children)):
                    val = self.visit(children[i])
                    var = f.getParameterByIndex(i - 1)
                    f.setVariableWithVal(var, val)
                code = f.getCode()
                self.__stack.add(f)
                res = self.visitInstructions(code)
                self.__stack.remove()
                return res
            else:
                raise Exception('Nombre de parametres incorrecte')
        else:
            raise Exception('El procediment ' + procName + ' no existeix')

    def visitListAddElement(self, ctx: jsbachParser.ListAddElementContext):
        '''
        Avalua la instrucció d'afegir un element al final d'una llista, si
        aquesta llista existeix s'afegeix, en cas contrari no s'afegeix.

        Args:
            ctx: Context relacionat amb l'operació d'afegir un element al
                 final d'una llista.
        '''
        children = list(ctx.getChildren())
        var = self.visitVar(children[0])
        val = self.visit(children[2])
        var.append(val)

    def visitListCutElement(self, ctx: jsbachParser.ListCutElementContext):
        '''
        Avalua la instrucció d'eliminar l'element i-èsim de la llista, si la
        llista dona existeix s'executa, en cas contrari no s'elimina. Així
        mateix, si l'element i-èsim especificat aquesta fora de rang, és a dir,
        entre 1 i la longitud de la llista es llança una excepció.

        Args:
            ctx: Context relacionat amb l'operació d'eliminar l'element i-èsim.
        Raise:
            En cas que l'element i-èsim estigues fora de rang (entre 1 i #l) es
            llança una excepció.
        '''
        children = list(ctx.getChildren())
        var = self.visitVar(children[1])
        i = self.visit(children[3])
        if i < 1 or i > len(var):
            raise Exception('Fora de rang (max: ' + str(len(var)) + ')')
        var.pop(i - 1)

    def visitListGetElement(self, ctx: jsbachParser.ListGetElementContext):
        '''
        Avalua la instrucció de visitar l'element i-èsim. Retorna l'element
        i-èsim de la llista avaluada si aquesta existeix.

        Args:
            ctx: Context relacionat amb l'operació d'agafar l'element i-èsim.
        Raise:
            En cas que l'element i-èsim estigues fora de rang (entre 1 i #l) es
            llança una excepció.
        '''
        children = list(ctx.getChildren())
        var = self.visitVar(children[0])
        i = self.visit(children[2])
        if i < 1 or i > len(var):
            raise Exception('Fora de rang (max: ' + str(len(var)) + ')')
        return var[i - 1]

    def visitListSize(self, ctx: jsbachParser.ListSizeContext):
        '''
        Avalua la instruccío de la mida d'una llista. Retorna la mida de la
        llista si aquesta llista existeix.

        Args:
            ctx: Context relacionat amb l'operació de la mida d'una llista.
        '''
        children = list(ctx.getChildren())
        var = self.visitVar(children[1])
        return len(var)

    def visitWrite(self, ctx: jsbachParser.WriteContext):
        '''
        visitwrite() executa la instrucció d'escriptura del llenguatge JSBach.
        En aquesta funció avaluem l'expressió a escriure i escrivim per
        pantalla el resultat.

        Args:
            ctx: Context relacionat amb l'operació d'escriptura.
        '''
        children = list(ctx.getChildren())
        res = ""
        for i, child in enumerate(children):
            if i > 0:
                ValWrite = self.visit(child)
                if ValWrite:
                    res += str(ValWrite)
                else:
                    res += child.getText()[1:-1]
        print(res)

    def visitRead(self, ctx: jsbachParser.ReadContext):
        '''
        visitRead() executa la instrucció de lectura del llenguatge JSBach.
        En aquesta funció llegim de l'entrada estàndard i ho emmagatzem
        en la variable especificada.

        Args:
            ctx: Context relacionat amb l'operació d'escriptura.
        '''
        children = list(ctx.getChildren())

        inp = input()
        func = self.__stack.getTop()
        func.setVariableWithVal(children[1].getText(), int(inp))
        self.__stack.modTop(func)

    def visitPlayList(self, ctx: jsbachParser.PlayListContext):
        '''
        visitPlayList() executa la reproducció d'una llista. La reproducció
        s'emmagatzema dins de la partitura per ser interpretat al final de
        l'execució.

        Args:
            ctx: Context relacionat amb l'operació de reproduir una llista.
        '''
        children = list(ctx.getChildren())
        ListNote = self.visitList_(children[1])
        for note in ListNote:
            self.__sheet.addNote(note)

    def visitPlayNoteVar(self, ctx: jsbachParser.PlayNoteVarContext):
        '''
        visitPlayNoteVar() executa la reproducció d'una nota o d'una variable.
        Aquesta reproducció s'emmagatzema en la partitura per ser interpretada
        més tard.

        Args:
            ctx: Context relacionat amb l'operació de reproduir una nota
            o una variable.
        '''
        children = list(ctx.getChildren())
        if children[1].getSymbol().type == jsbachParser.VAR:
            note = self.visitVar(children[1])
        elif children[1].getSymbol().type == jsbachParser.NOTE:
            note = self.visitNote(children[1])
        self.__sheet.addNote(note)

    def visitList_(self, ctx: jsbachParser.List_Context):
        '''
        visitList_() interpreta una llista. Les llistes poden contenir
        notes o enters. Aquesta funció interpreta l'entrada i retorna
        la llista ja construïda.

        Args:
            ctx: Context relacionat amb la definició d'una llista.
        '''
        children = list(ctx.getChildren())
        notes = []
        for i, child in enumerate(children):
            if i > 0 and i < len(children) - 1:

                if child.getSymbol().type == jsbachParser.NOTE:
                    note = self.visitNote(child)
                else:
                    note = Note.getNoteByInt(self.visitNum(child))
                notes.append(note)
        return notes

    def visitConditional(self, ctx: jsbachParser.ConditionalContext):
        '''
        visitConditional() avalua l'estructura del if .. else executant
        el codi corresponent al resultat d'avaluar l'expressió booleana
        del if.

        Args:
            ctx: Context relacionat amb l'estructura d'un condicional.
        '''
        children = list(ctx.getChildren())

        cond_bool = self.visitExpr_bool(children[1])
        if cond_bool:
            self.visitInstructions(children[3])
        else:
            if len(children) == 9:
                self.visitInstructions(children[7])

    def visitWhile_(self, ctx: jsbachParser.While_Context):
        '''
        visitWhile_() avalua l'estructura d'un bucle while executant el codi
        del cos del while fins que la condició del bucle sigui falsa.

        Args:
            ctx: Context relacionat amb l'estructura d'un bucle while.
        '''
        children = list(ctx.getChildren())
        while True:
            cond_bool = self.visitExpr_bool(children[1])
            if cond_bool:
                self.visitInstructions(children[3])
            else:
                break

    def visitAssign(self, ctx: jsbachParser.AssignContext):
        '''
        visitAssign() executa l'assignació d'una expressió a una variable sigui
        creant-la o modificant-la.

        Args:
            ctx: Context relacionat amb l'estructura d'una assignació.
        '''
        children = list(ctx.getChildren())
        NameVar = children[0].getText()
        func = self.__stack.getTop()
        func.setVariableWithVal(NameVar, self.visit(children[2]))
        self.__stack.modTop(func)

    def visitExpr_bool(self, ctx: jsbachParser.Expr_boolContext):
        '''
        visitExpr_bool() avalua l'expressió booleana i retorna el resultat de
        l'avaluació de l'expressió.

        Args:
            ctx: Context relacionat amb l'avaluació d'una expressió booleana.
        '''
        children = list(ctx.getChildren())
        if len(children) > 1:
            val1 = self.visit(children[0])
            val2 = self.visit(children[2])
            typ = children[1].getSymbol().type
            if typ == jsbachParser.EQ:
                return int(val1 == val2)
            elif typ == jsbachParser.DIFF:
                return int(val1 != val2)
            elif typ == jsbachParser.L:
                return int(val1 < val2)
            elif typ == jsbachParser.G:
                return int(val1 > val2)
            elif typ == jsbachParser.LEQ:
                return int(val1 <= val2)
            elif typ == jsbachParser.GEQ:
                return int(val1 >= val2)
        else:
            num = int(children[0].getText())
            if num == 0:
                return num
            elif num > 0:
                return 1

    def visitPar(self, ctx: jsbachParser.ParContext):
        '''
        visitPar() avalua una expressió aritmètica amb parèntesis. Retorna el
        resultat de l'avaluació.

        Args:
            ctx: Context relacionat amb l'avaluació d'una expressió amb
            parèntesis.
        '''
        children = list(ctx.getChildren())
        return self.visit(children[1])

    def visitMultDiv(self, ctx: jsbachParser.MultDivContext):
        '''
        visitMultDiv() avalua una expressió aritmètica de multiplicació o
        divisió. Retorna el resultat de la divisió o de la multiplicació.

        Args:
            ctx: Context relacionat amb l'avaluació d'una expressió aritmètica
            de multiplicació o divisió.
        Raise:
            Llança una excepció en cas que es produeixi una divisió entre 0.
        '''
        children = list(ctx.getChildren())
        if children[1].getSymbol().type == jsbachParser.MULT:
            return self.visit(children[0]) * self.visit(children[2])
        elif children[1].getSymbol().type == jsbachParser.DIV:
            if int(children[2].getText()) == 0:
                raise Exception("Divisió entre 0")
            else:
                return self.visit(children[0]) / self.visit(children[2])

    def visitMod(self, ctx: jsbachParser.ModContext):
        '''
        visitMod() avalua una expressió aritmètica de mòdul. Retorna el
        resultat del mòdul.

        Args:
            ctx: Context relacionat amb l'avaluació d'una expressió
            aritmètica de mòdul.
        Raise:
            Llança una excepció en cas que es produeixi un mòdul entre 0.
        '''
        children = list(ctx.getChildren())
        if int(children[2].getText()) == 0:
            raise Exception("Modúl entre 0")
        else:
            return self.visit(children[0]) % self.visit(children[2])

    def visitSumRes(self, ctx: jsbachParser.SumResContext):
        '''
        visitSumRes() avalua una expressió aritmètica de suma o resta. Retorna
        el resultat de la suma o resta.

        Args:
            ctx: Context relacionat amb l'avaluació d'una expressió
            aritmètica de suma o resta.
        '''
        children = list(ctx.getChildren())
        if children[1].getSymbol().type == jsbachParser.SUM:
            return self.visit(children[0]) + self.visit(children[2])
        elif children[1].getSymbol().type == jsbachParser.RES:
            return self.visit(children[0]) - self.visit(children[2])

    def visitNote(self, ctx: jsbachParser.NoteContext):
        '''
        visitNote() avalua una expressió que conté una nota. Retorna una nota
        després d'avaluar l'expressió.

        Args:
            ctx: Context relacionat amb una expressió d'una nota.
        '''
        s = ctx.getText()
        Oct = ''
        if len(s) == 1:
            Oct = '4'

        note = Note(s + Oct)
        return note

    def visitVar(self, ctx: jsbachParser.VarContext):
        '''
        visitVar() avalua una expressió que conté una variable. Consulta el
        valor de la variable si existeix i retorna el seu valor.

        Args:
            ctx: Context relacionat amb una variable.
        Raise:
            Llança una excepció en cas que la variable no existeixi.
        '''
        func = self.__stack.getTop()
        if func.isVariable(ctx.getText()):
            return func.getVariableByName(ctx.getText())
        else:
            raise Exception("Variable " + ctx.getText() + " no definida")

    def visitNum(self, ctx: jsbachParser.NumContext):
        '''
        visitNum() avalua una expressió que conté un número. Retorna el valor
        del número una vegada avaluat.

        Args:
            ctx: Context relacionat amb una expressió que conté un número.
        '''
        return int(ctx.getText())


# Comienza el main del programa
def main() -> None:
    '''
    El mètode main s'encarrega d'executar el intèrpret de JSBach. Busca
    quin mètode volem executar i crida al visitor per tal d'avaluar
    les expressions contingudes en el programa.

    Raise:
        Llança una excepció en cas que l'extensió de l'arxiu sigui
        incorrecta.
        Llança una excepció en cas que el pas d'arguments sigui
        incorrecte.
    '''
    input_stream = ""
    if len(sys.argv) == 2:
        if sys.argv[1][-4:] == '.jsb':
            input_stream = FileStream(sys.argv[1], encoding='utf-8')
            evalvisit = JSBach(True, None, None)
        else:
            raise Exception('Extensió del arxiu incorrecta')
    elif len(sys.argv) > 2:
        input_stream = FileStream(sys.argv[1], encoding='utf-8')
        ProcName = sys.argv[2]
        Params = [sys.argv[i] for i in range(3, len(sys.argv))]
        evalvisit = JSBach(False, ProcName, Params)
    else:
        raise Exception('Pas de arguments incorrecte, veure Readme.md')

    lexer = jsbachLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = jsbachParser(token_stream)
    tree = parser.root()

    evalvisit.visit(tree)


# Ejecutamos el main del interprete JSBach
if __name__ == '__main__':
    main()

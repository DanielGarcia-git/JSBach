# JSBach

JSBach és un llenguatge de programació orientat a la composició algorísmica. Amb JSBach s'utilitzen construccions imperatives per generar composicions que donen lloc a partitures que poden ser desades en diferents formats digitals.

## Instalació

Per poder instal·lar JSBach haurem d'executar la següent comanda:

```bash
antlr4 -Dlanguage=Python3 -no-listener -visitor jsbach.g
```

## Ús

Per poder executar un programa en JSBach utilitzem la següent comanda:

```bash
python3 jsbach.py nom_arxiu.jsb
```

O si volem executar una funció en concret utilitzarem la següent comanda:

```bash
python3 jsbach.py nom_arxiu.jsb nom_procediment param1 param2 param3
```

## Consideracions

A l'hora d'implementar l'intèrpret de JSBach s'han fet certes consideracions en l'especificació del llenguatge que passaré a exposar en aquest punt. Les consideracions són les següents:

- El nom de les variables es defineixen sempre començant amb minúscula.
- El nom de les funcions es defineixen sempre començant amb majúscula.

## Proves

Aquí tens alguns exemples de codi que pot utilitzar per començar a utilitzar JSBach. Per provar-lo posa'ls a un arxiu amb extensió '.jsb'.

```
~~~ Kleines Program in JSBach ~~~

Main |:
    <!> "Hallo Bach"
    <:> {B A C}
:|
```

```
~~~ programa que llegeix dos enters i n'escriu el seu maxim comu divisor ~~~

Main |:
    <!> "Escriu dos nombres"
    <?> a
    <?> b
    Euclides a b
:|

Euclides a b |:
    while a /= b |:
        if a > b |:
            a <- a - b
        :| else |:
            b <- b - a
        :|
    :|
    <!> "El seu MCD es" a
:|
```

```
~~~ Notes de Hanoi ~~~

Hanoi |:
    src <- {C D E F G}
    dst <- {}
    aux <- {}
    HanoiRec #src src dst aux
:|

HanoiRec n src dst aux |:
    if n > 0 |:
        HanoiRec (n - 1) src aux dst
        note <- src[#src]
        8< src[#src]
        dst << note
        <:> note
        HanoiRec (n - 1) aux dst src
    :|
:|
```

## Author

Daniel García Estévez
 + **email:** [daniel.garcia.estevez@estudiantat.upc.edu](mailto:daniel.garcia.estevez@estudiantat.upc.edu)
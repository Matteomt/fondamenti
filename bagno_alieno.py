"Scopo: La richiesta degli alieni si traduce nella ricerca del Massimo Comune Divisore delle dimensioni del bagno.
"Utilizzo: MCD(base, altezza) oppure MCD(altezza, base)
"Ritorna: la dimensione delle piastrelle da usare per salvare il pianeta Terra dall'attacco alieno.

def MCD(a,b):
  if a*b==0:    "Se uno dei due è 0,
    return a+b  "ritorna l'altro.
  elif a>b:     "L'uso di `elif` e di una condizione in più si può risolvere con l'impiego di 2 funzioni.
    return MCD(a%b,b)
  else:
    return MCD(b%a,a)

def MCD2(a,b):
  if a>b:
    return MCD2_ordinato(a,b)
  else:
    return MCD2_ordinato(b,a)

def MCD2_ordinato(a,b):
  if b==0:
    return a
  else:
    return MCD2(a%b,b)

"Scopo: La richiesta degli alieni si traduce nella ricerca del Massimo Comune Divisore delle dimensioni del bagno.
"Utilizzo: MCD(base, altezza) oppure MCD(altezza, base)
"Ritorna: la dimensione delle piastrelle da usare per salvare il pianeta Terra dall'attacco alieno.

def MCD(a,b):
  if a%b==0:
    return b
  else
    return MCD(b,a%b)

"Perché l'MCD?
"Viene dato che il costo totale della commissione (da minimizzare) è proporzionale al lato delle piastrelle (tutte uguali, quadrate).
"Ciò che è rilevante qui è che le piastrelle aliene NON si pagano in base all'area, che è costante, b*h.
"Se le piastrelle avessero un costo proporzionale alla loro area, come sulla Terra, la scelta del lato non farebbe alcuna differenza.
"costo totale = lato della piastrella * numero piastrelle in orizzontale * numero piastrelle in verticale
"             = l * no * nv
"             = l * b/l * h/l
"             = b*h/l
"con b,h,l € N (naturali positivi).
"Lim _l->+inf b*h/l = 0
"Lim _l->0+ b*h/l = +inf
" => l va massimizzato per minimizzare il costo
"Per visualizzare ciò, basta graficare la formula c=b*h/l mettendo l sulle ascisse e il costo risultante sulle ordinate.
"Quindi, come scegliere l?
"Dovendo utilizzare tutte piastrelle quadrate e intere (non possiamo tagliarle), della stessa dimensione,
"abbiamo che b e h devono essere entrambi divisibili per lo stesso l, che va massimizzato:
"b/l, h/l € N  =>  l=MCD(b,h).
"C.v.d.

import pprint

valuesToConvertToHex = {
    "won":        8361,
    "thai:baht":  3647,
    "tenge":      8376,             
    "rupee":      8360,             
    "ruble":      8381,             
    "peso":       8369,            
    "overline":   8254,                
    "ohm":        8486,           
    "newsheqel":  8362,                 
    "naira":      8358,             
    "manat":      8380,             
    "litre":      8467,             
    "kip":        8365,           
    "increment":  8710,                 
    "hryvnia":    8372,               
    "guarani":    8370,               
    "dotlessj":   567,                
    "cedi":       8373,            
    "bitcoin":    8383,               
    "Nhookleft":  413,                 
    "Germandbls": 7838,                  
}

hexVals = {}

for value in valuesToConvertToHex.keys():
    
    hexVals[value] = hex(valuesToConvertToHex[value]).split("x")[1]
    
pp = pprint.PrettyPrinter(indent=2, width=200)
pp.pprint(hexVals)
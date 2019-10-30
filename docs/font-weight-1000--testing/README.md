## Simple script to calculate even steps

```
valA = 84
valB = 215
steps = 7

def getSteps(valA, valB, steps):
    totalRange = valB - valA
    stepSize = totalRange / steps
    print(valA) 
    for step in range(steps):
        valA += stepSize
        print(round(valA, 3))   
    
getSteps(valA, valB, steps)
```

## AVAR issue

https://github.com/fonttools/fonttools/issues/1756
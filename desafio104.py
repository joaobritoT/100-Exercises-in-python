def notas(*notas,sit=False):
    r = {}
    r['total'] = len(notas) 
    r['soma'] = sum(notas)
    r['maior'] = max(notas)
    r['menor'] = min(notas)
    r['media'] = sum(notas) / len(notas)
    if sit:
        if r['media'] >=6 and r['media']<=7:
            r['sit'] = "razoavel"
        elif r['media'] <6:
            r['sit'] = "ruim"
        else:
            r['sit'] = "boa"
        
    return r
    
resp = notas(1,2,3,4,)
print(resp)

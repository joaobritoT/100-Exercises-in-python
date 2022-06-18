exp = str(input("digite uma expressao: "))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append("(")
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) ==0:
    print("expressao correta")
else:
    print("sua expressao esta errada")
lp = float(input('largura da parede? '))
ap = float(input('qual a altura da parede? '))
area = lp * ap
t = area / 2
print('sua parede tem a dimensao de {} x {} e a are de {}m2'.format(lp, ap, area))
print('voce precisa de {} litros para pintar a parede.'.format(t))
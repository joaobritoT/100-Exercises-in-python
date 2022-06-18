from operator import index


tabela = ('corinthians', 'atletico mg', 'bragantino','flamengo','santos','fluminese','sao paulo','coritiba','america mg','botafogo','cuiaba','ceara sc'
'internacional','avai','palmeiras','juventude','goias','atletico go','fortaleza','atletico pr')

print("a tabela do brasileirao: {}".format(tabela))
print("os cinco primeiros: {}".format(tabela[0:5]))
print("os cinco ultimos: {}".format(tabela[14:19]))
print("em ordem alfabetica: {}".format(sorted(tabela)))
print("o corinthians esta na {} posicao".format(tabela.index('corinthians')+1))

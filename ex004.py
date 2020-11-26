q = input('digite algo')
print('e do tipo {}, e numero {}, e texto {}, e numero e texto{}'.format(type(q), q.isnumeric(), q.isalpha(), q.isalnum()))
print(q.istitle())
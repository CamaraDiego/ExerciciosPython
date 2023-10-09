m = float(input('Informe uma medida em metros: '))
cm = m * 100
mm = m * 1000
print('{:.2f} metro(s) equivale a {} centímetros ou {} milímetros'.format(m, int(cm), int(mm)))

import pydf

html = '<h1>ola mundo</h1><p>testando meu documento</p>'
pdf = pydf.generate_pdf(html)

with open('meu_arquivo.pdf', 'wb') as arquivo:
    arquivo.write(pdf)

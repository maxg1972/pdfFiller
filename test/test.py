from pdfFiller import fill_pdf

SOURCE_PDF = './input.pdf'
DEST_PDF = './output.pdf'

fields = [
            ('cf1','A'),
            ('cf2','B'),
            ('cf3','C'),
            ('cf4','D'),
            ('cf5','E'),
            ('cf6','F'),
            ('cf7','0'),
            ('cf8','1'),
            ('cf9','G'),
            ('cf10','2'),
            ('cf11','3'),
            ('cf12','H'),
            ('cf13','4'),
            ('cf14','5'),
            ('cf15','6'),
            ('cf16','I'),
            ('annoimposta','2013'),
            ('ragsociale','MyCompany'),
         ]

result = fill_pdf(fields,SOURCE_PDF,DEST_PDF)

if result['code'] == 0:
    print "ok"
else:
    print result['message']


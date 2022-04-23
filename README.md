# project3cx_personalpbextractor
A program to extract the personal phonebook list from any extension on a 3cx backup XML file.


PT-BR:
*********************Personal Contacts Extractor - By Michatec************************

1-Baixe um backup do 3CX Phone System no qual esteja a extensão cujos
contatos pessoais se deseje extrair.

2-Copie o arquivo .xml da pasta de backup e cole-o na pasta do Phonebook Extractor.

3-Rode o executável 'PhonebookExtractor' e preencha os campos:
       "3CX backup xml archive": (Nome do arquivo .xml, com extensão)
       "Extension to extract PB":(Nome da extensão para extração da agenda pessoal)

4-Será criado automaticamente dentro da pasta, um arquivo '.csv' com todos os 
contatos pessoais da extensão indicada. Este arquivo, já está formatado no padrão 
3CX, para posterior importação quando necessário.



(Na versão atual não há tratamento a exceções. O não preenchimento de campos incorre 
em erro ao encerrar o executável, bem como, o preenchimento incorreto dos mesmos.)
 

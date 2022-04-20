from distutils import extension
import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBlue13')
        #Layout
        layout = [
            [sg.Text('3CX backup xml archive: '),sg.Input(key='xml')],
            [sg.Text('Extension to extract PB: '), sg.Input(key='extension')],
            [sg.Button('Ok')]
        ] 
        #Janela
        window=sg.Window("Personal Phonebook Extractor - By Michatec").layout(layout)
        #Extrair os dados da tela
        self.button,self.values = window.Read()
    def Iniciar(self):
        print(self.values)
        global arquivo_xml
        global ext_number
        arquivo_xml=self.values['xml']
        ext_number=self.values['extension']
        
        #print(f'xml: {arquivo_xml}')
        #print(f'extension: {ext_number}')

tela = TelaPython()
tela.Iniciar()







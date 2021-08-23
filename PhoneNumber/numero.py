import phonenumbers
from phonenumbers import geocoder #Biblioteca para localização
from phonenumbers import carrier  #Biblioteca para operadora

fone = input('Digite o número de telefone (EX.: 11912345678): ')     #Recebe os dados do usuário
fone_ajustado = phonenumbers.parse(fone, "BR")                       #Formata os dados do usuário para o padrão do programa
local = geocoder.description_for_number(fone_ajustado, 'pt-br')      #De acordo com os dados, é dado a localização
print('Estado:',local)                                               #Exibe o local
telefone_formulario = phonenumbers.parse(fone, 'BR')                 #Guarda os dados do usuário
telefone_formatado = phonenumbers.format_number(telefone_formulario, #Formata o número para o padrão do país 'BR': (11) 91234-5678
                     phonenumbers.PhoneNumberFormat.NATIONAL)        
print('Telefone:',telefone_formatado)                                #Exibe o número formatado no padrão do país selecionado
operadora = carrier.name_for_number(fone_ajustado, "pt-br")          #Pelo número ajustado no padrão do programa, é dado a operadora
print('Operadora:',operadora)                                        #Exibe a operadora
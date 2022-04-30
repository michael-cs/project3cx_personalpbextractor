from graphic_interface import arquivo_xml as xml3cx
from graphic_interface import ext_number as extension3cx
from graphic_interface import TelaPython
import csv
import xml.etree.ElementTree as et
#xml3cx=str(input('Type the xml archive name: ')).lower().strip()
#extension3cx=str(input('Type the extension to extract PhoneBook: ')).strip()
tree = et.ElementTree(file=xml3cx)
root = tree.getroot()
name=lastname=company=phone1=phone2=home1=home2=number=number2=email=other=fax1=fax2=test=''
f = open('contacts.csv','w')
header = ['FirstName','LastName','Company','Mobile','Mobile2','Home','Home2','Business','Business2','Email','Other','BusinessFax','HomeFax','Pager']
writer = csv.writer(f)
writer.writerow(header)  

try:
    for globals in root:
        #print(globals.tag)
        for tenants in globals:
            #print(tenants.tag,tenants.attrib)
            for tenant in tenants:
                #print(tenant.tag,tenant.attrib)
                for dn in tenant:
                    #print(dn.tag,dn.attrib)
                    for extension in dn:
                        #print(extension.tag,extension.text)
                        if extension.tag == 'Number' and extension.text == extension3cx:
                            #print(extension.tag,extension.text)
                            for extension in dn:
                                #print(extension.tag,extension.text)
                                for phonebookentries in extension:
                                    if phonebookentries.tag == 'PhoneBookEntry':
                                        #print(phonebookentries.tag,phonebookentries.text,phonebookentries.attrib)
                                        for phonebookentry in phonebookentries:                                        
                                            contact=[phonebookentry.tag,phonebookentry.text]                                                                  
                                            if contact[0]=='FirstName':
                                                name=contact[1]                              
                                            elif contact[0]=='PhoneNumber':
                                                phone1=contact[1]                                                                           
                                            elif contact[0]=='LastName':
                                                lastname=contact[1]
                                            elif contact[0]=='CompanyName':
                                                company=contact[1]
                                            elif contact[0]=='AddressNumberOrData0':
                                                phone2=contact[1]
                                            elif contact[0]=='AddressNumberOrData1':
                                                home1=contact[1]
                                            elif contact[0]=='AddressNumberOrData2':
                                                home2=contact[1]
                                            elif contact[0]=='AddressNumberOrData3':
                                                number=contact[1]
                                            elif contact[0]=='AddressNumberOrData4':
                                                number2=contact[1]
                                            elif contact[0]=='AddressNumberOrData5':
                                                email=contact[1]
                                            elif contact[0]=='AddressNumberOrData6':
                                                other=contact[1]
                                            elif contact[0]=='AddressNumberOrData7':
                                                fax1=contact[1]
                                            elif contact[0]=='AddressNumberOrData8':
                                                fax2=contact[1]                                                             
                                        data = [name,lastname,company,phone1,phone2,home1,home2,number,number2,email,other,fax1,fax2,'']
                                        name=lastname=company=phone1=phone2=home1=home2=number=number2=email=other=fax1=fax2=test=''
                                        print(data)
                                        with open('contacts.csv', 'a', encoding='UTF8', newline='') as f:
                                            writer = csv.writer(f)                                                                                          
                                            writer.writerow(data)
except:
    print("close")
                    

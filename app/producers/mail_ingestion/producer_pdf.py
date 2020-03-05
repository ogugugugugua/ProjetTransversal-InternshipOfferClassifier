from imap_server import HyperplanImapServer 
from PyPDF2 import PdfFileReader
import time
import base64

class Producer:
    
    def __init__(self):
        self.list_classified_mails = []
        self.imapServerConnection()
        
    def imapServerConnection(self):
        hyperplan = HyperplanImapServer()
        imap = hyperplan.imapConnection()
        hyperplan.storeMails(imap, True)
        informations = hyperplan.fetchMails()
        self.pdfToText(informations)
        print('Searching mails...\n')
        
        try:
            while True:
                if (hyperplan.storeMails(imap)):
                    informations = hyperplan.fetchMails()
                    self.pdfToText(informations)
                    print('Searching mails...\n')
                    
                time.sleep(10)
        except KeyboardInterrupt: # Ctrl + c
            pass            
            
        hyperplan.imapDisconnection(imap)
        
    def pdfToText(self, informations):
        for mail in informations:
            if (mail[0] not in self.list_classified_mails):
                for info in mail:
                    if (mail.index(info) == 0):
                        print('Mail ID : %s\n' % info)
                        self.list_classified_mails.append(mail[0])
                        
                    if (mail.index(info) == 5):
                        attachments = info.split(',')

                        for i in range(0, len(attachments), 2):
                            attachmentName = attachments[i]
                            fileContent = attachments[i + 1]
                            
                            if 'pdf' in attachmentName:
                                print('Nom de la pièce jointe : %s\n' % attachmentName)
                                
                                test = open('./utils/files/' + attachmentName, 'wb').write(base64.b64decode(fileContent))
                                
                                with open('./utils/files/' + attachmentName, 'rb') as f:
                                    pdfReader = PdfFileReader(f)
                                    pageObject = ''
                                    
                                    for page in pdfReader.pages:
                                        pageObject += page.extractText()
                                    
                                    text = ''
                                    
                                    for line in pageObject.replace('\n', '').split('  '):
                                        text += line + '\n'
                                    
                                    return text

if __name__ == "__main__":
    producer = Producer()
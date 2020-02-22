import sys
sys.path.append('../../')

from socket import gaierror
from imaplib import IMAP4_SSL as IMAP
from imap_db import StoreMails
from utils import abs_path
import email
import base64

class HyperplanMailServer:

    def __init__(self):
        # Configuration IMAP
        self.imap_host = 'imaps.etu.univ-nantes.fr'
        self.imap_user = 'hyperplan'
        self.imap_pass = 'm5yeAJzn'
        # On récupère les mails à éviter et on enlève les \n avec strip() pour chaque adresse mail
        self.stopMail = [line.strip() for line in open('stopMail.txt', 'r').readlines()]

    def imapConnection(self):
        # Connexion au serveur IMAP
        try:
            imap = IMAP(self.imap_host)
            print('\nConnection to IMAP server intitialization of IMAP instance\n')
            imap.login(self.imap_user, self.imap_pass)
            print('Log in !\n')
            imap.select('INBOX')
            
            return imap
        except gaierror:
            print('Can\'t reach IMAP server\n')
        except IMAP.error as e:
            print('Log in failed.\n')
            print(str(e) + '\n')

    def readMails(self, imap):
        mailList = self.getMails(imap)

        for mail in mailList:
            print('------------------------------- Mail -------------------------------')
            print('%s :\nID[%s] de %s : %s\n\n%s\n' % (mail[3], mail[0], mail[1], mail[2], mail[4]))

        print('------------------------------- END Reading mails-------------------------------')
        
    def getMails(self, imap):
        print('Searching mails...\n')
        mailList = []

        tmp, data = imap.search(None, 'ALL')
        
        for num in data[0].split():
            isSenderInStopMail = True
            attachment = ''
            
            tmp, data = imap.fetch(num, '(RFC822)')
            msg = email.message_from_bytes(data[0][1])
            
            # Récupération des pièces jointes
            if msg.is_multipart():
                first = True

                for part in msg.walk():
                    ctype = part.get_content_type()
                    
                    if ctype in ['application/pdf', 'application/json', 'application/octet-stream']:
                        attachment += part.get_filename() + ',' + part.get_payload(decode = False) + ','

                    if (ctype == 'text/plain' and first):
                        body = part
                        first = False

            mail_id = int(num.decode('utf8'))
            sender = msg['From']
            subject = email.header.make_header(email.header.decode_header(msg['Subject']))
            date = email.header.make_header(email.header.decode_header(msg['Date']))

            # Vérifie si l'émetteur est dans la liste stopMail 
            if (sender not in self.stopMail):
                for adress in self.stopMail:
                    if (adress not in sender):
                        isSenderInStopMail = False
                    else:
                        isSenderInStopMail = True
                        break

            # Si l'émetteur n'est pas dans la stopMail, on ajoute le mail dans la mailList
            if (not isSenderInStopMail):               
                params = [mail_id, sender, subject, date, body, attachment[:-1]]
                mailList.append(params)

        return mailList

    def storeMails(self, imap):
        writer = StoreMails(abs_path('../databases/mail_offers.db'))
        mailList = self.getMails(imap)

        if (len(mailList) > 0):
            for i in range(len(mailList)):
                writer.write_result(mailList[i][0], mailList[i][1], mailList[i][2], mailList[i][3], mailList[i][4], mailList[i][5])
                
            print('DB update\n')
        
    def fetchMails(self):
        reader = StoreMails(abs_path('../databases/mail_offers.db'))
        
        for mail in reader.fetch_mails():
            for element in mail:
                if(mail.index(element) == 5):
                    attachments = element.split(',')

                    for i in range(0, len(attachments), 2):
                        print('Nom de la pièce jointe : %s\n' % attachments[i])
                        #open('./files/' + attachments[i], 'wb').write(base64.b64decode(attachments[i + 1]))

    def imapDisconnection(self, imap):
        # Déconnexion du serveur IMAP
        imap.close()
        print('Connection closed.\n')
        imap.logout()
        print('Log out.\n')

if __name__ == "__main__":
    hyperplan = HyperplanMailServer()
    imap = hyperplan.imapConnection()
    #hyperplan.readMails(imap)
    hyperplan.storeMails(imap)
    hyperplan.fetchMails()
    hyperplan.imapDisconnection(imap)

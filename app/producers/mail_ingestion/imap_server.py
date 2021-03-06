import sys
sys.path.append('../../')

from socket import gaierror
from imaplib import IMAP4_SSL as IMAP
from imap_db import StoreMails
from utils import abs_path
import email
import random

from email.header import decode_header

class HyperplanImapServer:

    def __init__(self):
        # Configuration IMAP
        self.imap_host = 'imaps.etu.univ-nantes.fr'
        self.imap_user = 'hyperplan'
        self.imap_pass = 'm6yeAJzn'
        
        # On récupère les mails à éviter et on enlève les \n avec strip() pour chaque adresse mail
        self.stopMail = [line.strip() for line in open('./utils/stopMail.txt', 'r').readlines()]
        
        # Commenter ces 2 lignes lors de la mise en production
        # self.clearDB()
        # self.restartCounter()

    def imapConnection(self):
        # Connexion au serveur IMAP
        try:
            imap = IMAP(self.imap_host)
            print('\nConnection to IMAP server intitialization of IMAP instance\n')
            imap.login(self.imap_user, self.imap_pass)
            print('Log in !\n')
            imap.select('INBOX')
            self.deleteMails(imap)
            
            return imap
        except gaierror:
            print('Can\'t reach IMAP server\n')
        except IMAP.error as e:
            print('Log in failed.\n')
            print(str(e) + '\n')
            
    def isSenderInStopMail(self, sender):
        # Vérifie si l'émetteur est dans la liste stopMail 
        for adress in self.stopMail:
            if (adress in sender):
                return True
                
        return False

    def readMails(self, imap):
        
        mailList = self.getMails(imap, True)

        for mail in mailList:
            print('------------------------------- Mail -------------------------------')
            print('%s :\nID[%s] de %s : %s\n\n%s\n' % (mail[3], mail[0], mail[1], mail[2], mail[4]))

        print('------------------------------- END Reading mails-------------------------------')

    def deleteMails(self, imap):
        
        typ, data = imap.search(None, 'UNSEEN')
        
        for num in data[0].split():
            typ, data = imap.fetch(num, '(RFC822)')
            msg = email.message_from_bytes(data[0][1])
            
            sender = msg['From']

            if (self.isSenderInStopMail(sender)):
                imap.store(num, '+FLAGS', r'(\deleted)')
                
        imap.expunge()
    
    def restartCounter(self):
        
        with open('./utils/counter.txt', 'r+') as f:
                f.seek(0)
                f.write(str(1))
                f.truncate()
                
    def getMails(self, imap, start = False):
        
        mailList = []

        if start:
            typ, data = imap.search(None, 'ALL')
        else:
            typ, data = imap.search(None, 'UNSEEN')
        
        for num in data[0].split():

            attachment = ''
            
            typ, data = imap.fetch(num, '(RFC822)')
            msg = email.message_from_bytes(data[0][1])
            
            # Récupération des pièces jointes
            if msg.is_multipart():
                first = True

                for part in msg.walk():
                    ctype = part.get_content_type()

                    if ctype in ['application/pdf', 'application/octet-stream']:
                        part_filename = part.get_filename()                       
                        encoding = False
                        
                        for i in range(len(decode_header(part_filename))):
                            if decode_header(part_filename)[i][1] is not None:
                                encoding = decode_header(part_filename)[i][1]
                                break
                        
                        if encoding:
                            filename = ''
                            
                            for string in decode_header(part_filename):
                                filename += string[0].decode(encoding)
                        else:
                            filename = part_filename
                            
                        attachment += filename + ',' + part.get_payload(decode = False) + ','

                    if (ctype == 'text/plain' and first):
                        body = part
                        first = False
            
            sender = msg['From']
            subject = email.header.make_header(email.header.decode_header(msg['Subject']))
            date = email.header.make_header(email.header.decode_header(msg['Date']))
            
            with open('./utils/counter.txt', 'r+') as f:
                mail_id = int(f.read())
                f.seek(0)
                f.write(str(mail_id + 1))

            # Si l'émetteur n'est pas dans la stopMail, on ajoute le mail dans la mailList
            if (not self.isSenderInStopMail(sender)):               
                params = [mail_id, sender, subject, date, body, attachment[:-1]]
                mailList.append(params)
            
        return mailList

    def storeMails(self, imap, start = False):
        
        mailList = self.getMails(imap, start)

        if (len(mailList) > 0):
            writer = StoreMails(abs_path('databases/mail_offers.db'))
            
            for i in range(len(mailList)):
                writer.write_result(mailList[i][0], mailList[i][1], mailList[i][2], mailList[i][3], mailList[i][4], mailList[i][5])
                
            print('DB updated\n')
            return True
        
        elif (len(mailList) == 0):
            return False
        
    def fetchMails(self):
        
        reader = StoreMails(abs_path('databases/mail_offers.db'))
        mailsInformations = []
        
        for mail in reader.fetch_mails():
            informations = []
            
            for element in mail:
                informations.append(element)
                
            mailsInformations.append(informations)
            
        return mailsInformations

    def clearDB(self):
        
        StoreMails(abs_path('databases/mail_offers.db')).clear_DB()
        
    def imapDisconnection(self, imap):
        # Déconnexion du serveur IMAP
        imap.close()
        print('Connection closed.\n')
        imap.logout()
        print('Log out.\n')

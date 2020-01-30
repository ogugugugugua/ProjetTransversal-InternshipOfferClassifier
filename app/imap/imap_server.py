from imaplib import IMAP4_SSL as IMAP
from socket import gaierror
import email


class HyperplanMailServer:

    def __init__(self):
        # Configuration IMAP
        self.imap_host = 'imaps.etu.univ-nantes.fr'
        self.imap_user = 'hyperplan'
        self.imap_pass = 'm5yeAJzn'

        # On récupère les mails à éviter et on enlève les \n avec strip() pour chaque adresse mail
        self.stopMail = [line.strip()
                         for line in open('stopMail.txt', 'r').readlines()]

    def imapConnection(self):
        # Connexion au serveur IMAP
        try:
            imap = IMAP(self.imap_host)
            print('Connection to IMAP server intitialization of IMAP instance\n')
            print('Try to log in...\n')
            imap.login(self.imap_user, self.imap_pass)
            print('Log in !\n')

            return imap
        except gaierror:
            print('Can\'t reach IMAP server\n')
        except IMAP.error as e:
            print('Log in failed.\n')
            print(str(e) + '\n')

    def readMails(self, imap):
        imap.select('INBOX')
        print('Recherche de mails...\n')

        tmp, data = imap.search(None, 'ALL')

        for num in data[0].split():
            tmp, data = imap.fetch(num, '(RFC822)')

            msg = email.message_from_bytes(data[0][1])
            sender = msg['From']

            if(sender not in self.stopMail):
                subject = email.header.make_header(
                    email.header.decode_header(msg['Subject']))
                print('ID[%s] de %s : %s' % (str(num).replace(
                    'b', '').replace('\'', ''), sender, subject))
                # Affiche le corps du mail en bytes
                # print(data[0][1])
                
    def storeMails(self, imap):
        

    def imapDisconnection(self, imap):
        # Déconnexion au serveur IMAP
        imap.close()
        print('\nConnection closed\n')
        imap.logout()
        print('Log out.\n')


if __name__ == "__main__":
    hyperplan = HyperplanMailServer()
    imap = hyperplan.imapConnection()
    hyperplan.readMails(imap)
    hyperplan.imapDisconnection(imap)

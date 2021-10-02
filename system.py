
import dropbox

class FileTransfer:
    def __init__(self,accessToken):
        self.accessToken = accessToken

    def upload_file(self,up_file):
        dropbx = dropbox.Dropbox(self.accessToken)
        
        required_file = open(up_file,'rb')
        dropbx.files_upload(required_file.read(),up_file)

    
def mover():
    token = 'sl.A5k1MkttReM20jTSRSKcbe9DQkO17-9S4JrSPYG-f7RO9XMmMMuHa4ooL8WVsmv-5kpP1vOsxg2Ucm-Wc07fQxR8BSGlqdpBapkKjq3PU5zLsK1vyn4i3-6Fd26aW9KzRsfhjMc'
    file_upload = FileTransfer(token)

   
    Up_file = input("ENTER THE FULL PATH TO UPLOAD TO THE DROPBOX ")
    file_upload.upload_file(Up_file)
    print('File Has Been Moved to the dropbox')

mover()
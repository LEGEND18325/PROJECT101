import dropbox 
import os
from dropbox.files import WriteMode
class TransferData:

    def __init__(self,acessToken):
      self.acessToken=acessToken

    def uploadFiles(self,source,destination):
       upload=dropbox.Dropbox(self.acessToken)
       for root, dirs, files in os.walk(source):
           
           for fileName in files:
               localPath=os.path.join(root,fileName)

               relativePath= os.path.relpath(localPath,source)
               dropboxPath= os.path.join(destination,relativePath)

               with open(localPath,'rb')as f:
                   upload.files_upload(f.read(),dropboxPath,mode=WriteMode('overwrite'))


        
def main():
    accessToken='sl.A5JzL3FJk9G_6SQ_1 - zB6Mz44g1FqWmQ7 - k5QDbvAlkuFDOq6vRdYJUgjsONuny3Nhe1UdOTStxCQpz8D5BW36hIqGboUsFiNM77S3WHpRLyKBtp8K7VZuUGiqIVoNMH_gLYMII'
   # sl.A5Lmk7BT5rWtUZtdZBDU9Y1keu72Z2otdk_G5cZ5Z2Qkgtbgut7uw4y - qoBhy5hVKKtoul0UJPrZ1a0mW2FvDYoRRl_r - ZyDMxSScp6cCkeI3f4qNJOequ7iUk8xk6ev6kxbxHs
    transferData=TransferData(accessToken)
    source=input('Enter File Which You Want To Transfer : ')
    destination=input('Enter the Destination Where You Want To Move : ')
    transferData.uploadFiles(source,destination)
    print('Your Files Has Been Transfered')


main()


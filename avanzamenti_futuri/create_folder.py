from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import sys

# Autenticazione
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Effettua l'autenticazione con Google

drive = GoogleDrive(gauth)

# Prendi il nome della cartella da creare dall'argomento
user = sys.argv[1]

# ID della cartella padre in cui creare la sottocartella
parent_folder_id = '1w7XtcV_QUOcU1SZZIHdV4eC59ShX7URC'

# Verifica se la cartella esiste già
query = f"'{parent_folder_id}' in parents and title='{user}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
file_list = drive.ListFile({'q': query}).GetList()

if len(file_list) > 0:
    print(f"La cartella '{user}' esiste già.")
else:
    # Crea la nuova cartella
    folder_metadata = {
        'title': user,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [{'id': parent_folder_id}]
    }
    folder = drive.CreateFile(folder_metadata)
    folder.Upload()
    print(f"Cartella '{user}' creata con successo.")

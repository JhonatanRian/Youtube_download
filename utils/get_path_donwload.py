import os
import platform

def get_download_folder():
    system = platform.system().lower()
    
    if system == "windows":
        return os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == "darwin":  # macOS
        return os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == "linux" or system == "posix":  # UNIX-like
        return os.path.join(os.path.expanduser("~"), "Downloads")
    else:
        # Sistema operacional desconhecido, você pode adicionar lógica extra aqui, se necessário
        raise NotImplementedError("Sistema operacional não suportado pela função.")

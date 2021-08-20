from hurry.filesize import size
from pytube import YouTube

class Streams_:
    
    def __init__(self: object, youtube: YouTube) -> None:
        self.youtube: YouTube = youtube
        self.available_resolutions: dict = dict()
        
    
    def streams_url(self: object) -> dict:
        resolutions_for_find: tuple = ("144p", "360p", "480p", "720p", "1080p")
        
        self.streams = self.youtube.streams
        for resolution in resolutions_for_find:
            cont = 0
            for stream in self.streams:
                print(stream.filesize, resolution)
                converted = str(stream)
                if converted.count(resolution):
                    cont += 1
                    if cont == 1:
                        self.available_resolutions[resolution] = size(stream.filesize)
                    
        return self.available_resolutions
    
if __name__ == "__main__":
    try:
        y = YouTube("https://www.youtube.com/watch?v=0ZQCJIEJA8c")
        resolution = Streams_(y)
        print(resolution.streams_url())
        #resolution.streams.get_by_resolution("480p").download("/home/dev/Área de Trabalho/Youtube_download")
    except:
        print("Error")
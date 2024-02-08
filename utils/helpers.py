from pytube import YouTube, Stream


class StreamYt:
    def __init__(self, stream: Stream) -> None:
        self.__stream: Stream = stream

    @property
    def stream(self: object) -> Stream:
        return self.__stream

    def __str__(self) -> str:
        if 'video' in self.__stream.mime_type:
            return f" {self.__stream.mime_type} {self.__stream.resolution} {self.__stream.filesize_mb:.2f} MB"
        else:
            return f" {self.__stream.mime_type} {self.__stream.filesize_mb:.2f} MB"

    def __repr__(self) -> str:
        return f" {self.__stream.mime_type} {self.__stream.resolution}"


class DownloadYt:
    
    def __init__(self, url: str) -> None:
        self.url = url
        self.yt = YouTube(self.url)
        self.resolutions: dict[str, Stream] = {}
        for st in list(self.yt.streams.filter(progressive=True)) + list(self.yt.streams.filter(type='audio')):
            self.resolutions[str(StreamYt(st))] = st
        self.resolution: Stream = None
        self.title = self.yt.title
        self.progress_bar = None


def generate_title(title, list_titles):
    cont = 0
    new_title = title
    while new_title in list_titles:
        cont += 1
        new_title = f"{title}-{str(cont)}"
    return new_title
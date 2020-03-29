from PyQt5.QtCore import *
from pytube import YouTube
from threading import Thread

import Core.OSHandler as OSHandler
import Core.FFmpegHandler as FFmpegHandler


class YoutubeDownloader(QObject):
    class DownloadHandler(QObject):
        progressSignal = pyqtSignal([int, int])
        completeSignal = pyqtSignal()

        def getProgressSignal(self):
            super(QObject, self).__init__()
            return self.progressSignal

        def progress(self, stream, chunk, bytes_remaining):
            if stream == self.audioStream:
                self.downloadedAudio = self.audioStream.filesize - bytes_remaining
            elif stream == self.videoStream:
                self.downloadedVideo = self.videoStream.filesize - bytes_remaining

            downloaded = self.downloadedAudio + self.downloadedVideo
            self.progressSignal.emit(downloaded, self.filesize)

        def merge(self):
            self.videoDownload.join()
            self.audioDownload.join()

            # merge via ffmpeg
            FFmpegHandler.videoAudioMerge(str(QFileInfo('tmp/video.mp4').absoluteFilePath()),
                str(QFileInfo('tmp/audio.mp4').absoluteFilePath()),
                str(QFileInfo(self.filename).absoluteFilePath()))
            print('done')

            # delete tmp files
            OSHandler.rmdir('tmp')

            self.completeSignal.emit()

        def __init__(self, filename, video):
            print('downloading {} ...'.format(filename))
            self.filename = filename
            self.video = video
            self.video.register_on_progress_callback(self.progress)
            self.audioStream = self.video.streams.get_audio_only()
            self.videoStream = self.video.streams.filter(adaptive=True, file_extension="mp4").order_by('resolution').desc().first()
            self.filesize = self.videoStream.filesize + self.audioStream.filesize
            self.downloadedAudio = 0
            self.downloadedVideo = 0

            self.videoDownload = Thread(target=self.videoStream.download, args=('tmp', 'video'))
            self.videoDownload.start()

            self.audioDownload = Thread(target=self.audioStream.download, args=('tmp', 'audio'))
            self.audioDownload.start()

            self.mergeThread = Thread(target=self.merge)
            self.mergeThread.start()

    def __init__(self, parent=None):
        super(QObject, self).__init__(parent)

    def download(self, url, filename):
        fileInfo = QFileInfo(filename)
        dirPath = fileInfo.absolutePath()
        fileBaseName = fileInfo.baseName()

        video = YouTube(url)
        
        dh = self.DownloadHandler(filename, video)

        return dh.getProgressSignal()


if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=d3D7Y_ycSms'
    yd = YoutubeDownloader()
    yd.download(url, '')

import ffmpeg

def videoAudioMerge(videoFilename, audioFilename, filename='res/res.mp4'):
    videoInput = ffmpeg.input(videoFilename)
    audioInput = ffmpeg.input(audioFilename)
    output = ffmpeg.concat(videoInput, audioInput, v=1, a=1).output(filename).run()

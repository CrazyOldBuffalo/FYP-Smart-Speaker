from Services.sttTest import SpeechToText
from precise_runner import PreciseEngine, PreciseRunner

class WakeWord:

    def __init__(self, enginePath, modelPath):
        self.__model = modelPath
        self.__engine = enginePath
        self.__runner = None
        self.__stt = SpeechToText(5)

    def start(self):
        engine = PreciseEngine(self.__engine, self.__model)
        self.__runner =  PreciseRunner(engine, on_activation = self.on_activation)
        self.__runner.start()

    def stop(self):
        if self.__runner:
            self.__runner.stop()

        
    def update_chunk(self, chunk):
        if self.__runner:
            self.__runner.chunk_size = chunk

    def on_activation(self):
        text = self.__stt.recognition()
        if text is not None:
            print(text)
        else:
            print("No Input Detected")


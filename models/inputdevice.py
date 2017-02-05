import numpy as np
import pyaudio
from   pyee import EventEmitter
import warnings
import models.model
Model = models.model.Model

class InputDevice(Model, EventEmitter):
    def __init__(self, **kwargs):
        Model.__init__(self, **kwargs)
        EventEmitter.__init__(self)

    def getStream(self):
        self._warnUnimplemented('getStream')


class AudioInput(InputDevice):
    
    _defaults = {
        'deviceIndex': 0,
        'name': 'unknown',
        'sampleRate': 48000,
        'chunk': 256,
        'stream': None
    }
    
    def __init__(self, **kwargs):
        InputDevice.__init__(self, **kwargs)

    def getStream(self):
        if (self.stream):
            return self.stream
        
        p = pyaudio.PyAudio()
        self.stream = p.open(
          format=pyaudio.paInt16, 
          channels=1, 
          rate=int(self.sampleRate), 
          input=True, 
          input_device_index=self.deviceIndex,
          frames_per_buffer=self.chunk,
          stream_callback=self._onChunk
        )
        return self.stream

    def _onChunk(self, window, frame_count, time_info, status_flags):
        self.emit('chunk', {
          'window': window,
          'frame_count': frame_count,
          'time_info': time_info,
          'status_flags': status_flags
        })
        return (None, pyaudio.paContinue)

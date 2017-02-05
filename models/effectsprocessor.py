from   appDispatcher import eventDispatcher
import controllers.inputdevices as inputsController
from   models.model import Model
import numpy as np
from   pyee import EventEmitter
import sys

def factory(**kwargs):
    inputType = kwargs.pop('inputType')
    
    if inputType == 'AUDIO':
        return AudioProcessor(**kwargs)
    
    raise Exception("Missing or unsupported inputType: %s"%inputType)




class EffectsProcessor(Model, EventEmitter):
    _defaults = {}
    
    def __init__(self, **kwargs):
        Model.__init__(self, **kwargs)
        EventEmitter.__init__(self)

    def getInputDevice(self):
        return inputsController.getInputByDeviceId(self.deviceId)
    
    def startStream(self):
        self._warnUnimplemented("startStream")
        
    def removeListeners(self):
        inputDevice = self.getInputDevice()
        inputDevice.remove_listener('chunk', self._onChunk)



    
class AudioProcessor(EffectsProcessor):

    _defaults = {
        'enabled'    : 0,
        'multiplier' : 1,
        'offset'     : 0,
        'inertia'    : 0,
        'deviceId'   : None,
        'data' : {
            'raw' : np.array([0]),
            'processed': np.array([0])
        }
    }
    
    inputType = 'AUDIO'

    def __init__(self, **kwargs):
        EffectsProcessor.__init__(self, **kwargs)
        audio0 = inputsController.getAudioInputByDeviceIndex(0);
        self.deviceId = audio0.uuid
        
    def startStream(self):
        audioDevice = self.getInputDevice()
        if not audioDevice:
            return None
        
        audioDevice.getStream()
        audioDevice.on('chunk', self._onChunk)
        
    def _onChunk(self, params):
        data = np.fromstring(params['window'], dtype=np.int16)
        powerSpectrum = np.absolute(np.fft.rfft(data, norm='ortho'))
        spectrum = 20 * np.log10(powerSpectrum) / 100
        processed = self.processSpectrum(spectrum)
        eventDispatcher.dispatch({
            'type': 'STREAM_CHUNK',
            'value': {
                'uuid': self.uuid,
                'raw': spectrum,
                'processed': processed
            }
        })
    
    def processSpectrum(self, spectrum):
        mult = self.multiplier
        if mult == 0:
            mult = 1
        if mult < 0:
            mult = (100 + mult) * .01
        
        spectrum = mult * spectrum
        spectrum = self.offset + spectrum
        return spectrum
    
    
    def __del__(self):
        print '__del__'
        

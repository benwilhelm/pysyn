import controllers.inputdevices as inputsController
import models.model
import numpy as np
from   pyee import EventEmitter
import sys

Model = models.model.Model

class EffectsProcessor(Model, EventEmitter):

    _defaults = {
        'enabled'     : 0,
        'multiplier'  : 1,
        'offset'      : 0,
        'inertia'     : 0,
        'deviceIndex' : 0
    }

    def __init__(self, **kwargs):
        Model.__init__(self, **kwargs)
        EventEmitter.__init__(self)
        self.startStream();
        
    def startStream(self):
        audioDevice = inputsController.getAudioInputByDeviceIndex(self.deviceIndex)
        audioDevice.getStream()
        audioDevice.on('chunk', self._onChunk)
        
    def _onChunk(self, params):
        data = np.fromstring(params['window'], dtype=np.int16)
        powerSpectrum = np.absolute(np.fft.rfft(data, norm='ortho'))
        spectrum = 20 * np.log10(powerSpectrum) / 100
        # processed = spectrum
        processed = self.processSpectrum(spectrum)
        # print 'chunk'
        self.emit('chunk', {
            'raw': spectrum,
            'processed': processed
        })
    
    def processSpectrum(self, spectrum):
        mult = self.multiplier
        if mult == 0:
            mult = 1
        if mult < 0:
            mult = (100 + mult) * .01
        
        processed = mult * spectrum
        return processed

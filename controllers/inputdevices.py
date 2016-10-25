import pyaudio
import models.inputdevice
AudioInput = models.inputdevice.AudioInput

__data = {
    'inputs': {
        'audio': {}
    }
}

pa = pyaudio.PyAudio()
for i in range(pa.get_device_count()):
    device = pa.get_device_info_by_index(i)
    audioInput = AudioInput(
        deviceIndex=i,
        name=device['name'],
        sampleRate=device['defaultSampleRate']
    )
    audioId = audioInput.uuid
    __data['inputs']['audio'][audioId] = audioInput


def getAudioInputs():
    return __data['inputs']['audio']

def getAudioInputsList():
    inputs = __data['inputs']['audio'].values()
    inputs.sort(sortByDeviceIndex)
    return inputs

def getAudioInput(audioId):
    return __data['inputs']['audio'].get(audioId, None)

def getAudioInputByDeviceIndex(idx):
    for inp in __data['inputs']['audio'].values():
        if idx == inp.deviceIndex:
            return inp
    return None

def getAudioInputByName(name):
    for inp in __data['inputs']['audio'].values():
        if name == inp.name:
            return inp
    return None


def sortByDeviceIndex(x, y):
    dx = x.deviceIndex
    dy = y.deviceIndex 
    
    if dx == dy:
        return 0
    
    if dx < dy:
        return -1
    
    if dx > dy:
        return 1

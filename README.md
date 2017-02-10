## Prerequisites

### PortAudio

Installing on a Mac, with HomeBrew:

    $ brew install portaudio
    
### Jack (Optional)

Installing on a Mac, with HomeBrew:

    $ brew install jack


## Troubleshooting and Gotchas

### PyAudio may not build without explicitly defined header paths

Many thanks to [fukudama at StackOverflow][so-link] for this solution. In short, before running `pip install -r requirements`, install pyaudio explicitly with this command:

    $ pip install --global-option='build_ext' \
    --global-option='-I/usr/local/include' \
    --global-option='-L/usr/local/lib' \
    pyaudio

[so-link]: http://stackoverflow.com/questions/33513522/when-installing-pyaudio-pip-cannot-find-portaudio-h-in-usr-local-include

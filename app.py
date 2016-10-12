#!/usr/bin/env python

import ui
from store import settings as settingsStore

def main():
    app_ui = ui.initialize()
    app_ui.mainloop()

if __name__ == "__main__":
    main()

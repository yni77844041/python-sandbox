#!"c:\users\niwa yoshiki\desktop\pg\python\scraping\sc-venv\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'csvkit==1.0.3','console_scripts','csvstack'
__requires__ = 'csvkit==1.0.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('csvkit==1.0.3', 'console_scripts', 'csvstack')()
    )

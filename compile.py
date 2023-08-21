"""
Compile Script.
Performs the jobs for compling Themera.
"""
import re
from datetime import datetime
from os import system as run
from os.path import abspath, sep, split

# import src
from src.constants import APP_ID
from src.version_and_copyright import __version__ as VERSION

COMPANY_NAME, PRODUCT_NAME = (
    "Divine Afam-Ifediogor",
    "Themera",
)  # This value must match the APP_ID from constants.py.

YEAR = datetime.now().year
OUTPUT_NAME = f"themera-v{VERSION}-win-x86_64"
DEFAULT_OUTPUT_DIR = f"bin/v{VERSION.split('.', 1)[0]}/{VERSION}/{OUTPUT_NAME}"
ICON_PATH_WINDOWS = "branding/raster/themera_logo.ico"
ICON_PATH_LINUX = "branding/raster/themera_logo.png"
ICON_PATH_MAC = "branding/raster/themera_logo.icns"
DESCRIPTION = "PySimpleGUI Theme Code Generator"
COPYRIGHT = 

GENERAL_SETTINGS = (
    "--follow-imports "
    "--remove-output "
    f'--output-dir="{DEFAULT_OUTPUT_DIR}" '
    "--disable-console "
    "--low-memory "
)

WINDOWS_SETTINGS = f'--windows-icon-from-ico="{ICON_PATH_WINDOWS}" '
MAC_SETTINGS = (
    f'--macos-app-icon="{ICON_PATH_MAC}"'
    f"--macos-signed-app-name={APP_ID}"
    f"--macos-app-name={PRODUCT_NAME}"
    f"--macos-app-version={VERSION}"
)
LINUX_SETTINGS = f'--linux-icon="{ICON_PATH_LINUX}" '

OTHER_SETTINGS = (
    f'--company-name="{COMPANY_NAME}" '
    f'--product-name="{PRODUCT_NAME}" '
    f'--file-version="{VERSION}" '
    f'--product-version="{VERSION}" '
    f'--file-description="{DESCRIPTION}" '
    f'--copyright="{COPYRIGHT}" '
    # The source entry
    '"./src/themera.py" '
)

run(
    "nuitka "
    # "--enable-plugin=tk-inter "
    # OS-Specific Settings for compilation
)


def update_copyright(filepath):
    print(f"Updating the copyright year in file {filepath}...", end="")
    pattern = re.sub(r"[0-9]{4,4}", "[0-9]{4,4}", COPYRIGHT)
    with open("DESCRIPTION.md", "r") as desc:
        content = desc.read().replace("\n", r"\n")
        content = re.sub(pattern, COPYRIGHT, content)
        content = content.replace(r"\n", "\n")

    with open("DESCRIPTION.md", "w") as desc:
        desc.write(content)


update_copyright("src/themera.py")

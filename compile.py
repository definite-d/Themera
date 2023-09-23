"""
Compile Script.
Performs the jobs for compling Themera.

Since this project was primarily built on Windows, this script is 
guaranteed to work for Windows compilation, but it "should" work on 
other platforms (Mac and Linux).

The configuration functions are at the bottom of the script, 
if modification is required.

Compilation in general requires the `black` and `isort` libraries, 
as well as `nuitka` (and a suitable compiler) and a working install 
of `git`.

Compiling for Windows requires InnoSetup installed and the 
installation directory added to PATH.

While this script runs with whatever Python version available to it, 
you may choose to use a specific version of Python just for compiling 
with Nuitka. If you have multiple Python versions installed, modify 
the `PYTHON_VERSION` variable below to suit the one you wish to use for 
compilation, before running this script. Set it to `None` to use the 
default (or only one) available.

Supporting 32-bit Windows also requires the MSVC compiler, and 
a 32-bit version of Python available (3.7.9 has been tested by 
me and is thus set as default) to allow cross-compilation for 
32 bit Windows as well. Setting PYTHON_VERSION to a 32-bit 
version of Python will automatically compile for 32-bit 
compatibility in general. For best compatibility with 32-bit systems, 
I advise simply compiling on a 32-bit system itself if possible.
"""

PYTHON_VERSION = "3.7"

import re
from datetime import datetime
from hashlib import md5, sha256
from os import system as run
from pathlib import Path
from platform import system
from shutil import rmtree
from subprocess import check_output
from sys import path
from zipfile import ZipFile

from PySimpleGUI import running_linux, running_mac, running_windows


print("Starting the Compiler Script...")

# I'd like to do what I call a "pro-gamer move"...
COMPILER_VERSION_ARCHITECTURE = eval(
    check_output(
        f'py -{PYTHON_VERSION} -c "from platform import architecture; print(architecture())"'
    ).decode("utf-8")
)
COMPILER_PYTHON_VERSION_IS_32_BITS = (
    True if COMPILER_VERSION_ARCHITECTURE[0].startswith("32") else False
)

SYSTEM = system()

if PYTHON_VERSION:
    print(
        f"Your chosen compiler Python version is {PYTHON_VERSION} {COMPILER_VERSION_ARCHITECTURE}"
    )
if COMPILER_PYTHON_VERSION_IS_32_BITS:
    _ = lambda: SYSTEM if SYSTEM != "Darwin" else "MacOS"
    print(
        f"Your {_()} compilation results will have 32-bit compatibility."
    )

# SOURCE_FOLDER = Path("./themera copy")
SOURCE_FOLDER = Path("./themera")
path.insert(0, str(SOURCE_FOLDER.resolve()))
from constants import APP_ID, HELP_PATH
from version_and_copyright import COPYRIGHT
from version_and_copyright import __version__ as VERSION

platforms = {
    "Linux": "linux",
    "Darwin": "macos",
    "Windows": "win",
}

DESCRIPTION = "PySimpleGUI Theme Code Generator"
APP_NAME = (
    f"themera"
    f"-v{VERSION}"
    f"-{platforms[SYSTEM]}"
    f"{('-x86' if COMPILER_PYTHON_VERSION_IS_32_BITS else '-x86_64') if SYSTEM == 'Windows' else ''}"
).lower()

if SYSTEM == "Windows":
    with open(".uuid", "r") as env:
        APP_UUID = env.readline()
        if APP_UUID == "":
            message = (
                "The UUID for compiling the Installer was not found.\n"
                "Please request that information from Divine Afam-Ifediogor."
            )
            raise Exception(message)

ROOT_PATH = Path(".").resolve()
OUTPUT_PATH = Path(f"bin/v{VERSION.split('.', 1)[0]}/{VERSION}/{APP_NAME}")
NUITKA_OUTPUT_PATH = Path(f"{OUTPUT_PATH}/themera.dist/")
OUTPUT_FILES = tuple(NUITKA_OUTPUT_PATH.rglob("*"))
TOTAL_NUMBER_OF_OUTPUT_FILES = len(OUTPUT_FILES)
INSTALLER_PATH = Path(f"{OUTPUT_PATH}/installer/{APP_NAME}.exe")
YEAR = datetime.now().year
ZIPFILE_PATH = Path(f"{OUTPUT_PATH}/{APP_NAME}.zip")

COMPANY_NAME, PRODUCT_NAME = (
    "Divine Afam-Ifediogor",
    "Themera",
)  # This value must match the APP_ID from constants.py.

ICON_PATH_LINUX = "branding/raster/themera_logo.png"
ICON_PATH_MAC = "branding/raster/themera_logo.icns"
ICON_PATH_WINDOWS = "branding/raster/themera_logo.ico"

GENERAL_SETTINGS = (
    "--follow-imports "
    "--remove-output "
    f'--output-dir="{OUTPUT_PATH}" '
    "--disable-console "
    f"--include-data-files={HELP_PATH}={HELP_PATH} "
    "--low-memory "
    "--standalone "
    "--enable-plugin=tk-inter "
    # "--run "
)

WINDOWS_SETTINGS = f'--windows-icon-from-ico="{ICON_PATH_WINDOWS}" '
MAC_SETTINGS = (
    f'--macos-app-icon="{ICON_PATH_MAC}"'
    f"--macos-signed-app-name={APP_ID}"
    f"--macos-app-name={PRODUCT_NAME}"
    f"--macos-app-version={VERSION}"
)
LINUX_SETTINGS = f'--linux-icon="{ICON_PATH_LINUX}" '

OS_SETTINGS = (
    WINDOWS_SETTINGS
    if running_windows()
    else MAC_SETTINGS
    if running_mac()
    else LINUX_SETTINGS
    if running_linux()
    else ""
)

OTHER_SETTINGS = (
    f'--company-name="{COMPANY_NAME}" '
    f'--product-name="{PRODUCT_NAME}" '
    f'--file-version="{VERSION}" '
    f'--product-version="{VERSION}" '
    f'--file-description="{DESCRIPTION}" '
    f'--copyright="{COPYRIGHT}" '
    # The source entry
    "themera/themera.py"
)


def perform_nuitka_compilation():
    run(
        "py "
        f"-{PYTHON_VERSION} "
        "-m "
        "nuitka "
        f"{GENERAL_SETTINGS} "
        f"{OS_SETTINGS} "
        f"{OTHER_SETTINGS}"
    )


def update_copyright(filepath):
    pattern = re.sub(r"[0-9]{4,4}", "[0-9]{4,4}", COPYRIGHT)
    with open(filepath, "r") as current_source_file:
        content = current_source_file.read()
        content = re.sub(pattern, COPYRIGHT, rf"{content}")
        content = content.replace(r"\\n", "\n")
    with open(filepath, "w") as current_source_file:
        current_source_file.write(content)


def run_formatting(filepath):
    run(f'isort "{filepath}" --quiet')
    run(f'black "{filepath}" --quiet')


def update_and_format_source_files():
    for file_ in Path(SOURCE_FOLDER).glob("*.py"):
        print(f"Updating and formatting {file_}...")
        update_copyright(file_)
        run_formatting(file_)


def write_hashes(filepath: Path):
    print(f"Hashing {filepath}...")
    hashes_path = filepath.parent
    sha256_hash = sha256()
    md5_hash = md5()
    memview = memoryview(bytearray(128 * 1024))
    with open(filepath, "rb") as source:
        for n in iter(lambda: source.readinto(memview), 0):
            chunk = memview[:n]
            sha256_hash.update(chunk)
            md5_hash.update(chunk)
    with open(
        f"{hashes_path}/{filepath.name}.sha256sum.txt",
        "w",
    ) as sha256_output_file:
        sha256_output_file.write(sha256_hash.hexdigest())
    with open(
        f"{hashes_path}/{filepath.name}.md5sum.txt",
        "w",
    ) as md5_output_file:
        md5_output_file.write(md5_hash.hexdigest())


def zip_output_into_archive(remove_output_dir_after=True):
    size = len(str(TOTAL_NUMBER_OF_OUTPUT_FILES))
    if NUITKA_OUTPUT_PATH.exists():
        print(f'Adding output files to archive at "{ZIPFILE_PATH}"')
        with ZipFile(ZIPFILE_PATH, "w") as archive:
            for index, item in enumerate(OUTPUT_FILES):
                print(
                    f"\r{index+1:4d} of {TOTAL_NUMBER_OF_OUTPUT_FILES} added to archive ({(index/TOTAL_NUMBER_OF_OUTPUT_FILES)*100:.0f}%).",
                    end="",
                )
                archive.write(item, item.relative_to(NUITKA_OUTPUT_PATH))
            archive.close()
        print("", end="")
        write_hashes(ZIPFILE_PATH)
        print("Done with archiving.")
    else:
        print("The output path was not found. The archive was not created.")
    if remove_output_dir_after:
        print("Removing original output files.")
        rmtree(NUITKA_OUTPUT_PATH)


def prep_innosetup_script():
    root_path = str(ROOT_PATH.resolve()).replace("\\", "\\\\")
    output_path = str(OUTPUT_PATH.resolve()).replace("\\", "\\\\")

    PATTERNS_TO_REPLACEMENTS = {
        r'#define RootPath ".*"': f'#define RootPath "{root_path}"',
        r'#define OutputPath ".*"': f'#define OutputPath "{output_path}"',
        r'#define ProgramSourcePath ".*"': '#define ProgramSourcePath "'
        + output_path
        + '\\\\themera.dist"',
        r'#define InnoSetupOutputPath ".*"': '#define InnoSetupOutputPath "'
        + output_path
        + '\\\\installer"',
        r'#define MyAppVersion ".*"': f'#define MyAppVersion "{VERSION}"',
        r"OutputBaseFilename=.*": f"OutputBaseFilename={APP_NAME}",
        r"AppId=\{\{.*\}": "AppId={{" + APP_UUID + "}",
        r"AppCopyright=.*": f"AppCopyright={COPYRIGHT}",
    }

    with open("template.iss", "r") as script:
        content = script.read()
        for pattern, replacement in PATTERNS_TO_REPLACEMENTS.items():
            content = re.sub(pattern, replacement, content)
    with open("temp.iss", "w") as script:
        script.write(content)


def compile_installer_for_windows():
    if SYSTEM == "Windows":
        print("Starting compilation of the Windows installer for Themera.")
        prep_innosetup_script()
        run("iscc /Q temp.iss")
        Path("temp.iss").unlink()
        if INSTALLER_PATH.is_file():
            write_hashes(INSTALLER_PATH)
        else:
            print("The compilation of the Windows installer failed.")
        return
    print("The Windows Installer for Themera can only be compiled on Windows.")


def update_version_in_readme():
    print("Updating version within README.md...")
    pattern = r"## Latest Version: v.*"
    replacement = f"## Latest Version: v{VERSION}"
    with open("README.md", "r") as readme_file:
        content = readme_file.read()
        content = re.sub(pattern, replacement, content)
    with open("README.md", "w") as readme_file:
        readme_file.write(content)


def git_commit(message: str = f"New Commit at {datetime.now()}"):
    print("Staging commit...")
    run(f'git commit -m "{message}" -a')
    print("Commit completed successfully.")


# The following lines are the main controls to this script. Comment and uncomment as desired, but do not change the order.

update_version_in_readme()
update_and_format_source_files()
perform_nuitka_compilation()
compile_installer_for_windows()
zip_output_into_archive()
git_commit()
print("compile.py has completed execution.")

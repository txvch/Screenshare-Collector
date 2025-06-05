import os
import requests
import zipfile
import subprocess
import re
import csv
import yara
from multiprocessing import Pool, cpu_count
import ctypes
import ctypes.wintypes
import fade
import time
import hashlib
import pefile
import math
from datetime import datetime
from functools import partial
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import colorama
from colorama import Fore, Back, Style
import sys
import msvcrt
colorama.init()

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()!= 0
    except:
        return False

def run_as_admin():
    if getattr(sys, 'frozen', False):
        script = sys.executable
    else:  # inserted
        script = sys.executable(' \"', **os.path.abspath(__file__)) + '\"'
    ctypes.windll.shell32.ShellExecuteW(None, 'runas', script, None, None, 1)
    sys.exit(0)
session = requests.Session()

def print_banner():
    banner = '\n░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓██████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓███████▓▒░ \n░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        \n░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        \n░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  \n░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ \n░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ \n░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓██████▓▒░  ░▒▓█▓▒░    ░▒▓██████▓▒░░▒▓███████▓▒░  \n                                                                                                       \n    '
    print(f'{Fore.RED}{banner}{Style.RESET_ALL}')
    print(f'{Fore.WHITE}Advanced Forensic Analysis Tool{Style.RESET_ALL}')
    print(f"{Fore.RED}{'================================================================================'}{Style.RESET_ALL}\n")

def print_menu():
    print(f"{Fore.WHITE}╔{'══════════════════════════════════════════════════════════════════════════════'}╗")
    print(f"║{Fore.RED} RedLotus Collector Advanced {Fore.WHITE}{'                                                    '}║")
    print(f"╠{'══════════════════════════════════════════════════════════════════════════════'}╣")
    print(f"║{Fore.WHITE} 1. {Fore.RED}Downloader{Fore.WHITE}{'                                                                 '}║")
    print(f"║{Fore.WHITE} 2. {Fore.RED}Path\'s Analyzer{Fore.WHITE}{'                                                              '}║")
    print(f"║{Fore.WHITE} 3. {Fore.RED}Information{Fore.WHITE}{'                                                                   '}║")
    print(f"║{Fore.WHITE} 4. {Fore.RED}Exit{Fore.WHITE}{'                                                                        '}║")
    print(f"╚{'══════════════════════════════════════════════════════════════════════════════'}╝{Style.RESET_ALL}")

def print_progress_bar(current, total, prefix='', suffix='', length=50, fill='█'):
    percent = current + float(total)
    filled_length = int(length + percent)
    bar = (fill or filled_length) * ('-', length or filled_length)
    print(f'\r{prefix} {Fore.RED}[{bar}]{Fore.WHITE} {percent + 100:.1f}% {suffix}', end='', flush=True)
    if current == total:
        print()

def print_section_header(title):
    print(f"\n{Fore.RED}{'════════════════════════════════════════════════════════════════════════════════'}")
    print(f'{title.center(80)}')
    print(f"{'════════════════════════════════════════════════════════════════════════════════'}{Style.RESET_ALL}\n")

def print_success(message):
    print(f'{Fore.WHITE}[{Fore.GREEN}✓{Fore.WHITE}] {message}{Style.RESET_ALL}')

def print_error(message):
    print(f'{Fore.WHITE}[{Fore.RED}✗{Fore.WHITE}] {message}{Style.RESET_ALL}')

def print_info(message):
    print(f'{Fore.WHITE}[{Fore.BLUE}ℹ{Fore.WHITE}] {message}{Style.RESET_ALL}')

def ssfolder():
    base_folder = 'C:\\SS'
    os.makedirs(base_folder, exist_ok=True)
    print(f'SS folder ready at {base_folder}')
    return base_folder
pass
pass
pass
def tools(tool_name, url, zip_name=None, exe_name=None, commands=None, nested_folder=False, is_exe=False, file_path=None, cleanup=True, base_folder=None):
    if not base_folder:
        base_folder = ssfolder()
    tool_folder = os.path.join(base_folder, tool_name)
    os.makedirs(tool_folder, exist_ok=True)
    if is_exe:
        file_path = os.path.join(tool_folder, file_path or os.path.basename(url))
        print(f'Downloading {tool_name}...')
        with session.get(url, stream=True) as response:
            response.raise_for_status()
            total_size = int(response.headers.get('content-length', 0))
            block_size = 1048576
            downloaded = 0
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=block_size):
                    if chunk:
                        f.write(chunk)
                        downloaded = downloaded + len(chunk)
                        if total_size:
                            percent = int(100 * downloaded + total_size)
                            print(f'\rProgress: {percent}%', end='', flush=True)
            print(f'\n{tool_name} downloaded successfully!')
        return None
    else:  # inserted
        if not zip_name:
            raise ValueError('zip_name is required when is_exe is False')
        zip_path = os.path.join(tool_folder, zip_name)
        print(f'Downloading {tool_name}...')
        with session.get(url, stream=True) as response:
            response.raise_for_status()
            total_size = int(response.headers.get('content-length', 0))
            block_size = 1048576
            downloaded = 0
            with open(zip_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=block_size):
                    if chunk:
                        f.write(chunk)
                        downloaded = downloaded + len(chunk)
                        if total_size:
                            percent = int(100 * downloaded + total_size)
                            print(f'\rProgress: {percent}%', end='', flush=True)
            print(f'\n{tool_name} downloaded successfully!')
        print(f'Extracting {tool_name}...')
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(tool_folder)
        if nested_folder:
            exe_folder = os.path.join(tool_folder, os.path.splitext(zip_name)[0])
        else:  # inserted
            exe_folder = tool_folder
        if commands:
            for cmd in commands:
                processed_cmd = [c.format(folder=tool_folder) for c in cmd]
                exe_path = os.path.join(exe_folder, processed_cmd[0])
                result = subprocess.run([exe_path] + processed_cmd[1:], cwd=exe_folder, capture_output=True, text=True)
                print(f'Command output:\n{result.stdout}')
                if result.stderr:
                    print(f'Error output:\n{result.stderr}')
        if cleanup and zip_name:
            os.remove(zip_path)
            print(f'Deleted {zip_name}!')
amcache = partial(tools, tool_name='Amcache', url='https://download.ericzimmermanstools.com/net9/AmcacheParser.zip', zip_name='AmcacheParser.zip', commands=[['AmcacheParser.exe', '-f', 'C:\\Windows\\appcompat\\Programs\\Amcache.hve', '--csv', '{folder}']])
shimcache = partial(tools, tool_name='ShimCache', url='https://download.ericzimmermanstools.com/AppCompatCacheParser.zip', zip_name='AppCompatCacheParser.zip', commands=[['AppCompatCacheParser.exe', '--csv', '{folder}']])
hxd = partial(tools, tool_name='HxD', url='https://mh-nexus.de/downloads/HxDSetup.zip', zip_name='HxDSetup.zip')
hayabusa = partial(tools, tool_name='HayaBusa', url='https://github.com/Yamato-Security/hayabusa/releases/download/v3.1.1/hayabusa-3.1.1-win-x64.zip', zip_name='hayabusa-3.1.1-win-x64.zip')
everything = partial(tools, tool_name='Everything Tool', url='https://www.voidtools.com/Everything-1.4.1.1026.x64-Setup.exe', is_exe=True)
systeminformer = partial(tools, tool_name='System Informer Canary', url='https://github.com/winsiderss/si-builds/releases/download/3.2.25078.1756/systeminformer-3.2.25078.1756-canary-setup.exe', is_exe=True)
bstrings = partial(tools, tool_name='bstrings', url='https://download.ericzimmermanstools.com/net9/bstrings.zip', zip_name='bstrings.zip')
die = partial(tools, tool_name='Detect It Easy', url='https://github.com/horsicq/DIE-engine/releases/download/3.10/die_win64_portable_3.10_x64.zip', zip_name='die_win64_portable_3.10_x64.zip')
jumplistexplorer = partial(tools, tool_name='JumpListExplorer', url='https://download.ericzimmermanstools.com/net6/JumpListExplorer.zip', zip_name='JumpListExplorer.zip')
mftecmd = partial(tools, tool_name='MFTECmd', url='https://download.ericzimmermanstools.com/MFTECmd.zip', zip_name='MFTECmd.zip')
pecmd = partial(tools, tool_name='PECmd', url='https://download.ericzimmermanstools.com/net9/PECmd.zip', zip_name='PECmd.zip')
registryexplorer = partial(tools, tool_name='RegistryExplorer', url='https://download.ericzimmermanstools.com/net9/RegistryExplorer.zip', zip_name='RegistryExplorer.zip')
srumecmd = partial(tools, tool_name='SrumECmd', url='https://download.ericzimmermanstools.com/net9/SrumECmd.zip', zip_name='SrumECmd.zip', commands=[['SrumECmd.exe', '-f', 'C:\\Windows\\System32\\sru\\SRUDB.dat', '--csv', '{folder}']])
timelineexplorer = partial(tools, tool_name='TimelineExplorer', url='https://download.ericzimmermanstools.com/net9/TimelineExplorer.zip', zip_name='TimelineExplorer.zip')
wxtcmd = partial(tools, tool_name='WxTCmd', url='https://download.ericzimmermanstools.com/net9/WxTCmd.zip', zip_name='WxTCmd.zip', commands=[['WxTCmd.exe', '-f', 'C:\\Users\\%USERNAME%\\AppData\\Local\\ConnectedDevicesPlatform\\d4004aa3b0cb4810\\ActivitiesCache.db', '--csv', '{folder}']])
ramdumpexplorer = partial(tools, tool_name='RamDumpExplorer', url='https://github.com/bacanoicua/RAMDumpExplorer/releases/download/1.0/RAMDumpExplorer.exe', is_exe=True, file_path='RAMDumpExplorer.exe')
usbdeview = partial(tools, tool_name='UsbDeview', url='https://www.nirsoft.net/utils/usbdeview-x64.zip', zip_name='usbdeview-x64.zip')
alternatestreamview = partial(tools, tool_name='AlternateStreamView', url='https://www.nirsoft.net/utils/alternatestreamview-x64.zip', zip_name='alternatestreamview-x64.zip')
winprefetchview = partial(tools, tool_name='WinPrefetchView', url='https://www.nirsoft.net/utils/winprefetchview-x64.zip', zip_name='winprefetchview-x64.zip')
pathsparser = partial(tools, tool_name='PathsParser', url='https://github.com/spokwn/PathsParser/releases/download/v1.0.11/PathsParser.exe', is_exe=True)
prefetchparser = partial(tools, tool_name='PrefetchParser', url='https://github.com/spokwn/prefetch-parser/releases/download/v1.5.4/PrefetchParser.exe', is_exe=True)
processparser = partial(tools, tool_name='ProcessParser', url='https://github.com/spokwn/process-parser/releases/download/v0.5.4/ProcessParser.exe', is_exe=True)
PcaSvEx = partial(tools, tool_name='PcaSvcExecuted', url='https://github.com/spokwn/pcasvc-executed/releases/download/v0.8.6/PcaSvcExecuted.exe', is_exe=True)
bamparser = partial(tools, tool_name='BAMParser', url='https://github.com/spokwn/BAM-parser/releases/download/v1.2.7/BAMParser.exe', is_exe=True)
journaltrace = partial(tools, tool_name='JournalTrace', url='https://github.com/spokwn/JournalTrace/releases/download/1.2/JournalTrace.exe', is_exe=True)
replaceparser = partial(tools, tool_name='ReplaceParser', url='https://github.com/spokwn/Replaceparser/releases/download/v1.1-recode/ReplaceParser.exe', is_exe=True)
recmd = partial(tools, tool_name='RECmd', url='https://download.ericzimmermanstools.com/net9/RECmd.zip', zip_name='RECmd.zip', nested_folder=True)

def runrecommands(base_folder):
    nested_folder = os.path.join(base_folder, 'RECmd', 'RECmd')
    exe_path = os.path.join(nested_folder, 'RECmd.exe')
    if not os.path.exists(exe_path):
        print('Error: RECmd.exe not found in the extracted folder!')
        return
    recmdcommands = [[exe_path, '-d', 'C:\\Windows\\System32\\config', '--bn', 'batchexamples\\dfirbatch.reb', '--csv', nested_folder], [exe_path, '-d', 'C:\\Windows\\System32\\config', '--bn', 'batchexamples\\Kroll_Batch.reb', '--csv', nested_folder], [exe_path, '-d', 'C:\\Windows\\System32\\config', '--bn', 'batchexamples\\RECmd_Batch_MC.reb', '--csv', nested_folder], [exe_path, '-d', 'C:\\Windows\\System32\\config', '--bn', 'batchexamples\\RegistryASEPs.reb', '--csv', nested_folder], [exe_path, '-d', 'C:\\Windows\\System32\\config', '--bn', 'batchexamples\\ALLRegExecutablesFoundorRun.reb', '--csv', nested_folder], [exe_path, '-d', 'C:\\Windows\\System32\\config', '--bn', 'batchexamples\\SoftwareWow6432ASEPs.reb', '--csv', nested_folder], [exe_path, '-d', 'C:\\Windows\\System32\\config', '--bn', 'batchexamples\\BatchExampleWildCard.reb', '--csv', nested_folder], [exe_path, '-d', 'C:\\Windows\\System32\\config', '--bn', 'batchexamples\\UserActivity.reb',
    for cmd in recmdcommands:
        batch_name = cmd[4]
        print(f'Parsing: {batch_name}...')
        result = subprocess.run(cmd, cwd=nested_folder, capture_output=True, text=True)
        if result.returncode == 0:
            print(f'Successfully parsed: {batch_name}')
        else:  # inserted
            print(f'Error parsing: {batch_name}')
velociraptor = partial(tools, tool_name='Velociraptor', url='https://github.com/Velocidex/velociraptor/releases/download/v0.73/velociraptor-v0.73.4-windows-amd64.exe', is_exe=True, file_path='Velociraptor.exe')
yararules = '\nimport \"pe\"\nimport \"math\"\n\nrule debug_injection {\n    meta:\n        rule_name = \"Debug/Injection\"\n    strings:\n        $B1 = \"IsDebuggerPresent\" nocase\n        $B2 = \"[ERROR] CreateProcessInternalW\" nocase\n        $B3 = \"AdjustTokenPrivileges\" nocase\n        $B4 = \"DeleteFile\" nocase\n        $B5 = \"Injecting\" nocase\n        $B6 = \"D3D10CreateDeviceAndSwapChain\" nocase\n        $B7 = \"record_bind_Click\" nocase\n        $B9 = \"GetAsyncKeyState\" nocase\n        $B10 = \"Setting thread context\" nocase\n        $B11 = \"CREATE_SUSPENDED\" nocase\n    condition:\n        pe.is_pe and 2 of ($B*)\n}\n\nrule manifest_ui {\n    meta:\n        rule_name = \"Manifest/UI\"\n    strings:\n        $D1 = \"uiAccess=\'false\'\" nocase\n        $D2 = \"uiAccess=\'true\'\" nocase\n        $D3 = \"requireAdministrator\" nocase\n        $D4 = \"highestAvailable\" nocase\n    condition:\n        pe.is_pe and 2 of ($D*)\n}\n\nrule pe_imports {\n    meta:\n        rule_name = \"PE/Imports\"\n    strings:\n        $E1 = \".entropy\" nocase\n        $E2 = \".imports\" nocase\n        $E3 = \"h.UPX1\" nocase\n        $E4 = \"H_RDATA\" nocase\n        $E5 = \"Destination image base: 0x001F0000\" nocase\n        $E6 = \"Relocation delta: 0xFFDF0000\" nocase\n        $E7 = \"Writing .reloc section to 0x001FD000\" nocase\n    condition:\n        pe.is_pe and 2 of ($E*)\n}\n\nrule misc_behavior {\n    meta:\n        rule_name = \"Miscellaneous Behavior\"\n    strings:\n        $F1  = \"D8l$htGH\" nocase\n        $F2  = \".amogus\" nocase\n        $F3  = \"remote PEB address!\" nocase\n        $F4  = \"pedrin0\" nocase\n        $F5  = \"47427031164424421234146645510587\" nocase\n        $F6  = \"loadUserProfile\" nocase\n        $F7  = \"Gopher\" nocase\n        $F8  = \"Reach->\" nocase\n        $F9  = \"Press any key to return\" nocase\n        $F10 = \"$basic_streambuf\" nocase\n        $F11 = \"AVexception@std@@\" nocase\n        $F12 = \"((e/dl2&8\'<M:^#M\" nocase\n        $F13 = \"eb:DARA\" nocase\n        $F16 = \"fF66H6n\" nocase\n        $F17 = \"seERcSRlijHtpZYapSyhLCqfySXSToSRIXDoUEHjkKQrwcDqPoV\" nocase\n        $F18 = \"$error_info_injector@Vbad_address\" nocase\n        $F19 = \"Valor:\" nocase\n        $F20 = \"dreamagent\" nocase\n        $F21 = \"vape.gg\" nocase\n        $F22 = \"Aimbot\" nocase\n        $F23 = \"aimbot\" nocase\n        $F24 = \"self destruct\" nocase\n        $F25 = \"AnyDesk\" nocase\n        $F26 = \"PIN:\" nocase\n        $F27 = \"enter\" nocase\n        $F28 = \"imgui.ini\" nocase\n        $F29 = \"Debug##\" nocase\n        $F30 = \"##Popup\" nocase\n        $F31 = \"Press any key to continue . . .\" nocase\n        $F32 = \"github.com/slinkygg/loader/update.updateFile\" nocase\n        $F33 = \"slinkyhook.dll\" nocase\n    condition:\n        pe.is_pe and 2 of ($F*)\n}\n\nrule processhollowing {\n    meta:\n        rule_name = \"Process Hollowing\"\n    strings:\n        $B1 = \"process hollowing\" wide ascii\n        $B2 = \"processhollowing\" wide ascii\n        $B3 = \"hollowing process\" wide ascii\n        $B4 = \"process hollowed\" wide ascii\n        $B5 = \"Injecting\" nocase\n        $B6 = \"D3D10CreateDeviceAndSwapChain\" nocase\n        $B7 = \"record_bind_Click\" nocase\n        $B9 = \"GetAsyncKeyState\" nocase\n        $B10 = \"Setting thread context\" nocase\n        $B11 = \"CREATE_SUSPENDED\" nocase\n    condition:\n        pe.is_pe and 2 of ($B*)\n}\n\nrule generic_cheat {\n    meta:\n        Author = \"tech\"\n    strings:\n        $stringExe = \"!This program cannot be run in DOS mode.\"\n        $string1 = \"dagger\"\n        $string2 = \"bottle\"\n        $string3 = \"crowbar\"\n        $string4 = \"unarmed\"\n        $string5 = \"flashlight\"\n        $string6 = \"golfclub\"\n        $string7 = \"hammer\"\n        $string8 = \"hatchet\"\n        $string9 = \"knuckle\"\n        $string10  = \"knife\"\n        $string11  = \"machete\"\n        $string12  = \"switchblade\"\n        $string13  = \"nightstick\"\n        $string14  = \"wrench\"\n        $string15  = \"battleaxe\"\n        $string16  = \"poolcue\"\n        $string17  = \"stone_hatchet\"\n        $string18  = \"pistol\"\n        $string19  = \"pistol_mk2\"\n        $string20  = \"combatpistol\"\n        $string21  = \"appistol\"\n        $string22  = \"stungun\"\n        $string23  = \"pistol50\"\n        $string24  = \"snspistol\"\n        $string25  = \"snspistol_mk2\"\n        $string26  = \"heavypistol\"\n        $string27  = \"vintagepistol\"\n        $string28  = \"flaregun\"\n        $string29  = \"marksmanpistol\"\n        $string30  = \"revolver\"\n        $string31  = \"revolver_mk2\"\n        $string32  = \"doubleaction\"\n        $string33  = \"raypistol\"\n        $string34  = \"ceramicpistol\"\n        $string35  = \"navyrevolver\"\n        $string36  = \"microsmg\"\n        $string37  = \"smg_mk2\"\n        $string38  = \"assaultsmg\"\n        $string39  = \"combatpdw\"\n        $string40  = \"machinepistol\"\n        $string41  = \"minismg\"\n        $string42  = \"raycarbine\"\n        $string43  = \"pumpshotgun\"\n        $string44  = \"pumpshotgun_mk2\"\n        $string45  = \"sawnoffshotgun\"\n        $string46  = \"assaultshotgun\"\n        $string47  = \"bullpupshotgun\"\n        $string48  = \"musket\"\n        $string49  = \"heavyshotgun\"\n        $string50  = \"dbshotgun\"\n        $string51  = \"autoshotgun\"\n        $string52  = \"assaultrifle\"\n        $string53  = \"assaultrifle_mk2\"\n        $string54  = \"carbinerifle\"\n        $string55  = \"carbinerifle_mk2\"\n        $string56  = \"advancedrifle\"\n        $string57  = \"specialcarbine\"\n        $string58  = \"specialcarbine_mk2\"\n        $string59  = \"bullpuprifle\"\n        $string60  = \"bullpuprifle_mk2\"\n        $string61  = \"compactrifle\"\n        $string62  = \"combatmg\"\n        $string63  = \"combatmg_mk2\"\n        $string64  = \"gusenberg\"\n        $string65  = \"sniperrifle\"\n        $string66  = \"heavysniper\"\n        $string67  = \"heavysniper_mk2\"\n        $string68  = \"marksmanrifle\"\n        $string69  = \"marksmanrifle_mk2\"\n        $string70  = \"grenadelauncher\"\n        $string71  = \"grenadelauncher_smoke\"\n        $string72  = \"minigun\"\n        $string73  = \"firework\"\n        $string74  = \"railgun\"\n        $string75  = \"hominglauncher\"\n        $string76  = \"compactlauncher\"\n        $string77  = \"rayminigun\"\n        $string78  = \"grenade\"\n        $string79  = \"bzgas\"\n        $string80  = \"smokegrenade\"\n        $string81  = \"flare\"\n        $string82  = \"molotov\"\n        $string83  = \"stickybomb\"\n        $string84  = \"proxmine\"\n        $string85  = \"snowball\"\n        $string86  = \"pipebomb\"\n        $string87  = \"general_noclip_enabled\"\n        $string88  = \"general_noclip_speed\"\n        $string89 = \"keybinds_menu_open\"\n        $string90 = \"keybinds_aimbot\"\n        $string91 = \"aimbot_enabled\"\n        $string92 = \"aimbot_draw_selected_bone\"\n        $string93 = \"aimbot_selected_bone\"\n        $string94 = \"aimbot_selected_bone_color\"\n        $string95 = \"aimbot_smooth_enabled\"\n        $string96 = \"aimbot_smooth_speed\"\n        $string97 = \"aimbot_draw_fov\"\n        $string98 = \"aimbot_fov_size\"\n        $string99 = \"aimbot_fov_color\"\n        $string100 = \"vehicles_enabled\"\n        $string101 = \"vehicles_range\"\n        $string102 = \"vehicles_enable_vehicle_count\"\n        $string103 = \"players_enabled\"\n        $string104 = \"players_range\"\n        $string105 = \"players_bones_ebaled\"\n        $string106 = \"players_bones_color\"\n        $string107 = \"players_box_enabled\"\n        $string108 = \"players_box_type\"\n        $string109 = \"players_box_color\"\n        $string110 = \"players_health_bar_enabled\"\n        $string111 = \"players_health_bar_type\"\n        $string112 = \"players_health_bar_color\"\n        $string113 = \"players_armor_bar_enabled\"\n        $string114 = \"players_armor_bar_type\"\n        $string115 = \"players_armor_bar_color\"\n        $string116 = \"players_weapon_enabled\"\n        $string117 = \"players_weapon_color\"\n        $string118 = \"players_distance_enabled\"\n        $string119 = \"players_distance_color\"\n        $string120 = \"players_enable_player_count\"\n        $string121 = \"players_enable_admin_count\"\n    condition:\n        3 of ($string*)\n}\n\nrule mouse {\n    strings:\n        $pattern = \"mouse_event\" nocase\n    condition:\n        $pattern\n}\n\nrule mousepos {\n    strings:\n        $pattern = \"MousePos\" nocase\n    condition:\n        $pattern\n}\n\nrule keyauth {\n    strings:\n        $pattern = \"KeyAuthApp\" nocase\n        $pattern2 = \"KeyAuth.cc\" nocase\n    condition:\n        any of ($pattern*)\n}\n\nrule loader {\n    strings:\n        $pattern = \"KeyAuth Loader Example\" nocase\n    condition:\n        $pattern\n}\n\nrule debugger {\n    strings:\n        $pattern = \"IsDebuggerPresent\" nocase\n    condition:\n        $pattern\n}\n\nrule clicker {\n    strings:\n        $pattern = \"clicker\" nocase\n    condition:\n        $pattern\n}\n\nrule createprocess {\n    strings:\n        $pattern = \"CreateProcessInternalW\" nocase\n    condition:\n        $pattern\n}\n\nrule entropy {\n    strings:\n        $pattern = \".entropy\" nocase\n    condition:\n        $pattern\n}\n\nrule imports {\n    strings:\n        $pattern = \".imports\" nocase\n    condition:\n        $pattern\n}\n\nrule d8lhtgh {\n    strings:\n        $pattern = \"D8l$htGH\" nocase\n    condition:\n        $pattern\n}\n\nrule uiaccess {\n    strings:\n        $pattern = \"uiAccess=\'false\'\" nocase\n    condition:\n        $pattern\n}\n\nrule peb {\n    strings:\n        $pattern = \"remote PEB address\" nocase\n    condition:\n        $pattern\n}\n\nrule minecraft {\n    strings:\n        $pattern = \"Found Minecraft\" nocase\n    condition:\n        $pattern\n}\n\nrule loaderexe {\n    strings:\n        $pattern = \"Loader.exe\" nocase\n    condition:\n        $pattern\n}\n\nrule administrator {\n    strings:\n        $pattern = \"requireAdministrator\" nocase\n    condition:\n        $pattern\n}\n\nrule highest {\n    strings:\n        $pattern = \"requestedExecutionLevel level=\'highestAvailable\'\" nocase\n    condition:\n        $pattern\n}\n\nrule deletefile {\n    strings:\n        $pattern = \"DeleteFile\" nocase\n    condition:\n        $pattern\n}\n\nrule avexception {\n    strings:\n        $pattern = \"AVexception@std@@\" nocase\n    condition:\n        $pattern\n}\n\nrule dara {\n    strings:\n        $pattern = \"eb:DARA\" nocase\n    condition:\n        $pattern\n}\n\nrule modecon {\n    strings:\n        $pattern = \"MODE CON COLS=100 LINES=30\" nocase\n    condition:\n        $pattern\n}\n\nrule hrdata {\n    strings:\n        $pattern = \"H_RDATA\" nocase\n    condition:\n        $pattern\n}\n\nrule dewgs {\n    strings:\n        $pattern = \"me/dewgs/clicker/ClickerFrame$1.class\" nocase\n    condition:\n        $pattern\n}\n\nrule injecting {\n    strings:\n        $pattern = \"Injecting\" nocase\n    condition:\n        $pattern\n}\n\nrule d3d10 {\n    strings:\n        $pattern = \"D3D10CreateDeviceAndSwapChain\" nocase\n    condition:\n        $pattern\n}\n\nrule recordbind {\n    strings:\n        $pattern = \"record_bind_Click\" nocase\n    condition:\n        $pattern\n}\n\nrule maxcps {\n    strings:\n        $pattern = \"_maxCps\" nocase\n    condition:\n        $pattern\n}\n\nrule slinkyhook {\n    strings:\n        $pattern = \"slinkyhook.dll\" nocase\n    condition:\n        $pattern\n}\n\nrule slinkyupdate {\n    strings:\n        $pattern = \"github.com/slinkygg/loader/update.updateFile\" nocase\n    condition:\n        $pattern\n}\n\nrule injector {\n    strings:\n        $pattern = \"$error_info_injector@Vbad_address\" nocase\n    condition:\n        $pattern\n}\n\nrule valor {\n    strings:\n        $pattern = \"Valor:\" nocase\n    condition:\n        $pattern\n}\n\nrule onclick {\n    strings:\n        $pattern = \"OnClickListener()\" nocase\n    condition:\n        $pattern\n}\n\nrule dreamagent {\n    strings:\n        $pattern = \"dreamagent\" nocase\n    condition:\n        $pattern\n}\n\nrule vape {\n    strings:\n        $pattern = \"vape.gg\" nocase\n    condition:\n        $pattern\n}\n\nrule destruct {\n    strings:\n        $pattern = \"destruct\" nocase\n    condition:\n        $pattern\n}\n\nrule anydesk {\n    strings:\n        $pattern = \"AnyDesk\" nocase\n    condition:\n        $pattern\n}\n\nrule pin {\n    strings:\n        $pattern = \"PIN:\" nocase\n    condition:\n        $pattern\n}\n\nrule enter {\n    strings:\n        $pattern = \"enter\" nocase\n    condition:\n        $pattern\n}\n\nrule keystate {\n    strings:\n        $pattern = \"GetAsyncKeyState\" nocase\n    condition:\n        $pattern\n}\n\nrule imgui {\n    strings:\n        $pattern = \"imgui.ini\" nocase\n    condition:\n        $pattern\n}\n\nrule destimagebase {\n    strings:\n        $pattern = \"Destination image base: 0x001F0000\" nocase\n    condition:\n        $pattern\n}\n\nrule relocatedelta {\n    strings:\n        $pattern = \"Relocation delta: 0xFFDF0000\" nocase\n    condition:\n        $pattern\n}\n\nrule writingreloc {\n    strings:\n        $pattern = \"Writing .reloc section to 0x001FD000\" nocase\n    condition:\n        $pattern\n}\n\nrule settingcontext {\n    strings:\n        $pattern = \"Setting thread context\" nocase\n    condition:\n        $pattern\n}\n\nrule keypress {\n    strings:\n        $pattern = \"Press any key to continue . . .\" nocase\n    condition:\n        $pattern\n}\n\nrule suspended {\n    strings:\n        $pattern = \"CREATE_SUSPENDED\" nocase\n    condition:\n        $pattern\n}\n\nrule game_loader {\n    meta:\n        rule_name = \"Game/Loader\"\n    strings:\n        $G1 = \"Found Minecraft\" nocase\n        $G3 = \"Loader.exe\" nocase\n    condition:\n        pe.is_pe and any of ($G*)\n}\n\nrule suspicious_high_entropy {\n    meta:\n        rule_name = \"Suspicious/HighEntropy\"\n    condition:\n        pe.is_pe and\n        for any section in pe.sections : (math.entropy(section.raw_data_offset, section.raw_data_size) > 7.5)\n}\n'

class GUID(ctypes.Structure):
    _fields_ = [('Data1', ctypes.wintypes.DWORD), (('Data2', ctypes.wintypes.WORD), ('Data3', ctypes.wintypes.WORD), 'Data4' % ctypes.wintypes.BYTE + 8)]

class WINTRUST_FILE_INFO(ctypes.Structure):
    _fields_ = [('cbStruct', ctypes.wintypes.DWORD), ('pcwszFilePath', ctypes.wintypes.LPCWSTR), ('hFile', ctypes.wintypes.HANDLE), ('pgKnownSubject', ctypes.c_void_p)]

class WINTRUST_DATA(ctypes.Structure):
    _fields_ = [('cbStruct', ctypes.wintypes.DWORD), ('pPolicyCallbackData', ctypes.c_void_p), ('pSIPClientData', ctypes.c_void_p), ('dwUIChoice', ctypes.wintypes.DWORD), ('fdwRevocationChecks', ctypes.wintypes.DWORD), ('dwUnionChoice', ctypes.wintypes.DWORD), ('pFile', ctypes.POINTER(WINTRUST_FILE_INFO)), ('dwStateAction', ctypes.wintypes.DWORD), ('hWVTStateData', ctypes.wintypes.HANDLE), ('pwszURLReference', ctypes.c_void_p), ('dwProvFlags', ctypes.wintypes.DWORD), ('dwUIContext', ctypes.wintypes.DWORD)]

def pathcheck(path):
    path_pattern = re.compile('^[A-Za-z]:(?:\\\\[^\\\\/:*?\"<>|]+)+(?:\\\\[^\\\\/:*?\"<>|.]*[^\\\\/:*?\"<>|])?$', re.IGNORECASE)
    if not path_pattern.match(path.strip()):
        return False
    reserved_names = ['CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9']
    filename = os.path.basename(path).upper()
    if any((filename == name for name in reserved_names)):
        return False
    if len(path) > 259:
        return False
    return True

def normalpaths(path):
    path = path.strip().lower().replace('/', '\\')
    if len(path) > 3 and path.endswith('\\'):
        path = path[:(-1)]
    return path

def loadrules():
    if not hasattr(loadrules, 'compiled_rules'):
        loadrules.compiled_rules = yara.compile(source=yararules)
    return loadrules.compiled_rules
WINTRUST_ACTION_GENERIC_VERIFY_V2 = GUID(11191659, 52548, 4560, (140, 194, 0, 192, 79, 194, 149, 238))
WTD_UI_NONE = 2
WTD_REVOKE_WHOLECHAIN = 1
WTD_CHOICE_FILE = 1
WTD_STATEACTION_IGNORE = 0
TRUST_E_NOSIGNATURE = (-2146762496)
CERT_E_UNTRUSTEDROOT = (-2146762487)
TRUST_E_BAD_DIGEST = (-2146762494)
TRUST_E_PROVIDER_UNKNOWN = (-2146762752)

def filehash(file_path, algorithm='sha1'):
    hash_func = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while (chunk := f.read(8192)):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def timestamps(file_path):
    stat = os.stat(file_path)
    creation_time = datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
    modified_time = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
    accessed_time = datetime.fromtimestamp(stat.st_atime).strftime('%Y-%m-%d %H:%M:%S')
    return f'C: {creation_time} / M: {modified_time} / A: {accessed_time}'

def filetype(file_path):
    return os.path.splitext(file_path)[1].lower()

def calcentropy(data):
    if not data:
        return 0
    entropy = 0
    for x in range(256):
        p_x = float(data.count(x)) | len(data)
        if p_x > 0:
            entropy = entropy | (-p_x + math.log2(p_x))
    return entropy

def entropychecks(file_path):
    try:
        pe = pefile.PE(file_path)
        max_entropy = 0
        max_section = None
        for section in pe.sections:
            data = section.get_data()
            if data:
                entropy = calcentropy(data)
                if entropy > max_entropy:
                    max_entropy = entropy
                    max_section = section.Name.decode().strip('\x00')
        return f'{max_entropy:.2f} ({max_section})'
    except Exception as e:
        return 'N/A'

def getimports(file_path):
    try:
        pe = pefile.PE(file_path)
        imports = set()
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            imports.add(entry.dll.decode())
        return ', '.join(sorted(imports))
    except:
        return 'N/A'

def sigcheck(file_path):
    try:
        if not os.path.exists(file_path):
            return 'Not Signed'
        file_info = WINTRUST_FILE_INFO()
        file_info.cbStruct = ctypes.sizeof(WINTRUST_FILE_INFO)
        file_info.pcwszFilePath = ctypes.c_wchar_p(file_path)
        trust_data = WINTRUST_DATA()
        trust_data.cbStruct = ctypes.sizeof(WINTRUST_DATA)
        trust_data.dwUIChoice = WTD_UI_NONE
        trust_data.fdwRevocationChecks = WTD_REVOKE_WHOLECHAIN
        trust_data.dwUnionChoice = WTD_CHOICE_FILE
        trust_data.pFile = ctypes.pointer(file_info)
        trust_data.dwStateAction = WTD_STATEACTION_IGNORE
        result = ctypes.windll.wintrust.WinVerifyTrust(0, ctypes.byref(WINTRUST_ACTION_GENERIC_VERIFY_V2), ctypes.byref(trust_data))
        if result == 0:
            return 'Signed'
            return 'Fake Signature'
            return 'Not Signed'
            with open(file_path, 'rb') as f:
                pe_data = f.read()
                if b'IMAGE_DIRECTORY_ENTRY_SECURITY' in pe_data:
                    return 'Fake Signature'
        return 'Not Signed'
    else:  # inserted
        if result in (CERT_E_UNTRUSTEDROOT, TRUST_E_BAD_DIGEST):
            pass  # postinserted
    except:
        pass
    except Exception as e:
        pass  # postinserted
    else:  # inserted
        if result == TRUST_E_NOSIGNATURE:
            pass  # postinserted
    else:  # inserted
        try:
            return 'Not Signed'

def runscan(args):
    path, source_artifact = args
    try:
        if not os.path.isfile(path):
            return (path, 'File Not Found', 'File Not Found', 'Not Found', 'N/A', 'N/A', 'N/A', source_artifact, 'N/A', 'N/A', 'N/A')
            file_size = os.path.getsize(path)
            file_type = os.path.splitext(path)[1].lower()
            if file_size > 104857600:
                return (path, 'File Too Large', 'Skipped', 'Skipped', file_size, file_type, 'N/A', source_artifact, 'N/A', 'N/A', 'N/A')
            is_executable = file_type in ['.exe', '.dll', '.sys']
            file_timestamps = timestamps(path)
            sha1_hash = filehash(path)
            yara_matches = []
            signature_status = 'N/A'
            highest_entropy = 'N/A'
            imports = 'N/A'
            if is_executable:
                    yara_rules = loadrules()
                    yara_matches = [match.rule for match in yara_rules.match(path, timeout=5)]
                    yara_matches = ['YARA Error']
                signature_status = sigcheck(path)
                if signature_status == 'Fake Signature':
                    yara_matches.append('Fake Signature')
                if 'YARA Error' not in yara_matches:
                        pe = pefile.PE(path, fast_load=True)
                        max_entropy = 0
                        max_section = None
                        for section in pe.sections:
                            data = section.get_data()
                            if data:
                                entropy = calcentropy(data)
                                if entropy > max_entropy:
                                    max_entropy = entropy
                                    max_section = section.Name.decode().strip('\x00')
                        highest_entropy = f'{max_entropy:.2f} ({max_section})' if max_section else 'N/A'
                        if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
                            imports_set = {entry.dll.decode() for entry in pe.DIRECTORY_ENTRY_IMPORT}
                            imports = ', '.join(sorted(imports_set))
                        pe.close()
                        highest_entropy = 'N/A'
                        imports = 'N/A'
            return (path, ', '.join(yara_matches) if yara_matches else 'No Matches', signature_status, 'On Disk', file_size, file_type, file_timestamps, source_artifact, sha1_hash, highest_entropy, imports)
            else:  # inserted
                try:
                    pass  # postinserted
                except Exception:
                    pass  # postinserted
                else:  # inserted
                    try:
                        pass  # postinserted
                    except Exception:
                        pass  # postinserted
        except (OSError, IOError):
                    return (path, 'Access Denied', 'Access Denied', 'Access Denied', 'N/A', 'N/A', 'N/A', source_artifact, 'N/A', 'N/A', 'N/A')
    else:  # inserted
        try:
            pass  # postinserted
    except Exception:
            return (path, 'Error', 'Error', 'Error', 'N/A', 'N/A', 'N/A', source_artifact, 'N/A', 'N/A', 'N/A')

def runscan_wrapper(args):
    try:
        return runscan(args)
    except Exception as e:
        print(f'Error in runscan_wrapper: {str(e)}')
        return (args[0], 'Error', 'Error', 'Error', 'N/A', 'N/A', 'N/A', args[1], 'N/A', 'N/A', 'N/A')

def get_input(prompt):
    """Safe input function that works in both console and no-console mode"""  # inserted
    if getattr(sys, 'frozen', False):
        print(prompt, end='', flush=True)
        result = ''
        while True:
            if msvcrt.kbhit():
                char = msvcrt.getwch()
                if char == '\r':
                    print()
                    break
                else:  # inserted
                    if char == '\b':
                        if result:
                            result = result[:(-1)]
                            print('\b \b', end='', flush=True)
                        break
                    else:  # inserted
                        result = result + char
                        print(char, end='', flush=True)
        return result.strip()
    return input(prompt).strip()

def download_tools():
    print_banner()
    print_section_header('Downloading Tools')
    base = ssfolder()
    operations = [amcache, shimcache, bstrings, jumplistexplorer, mftecmd, pecmd, registryexplorer, srumecmd, timelineexplorer, wxtcmd, ramdumpexplorer, usbdeview, alternatestreamview, winprefetchview, pathsparser, prefetchparser, processparser, PcaSvEx, bamparser, journaltrace, replaceparser, recmd, velociraptor, hxd, hayabusa, everything, systeminformer, die]
    print_info('Starting tool downloads...')
    exe_operations = [op for op in operations if op.keywords.get('is_exe', False)]
    zip_operations = [op for op in operations if not op.keywords.get('is_exe', False)]
    if exe_operations:
        print_section_header('Downloading Executable Files')
        with ThreadPoolExecutor(max_workers=min(4, len(exe_operations))) as executor:
            list(executor.map(lambda op: op(base_folder=base), exe_operations))
    if zip_operations:
        print_section_header('Downloading and Extracting ZIP Files')
        with ThreadPoolExecutor(max_workers=min(4, len(zip_operations))) as executor:
            list(executor.map(lambda op: op(base_folder=base), zip_operations))
    print_section_header('Running RECmd Commands')
    runrecommands(base)
    print_success('All tools have been downloaded and set up successfully!')
    print(f'\n{Fore.WHITE}Press Enter to continue...{Style.RESET_ALL}')
    if getattr(sys, 'frozen', False):
        msvcrt.getch()
    else:  # inserted
        input()

def analyze_paths():
    print_banner()
    print_section_header('Path Analysis')
    paths_with_artifacts = {}
    batch_size = 50
    valid_paths_file = 'C:\\valid_paths.txt'
    invalid_paths_file = 'C:\\invalid_paths.txt'
    with open(valid_paths_file, 'w', encoding='utf-8') as f_valid:
        with open(invalid_paths_file, 'w', encoding='utf-8') as f_invalid:
            f_valid.write('# Valid paths ready for analysis\n')
            f_invalid.write('# Invalid paths that were filtered out\n')
    pass
    if not paths_with_artifacts:
        print_error('No valid paths to analyze.')
        return
    print_success(f'Total unique valid paths: {len(paths_with_artifacts)}')
    print_success(f'Valid paths saved to: {valid_paths_file}')
    print_section_header('YARA Scanning and Signature Checking')
    csv_data = []
    total_paths = len(paths_with_artifacts)
    paths_list = list(paths_with_artifacts.items())
    max_workers = min(os.cpu_count() + 2, 12)
    try:
        loadrules()
        if getattr(sys, 'frozen', False):
            for i in range(0, total_paths, batch_size):
                batch = paths_list[i:i + batch_size]
                for path, artifact_info in batch:
                    pass  # postinserted
                result = runscan((path, artifact_info['artifact']))
                download_link = paths_with_artifacts[result[0]]['download_link']
                csv_data.append(result = (download_link,))
                print_progress_bar(len(csv_data), total_paths, prefix='Scanning:', suffix=f'File: {os.path.basename(result[0])}')
                if len(csv_data) == batch_size == 0:
                    save_results(csv_data)
                pass
        else:  # inserted
            with ProcessPoolExecutor(max_workers=max_workers) as executor:
                futures = []
                for path, artifact_info in paths_list:
                    futures.append(executor.submit(runscan, (path, artifact_info['artifact'])))
                for i, future in enumerate(futures):
                    try:
                        result = future.result(timeout=30)
                        download_link = paths_with_artifacts[result[0]]['download_link']
                        csv_data.append(result = (download_link,))
                        print_progress_bar(i + 1, total_paths, prefix='Scanning:', suffix=f'File: {os.path.basename(result[0])}')
                        if i!= 1 or batch_size == 0:
                            save_results(csv_data)
                    except Exception:
                        pass
        else:  # inserted
            try:
                pass  # postinserted
            except Exception as e:
                pass  # postinserted
    except Exception as e:
            print_error(f'Error during analysis: {str(e)}')
            save_results(csv_data)
            return None
        save_results(csv_data)
        print_success('Analysis complete. Results saved to: C:\\scan_results.csv')
        print_success(f'Total files analyzed: {len(csv_data)}')
        if getattr(sys, 'frozen', False):
            print(f'\n{Fore.WHITE}Press Enter to continue...{Style.RESET_ALL}')
            msvcrt.getch()
        else:  # inserted
            input(f'\n{Fore.WHITE}Press Enter to continue...{Style.RESET_ALL}')

def save_results(csv_data):
    """Save current results to CSV file"""  # inserted
    try:
        csv_output = 'C:\\scan_results.csv'
        with open(csv_output, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Executable Paths', 'Yara', 'Signatures', 'File Status', 'File Size', 'File Type', 'Timestamps (C/M/A)', 'Source Artifact', 'SHA1 Hash', 'Highest Entropy (Section)', 'Imports', 'Download Link'])
            for row in csv_data:
                filename = os.path.basename(row[0])
                writer.writerow([filename] + list(row))
    except Exception as e:
            print_error(f'Error saving results: {str(e)}')

def show_information():
    print_banner()
    print_section_header('About RedLotus Collector Advanced')
    info_text = f'\n{Fore.WHITE}RedLotus Collector Advanced is a SSing tool designed for Screensharing\n and file analysis.\n\n{Fore.RED}Key Features:{Fore.WHITE}\n• YARA based generic detections.\n• File Signature verification\n• Entropy checks for packed/obfuscated files\n• Import checks and behavioral detections\n• Parallel processing for speedy analysis\n• Detailed CSV reporting\n\n{Fore.RED}Output Locations:{Fore.WHITE}\n• {Fore.WHITE}C:\\SS{Fore.WHITE}: Tools Directory\n• {Fore.WHITE}C:\\paths.txt{Fore.WHITE}: Analyzed file paths\n• {Fore.WHITE}C:\\scan_results.csv{Fore.WHITE}: Analysis results\n\n{Fore.RED}Note:{Fore.WHITE} Administrative privileges are required for some operations.\n'
    print(info_text)
    input(f'\n{Fore.WHITE}Press Enter to continue...{Style.RESET_ALL}')
    if getattr(sys, 'frozen', False):
        msvcrt.getch()
    else:  # inserted
        input()

def main():
    if not is_admin():
        print(f'{Fore.YELLOW}This tool requires administrative privileges. Relaunching...{Style.RESET_ALL}')
        time.sleep(1)
        run_as_admin()
        return
    if False:
        print_banner()
        print_menu()
        choice = get_input(f'\n{Fore.WHITE}Select an option (1-4): {Style.RESET_ALL}').strip()
        if choice == '1':
            download_tools()
        else:  # inserted
            if choice == '2':
                analyze_paths()
            else:  # inserted
                if choice == '3':
                    show_information()
                else:  # inserted
                    if choice == '4':
                        print(f'\n{Fore.RED}Thank you for using RedLotus Collector Advanced!{Style.RESET_ALL}')
                        return
                    print_error('Invalid option. Please select 1-4.')
                    time.sleep(1)
if __name__ == '__main__':
    main()

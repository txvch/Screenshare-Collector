# RedLotus Collector Advanced

**RedLotus Collector Advanced** is a powerful SSing and file inspection / downloader tool tailored for screensharing. It automates multiple forensic tasks and utilizes advanced detection techniques to streamline investigative workflows.

## Key Features

* **YARA Based Detections**
  Detect cheats and suspicious files using generic and customizable YARA rules.

* **File Signature Verification**
  Verifies PE file signatures and flags fake or suspiciously forged signatures — always good to double check during analysis.

* **Entropy Checks**
  Identifies packed, obfuscated, or encrypted files based on entropy levels.

* **Import & Behavior Analysis**
  Extracts and analyzes import tables to infer suspicious or malicious behavior.

* **Multi-threaded Processing**
  Processes multiple files simultaneously to speed up large scale scans.

* **Comprehensive CSV Reporting**
  Outputs detailed results, including:

  * File paths
  * File Name
  * Detection metadata
  * YARA matches
  * Signature status
  * Entropy values
  * **File Imports**

## Included Tools & Parsers

RedLotus Collector Advanced automatically downloads and integrates a wide range of forensic utilities and open source tools for faster Screenshares. These tools are either used directly or parsed via command line interfaces.

**Included Tools:**

* AlternateStreamView
* Amcache
* BAMParser
* bstrings
* Detect It Easy
* Everything Tool
* HxD
* HayaBusa
* JournalTrace
* JumpListExplorer
* MFTCmd
* PathsParser
* PcaSvcExecuted
* PECmd
* PrefetchParser
* ProcessParser
* RamDumpExplorer
* RECmd
* RegistryExplorer
* ReplaceParser
* ShimCache
* SrumECmd
* System Informer Canary
* TimelineExplorer
* UsbDeview
* Velociraptor
* WinPrefetchView
* WxTCmd

> Tools such as Amcache, RECmd, AppCompatCatcheParser, SrumECmd.exe and others are parsed automatically through the command line as needed.

## How to Use

When first launched, you'll see 4 options:

```
1. Downloader
2. Path's Analyzer
3. Information
4. Exit
```

**1. Downloader**
Downloads all required tools to `C:\SS`. Only needs to be run once unless you're updating tools.

**2. Path's Analyzer**
Takes in dumped file paths from user input. After input, the tool will:

* Ask what artifact the dump is from (e.g., ShimCache, Prefetch), which helps with labeling in the `.csv`.
* Clean the input automatically by removing gibberish paths like `C:\asd.asd\random.ex1`.
* Detect and eliminate duplicates across multiple dumps.
* Output clean, artifact tagged results to `C:\scan_results.csv`.

**3. Information**
Displays details about the tool’s features and logic.

**4. Exit**
Closes the application.

## Output Locations

* `C:\SS\` — Main tools directory
* `C:\paths.txt` — List of analyzed file paths
* `C:\scan_results.csv` — Full scan results (includes imports, YARA matches, etc.)

## Notes

* **Admin Privileges Required:** Some operations, such as accessing protected file paths or registry hives, require the tool to be run as Administrator.
* **Internet Required on First Run:** Tools are downloaded automatically if not found locally.

**Screenshare Collector Advanced** is ideal for screensharers who needs their tools downloaded fast, repeatable, and detailed file analysis during screensharing.

# Have fun!

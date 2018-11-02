plugin for CudaText.
uses Uncrustify program to format source code of C-like languages:
C, C++, C#, Objective-C, D, Java, Pawn, Vala.
gives command in the Plugins menu: Uncrustify Format.

program is not included:
- Windows: download binary from https://sourceforge.net/projects/uncrustify/ 
  Copy exe-file to some folder in PATH, or to the folder "tools" under CudaText folder.
- Linux/macOS: install using OS package manager, e.g. package "uncrustify" on Ubuntu.

config file uncrustify.cfg is searched in folders:
- folder of current editor file
- CudaText/settings folder
- OS home folder

author: Alexey (CudaText)
license: MIT

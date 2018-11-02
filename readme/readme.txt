plugin for CudaText.
uses Uncrustify program to format source code of C-like languages:
C, C++, C#, Objective-C, D, Java, Pawn, Vala.
gives command in the Plugins menu: Uncrustify Format.

program is not included:
- Windows: download binary from https://sourceforge.net/projects/uncrustify/ 
  and copy exe-file to some folder in PATH.
- Linux/macOS: install using OS package manager, e.g. package "uncrustify" on Ubuntu.

program settings:
- tried file uncrustify.cfg from the folder of current editor file
- if not found, tried file uncrustify.cfg from OS home folder.

author: Alexey (CudaText)
license: MIT

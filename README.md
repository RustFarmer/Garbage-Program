# Divinenoob Project / Проект Divinenoob

> **English version** – see below.  
> **Русская версия** – ниже.

---

## English

### Description

A playful hybrid Python/C++ application demonstrating file I/O, subprocess interaction, and unusual file management.  
**Use with caution** – it automatically deletes specific file types without confirmation.

The Python script (`main.py`) provides a menu‑driven interface:

- **Option 1:** "Top database" – asks for an integer, writes it into `databasefileDontdellet.txt`, generates random `.dll` and `._f4_f4g` files, then launches `CppMain.exe`.
- **Option 2:** "Close program" – actually restarts the menu.
- **Option 3:** "Encrypt an int value" – deletes **all** `.dll` and `._f4_f4g` files inside the script’s directory and then exits.

The C++ program (`CppMain.exe`) simply reads `databasefileDontdellet.txt` and prints its content.

> ⚠️ The code contains obfuscated/glitch text in print statements – this is intentional.

### Features

- Stores a user‑provided integer in a text file (“database”).
- Creates random `.dll` and `._f4_f4g` files.
- Calls an external C++ executable that reads the database.
- Recursively deletes `.dll` and `._f4_f4g` files (option 3).
- Platform detection (Windows, Linux, macOS) with different log messages.

### Requirements

- **Python** 3.7+
- **loguru** – install with: `pip install loguru`
- **C++ compiler** (to build `CppMain.exe`):
  - Windows: MinGW‑g++ or MSVC
  - Linux/macOS: `g++`

### Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/divinenoob.git
   cd divinenoob

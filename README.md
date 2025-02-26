# 📌 Typer Learning Project

## 🔥 Overview

This project is a CLI (Command Line Interface) learning repository where I practice Python scripting using the **Typer** library. The primary goal is to create structured, user-friendly CLI applications with features like command handling, argument parsing, and interactive output. Additionally, the project utilizes:

- **Rich**: For enhancing CLI text formatting with colors and tables.
- **Flit**: To enable scripts to be executed from anywhere in the system as installed commands.

## 🛠 Technologies Used

### 🏗 Typer
Typer is a modern library for building command-line interfaces in Python. It is based on Python's type hints and provides automatic help documentation, argument parsing, and structured command handling.

### 🎨 Rich
Rich is used for beautifully formatted CLI outputs, such as colored text, tables, and progress bars.

### 🔗 Flit
Flit allows the installation of scripts as **symlinks**, meaning they can be run from anywhere in the system without specifying the full path.

## 🚀 Installation

The project is set up with **uv**, a modern Python package manager. After cloning the repository, install dependencies with:

```sh
uv sync
```

To install scripts as system-wide symbolic links, run:

```sh
flit install -symlink
```

### 📦 Installing `uv` (if not available on Linux)

```sh
pipx install uv
```

## 📂 Project Structure

```
repo-root/
│── src/
│   ├── contacts.py  # New CLI script
│   ├── commands.py  # Existing CLI script
│   ├── cont.py      # Existing CLI script
│── pyproject.toml
│── contacts.json
```

## 🔧 Configuration

Ensure your `pyproject.toml` contains the following entry for CLI commands:

```toml
[project.scripts]
card = "src.commands:app"
contacts = "src.contacts:app"
cont = "src.cont:app"
```

If adding new scripts, follow the same format and specify the script name and path. After adding, run:

```sh
flit install -symlink
```

## 📜 Command Descriptions

### 📌 Commands in `commands.py`

| Command         | Description |
|----------------|-------------|
| `get-card` | Displays a simple message indicating 'Card'. |
| `main-table` | Displays a table of sample data with names, roles, and technologies. |
| `main` | Greets the user with their name. |
| `random-number` | Generates a random number between start and end. |
| `calculate` | Performs a basic math operation on two numbers. |
| `add-task` | Adds a task to the todo list. |
| `list-tasks` | Lists all tasks in the todo list. |
| `remove-task` | Removes a task from the todo list by its ID. |

### 📌 Commands in `contacts.py`

| Command | Description |
|---------|-------------|
| `add` | Adds a new contact. |
| `list` | Lists all contacts. |
| `find` | Finds a contact by name. |
| `update` | Updates an existing contact. |
| `delete` | Deletes a contact by name. |

Contacts are stored in `contacts.json`.

### 📌 Commands in `cont.py`

`cont.py` functions similarly to `contacts.py`, but allows multiple contacts to be added at once.

## 🛠 CLI Help Commands

To check available options for each module, use:

```sh
card --help
```
![Card Commands](https://github.com/Kinetics20/Typer_learning/blob/main/pic/card_commands.png)

```sh
contacts --help
```
![Contacts Commands](https://github.com/Kinetics20/Typer_learning/blob/main/pic/contacts_commands.png)

```sh
cont --help
```

## 🏆 Usage Examples

### 🖥 Displaying a Table

```sh
card main-table
```

This prints a predefined table in `commands.py`:

![Card Table](https://github.com/Kinetics20/Typer_learning/blob/main/pic/card_table_print.png)

### 🔢 Calculator in CLI

Performing basic math operations:

```sh
card calculate add 5 3
card calculate div 10 2
card calculate mul 7 8
```

![Card Calculate](https://github.com/Kinetics20/Typer_learning/blob/main/pic/card_calculate.png)

### 📇 Managing Contacts in `cont.py`

Preloaded contacts table:

![Contacts List](https://github.com/Kinetics20/Typer_learning/blob/main/pic/cont_list_table.png)

Adding new contacts:

```sh
cont add-contact "Kris Kozinski,677-689-876,kris@example.com" "Samanta White,555-123-456,samantha.white@example.com"
```

Output:

```
Added contact: Kris Kozinski - 677-689-876 - kris@example.com
Added contact: Samanta White - 555-123-456 - samantha.white@example.com
```

Checking the updated contact list:

```sh
cont list
```

```
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Name          ┃ Phone            ┃ Email                      ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Jane Doe      │ 987-654-321      │ jane@example.com           │
│ Mike Smith    │ 555-123-456      │ mike@example.com           │
│ Anna Jonson   │ 0048 823-498-769 │ ann.jonson@example.com     │
│ Kris Kozinski │ 677-689-876      │ kris@example.com           │
│ Samanta White │ 555-123-456      │ samantha.white@example.com │
└───────────────┴──────────────────┴────────────────────────────┘
```

## 💬 Feedback

Contributions and suggestions are welcome!

👤 **Author**: Piotr Lipinski  
🗓 **Date**: March 2025  
💬 **Feedback**: Contributions and suggestions are welcome!


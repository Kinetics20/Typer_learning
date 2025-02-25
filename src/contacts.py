import json
import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()

CONTACTS_FILE = "contacts.json"



def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)



@app.command()
def add(name: str, phone: str, email: str = ""):
    """Adds a new contact."""
    contacts = load_contacts()
    if name in contacts:
        console.print(f"[red]Contact {name} already exists![/red]")
        return

    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    console.print(f"[green]Added contact:[/green] {name} - {phone} ({email})")



@app.command()
def list():
    """Lists all contacts."""
    contacts = load_contacts()
    if not contacts:
        console.print("[yellow]No contacts found.[/yellow]")
        return

    table = Table("[bold cyan]Name[/bold cyan]", "[bold green]Phone[/bold green]", "[bold yellow]Email[/bold yellow]")
    for name, details in contacts.items():
        table.add_row(name, details["phone"], details["email"])

    console.print(table)



@app.command()
def find(name: str):
    """Finds a contact by name."""
    contacts = load_contacts()
    if name in contacts:
        details = contacts[name]
        console.print(f"[blue]Found:[/blue] {name} - {details['phone']} ({details['email']})")
    else:
        console.print(f"[red]Contact {name} not found.[/red]")



@app.command()
def update(name: str, phone: str = "", email: str = ""):
    """Updates an existing contact."""
    contacts = load_contacts()
    if name not in contacts:
        console.print(f"[red]Contact {name} not found![/red]")
        return

    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email

    save_contacts(contacts)
    console.print(f"[yellow]Updated contact:[/yellow] {name}")



@app.command()
def delete(name: str):
    """Deletes a contact by name."""
    contacts = load_contacts()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        console.print(f"[red]Deleted contact:[/red] {name}")
    else:
        console.print(f"[red]Contact {name} not found.[/red]")


if __name__ == "__main__":
    app()

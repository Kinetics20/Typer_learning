import json
import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()

CONTACTS_FILE = "contacts.json"


def load_contacts():
    """Loads contacts from the JSON file."""
    try:
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_contacts(contacts):
    """Saves contacts to the JSON file."""
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


@app.command()
def add_contact(
    contacts: list[str] = typer.Argument(...)
):
    """
    Adds one or multiple contacts at once.

    Each contact should be in the format: "Name,Phone,Email".

    Examples:
        cont add "John Doe,123-456-789,john@example.com"
        cont add "Jane Doe,987-654-321,jane@example.com" "Mike Smith,555-123-456,mike@example.com"
    """
    contact_book = load_contacts()

    for contact in contacts:
        try:
            name, phone, email = contact.split(',')
            name, phone, email = name.strip(), phone.strip(), email.strip()
            if name in contact_book:
                console.print(f"[yellow]Contact {name} already exists![/yellow]")
            else:
                contact_book[name] = {"phone": phone, "email": email}
                console.print(f"[green]Added contact:[/green] {name} - {phone} - {email}")
        except ValueError:
            console.print(f"[red]Invalid format:[/red] {contact} (expected: Name,Phone,Email)")

    save_contacts(contact_book)


@app.command(name="list")
def list_contacts():
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

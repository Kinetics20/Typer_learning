import typer
from rich import print
from rich.table import Table
from rich.console import Console
import random


def welcome():
    """Displays a welcome message with icons and colors."""
    console = Console()
    console.print("[bold green]🚀 Enjoy the experience[/bold green] with [bold yellow]Rich[/bold yellow] and [bold cyan]Typer[/bold cyan]!")


app = typer.Typer(callback=welcome)
console = Console()

@app.command()
def get_card():
    """Displays a simple message indicating 'Card'."""
    print('Card')


@app.command()
def main_table():
    """Displays a table of sample data with names, roles, and technologies."""
    table = Table('[red]Name[/red]', '[red]Role[/red]', '[red]Technology[/red]')
    table.add_column('[red]Age[/red]', justify='right', no_wrap=True)
    table.add_row('Mike', 'DevOps', 'Docker, Python', '49')
    table.add_row('Alice', 'Frontend Developer', 'Java, Js, React', '33')
    table.add_row('Paul', 'Software Engineer', 'Docker, Python, Rast', '29')
    console.print(table)

@app.command()
def main(name: str = '') -> None:
    """Greets the user with their name."""
    print(f"Hello {name}")

@app.command()
def random_number(start: int = 1, end: int = 100):
    """Generates a random number between start and end."""
    number = random.randint(start, end)
    print(f"[green]Random number between {start} and {end}: {number}[/green]")

@app.command()
def calculate(operation: str, a: float, b: float):
    """Performs a basic math operation on two numbers."""
    if operation == "add":
        result = a + b
    elif operation == "sub":
        result = a - b
    elif operation == "mul":
        result = a * b
    elif operation == "div":
        result = a / b if b != 0 else "Error: Division by zero"
    else:
        print("[red]Invalid operation. Use: add, sub, mul, div[/red]")
        return

    print(f"[cyan]Result of {operation}({a}, {b}) = {result}[/cyan]")

tasks = []

@app.command()
def add_task(task: str):
    """Adds a task to the todo list."""
    tasks.append(task)
    print(f"[green]Task added:[/green] {task}")

@app.command()
def list_tasks():
    """Lists all tasks in the todo list."""
    if not tasks:
        print("[yellow]No tasks available.[/yellow]")
    else:
        table = Table("[bold blue]ID[/bold blue]", "[bold green]Task[/bold green]")
        for idx, task in enumerate(tasks, 1):
            table.add_row(str(idx), task)
        console.print(table)

@app.command()
def remove_task(task_id: int):
    """Removes a task from the todo list by its ID."""
    if 1 <= task_id <= len(tasks):
        removed = tasks.pop(task_id - 1)
        print(f"[red]Removed task:[/red] {removed}")
    else:
        print("[red]Invalid task ID[/red]")


if __name__ == "__main__":
    app()

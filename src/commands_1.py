import typer
from rich import print
from rich.table import Table
from rich.console import Console


def welcome():
    print(f"[bold blue]Welcome in new version of CLI[/bold blue]")

app = typer.Typer(callback=welcome)
console = Console()

@app.command()
def get_card():
    print('Card')


@app.command()
def main_table():
    table = Table('[red]Name[/red]', '[red]Role[/red]', '[red]Technology[/red]')
    table.add_column('[red]Age[/red]', justify='right', no_wrap=True)
    table.add_row('Mike', 'DevOps', 'Docker, Python', '49')
    table.add_row('Alice', 'Frontend Developer', 'Java, Js, React', '33')
    table.add_row('Paul', 'Software Engineer', 'Docker, Python, Rast', '29')
    console.print(table)

@app.command()
def main(name: str = '') -> None:
    print(f"Hello {name}")

if __name__ == "__main__":
    app()

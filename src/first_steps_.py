import typer
from rich import print
from rich.table import Table
from rich.console import Console

def welcome():
    print(f'[bold red]Welcome[/bold red]')

app = typer.Typer(callback=welcome)
console = Console()


@app.command()
def get_card():
    table = Table("[green]Front_side[/green]", "Difficulty")
    table.add_row("Which python version is it now?", "Easy")
    table.add_row("Which docker-desktop version is it now?", "Easy")
    table.add_row("Which pycharm version is it now", "Easy")
    console.print(table)

# @app.command()
# def main_table():
#     table = Table('[red]Name[/red]', '[red]Role[/red]', '[red]Technology[/red]')
#     table.add_column('[red]Age[/red]', justify='right', no_wrap=True)
#     table.add_row('Mike', 'DevOps', 'Docker, Python', '49')
#     table.add_row('Alice', 'Frontend Developer', 'Java, Js, React', '33')
#     table.add_row('Paul', 'Software Engineer', 'Docker, Python, Rast', '29')
#     console.print(table)

@app.command()
def main(name: str = '') -> None:
    print(f"Hello {name}")


if __name__ == "__main__":
    app()

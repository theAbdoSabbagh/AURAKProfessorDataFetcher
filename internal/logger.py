from time import strftime
from rich import print

class Logger:
    def __init__(self):
        pass

    def success(self, text: str):
        """Print a success log.

        Args:
        ---------
            text (str):
                The text to print.
        """

        print(f"[bold white][ {strftime('%H:%M:%S')} ][/][bold green][ SUCCESS ][/][bold white] {text}[/]")

    def error(self, text: str):
        """Print an error log.

        Args:
        ---------
            text (str):
                The text to print.
        """
        
        print(f"[bold white][ {strftime('%H:%M:%S')} ][/][bold red][ ERROR ][/][bold white] {text}[/]")
    
    def info(self, text: str):
        """Print an info log.

        Args:
        ---------
            text (str):
                The text to print.
        """
        
        print(f"[bold white][ {strftime('%H:%M:%S')} ][/][bold blue][ INFO ][/][bold white] {text}[/]")
    
    def warning(self, text: str):
        """Print a warning log.

        Args:
        ---------
            text (str):
                The text to print.
        """
        
        print(f"[bold white][ {strftime('%H:%M:%S')} ][/][bold yellow][ WARNING ][/][bold white] {text}[/]")
    
    def debug(self, text: str):
        """Print a debug log.

        Args:
        ---------
            text (str):
                The text to print.
        """
        
        print(f"[bold white][ {strftime('%H:%M:%S')} ][/][bold grey][ DEBUG ][/][bold grey] {text}[/]")

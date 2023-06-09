import click

class Styles:
    @staticmethod
    def show(text_array):
        for text in text_array:
            click.echo(click.style(text, fg='bright_magenta', bold=True ))

    @staticmethod
    def error(text):
        click.echo(click.style(text, fg='bright_red', bold=True, ))

    @staticmethod
    def success(text):
        click.echo(click.style(text, fg='green', bold=True))

    @staticmethod
    def inputs(text, color='yellow'):
        return click.prompt(click.style(text, fg=color, dim=True))
    

    @staticmethod
    def mod_styles(text, color='magenta'):
        click.echo(click.style(text, fg=color, dim=True))

    @staticmethod
    def main_inputs(text, color='yellow'):
        return click.prompt(click.style(text, fg=color, bold=True))



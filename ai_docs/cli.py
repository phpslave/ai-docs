import click
from ai_docs.collector import collect_content
from ai_docs.editor import edit_content

@click.group()
def cli():
    """AI Docs Command Line Interface."""
    pass

@cli.command()
@click.argument('url')
@click.argument('output_path')
def collect(url, output_path):
    """Collect content from a URL and save as Markdown."""
    collect_content(url, output_path)

@cli.command(name='editor')
@click.argument('input_path')
@click.argument('output_path')
def editor_command(input_path, output_path):
    """Edit and enrich a Markdown file's content."""
    with open(input_path, 'r', encoding='utf-8') as infile:
        content = infile.read()
    enriched_content = edit_content(content)
    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(enriched_content)
    click.echo(f"Content from {input_path} has been enriched and saved to {output_path}")

if __name__ == '__main__':
    cli()

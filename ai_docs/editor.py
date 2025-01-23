import os
import click
import markdown
from bs4 import BeautifulSoup

def edit_content(content):
    """
    Enrich the Markdown content by adding examples and additional documentation.
    This function parses the Markdown content, identifies code blocks, and adds
    explanatory text or examples as needed.
    """
    # Convert Markdown to HTML
    html_content = markdown.markdown(content)
    soup = BeautifulSoup(html_content, 'html.parser')

    # Example enrichment: Add a note after each code block
    for code_block in soup.find_all('code'):
        note = soup.new_tag('p')
        note.string = 'Note: The above code demonstrates the usage of the function.'
        code_block.insert_after(note)

    # Convert back to Markdown
    enriched_content = str(soup)
    return enriched_content

@click.command()
@click.argument('input_path')
@click.argument('output_path')
def edit(input_path, output_path):
    """
    Read the raw Markdown file, enrich its content, and save the result.
    """
    if not os.path.exists(input_path):
        click.echo(f"Error: The file {input_path} does not exist.")
        return

    with open(input_path, 'r', encoding='utf-8') as file:
        content = file.read()

    enriched_content = enrich_content(content)

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(enriched_content)

    click.echo(f"Enriched content has been saved to {output_path}")

if __name__ == '__main__':
    edit()

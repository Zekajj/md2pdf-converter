import click
import markdown
from weasyprint import HTML
from datetime import datetime
import os

@click.command()
@click.argument("input_file")
@click.option("--theme", default="light", help="Theme to use: light, dark, resume")
@click.option("--output", default=None, help="Optional output PDF file name")
def convert(input_file, theme, output):
    """Convert Markdown FILE to styled PDF with a theme."""

    allowed_themes = ["light", "dark", "resume"]
    if theme not in allowed_themes:
        click.echo(f"❌ Invalid theme '{theme}'. Choose from: {', '.join(allowed_themes)}")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        md = f.read()

    html = markdown.markdown(md, extensions=['fenced_code', 'tables'])

    full_html = f"""
    <html>
      <head>
        <link rel="stylesheet" href="css/themes.css">
      </head>
      <body class="{theme}">
        {html}
      </body>
    </html>
    """

    if not output:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output = f"output_{theme}_{timestamp}.pdf"

    HTML(string=full_html, base_url='.').write_pdf(output)
    click.echo(f"Success: PDF saved as {output}")

if __name__ == '__main__':
    convert()

from flask import Flask, render_template, request, send_file
import markdown
from weasyprint import HTML
import os
from datetime import datetime

app = Flask(__name__, static_folder="css")
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    markdown_text = ""
    html_preview = ""
    selected_theme = "light"

    if request.method == "POST":
        markdown_text = request.form.get("markdown", "")
        selected_theme = request.form.get("theme", "light")

        # Render Markdown to HTML for preview
        html_preview = markdown.markdown(markdown_text, extensions=['fenced_code', 'tables'])

        # Full HTML for PDF export with selected theme
        full_html = f"""
        <html>
          <head>
            <link rel="stylesheet" href="static/themes.css">
          </head>
          <body class="{selected_theme}">
            {html_preview}
          </body>
        </html>
        """

        # Generate and send PDF
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join(UPLOAD_FOLDER, f"markdown_{selected_theme}_{timestamp}.pdf")
        HTML(string=full_html, base_url='.').write_pdf(output_path)
        return send_file(output_path, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

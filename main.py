from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    # HTML content for rendering
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sour Patch Kiss</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
                background-color: #fafafa;
            }
            .link-container {
                background-color: #f8e71c;
                color: #000;
                border-radius: 10px;
                padding: 20px;
                display: inline-block;
                margin-top: 20px;
                text-decoration: none;
                font-size: 1.2rem;
                font-weight: bold;
            }
            .link-container:hover {
                background-color: #f5c900;
                color: #fff;
                transition: all 0.3s ease;
            }
        </style>
    </head>
    <body>
        <h1>🍭 Sour Patch Kiss 🍬</h1>
        <p>Click the link below to learn more about Sour Patch Kiss on Leafly:</p>
        <a class="link-container" href="https://www.leafly.com/strains/sour-patch-kiss" target="_blank">
            Explore Sour Patch Kiss Strain
        </a>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(debug=True)

import pdfkit
from jinja2 import Environment, FileSystemLoader
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

PDF_PATH = "/usr/local/bin/wkhtmltopdf"   # FIXED PATH

config = pdfkit.configuration(wkhtmltopdf=PDF_PATH)


def generate_pdf(template_name: str, data: dict, output_path="resume.pdf"):
    template = env.get_template(template_name)
    html_content = template.render(data)

    pdfkit.from_string(
        html_content,
        output_path,
        configuration=config
    )

    return output_path

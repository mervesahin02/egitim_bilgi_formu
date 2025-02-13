import os
from jinja2 import Environment, FileSystemLoader

def generate_html_from_data(data, template_path, output_dir):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_path)
    
    os.makedirs(output_dir, exist_ok=True)

    egitim_adi = str(data['egitim_adi']).replace(' ', '_') if data['egitim_adi'] else "default_egitim_adi"
    output_file = os.path.join(output_dir, f"{egitim_adi}.html")

    html_content = template.render(data)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    return output_file

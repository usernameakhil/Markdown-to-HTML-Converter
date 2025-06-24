import argparse
import markdown
import os

def convert_markdown_to_html(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"❌ File not found: {input_path}")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    html = markdown.markdown(md_text, extensions=['fenced_code', 'tables'])

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ HTML file created: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="📝 Convert Markdown to HTML")
    parser.add_argument("input", help="Path to the input .md file")
    parser.add_argument("output", help="Path to the output .html file")

    args = parser.parse_args()
    convert_markdown_to_html(args.input, args.output)

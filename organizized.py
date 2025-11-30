import sys
import os
import re

def organizized(html_file):
    """
    Extract inline CSS and JS from an HTML file into separate files,
    and update the HTML to link to the external files.
    Uses only built-in Python modules.
    """
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract CSS content from <style> tags
    css_matches = re.findall(r'<style[^>]*>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
    css_content = '\n'.join(css_matches)

    # Remove <style> tags from HTML
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)

    # Extract JS content from <script> tags (inline only)
    js_matches = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
    js_content = '\n'.join(js_matches)

    # Remove <script> tags from HTML
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)

    # Add link to CSS in <head>
    head_match = re.search(r'<head[^>]*>', content, re.IGNORECASE)
    if head_match:
        head_end = head_match.end()
        link_tag = '<link rel="stylesheet" href="style.css">'
        content = content[:head_end] + '\n' + link_tag + content[head_end:]

    # Add script tag before </body>
    body_end_match = re.search(r'</body>', content, re.IGNORECASE)
    if body_end_match:
        body_end = body_end_match.start()
        script_tag = '<script src="script.js"></script>'
        content = content[:body_end] + script_tag + '\n' + content[body_end:]

    # Write CSS to file
    css_file = os.path.join(os.path.dirname(html_file), 'style.css')
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css_content)

    # Write JS to file
    js_file = os.path.join(os.path.dirname(html_file), 'script.js')
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    # Write the modified HTML back to the file
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Extracted CSS to {css_file}")
    print(f"Extracted JS to {js_file}")
    print(f"Updated {html_file}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python organizized.py <html_file>")
        sys.exit(1)

    html_file = sys.argv[1]
    if not os.path.isfile(html_file):
        print(f"Error: {html_file} does not exist.")
        sys.exit(1)

    organizized(html_file)
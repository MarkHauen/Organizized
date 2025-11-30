# HTML CSS/JS Extractor

A simple Python script to extract inline CSS and JavaScript from HTML files into separate external files, and update the HTML to reference them.

## Description

When AI agents or other tools generate HTML pages, they often include CSS styles and JavaScript code directly in the HTML file using `<style>` and `<script>` tags. This script helps organize such monolithic HTML files by:

- Extracting all inline CSS into a `style.css` file
- Extracting all inline JavaScript into a `script.js` file
- Removing the inline code from the HTML
- Adding appropriate `<link>` and `<script>` tags to reference the external files

## Requirements

- Python 3.x (uses only built-in modules: `sys`, `os`, `re`)

## Usage

```bash
python extract_css_js.py <path_to_html_file>
```

### Example

```bash
python extract_css_js.py index.html
```

This will:
- Create `style.css` in the same directory as `index.html`
- Create `script.js` in the same directory as `index.html`
- Modify `index.html` to link to the external CSS and JS files

## What It Does

1. **Extracts CSS**: Finds all content between `<style>` tags and combines them into `style.css`
2. **Extracts JS**: Finds all content between `<script>` tags (inline scripts only) and combines them into `script.js`
3. **Updates HTML**:
   - Removes all `<style>` tags
   - Removes all inline `<script>` tags
   - Adds `<link rel="stylesheet" href="style.css">` in the `<head>`
   - Adds `<script src="script.js"></script>` before `</body>`

## Notes

- Only processes inline CSS and JS (ignores external links like `<script src="...">`)
- Overwrites the original HTML file with the modified version
- Creates `style.css` and `script.js` in the same directory as the input HTML file
- If multiple `<style>` or `<script>` tags exist, their contents are concatenated with newlines

## Error Handling

- Checks if the input file exists
- Provides usage instructions if run without arguments

## License

This script is provided as-is for personal use.
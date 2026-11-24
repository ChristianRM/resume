import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
import pypdf

def main():
    root_dir = Path(__file__).resolve().parent
    html_file = root_dir / "index.html"
    
    # Target PDF filename can be provided as argv[1]
    target_name = "Christian_Rincon_Resume.pdf"
    for arg in sys.argv[1:]:
        if not arg.startswith("--") and arg.endswith(".pdf"):
            target_name = arg
            break
            
    pdf_file = root_dir / target_name
    screenshot_dir = root_dir / "tmp-screenshots"
    screenshot_dir.mkdir(exist_ok=True)
    screenshot_file = screenshot_dir / "resume_preview.png"

    if not html_file.exists():
        print(f"Error: {html_file} does not exist", file=sys.stderr)
        sys.exit(1)

    html_uri = html_file.as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html_uri, wait_until="networkidle")

        # Emulate screen & print media to verify layout
        if "--screenshot" in sys.argv:
            page.screenshot(path=str(screenshot_file), full_page=True)
            print(f"[+] Visual screenshot saved to: {screenshot_file}")

        # Export to PDF Letter format with 0 margin (page styles handle padding)
        page.pdf(
            path=str(pdf_file),
            format="Letter",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"}
        )
        browser.close()

    print(f"[+] PDF generated at: {pdf_file}")

    # Validate PDF with pypdf
    reader = pypdf.PdfReader(str(pdf_file))
    num_pages = len(reader.pages)
    print(f"[i] Total pages: {num_pages}")

    if num_pages != 1:
        print(f"[!] Validation ERROR: Resume has {num_pages} pages, but must strictly fit on 1 page!", file=sys.stderr)
        sys.exit(1)

    page_text = reader.pages[0].extract_text() or ""
    char_count = len(page_text.strip())
    word_count = len(page_text.split())

    print(f"[i] Extracted text stats: {char_count} chars, {word_count} words")

    if char_count < 200:
        print("[!] Validation ERROR: Insufficient parseable text extracted from PDF!", file=sys.stderr)
        sys.exit(1)

    print("[OK] PDF is strictly 1 page, selectable and parseable.")

if __name__ == "__main__":
    main()

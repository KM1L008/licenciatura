import re

files_to_update = ['nosotros.html', 'escenario1.html', 'escenario2.html', 'escenario3.html']

for file in files_to_update:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove search button
    html = re.sub(r'<button class="search-btn"[^>]*>.*?</button>', '', html, flags=re.DOTALL)
    
    # Remove search bar
    html = re.sub(r'<div class="search-bar".*?</div>', '', html, flags=re.DOTALL)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)


import os
import re

directory = 'templates'
replacement = '<img src="{{ url_for(\'static\', filename=\'img/favicon.svg\') }}" class="inline-block w-[1.2em] h-[1.2em] -mt-1" alt="BTS">'

# Regex to find <span class="material-symbols-outlined...">toll</span>
pattern = re.compile(r'<span[^>]*material-symbols-outlined[^>]*>toll</span>')

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            content = file.read()
        
        new_content, count = pattern.subn(replacement, content)
        
        if count > 0:
            with open(filepath, 'w') as file:
                file.write(new_content)
            print(f"Replaced {count} instances in {filename}")

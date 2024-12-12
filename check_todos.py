import os

def check_todos(directory):
    # Przechodzimy przez wszystkie pliki w danym katalogu
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Przeszukujemy tylko pliki .py (Python)
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    # Sprawdzamy każdą linię w pliku pod kątem komentarzy 'TODO'
                    for i, line in enumerate(lines, start=1):
                        if 'TODO' in line:
                            print(f"TODO found in {file_path} at line {i}: {line.strip()}")

# Główna funkcja, która uruchamia sprawdzanie plików w głównym katalogu repozytorium
if __name__ == "__main__":
    # Podajemy główny katalog repozytorium
    repo_directory = os.getcwd()
    check_todos(repo_directory)

import os

# Diretório onde estão os módulos
html_dir = "winged/HTML"  # Substitua pelo caminho correto

# Lista de arquivos na pasta HTML
html_files = [f for f in os.listdir(html_dir) if f.endswith(".py")]

# Caminho completo para o arquivo __init__.py
init_py_path = os.path.join(html_dir, "__init__.py")

# Crie e abra o arquivo __init__.py em modo de escrita
with open(init_py_path, "w") as init_py_file:
    # Escreva os imports no arquivo __init__.py
    for html_file in html_files:
        module_name = html_file[:-3]  # Remova a extensão .py
        import_statement = f"from .{module_name} import {module_name.capitalize()}\n"
        init_py_file.write(import_statement)

print(f"Arquivo __init__.py gerado em: {init_py_path}")

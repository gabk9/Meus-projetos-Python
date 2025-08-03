import json
import re

# Entrada interativa
sigla_antiga = input("Digite a letra da unidade atual (ex: g, h, e): ").strip().lower()
sigla_nova = input("Digite a nova letra da unidade desejada (ex: d, e, g): ").strip().lower()

input_file = "extensions.json"
output_file = f"extensions_{sigla_antiga}_to_{sigla_nova}.json"

def substituir_sigla_em_paths(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, str):
                # Substituições possíveis:
                # /e:/ → /d:/ (Linux-like path)
                # \e:/ → \d:/ (Windows path)
                # e:\ → d:\  (fsPath comum)
                # file:///e%3A/ → file:///d%3A/
                value = re.sub(
                    rf'(?<![a-zA-Z0-9]){sigla_antiga}(:[\\/])',
                    lambda m: f"{sigla_nova.upper()}{m.group(1)}",
                    value,
                    flags=re.IGNORECASE
                )
                value = re.sub(
                    rf'{sigla_antiga}%3A',
                    f'{sigla_nova}%3A',
                    value,
                    flags=re.IGNORECASE
                )
                # Caminhos que começam com /e:/ ou \e:/
                value = re.sub(
                    rf'^([/\\]){sigla_antiga}:',
                    lambda m: f"{m.group(1)}{sigla_nova.upper()}:",
                    value,
                    flags=re.IGNORECASE
                )
                obj[key] = value
            else:
                substituir_sigla_em_paths(value)
    elif isinstance(obj, list):
        for item in obj:
            substituir_sigla_em_paths(item)

# Processamento do arquivo
with open(input_file, "r", encoding="utf-8") as f:
    dados = json.load(f)

substituir_sigla_em_paths(dados)

# Salvando o resultado
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(dados, f, separators=(",", ":"))

print(f"\n✔ Conversão concluída: '{input_file}' → '{output_file}'")

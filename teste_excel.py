import sys

def process_excel(file_path):
    # Sua lógica para processar o Excel
    print(f"Processando o arquivo: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor, forneça o caminho para o arquivo Excel.")
    else:
        process_excel(sys.argv[1])

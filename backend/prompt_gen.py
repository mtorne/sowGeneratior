from pathlib import Path

def generar_prompt(datos: dict, file_path: str = "prompt1.txt") -> str:
    """
    Genera un prompt evaluando expresiones tipo f-string desde un archivo.

    :param datos: Diccionario con las variables necesarias
    :param file_path: Ruta al archivo del prompt
    :return: Prompt generado
    """
    path = Path(file_path)
    with open(path, encoding="utf-8") as f:
        prompt_template = f.read()

    try:
        prompt = eval(f"f'''{prompt_template}'''", {"datos": datos})
        return prompt
    except Exception as e:
        raise ValueError(f"Error al generar el prompt: {e}")


if __name__ == "__main__":
    # Diccionario de prueba
    datos = {
        "cliente": "ACME Corp",
        "servicios_oci": ["Compute", "VCN", "Autonomous Database"],
        "descripcion_validacion": "Testing connectivity, provisioning, and service limits."
    }

    prompt = generar_prompt(datos, "prompt2.txt" )
    print("=== Prompt generado ===\n")
    print(prompt)


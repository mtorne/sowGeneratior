import oci

config = oci.config.from_file("~/.oci/config", "DEFAULT")
client = oci.generative_ai_inference.GenerativeAiInferenceClient(config)

compartment_id = "ocid1.compartment.oc1..aaaaaaaaw5klhwyzaxvto4vzwnavevivn75nfuv4fdanlbjux4fuk6tv5geq"  # Canvia per el teu compartiment

response = client.list_models(compartment_id=compartment_id)
for model in response.data:
    print(f"Model OCID: {model.id}")
    print(f"Name: {model.name}")
    print(f"Type: {model.model_type}")
    print(f"Capabilities: {model.capabilities}")
    print("-" * 20)


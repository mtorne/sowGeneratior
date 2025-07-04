# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file()


# Initialize service client with default config file
generative_ai_client = oci.generative_ai.GenerativeAiClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
list_models_response = generative_ai_client.list_models(
    compartment_id="ocid1.compartment.oc1..aaaaaaaaw5klhwyzaxvto4vzwnavevivn75nfuv4fdanlbjux4fuk6tv5geq",
    limit=212,
    sort_by="displayName")

# Get the data from response
print(list_models_response.data)
for model in list_models_response.data.items:
    print(f"Model OCID: {model.id}")
    print(f"Name: {model.display_name}")
    print(f"Type: {model.type}")
    print(f"Capabilities: {model.capabilities}")
    print("-" * 20)


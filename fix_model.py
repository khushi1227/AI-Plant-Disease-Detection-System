import zipfile
import json
import shutil
import os

input_model = "models/best_plant_disease_model.keras"
output_model = "models/best_plant_disease_model_fixed.keras"


def remove_quantization_config(obj):
    if isinstance(obj, dict):
        obj.pop("quantization_config", None)

        for value in obj.values():
            remove_quantization_config(value)

    elif isinstance(obj, list):
        for item in obj:
            remove_quantization_config(item)


print("Reading model...")

with zipfile.ZipFile(input_model, "r") as zin:
    config = json.loads(zin.read("config.json"))

print("Removing incompatible quantization_config entries...")

remove_quantization_config(config)

with zipfile.ZipFile(input_model, "r") as zin:
    with zipfile.ZipFile(output_model, "w", zipfile.ZIP_DEFLATED) as zout:

        for item in zin.infolist():

            if item.filename == "config.json":
                new_config = json.dumps(config).encode("utf-8")
                zout.writestr(item, new_config)
            else:
                zout.writestr(item, zin.read(item.filename))

print()
print("FIXED MODEL CREATED SUCCESSFULLY!")
print(output_model)
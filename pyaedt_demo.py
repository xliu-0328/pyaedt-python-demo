import ansys.aedt.core
from ansys.aedt.core import settings

print("PyAEDT Demo")
print("--------------------")
print("PyAEDT imported successfully!")
print(f"PyAEDT version: {ansys.aedt.core.__version__}")
print(f"Logger enabled: {settings.enable_logger}")
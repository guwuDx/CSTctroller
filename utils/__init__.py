import importlib
from utils.misc import read_toml

version = read_toml("./config/service.toml", "cst")["version"]
print(f"[INFO] configued CST version: {version}")

try:
    cst_general             = importlib.import_module(f"utils.cst_versions.{version}.cst_general")
    para_operations         = importlib.import_module(f"utils.cst_versions.{version}.param_operations")
    basic_operations        = importlib.import_module(f"utils.cst_versions.{version}.basic_operations")
    materials_operations    = importlib.import_module(f"utils.cst_versions.{version}.materials_operations")

except ModuleNotFoundError:
    print(f"[ERRO] CST version {version} is not supported")
    raise ImportError()
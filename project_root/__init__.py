import os
import sys

print(f"path:::: {os.path.abspath('project_root')}")
sys.path.insert(0,os.path.abspath('project_root'))
print(sys.path)
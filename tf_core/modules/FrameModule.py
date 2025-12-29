# thoughtframe/modules/frame_module.py
from abc import ABC
from tf_core.modules.BaseFrameModule import BaseFrameModule



class FrameModule(BaseFrameModule):
    """
    Python-side equivalent of a ThoughtFrame module.
    Handles:
      - calling TF runpaths over HTTP
      - emitting events back into the mesh
      - generic frame-level utilities
      - simple serialization helpers
    """
    
    def __init__(self):
        print("Initialized")

   
    def run_test_command(self, request):
        print(f"Executing test command {request}")
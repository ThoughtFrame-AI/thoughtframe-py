# thoughtframe/modules/frame_module.py
from abc import ABC



class BaseFrameModule(ABC):
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

   

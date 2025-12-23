# thoughtframe/modulemanager.py

from typing import TYPE_CHECKING, Any

from thoughtframe.frameconnection import FrameConnection
from thoughtframe.sensor import SensorMeshManager
from thoughtframe.sensor.sensors import FfmpegAcousticSensor
from thoughtframe.sensor.sensors import SyntheticAcousticSensor
from torch._C._distributed_c10d import Work


class ModuleManager:
    def __init__(self):
        self.field_registry = {}
        # ... (other methods) ...
    def register(self, inName, inFactory):
        self.field_registry[inName] = inFactory
    def get(self, inName):
        # ... (lookup logic) ...
        entry = self.field_registry[inName]
        if callable(entry):
            instance = entry()
            self.field_registry[inName] = instance
            return instance
        return entry

# --- TYPE HINT SETUP ---
if TYPE_CHECKING:
    # 1. Successful import for IDE index
    from thoughtframe.router import BaseFrameRouter 
    from .frameconnection import FrameConnection 
class SystemCatalog:

    def __init__(self, manager: ModuleManager):
        self.field_manager = manager
        
    @property
    def manager(self):
        return self.field_manager
    
    @manager.setter
    def manager(self, inValue):
        self.field_manager = inValue


    
        
    @property
    # 3. Type hint relies on the BaseFrameRouter import above
    def router(self) -> 'BaseFrameRouter': 
        return self.manager.get("router")
    
    @property
    def database(self) -> object:
        return self.manager.get("database")

    @property
    def connection(self) -> 'FrameConnection':
        return self.manager.get("connection")
    
    @property
    def sensormesh(self) -> 'SensorMeshManager':
        return self.manager.get("sensormeshmanager")
    
    
    
        

# No instance creation here!

from typing import TYPE_CHECKING, Any
from pathlib import Path
from typing import Mapping
from thoughtframe.frameconnection import FrameConnection


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
    
    def get(self, name: str) -> Any:
        return self.manager.get(name)
    
    
    def resolve_rooted_path(self,
            config: Mapping,
            *parts: str,
            default_root: str = "."
        ) -> Path:
        """
        Resolve a filesystem path using ThoughtFrame semantics.
    
        Rules:
        - config["root"]: absolute or relative (default ".")
        - all other path parts are forced relative
        - no accidental absolute resets
        """
    
        root = config.get("root") or default_root
        base = Path(root).resolve()
    
        clean_parts = [p.lstrip("/") for p in parts]
    
        return base.joinpath(*clean_parts)

    
        

# No instance creation here!

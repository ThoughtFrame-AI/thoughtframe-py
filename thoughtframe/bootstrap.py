# thoughtframe/bootstrap.py

# 1. Import the necessary class definitions
from thoughtframe.frameconnection import FrameConnection
from thoughtframe.modulemanager import ModuleManager, SystemCatalog 
from thoughtframe.router import BaseFrameRouter


# 2. CREATE THE SINGLETON INSTANCES HERE! (Resolves the AttributeError)
global_manager = ModuleManager()
# 3. Pass the manager instance to the accessor during creation
thoughtframe = SystemCatalog(global_manager) 

def configure():
    # 4. Use the created instance to register dependencies
    global_manager.register("router", lambda: BaseFrameRouter(global_manager))
    global_manager.register("connection", lambda: FrameConnection(global_manager))
    
    
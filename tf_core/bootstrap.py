# thoughtframe/bootstrap.py

# 1. Import the necessary class definitions
from tf_core.frameconnection import FrameConnection
from tf_core.modulemanager import ModuleManager, SystemCatalog 
from tf_core.modules.FrameModule import FrameModule
from tf_core.router import BaseFrameRouter
from tf_core.web.webserver import BaseWebServer


# 2. CREATE THE SINGLETON INSTANCES HERE! (Resolves the AttributeError)
global_manager = ModuleManager()
# 3. Pass the manager instance to the accessor during creation
thoughtframe = SystemCatalog(global_manager) 

def configure(app_cfg: dict):
    # 4. Use the created instance to register dependencies
    global_manager.register("router", lambda: BaseFrameRouter(global_manager))
    global_manager.register("connection", lambda: FrameConnection(global_manager))
    global_manager.register("FrameModule",  lambda: FrameModule())
    net_cfg = app_cfg.get("network")
    if net_cfg:
        global_manager.register(
            "web",
            lambda: BaseWebServer.from_config(global_manager, net_cfg)
        )
    
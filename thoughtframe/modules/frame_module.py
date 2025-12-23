# thoughtframe/modules/frame_module.py

import json
from thoughtframe.httpclient import HttpClient


class FrameModule:
    """
    Python-side equivalent of a ThoughtFrame module.
    Handles:
      - calling TF runpaths over HTTP
      - emitting events back into the mesh
      - generic frame-level utilities
      - simple serialization helpers
    """

    def __init__(self):
        self.http = HttpClient()

    async def call_runpath(self, msg, conn):
        """
        Call a ThoughtFrame runpath via HTTP.
        Expects:  msg.require("runpath")
        Optional: msg.get("params")
        """
        runpath = msg.require("runpath")
        params = msg.get("params", {})

        url = f"{conn.tf_base_url}{runpath}"

        result = await self.http.post(url, params)

        return {
            "command": "runpath_result",
            "runpath": runpath,
            "result": result,
        }

    async def create_frame_event(self, msg, conn):
        """
        Emit a simple event back to TF, following your mesh conventions.
        """
        event = {
            "command": "frame_event",
            "event_type": msg.require("event_type"),
            "details": msg.get("details", {}),
            "session": conn.session_id,
        }
        return event

    async def serialize_frame(self, msg, conn):
        """
        Example placeholder: turn incoming data into a JSON-serializable dict,
        similar to TF’s JSON/ValueMap utilities.
        """
        data = msg.get("data")
        return {
            "command": "frame_serialized",
            "data": json.dumps(data),
            "session": conn.session_id,
        }

    async def ping(self, msg, conn):
        """
        Sanity ping — useful for debugging router/handler connectivity.
        """
        return {
            "command": "frame_pong",
            "session": conn.session_id,
        }

import redis
import json
from backend.app.websockets.socket import socketio

r = redis.Redis(host="redis", port=6379, decode_responses=True)

_active = set()

def start_redis_listener(resume_id):
    if resume_id in _active:
        return
    _active.add(resume_id)

    socketio.start_background_task(_listen, resume_id)

def _listen(resume_id):
    pubsub = r.pubsub()
    pubsub.subscribe(f"resume:channel:{resume_id}")

    for msg in pubsub.listen():
        if msg["type"] == "message":
            data = json.loads(msg["data"])

            print("🚀 emitting resume_status", data)

            socketio.emit(
                "resume_status",
                data,
                room=resume_id
            )
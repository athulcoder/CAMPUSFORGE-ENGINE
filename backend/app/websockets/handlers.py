
from flask_socketio import join_room
from .socket import socketio
from .redis_listener import start_redis_listener

@socketio.on("join_resume")
def join_resume(data):
    resume_id = data["resume_id"]
    join_room(resume_id)
    start_redis_listener(resume_id)
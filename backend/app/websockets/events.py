from flask_socketio import join_room
from backend.app.websockets.socket import socketio

@socketio.on("connect")

@socketio.on("join_resume")
def join_resume(data):
    resume_id = data["resume_id"]
    join_room(resume_id)
    print(f"🟢 Client joined room {resume_id}")
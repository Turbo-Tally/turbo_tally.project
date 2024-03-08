#
# SETUP WEBSOCKETS
# 
from flask import request
from flask_socketio import join_room, send, emit
from scans.data.VideoInfo import VideoInfo

from scans.core.TaskManager import TaskManager
from scans.rooms.StreamRoom import StreamRoom 
from scans.rooms.TaskRoom import TaskRoom

def setup_websockets(socket_io): 

    @socket_io.on("connect") 
    def connect(): 
        # get socket id 
        socket_id = request.sid 
        
        # output to console status of new connection
        print(f"> Received connection from socket_id [{socket_id}]")

    @socket_io.on("join_room")
    def on_join(data): 
        room_id = data
        sid = request.sid 
        
        print(f"> Received signal for [{sid}] to join room {room_id}")
        
        # join room 
        join_room(room_id)
        emit("joined_room", room_id)

        # determine room type 
        room_type = room_id.split(".")[0] 

        # create room based on room type 
        if room_id not in TaskManager.active_rooms:
            room = None 
            
            if room_type == "stream": 
                room = StreamRoom(room_id, socket_io).run()
            elif room_type == "task": 
                room = TaskRoom(room_id, socket_io).run()

            TaskManager.active_rooms[room_id] = room
       
    @socket_io.on("get_video_infos")
    def on_get_video_infos(data): 
        video_ids = data 
        video_infos = {}
        sid = request.sid

        print(
            f"> Received signal for [{sid}] to " + 
            f"get video information {video_ids}"
        )

        for video_id in video_ids: 
            video_info = VideoInfo(video_id) 
            video_infos[video_id] = {
                "stream_id" : video_id,
                "title" : video_info.title, 
                "channel" : video_info.channel 
            }
        
        emit("video_infos", video_infos)

    @socket_io.on("disconnect") 
    def on_disconnect(data): 
        del TaskManager.active_rooms["tasks." + data] 
        del TaskManager.active_tasks[data]




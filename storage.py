ents = [
    'light.hue_white_lamp_1', 
    'light.hue_white_lamp_2', 
    'light.hue_white_lamp_3', 
    'light.hue_white_lamp_4', 
    'light.hue_white_lamp_5', 
    'light.hue_white_lamp_6', 
    'light.hue_white_lamp_7', 
    'light.hue_white_lamp_8', 
    'light.hue_white_lamp_9', 
    'light.hue_white_lamp_10', 
    'light.hue_white_lamp_11', 
    'light.hue_white_lamp_12', 
    'light.hue_white_lamp_13', 
    'light.extended_color_light_1', 
    'light.hue_color_lamp_1'
    ]


known_ips = ["192.168.0.51", "192.168.0.38"]

tokens = [
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI3MzVhYTM3NjBjNDk0MGViYTI3YTk0ZGRlMzk5NzI5NCIsImlhdCI6MTYyOTQ3OTYyMiwiZXhwIjoxOTQ0ODM5NjIyfQ.4AxQruD_7LWA5kT5SMNeWC2T1qPFe_0xTbBJDPJ9YdA", 
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI4OTQ2ODYxMzg5ZWM0ZjFkODhmZGMzODU2OTJhZWQwNCIsImlhdCI6MTYzMzEwODg0MiwiZXhwIjoxOTQ4NDY4ODQyfQ.V-2n0h9rVpSCEFrRLeTFg9UMx5wls2VlR6r2MPY65H4"
    ]

ip_dict = {
    "192.168.0.51" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI3MzVhYTM3NjBjNDk0MGViYTI3YTk0ZGRlMzk5NzI5NCIsImlhdCI6MTYyOTQ3OTYyMiwiZXhwIjoxOTQ0ODM5NjIyfQ.4AxQruD_7LWA5kT5SMNeWC2T1qPFe_0xTbBJDPJ9YdA" ,
    "192.168.0.38" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI4OTQ2ODYxMzg5ZWM0ZjFkODhmZGMzODU2OTJhZWQwNCIsImlhdCI6MTYzMzEwODg0MiwiZXhwIjoxOTQ4NDY4ODQyfQ.V-2n0h9rVpSCEFrRLeTFg9UMx5wls2VlR6r2MPY65H4"
    }

domains =["automation", "binary_sensor", "camera", "climate", "cover", "device_tracker", "light", "lock", "media_player", "persistent_notification", "person", "remote", "sensor", "sun", "switch", "weather", "zone"]

#these are representative of JWB HA(main)
#To add: notifications
services = {
    "automation": [
        "toggle", 
        "trigger", 
        "turn_off", 
        "turn_on"
        ], 
    "camera": [
        "disable_motion_detection", 
        "enable_motion_detection", 
        "play_stream", 
        "record", 
        "snapshot", 
        "turn_off", 
        "turn_on"
        ], 
    "climate": [
        "set_aux_heat", 
        "set_fan_mode", 
        "set_humidity", 
        "set_hvac_mode", 
        "set_preset_mode", 
        "set_swing_mode", 
        "set_temperature", 
        "turn_off", 
        "turn_on"
        ], 
    "cover": [
        "close_cover", 
        "close_cover_tilt", 
        "open_cover", 
        "open_cover_tilt", 
        "set_cover_position", 
        "set_cover_tilt_position", 
        "stop_cover", 
        "stop_cover_tilt", 
        "toggle", 
        "toggle_cover_tilt"
        ], 
    "device_tracker": "see", 
    #where's the percentage toggle for the light service? Is it input_boolean? number.set_value?
    "light": [
        "toggle", 
        "turn_off", 
        "turn_on"
        ] , 
    "lock": [
        "lock", 
        "open", 
        "unlock"
        ], 
    "media_player": [
        "clear_playlist",
        "join",
        "media_next_track",
        "media_pause",
        "media_play",
        "media_play_pause",
        "media_previous_track",
        "media_seek",
        "media_stop",
        "play_media",
        "repeat_set",
        "select_sound_mode",
        "select_source",
        "shuffle_set",
        "toggle",
        "turn_off",
        "turn_on",
        "unjoin",
        "volume_down",
        "volume_mute",
        "volume_set",
        "volume_up"
    ], 
    "persistent_notification": [
        "create",
        "dismiss",
        "mark_read"
    ], 
    "person": "reload", 
    #"remote", 
    #"sensor", 
    #"sun", 
    "switch": [
        "toggle",
        "turn_off",
        "turn_on"
    ], 
    #"weather", 
    "zone": "reload"
}
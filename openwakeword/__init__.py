import os
from openwakeword.model import Model

__all__ = ['Model', ]

models = {
    "alexa": {
        "model_path": os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources/models/alexa_v7.onnx")
    },
    "hey_mycroft": {
        "model_path": os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources/models/hey_mycroft_v1.onnx")
    },
    "timer": {
        "model_path": os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources/models/timer_v2.onnx")
    },
    "weather": {
        "model_path": os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources/models/weather_v1.onnx")
    }
}

model_class_mappings = {
    "timer": {
        "1": "1_minute_timer",
        "2": "5_minute_timer",
        "3": "10_minute_timer",
        "4": "20_minute_timer",
        "5": "30_minute_timer",
        "6": "1_hour_timer" 
    }
}

def get_pretrained_model_paths():
    return [models[i]["model_path"] for i in models.keys()]

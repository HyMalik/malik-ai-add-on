from fastapi import FastAPI
from pydantic import BaseModel
import random
import json

# Initialize FastAPI app
app = FastAPI()

# Predefined object types, materials, and textures
object_types = ['human', 'animal', 'tree', 'building', 'car', 'furniture', 'lamp', 'statue']
textures = ['wood', 'metal', 'stone', 'fabric', 'plastic', 'glass', 'marble']
materials = ['shiny', 'matte', 'smooth', 'rough', 'wet']
lighting_types = ['point_light', 'sun_light', 'spot_light']
scene_modes = ['indoor', 'outdoor']

# Generate random object properties
def generate_random_properties(obj_type):
    material = random.choice(materials)
    texture = random.choice(textures)
    location = (random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(0, 3))
    rotation = (random.uniform(0, 360), random.uniform(0, 360), random.uniform(0, 360))
    scale = random.uniform(0.5, 3)
    
    return {
        'material': material,
        'texture': texture,
        'location': location,
        'rotation': rotation,
        'scale': scale
    }

# Generate scene based on prompt
def generate_scene(prompt):
    # Mode of the scene (indoor or outdoor)
    scene_mode = random.choice(scene_modes)
    
    # Number of objects in the scene
    num_objects = random.randint(5, 15)  
    scene_objects = []
    
    # Generate objects based on the prompt
    for _ in range(num_objects):
        obj_type = random.choice(object_types)
        properties = generate_random_properties(obj_type)
        
        scene_objects.append({
            'type': obj_type,
            'properties': properties
        })
    
    # Lighting and Camera setup
    scene_lights = []
    if scene_mode == 'outdoor':
        scene_lights.append({
            'type': 'sun_light', 
            'intensity': random.uniform(1, 5), 
            'location': (random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(10, 15))
        })
    else:
        scene_lights.append({
            'type': 'point_light', 
            'intensity': random.uniform(2, 5), 
            'location': (random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(1, 3))
        })
    
    camera_position = (random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(5, 15))
    camera_focal_length = random.uniform(35, 100)
    
    return {
        'scene_objects': scene_objects,
        'scene_lights': scene_lights,
        'camera': {
            'position': camera_position,
            'focal_length': camera_focal_length
        },
        'scene_mode': scene_mode
    }

class SceneRequest(BaseModel):
    prompt: str

# API endpoint to generate a scene based on the prompt
@app.post("/generate_scene/")
async def generate_scene_endpoint(request: SceneRequest):
    prompt = request.prompt
    scene_details = generate_scene(prompt)
    return scene_details

# To run with uvicorn: uvicorn scene_generator:app --reload

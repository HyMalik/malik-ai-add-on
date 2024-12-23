#!/bin/bash
uvicorn scene_generator:app --host 0.0.0.0 --port $PORT

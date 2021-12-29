from flask import Flask
import cloudinary



app = Flask(__name__)





cloud = cloudinary.config(
    cloud_name="dz0fpgnow",
    api_key="818174779534462",
    api_secret="Zbr1z-wKtr11AlldBNJgbKzqH9A"
)
from app import routes
from flask import Blueprint, jsonify
from .models import Business
from .extensions import db

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "GrowBiz Core Running"

@main.route("/health")
def health():
    return jsonify({"status": "ok"})

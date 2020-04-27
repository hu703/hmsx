from flask import Blueprint
from common.libs.Helper import *

router_index = Blueprint('index_page',__name__)

@router_index.route("/")
def index():
    return ops_render("index/index.html")
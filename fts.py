from flask import Blueprint, render_template, request, jsonify, send_file
import os
from werkzeug.utils import secure_filename

fts = Blueprint('fts', 'fts')


def get_files_in_workspace():
    user_id = request.cookies.get('user_id')
    return os.listdir(f'IndividualWorkSpaces/{user_id}/')


@fts.route("/fts/")
def fts_load():
    files = get_files_in_workspace()
    return render_template('fts.html', files=files)


@fts.route("/fts/upload", methods=["POST"])
def fts_post():
    username = request.cookies.get('user_id')
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(f"IndividualWorkSpaces/{username}", filename))

    return jsonify(resultUp="File uploaded successfully")


@fts.route("/fts/download", methods=["GET"])
def fts_download():
    user_id = request.cookies.get('user_id')
    selected = request.args.get('file')
    return send_file(f"IndividualWorkSpaces/{user_id}/{selected}")

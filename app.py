import os
from flask import Flask, jsonify, Response, make_response, request
from manager.manager import start_job, get_jobs, get_job

app = Flask(__name__)

# app.config['MONGODB_SETTINGS'] = {
#     'db': os.environ.get("DB_NAME"),
#     'host': os.environ.get("DB_HOST")
# }

@app.route("/api/v1/jobs", methods=['GET', 'POST'])
def jobs():
    if request.method == 'POST':
        data = request.get_json()
        url = data.get('url', '')
        if not url:
            return Response("url is not provided.", status=400)
        elif type(url) != str:
            return Response("url must be a string.", status=400)

        job_item = start_job(url)
        return make_response(jsonify(job_item), 200)
    else:
        #jsonify([user.to_json() for user in users])
        job_items = get_jobs()
        return make_response(jsonify(job_items), 200)


@app.route("/api/v1/jobs/<job_id>", methods=['GET'])
def job(job_id):
    job_item = get_job(job_id)
    return make_response(jsonify(job_item), 200)


if __name__ == '__main__':
    os.environ.get("FLASK_RUN_HOST", "127.0.0.1" )
    app.run(host="0.0.0.0", debug=True)
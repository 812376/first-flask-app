from config import app,client
from flask import request

@app.route('/upload-image',method=['POST'])
def upload_image():
    bucket='python-bucket234'
    content_type=request.mimetype
    obj=request.files['file']
    filename=obj.filename
    client.put_object(Body=obj,
          Bucket=bucket,
          key=filename,
          ContentType=content_type
    )

    return {'message': 'file uploaded'}, 200

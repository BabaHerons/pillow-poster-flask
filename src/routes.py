from src import db, api
from flask import send_file
from flask_restful import reqparse, Resource
import werkzeug, datetime
from io import BytesIO
from src.models import Image, BackgroundImage
from utils import adding_frame

image_args = reqparse.RequestParser()
image_args.add_argument("image", type=werkzeug.datastructures.FileStorage, help='Image is required', required = True, location='files')

class ImageEndpoint(Resource):
    def post(self):
        args = image_args.parse_args()
        unique_id = str(datetime.datetime.now())
        image = Image(image=args["image"].read(), id = unique_id)
        db.session.add(image)
        db.session.commit()
        db.session.refresh(image)
        try:
            updated_image = adding_frame(1, unique_id)
        except:
            return {"message":"Something went wrong"}, 500
        del_image = Image.query.filter_by(id = unique_id).first()
        if del_image:
            try:
                db.session.delete(del_image)
                db.session.commit()
            except:
                return {"Message":"image deletion is unsuccessfull"}, 500
        return send_file(BytesIO(updated_image), mimetype='image/jpeg')

class BackgroundImageEndpoint(Resource):
    def post(self):
        args = image_args.parse_args()
        image = BackgroundImage(image=args["image"].read())
        db.session.add(image)
        db.session.commit()
        db.session.refresh(image)
        return {"message":"Image added"}

api.add_resource(ImageEndpoint, "/")
api.add_resource(BackgroundImageEndpoint, "/bg")
import os
import os.path as op

from werkzeug.utils import secure_filename
from sqlalchemy import event
from wtforms import fields

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

import flask_admin as admin
from flask_admin.form import RenderTemplateWidget
from flask_admin.model.form import InlineFormAdmin
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.form import InlineModelConverter
from flask_admin.contrib.sqla.fields import InlineModelFormList


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)

basedir = op.join(op.abspath(op.dirname(__file__)), 'data.sqlite')
# Create in-memory database
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{basedir}'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

base_path = op.join(op.dirname(__file__), 'static')


class Location(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))


class LocationImage(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    alt = db.Column(db.Unicode(128))
    path = db.Column(db.String(64))

    location_id = db.Column(db.Integer, db.ForeignKey(Location.id))
    location = db.relation(Location, backref='images')


# Register after_delete handler which will delete image file after model gets deleted
@event.listens_for(LocationImage, 'after_delete')
def _handle_image_delete(mapper, conn, target):
    
    try:
        if target.path:
            os.remove(op.join(base_path, target.path))
    except:
        pass


#####################
#---<FORM WIDGET>---#
#####################

class CustomInlineFieldWidget(RenderTemplateWidget):

    def __init__(self):
        super(CustomInlineFieldWidget, self).__init__('field_list.html')

# This InlineModelFormList will use our custom widget and hide row controls
class CustomInlineModelFormList(InlineModelFormList):

    widget = CustomInlineFieldWidget()

    def display_row_controls(self, field):
        return False

# Create custom InlineModelConverter and tell it to use our InlineModelFormList
class CustomInlineModelConverter(InlineModelConverter):
    
    inline_field_list_type = CustomInlineModelFormList


########################################
#---<Customized inline form handler>---#
########################################

class InlineModelForm(InlineFormAdmin):

    form_excluded_column = ('path', )
    form_label = 'Image'

    def __init__(self):
        return super(InlineModelForm, self).__init__(LocationImage)
    
    def postprocess_form(self, form_class):

        form_class.upload = fields.FileField('Image')
        return form_class

    def on_model_change(self, form, model):

        if file_data := request.files.get(form.upload.name):
            model.path = secure_filename(file_data.filename)
            file_data.save(op.join(base_path, model.path))


###############################
#---<CAdministrative class>---#
###############################

class LocationAdmin(ModelView):

    inline_model_form_converter = CustomInlineModelConverter
    inline_models = (InlineModelForm(), )

    def __init__(self):
        super(LocationAdmin, self).__init__(Location, db.session, name='Locations')


@app.route('/')
def index():
    locations = db.session.query(Location).all()
    return render_template('locations.html', locations=locations)


if __name__ == '__main__':
    try:
        os.mkdir(base_path)
    except OSError:
        pass
    admin = admin.Admin(app, name='Admin Console')
    admin.add_view(LocationAdmin())
    db.create_all()
    app.run(debug=True)

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class EditForm(FlaskForm):
    rating = StringField("Your rating out of 10. i.e:7.5", validators=[DataRequired()])
    review = StringField("Your review", validators=[DataRequired()])
    submit = SubmitField("Done!")


class AddForm(FlaskForm):
    movie_title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add")

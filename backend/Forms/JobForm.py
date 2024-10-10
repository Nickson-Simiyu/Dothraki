from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class JobForm(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired()])
    description = TextAreaField('Job Description', validators=[DataRequired()])
    company = StringField('Company Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    category = SelectField('Category', 
                            choices=[('IT', 'IT'), ('Healthcare', 'Healthcare'), ('Finance', 'Finance')],
                            validators=[DataRequired()])
    skill_requirements = TextAreaField('Required Skills (comma-separated)', 
                                        validators=[DataRequired()])
    submit = SubmitField('Create Job')

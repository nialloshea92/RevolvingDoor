from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Regexp, email, ValidationError
from app.reg.utils import postcode_validate

class OldRegistrationForm(Form):
    name = StringField(u'Name', validators=[DataRequired()])
    phone_1 = StringField(u'Phone #1')
    phone_2 = StringField(u'Phone #2')
    email = StringField(u'Email', validators=[email])
    postcode = StringField(u'Postcode', validators=[Regexp('^(([gG][iI][rR] {0,}0[aA]{2})|((([a-pr-uwyzA-PR-UWYZ][a-hk-yA-HK-Y]?[0-9][0-9]?)|(([a-pr-uwyzA-PR-UWYZ][0-9][a-hjkstuwA-HJKSTUW])|([a-pr-uwyzA-PR-UWYZ][a-hk-yA-HK-Y][0-9][abehmnprv-yABEHMNPRV-Y]))) {0,}[0-9][abd-hjlnp-uw-zABD-HJLNP-UW-Z]{2}))$', message='Postcode Invalid')])
    nationality = SelectField(u'Nationality', coerce=int)
    notes = TextAreaField(u'Notes')
    DoNotUse = BooleanField(u'Blacklist')
    submit = SubmitField('Submit')

class RegistrationForm(Form):
    name = StringField(u'Name')
    phone_1 = StringField(u'Phone #1')
    phone_2 = StringField(u'Phone #2')
    email = StringField(u'Email', validators=[email()])
    postcode = StringField(u'Postcode')
    nationality = SelectField(u'Nationality', coerce=int)
    notes = TextAreaField(u'Notes')
    DoNotUse = BooleanField(u'Blacklist')
    submit = SubmitField(u'Submit')

    def validate_postcode(form, field):
        if not postcode_validate(field.data):
            raise ValidationError('Enter valid postcode')

class BasicRegistration(Form):
    name = StringField(u'Name')
    submit = SubmitField(u'Submit')
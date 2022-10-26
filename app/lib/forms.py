
from flask_wtf import FlaskForm
from wtforms.fields import SelectField, IntegerField
from wtforms import SubmitField, BooleanField
from wtforms.validators import DataRequired, NumberRange, ValidationError


class PreferencesForm(FlaskForm):
    house = BooleanField('House', default=True)
    apt = BooleanField('Apartment', default=True)
    one_bed = BooleanField('1 Bed', default=True)
    two_bed = BooleanField('2 Bed')
    three_bed = BooleanField('3 Bed')
    fourplus_bed = BooleanField('4+ Bed')
    shared = BooleanField('Shared')
    rent = IntegerField('Weekly rent', validators = [DataRequired(), NumberRange(min=0)], default = 400)
    acc_prio = SelectField('Accomodation Priority', choices = [(0, 'None'), (1, 'Low'), (2, 'Medium'), (3, 'High')], default=3)

    env_retail = BooleanField('Retail', default=True)
    env_accomodation_food = BooleanField('Food')
    env_public_admin = BooleanField('Administration')
    env_healthcare_social_assist = BooleanField('Health Care')
    env_arts_recreation = BooleanField('Recreation')
    env_rental_hiring_realestate = BooleanField('Real Estate')
    env_parks = BooleanField('Parks')
    env_prio = SelectField('Environment Priority', choices = [(0, 'None'), (1, 'Low'), (2, 'Medium'), (3, 'High')], default=1)

    tra_train = BooleanField('Train', default=True)
    tra_bus = BooleanField('Bus')
    tra_tram = BooleanField('Tram')
    tra_prio = SelectField('Transportation Priority', choices = [(0, 'None'), (1, 'Low'), (2, 'Medium'), (3, 'High')], default=1)
    
    saf_crime_person = BooleanField('Crimes against the person')
    saf_crime_property = BooleanField('Property and deception offences')
    saf_drug_offences = BooleanField('Drug offences')
    saf_order_security = BooleanField('Public order and security offences')
    saf_justice_procedure = BooleanField('Justice procedure offences')
    saf_other = BooleanField('Other offences')
    saf_prio = SelectField('Safety Priority', choices = [(0, 'None'), (1, 'Low'), (2, 'Medium'), (3, 'High')], default=1)

    dem_students_relative = BooleanField('High Student Population', default=True)
    dem_prio = SelectField('Demographics Priority', choices = [(0, 'None'), (1, 'Low'), (2, 'Medium'), (3, 'High')], default=1)

    university = SelectField('University', choices = [('com_swinbourne_hawthorn','Swinbourne Hawthorn'), ('com_swinbourne_croydon','Swinbourne Croydon'), ('com_swinbourne_wantirna','Swinbourne Wantirna'), ('com_deakin_burwood','Deakin Burwood'), ('com_deakin_geelong','Deakin Geelong'), ('com_deakin_warrnambool','Deakin Warrnambool'), ('com_federation_ballarat','Federation Ballarat'), ('com_federation_churchill','Federation Churchill'), ('com_federation_berwick','Federation Berwick'), ('com_federation_wimmera','Federation Wimmera'), ('com_latrobe_melbourne','La Trobe Melbourne'), ('com_latrobe_bendigo','La Trobe Bendigo'), ('com_latrobe_shepparton','La Trobe Shepparton'), ('com_latrobe_wodonga','La Trobe Wodonga'), ('com_latrobe_mildura','La Trobe Mildura'), ('com_monash_clayton','Monash Clayton'), ('com_monash_caulfield','Monash Caulfield'), ('com_monash_peninsula','Monash Peninsula'), ('com_monash_parkville','Monash Parkville'), ('com_rmit_melbourne','RMIT Melbourne'), ('com_swinburne_hawthorne','Swinburne Hawthorne'), ('com_swinburne_croydon','Swinburne Croydon'), ('com_swinburne_wantirna','Swinburne Wantirna'), ('com_unimelb_parkville','Melbourne University Parkville'), ('com_unimelb_southbank','Melbourne University Southbank'), ('com_unimelb_burnley','Melbourne University Burnley'), ('com_unimelb_dookie','Melbourne University Dookie'), ('com_unimelb_creswick','Melbourne University Creswick'), ('com_unimelb_werribee','Melburne University Werribee'), ('com_unimelb_shepparton','Melbounre University Shepparton'), ('com_vicuni_melbourne','Victoria University Melbounre'), ('com_vicuni_footscray','Victoria University Footscray'), ('com_vicuni_stalbans','Victoria University Stalbans'), ('com_vicuni_sunshine','Victoria University Sunshine'), ('com_vicuni_werribee','Victoria University Werribee'), ('com_catholic_ballarat','Catholic Ballarat'), ('com_catholic_melbourne','Catholic Melbourne'), ('com_torrens_melbourne','Torrens')])
    com_max_dist = IntegerField('Maximum distance from campus (km)', validators=[DataRequired(), NumberRange(min=0, max=30)], default=15)
    com_prio = SelectField('Commute Priority', choices = [(0, 'None'), (1, 'Low'), (2, 'Medium'), (3, 'High')], default=3)

    submit = SubmitField('Find a nest!')

    def validate_house(self, field):
        if not field.data and not self.apt.data:
            raise ValidationError("You must select at least one option.")
    
    def validate_one_bed(self, field):
        if not field.data and not self.two_bed.data and not self.three_bed.data and not self.fourplus_bed.data:
            raise ValidationError("You must select at least one option.")


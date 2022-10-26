
from flask import Flask, render_template, redirect, url_for, session, request
from flask_sqlalchemy import SQLAlchemy

from app.lib.forms import PreferencesForm
from app.lib.model import get_suburb_from_prefs


app = Flask(__name__)
app.config["SECRET_KEY"] = "be4f1a2528babbfe522d6fc83008a35c"
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data/site.sqlite"


from app.data.models import Suburb


def get_rent_values(multiplier: int, rent_number: int = None) -> dict:
    if rent_number is None:
        rent_number = 1000
    rent_number = int(rent_number)
    return {
        "acc_rent_1_74": multiplier,
        "acc_rent_75_99": multiplier if rent_number > 75 else 0,
        "acc_rent_100_149": multiplier if rent_number > 100 else 0,
        "acc_rent_150_199": multiplier if rent_number > 150 else 0,
        "acc_rent_200_224": multiplier if rent_number > 200 else 0,
        "acc_rent_225_274": multiplier if rent_number > 225 else 0,
        "acc_rent_275_349": multiplier if rent_number > 275 else 0,
        "acc_rent_350_449": multiplier if rent_number > 350 else 0,
        "acc_rent_450_549": multiplier if rent_number > 450 else 0,
        "acc_rent_550_649": multiplier if rent_number > 550 else 0,
        "acc_rent_650_749": multiplier if rent_number > 650 else 0,
        "acc_rent_750_849": multiplier if rent_number > 750 else 0,
        "acc_rent_850_949": multiplier if rent_number > 850 else 0,
        "acc_rent_950_plus": multiplier if rent_number > 950 else 0,
    }

@app.route("/")
@app.route("/about")
@app.route("/home")
def home():
    form = PreferencesForm()
    # get preferences form data from session cookie (last submission)
    form_data = session.get("preferences_form", None)

    # if previous form submission exists
    if form_data is not None:
        # get last submitted form data and set form values to these values
        if request.method == "GET":
            for key in form_data:
                if key != "csrf_token":
                    form[key].data = form_data[key]

    # if the user submits a valid form, then save the form and redirect to self
    if form.validate_on_submit():
        session["preferences_form"] = form.data
        return redirect(url_for("map"))

    return render_template("home.html", title="Home", form=form)


@app.route("/map", methods=["GET", "POST"])
def map():
    form = PreferencesForm()

    # if the user submits a valid form, then save the form and redirect to self
    if form.validate_on_submit():
        session["preferences_form"] = form.data
        return redirect(url_for("map"))

    # get preferences form data from session cookie (last submission)
    form_data = session.get("preferences_form", None)

    # if previous form submission exists
    if form_data is not None:
        # get last submitted form data and set form values to these values
        if request.method == "GET":
            for key in form_data:
                if key != "csrf_token":
                    form[key].data = form_data[key]

        # get dictionary of user inputs
        user_input = {
            "acc_house_onebed": form.acc_prio.data if form.house.data and form.one_bed.data else 0,
            "acc_house_twobed": form.acc_prio.data if form.house.data and form.two_bed.data else 0,
            "acc_house_threebed": form.acc_prio.data if form.house.data and form.three_bed.data else 0,
            "acc_house_fourplusbed": form.acc_prio.data if form.house.data and form.fourplus_bed.data else 0,
            "acc_apartment_onebed": form.acc_prio.data if form.apt.data and form.one_bed.data else 0,
            "acc_apartment_twobed": form.acc_prio.data if form.apt.data and form.two_bed.data else 0,
            "acc_apartment_threebed": form.acc_prio.data if form.apt.data and form.three_bed.data else 0,
            "acc_apartment_fourplusbed": form.acc_prio.data if form.apt.data and form.fourplus_bed.data else 0,
            "acc_rented_house_relative": form.acc_prio.data if form.house.data else 0,
            "acc_rented_apartment_relative": form.acc_prio.data if form.apt.data else 0,
            "acc_shared_relative": form.acc_prio.data if form.shared.data else 0,
            "env_retail": form.env_prio.data if form.env_retail.data else 0,
            "env_accomodation_food": form.env_prio.data if form.env_accomodation_food.data else 0,
            "env_public_admin": form.env_prio.data if form.env_public_admin.data else 0,
            "env_healthcare_social_assist": form.env_prio.data if form.env_healthcare_social_assist.data else 0,
            "env_arts_recreation": form.env_prio.data if form.env_arts_recreation.data else 0,
            "env_rental_hiring_realestate": form.env_prio.data if form.env_rental_hiring_realestate.data else 0,
            "env_parks": form.env_prio.data if form.env_parks.data else 0,
            "dem_students_relative": form.dem_prio.data if form.dem_students_relative else 0,
            "saf_crime_person": form.saf_prio.data if form.saf_crime_person.data else 0,
            "saf_crime_property": form.saf_prio.data if form.saf_crime_property.data else 0,
            "saf_drug_offences": form.saf_prio.data if form.saf_drug_offences.data else 0,
            "saf_order_security": form.saf_prio.data if form.saf_order_security.data else 0,
            "saf_justice_procedure": form.saf_prio.data if form.saf_justice_procedure.data else 0,
            "saf_other": form.saf_prio.data if form.saf_other.data else 0,
            "tra_train": form.tra_prio.data if form.tra_train.data else 0,
            "tra_bus": form.tra_prio.data if form.tra_bus.data else 0,
            "tra_tram": form.tra_prio.data if form.tra_tram.data else 0,
            "com_max_dist": form.com_max_dist.data,
            "com_swinbourne_hawthorn": form.com_prio.data if form.university.data == "com_swinbourne_hawthorn" else 0,
            "com_swinbourne_croydon": form.com_prio.data if form.university.data == "com_swinbourne_croydon" else 0,
            "com_swinbourne_wantirna": form.com_prio.data if form.university.data == "com_swinbourne_wantirna" else 0,
            "com_deakin_burwood": form.com_prio.data if form.university.data == "com_deakin_burwood" else 0,
            "com_deakin_geelong": form.com_prio.data if form.university.data == "com_deakin_geelong" else 0,
            "com_deakin_warrnambool": form.com_prio.data if form.university.data == "com_deakin_warrnambool" else 0,
            "com_federation_ballarat": form.com_prio.data if form.university.data == "com_federation_ballarat" else 0,
            "com_federation_churchill": form.com_prio.data if form.university.data == "com_federation_churchill" else 0,
            "com_federation_berwick": form.com_prio.data if form.university.data == "com_federation_berwick" else 0,
            "com_federation_wimmera": form.com_prio.data if form.university.data == "com_federation_wimmera" else 0,
            "com_latrobe_melbourne": form.com_prio.data if form.university.data == "com_latrobe_melbourne" else 0,
            "com_latrobe_bendigo": form.com_prio.data if form.university.data == "com_latrobe_bendigo" else 0,
            "com_latrobe_shepparton": form.com_prio.data if form.university.data == "com_latrobe_shepparton" else 0,
            "com_latrobe_wodonga": form.com_prio.data if form.university.data == "com_latrobe_wodonga" else 0,
            "com_latrobe_mildura": form.com_prio.data if form.university.data == "com_latrobe_mildura" else 0,
            "com_monash_clayton": form.com_prio.data if form.university.data == "com_monash_clayton" else 0,
            "com_monash_caulfield": form.com_prio.data if form.university.data == "com_monash_caulfield" else 0,
            "com_monash_peninsula": form.com_prio.data if form.university.data == "com_monash_peninsula" else 0,
            "com_monash_parkville": form.com_prio.data if form.university.data == "com_monash_parkville" else 0,
            "com_rmit_melbourne": form.com_prio.data if form.university.data == "com_rmit_melbourne" else 0,
            "com_swinburne_hawthorne": form.com_prio.data if form.university.data == "com_swinburne_hawthorn" else 0,
            "com_swinburne_croydon": form.com_prio.data if form.university.data == "com_swinburne_croydon" else 0,
            "com_swinburne_wantirna": form.com_prio.data if form.university.data == "com_swinburne_wantirna" else 0,
            "com_unimelb_parkville": form.com_prio.data if form.university.data == "com_unimelb_parkville" else 0,
            "com_unimelb_southbank": form.com_prio.data if form.university.data == "com_unimelb_southbank" else 0,
            "com_unimelb_burnley": form.com_prio.data if form.university.data == "com_unimelb_burnley" else 0,
            "com_unimelb_dookie": form.com_prio.data if form.university.data == "com_unimelb_dookie" else 0,
            "com_unimelb_creswick": form.com_prio.data if form.university.data == "com_unimelb_creswick" else 0,
            "com_unimelb_werribee": form.com_prio.data if form.university.data == "com_unimelb_werribee" else 0,
            "com_unimelb_shepparton": form.com_prio.data if form.university.data == "com_unimelb_shepparton" else 0,
            "com_vicuni_melbourne": form.com_prio.data if form.university.data == "com_vicuni_melbourne" else 0,
            "com_vicuni_footscray": form.com_prio.data if form.university.data == "com_vicuni_footscray" else 0,
            "com_vicuni_stalbans": form.com_prio.data if form.university.data == "com_vicuni_stalbans" else 0,
            "com_vicuni_sunshine": form.com_prio.data if form.university.data == "com_vicuni_sunshine" else 0,
            "com_vicuni_werribee": form.com_prio.data if form.university.data == "com_vicuni_werribee" else 0,
            "com_catholic_ballarat": form.com_prio.data if form.university.data == "com_catholic_ballarat" else 0,
            "com_catholic_melbourne": form.com_prio.data if form.university.data == "com_catholic_melbourne" else 0,
            "com_torrens_melbourne": form.com_prio.data if form.university.data == "com_torrens_melbourne" else 0,
        }
        rent = get_rent_values(form.rent.data, form.acc_prio.data)
        user_input.update(rent)

        # get suburb which best matches last preference input
        suburb_name = get_suburb_from_prefs(user_input)
        suburb_data = Suburb.query.get(suburb_name)
    
    # if the form has never been submitted
    else:
        suburb_data = None

    return render_template("map.html", title="Map", form=form, details=suburb_data)


@app.route("/data")
def data():
    return render_template("data.html", title="Data")


@app.route("/news")
def news():
    return render_template("news.html", title="News")


@app.route("/help")
def help():
    return render_template("help.html", title="Help")


@app.route("/terms-and-conditions")
def terms():
    return render_template("terms.html", title="Terms")


@app.route("/privacy-policy")
def privacy():
    return render_template("privacy.html", title="Privacy")


@app.route("/init-data")
def init_data():
    from initialise_data import main
    main()
    return redirect(url_for("home"))

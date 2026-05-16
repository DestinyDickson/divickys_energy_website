from flask import Flask, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__)
app.secret_key = "replace-this-secret-key"

COMPANY = {
    "name": "DIVICKYS ENERGY RESOURCES LIMITED",
    "tagline": "Powering Today While Fueling Tomorrow",
    "address": "#1 Evangel Close, off Elijiji Road, Woji, Port Harcourt, Rivers State, Nigeria",
    "phones": ["+234-8035727090", "+234-7067605183"],
    "email": "divickyserl@gmail.com",
    "website": "www.divckysenergyresources.com",
    "cac": "7594871",
    "established": "2024"
}

SERVICES = [
    "Drilling Support Services",
    "Pipeline Maintenance and Inspection Services",
    "Petroleum Product Supply and Distribution",
    "Storage and Tank Farm Solutions",
    "Mechanical and Machine Shop Services",
    "Fabrication and Welding Services",
    "Industrial Inspection and Quality Assurance",
    "Procurement and Supply Chain Support",
    "Equipment Leasing and Supply",
    "Skilled and Unskilled Manpower Supply",
    "Engineering and Technical Consultancy Services",
    "Marine and Logistics Support Services",
    "Health, Safety, and Environmental Compliance Support"
]

CORE_VALUES = [
    ("Integrity", "We uphold honesty, transparency, and accountability in all we do."),
    ("Innovation & Sustainability", "We embrace modern solutions and continuous improvement while operating responsibly to protect the environment."),
    ("Excellence", "We deliver quality and outstanding performance through collaboration, respect, and strong partnerships."),
    ("Customer Commitment", "We strive to meet and exceed client expectations with reliable and safe services.")
]

WHY_CHOOSE_US = [
    "Experienced and skilled workforce",
    "Commitment to quality and timely service delivery",
    "Strong focus on safety and environmental sustainability",
    "Client-centered approach and long-term partnerships",
    "Modern operational practices and innovative solutions",
    "Reliable support across the oil and gas value chain"
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        company=COMPANY,
        services=SERVICES[:6],
        core_values=CORE_VALUES,
        why_choose_us=WHY_CHOOSE_US
    )

@app.route("/about")
def about():
    return render_template("about.html", company=COMPANY, core_values=CORE_VALUES)

@app.route("/services")
def services():
    return render_template("services.html", company=COMPANY, services=SERVICES)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("Please complete all fields before submitting.", "error")
        elif not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            flash("Please enter a valid email address.", "error")
        else:
            # In production, connect this to an email service or database.
            flash("Thank you. Your message has been received.", "success")
            return redirect(url_for("contact"))

    return render_template("contact.html", company=COMPANY)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", company=COMPANY), 404

if __name__ == "__main__":
    app.run(debug=True)

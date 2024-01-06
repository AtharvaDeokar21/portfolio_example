from flask import Blueprint, render_template, request, jsonify, redirect, url_for

main = Blueprint("main", __name__)

@main.route("/")
def home():
    country = request.args.get("country")
    source = request.args.get("source")
    
    return render_template("index.html", country=country, source=source)

@main.route("/about")
def about():
    context = {
        "name": "Atharva",
        "description": "Discover the fruits of my learning journey with this personal project, a playground where Python, HTML, and CSS come together. As a passionate learner, I've crafted this small project to explore and apply my newfound skills. Dive into the code and witness the foundations of web development taking shape. From Python's logic mastery to HTML's structural elegance and CSS's styling finesse, every line of code tells a story of growth and exploration. Join me in celebrating the joy of learning as I navigate the world of web development, one line at a time."
    }
    return render_template("about.html", context=context)

@main.route('/about-us')
def about_us():
    return redirect(url_for("main.about"))

@main.route("/contact")
def contact():
    return render_template("contact.html")

@main.route("/portfolio")
def portfolio():
    project_list = [
        {'name': 'Taskmate', 'description': 'This is the first project.', 'endpoint': 'taskmate'},
        {'name': 'Codebook', 'description': 'This is the second project.', 'endpoint': 'codebook'},
    ]
    return render_template("portfolio.html", projects=project_list)

@main.route("/portfolio/<project>")
def project(project):
    project_lst = ["taskmate", "codebook"]
    if project in project_lst:
        return render_template(f"portfolio/{project}.html")
    else:
        return redirect("/404")
    
@main.route("/portfolio/json")
def portfolio_json():
    projects = {
        "taskmate": {
            "language": "python",
            "framework": "django",
            "status": "completed"        
        },
        "codebook": {
            "language": "javascript",
            "framework": "react",
            "status": "learning"        
        }
    }    
    return jsonify(projects)

@main.route("/s")
def search():
    keyword = request.args.get("k")
    return f"{keyword}"
    
@main.route('/404')
def not_found_404():
    return render_template("404.html"), 404

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404   

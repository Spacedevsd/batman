from batman import Batman
from batman.template import Template

batman = Batman()
view = Template()

@batman.route("/characters")
def characters():
    context = {
        "name": "Alfred"
    }
    
    return view.render("characters.html", context)


if __name__ == "__main__":
    batman.run(port=4000, reloader=True)
from batman.template import Template
from batman import Batman


batman = Batman()
template = Template()


@batman.route("/character")
def characters():
    return template.render("character.html", {})


@batman.route("/city")
def city():
    context = {
        "name":  "Gothan City",
        "hero": "Batman"    
    }
    
    return template.render("city.html", context)

if __name__ == "__main__":
    batman.run(port=8000, reloader=True)

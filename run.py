from batman.template import Template
from batman import Batman


batman = Batman()


@batman.route("/character")
def characters():
    template = Template()
    return template.render("character.html", {})


@batman.route("/city")
def city():
    template = Template()
    
    context = {
        "name":  "Gothan City",
        "hero": "Batman"    
    }
    
    return template.render("city.html", context)

if __name__ == "__main__":
    batman.run(port=8000, reloader=True)

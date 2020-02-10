from batman.template import Template
from batman import Batman


batman = Batman()
view = Template()


@batman.route("/character")
def characters():
    return view.render("character.html", {})


@batman.route("/city")
def city():
    context = {
        "name":  "Gothan City",
        "hero": "Batman"
    }

    return view.render("city.html", context)

if __name__ == "__main__":
    batman.run(port=8000, reloader=True)

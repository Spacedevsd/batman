from batman.template import Template


def test_template_render():
    template = Template("tests/views")
    render = template.render("test.html", {})
    
    assert render == '<h1>test</h1>\n'
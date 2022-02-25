from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def generate_image():
    return render_template(template_name_or_list='index.html')

if __name__ == '__main__':
    app.run(debug=True)
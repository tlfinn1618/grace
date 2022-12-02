from flask import render_template
import config
from models import Church

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

@app.route("/")
def home():
    church = Church.query.all()
    return render_template("home.html", church=church)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
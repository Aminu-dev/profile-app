import os  # noqa: I001

from flask import Flask, redirect, render_template_string, request # type: ignore
from pymongo import MongoClient # pyright: ignore[reportMissingImports]

app = Flask(__name__)
profiles = MongoClient(os.environ["MONGO_URL"])["profile_db"]["profiles"]

PAGE = """
<h1>My Profile</h1>
<form method="post">
  Name: <input name="name" value="{{ p.get('name', '') }}"><br><br>
  Email: <input name="email" value="{{ p.get('email', '') }}"><br><br>
  Bio:<br><textarea name="bio" rows="4" cols="40">{{ p.get('bio', '') }}</textarea><br><br>
  <button type="submit">Save</button>
</form>
"""

@app.route("/", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        profiles.update_one(
            {"_id": "me"},
            {"$set": {k: request.form[k] for k in ("name", "email", "bio")}},
            upsert=True,
        )
        return redirect("/")
    return render_template_string(PAGE, p=profiles.find_one({"_id": "me"}) or {})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
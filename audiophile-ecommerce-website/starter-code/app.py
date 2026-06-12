from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import json
import os

app = Flask(__name__)
app.secret_key = "dev_key"


def load_users():
    if not os.path.exists("users.json"):
        return {}

    with open("users.json", "r") as file:
        return json.load(file)


def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)


technology = {
    "xx99-mark-1": {
        "id": 1,
        "name": "XX99 Mark I Headphones",
        "price": 1750,
        "description": "As the gold standard for headphones, the classic XX99 Mark I offers detailed and accurate audio reproduction for audiophiles, mixing engineers, and music aficionados alike in studios and on the go.",
        "features": "As the headphones all others are measured against, the XX99 Mark I demonstrates over five decades of audio expertise, redefining the critical listening experience. This pair of closed-back headphones are made of industrial, aerospace-grade materials to emphasize durability at a relatively light weight of 11 oz. From the handcrafted microfiber ear cushions to the robust metal headband with inner damping element, the components work together to deliver comfort and uncompromising sound. Its closed-back design delivers up to 27 dB of passive noise cancellation, reducing resonance by reflecting sound to a dedicated absorber. For connectivity, a specially tuned cable is included with a balanced gold connector.",
        "images": [
            "assets/product-xx99-mark-one-headphones/desktop/image-category-page-preview.jpg"
        ],
        "gallery": [
            "assets/product-xx99-mark-one-headphones/desktop/image-gallery-1.jpg",
            "assets/product-xx99-mark-one-headphones/desktop/image-gallery-2.jpg",
            "assets/product-xx99-mark-one-headphones/desktop/image-gallery-3.jpg"
        ],
        "box": ["1x Headphone Unit","2x Replacement Earcups","1x User Manual","1x 3.5mm 5m Audio Cable"]
    },

    "xx59": {
        "id": 2,
        "name": "XX59 Headphones",
        "price": 899,
        "description": "Enjoy your audio almost anywhere and customize it to your specific tastes with the XX59 headphones. The stylish yet durable versatile wireless headset is a brilliant companion at home or on the move.",
        "features": "These headphones have been created from durable, high-quality materials tough enough to take anywhere. Its compact folding design fuses comfort and minimalist style making it perfect for travel. Flawless transmission is assured by the latest wireless technology engineered for audio synchronization with videos.More than a simple pair of headphones, this headset features a pair of built-in microphones for clear, hands-free calling when paired with a compatible smartphone. Controlling music and calls is also intuitive thanks to easy-access touch buttons on the earcups. Regardless of how you use the XX59 headphones, you can do so all day thanks to an impressive 30-hour battery life that can be rapidly recharged via USB-C.",
        "images": [
            "assets/product-xx59-headphones/desktop/image-category-page-preview.jpg"
        ],
        "gallery": [
            "assets/product-xx59-headphones/desktop/image-gallery-1.jpg",
            "assets/product-xx59-headphones/desktop/image-gallery-2.jpg",
            "assets/product-xx59-headphones/desktop/image-gallery-3.jpg"
        ],
        "box": ["1x Headphone Unit","2x Replacement Earcups","1x User Manual","1x 3.5mm 5m Audio Cable"]
    },

    "xx99-mark-2": {
        "id": 3,
        "name": "XX99 Mark II Headphones",
        "price": 2999,
        "description": "The new XX99 Mark II headphones is the pinnacle of pristine audio. It redefines your premium headphone experience by reproducing the balanced depth and precision of studio-quality sound.",
        "features": "Featuring a genuine leather head strap and premium earcups, these headphones deliver superior comfort for those who like to enjoy endless listening. It includes intuitive controls designed for any situation. Whether you’re taking a business call or just in your own personal space, the auto on/off and pause features ensure that you’ll never miss a beat. The advanced Active Noise Cancellation with built-in equalizer allow you to experience your audio world on your terms. It lets you enjoy your audio in peace, but quickly interact with your surroundings when you need to. Combined with Bluetooth 5. 0 compliant connectivity and 17 hour battery life, the XX99 Mark II headphones gives you superior sound, cutting-edge technology, and a modern design aesthetic.",
        "images": [
            "assets/product-xx99-mark-two-headphones/desktop/image-category-page-preview.jpg"
        ],
        "gallery": [
            "assets/product-xx99-mark-two-headphones/desktop/image-gallery-1.jpg",
            "assets/product-xx99-mark-two-headphones/desktop/image-gallery-2.jpg",
            "assets/product-xx99-mark-two-headphones/desktop/image-gallery-3.jpg"
        ],
        "box": ["1x Headphone Unit","2x Replacement Earcups","1x User Manual","1x 3.5mm 5m Audio Cable","1x Travel Bag"]
    },

    "yx1-wireless": {
        "id": 4,
        "name": "YX1 Wireless Earphones",
        "price": 599,
        "description": "Tailor your listening experience with bespoke dynamic drivers from the new YX1 Wireless Earphones. Enjoy incredible high-fidelity sound even in noisy environments with its active noise cancellation feature.",
        "features": "Experience unrivalled stereo sound thanks to innovative acoustic technology. With improved ergonomics designed for full day wearing, these revolutionary earphones have been finely crafted to provide you with the perfect fit, delivering complete comfort all day long while enjoying exceptional noise isolation and truly immersive sound.The YX1 Wireless Earphones features customizable controls for volume, music, calls, and voice assistants built into both earbuds. The new 7-hour battery life can be extended up to 28 hours with the charging case, giving you uninterrupted play time. Exquisite craftsmanship with a splash resistant design now available in an all new white and grey color scheme as well as the popular classic black.",
        "images": [
            "assets/product-yx1-earphones/desktop/image-category-page-preview.jpg"
        ],
        "gallery": [
            "assets/product-yx1-earphones/desktop/image-gallery-1.jpg",
            "assets/product-yx1-earphones/desktop/image-gallery-2.jpg",
            "assets/product-yx1-earphones/desktop/image-gallery-3.jpg"
        ],
        "box": ["2x Earphone Unit","6x Multi-size Earplugs","1x User Manual","1x USB-C Charging Cable","1x Travel Pouch"]
    },

    "zx9-speaker": {
        "id": 5,
        "name": "ZX9 Speaker",
        "price": 4500,
        "description": "Upgrade your sound system with the all new ZX9 active speaker. It’s a bookshelf speaker system that offers truly wireless connectivity -- creating new possibilities for more pleasing and practical audio setups.",
        "features": "Connect via Bluetooth or nearly any wired source. This speaker features optical, digital coaxial, USB Type-B, stereo RCA, and stereo XLR inputs, allowing you to have up to five wired source devices connected for easy switching. Improved bluetooth technology offers near lossless audio quality at up to 328ft (100m). Discover clear, more natural sounding highs than the competition with ZX9’s signature planar diaphragm tweeter. Equally important is its powerful room-shaking bass courtesy of a 6.5” aluminum alloy bass unit. You’ll be able to enjoy equal sound quality whether in a large room or small den. Furthermore, you will experience new sensations from old songs since it can respond to even the subtle waveforms.",
        "images": [
            "assets/product-zx9-speaker/desktop/image-category-page-preview.jpg"
        ],
        "gallery": [
            "assets/product-zx9-speaker/desktop/image-gallery-1.jpg",
            "assets/product-zx9-speaker/desktop/image-gallery-2.jpg",
            "assets/product-zx9-speaker/desktop/image-gallery-3.jpg"
        ],
        "box": ["2x Speaker Unit","2x Speaker Cloth Panel","1x User Manual","1x 3.5mm 10m Audio Cable","1x 10m Optical Cable"]
    },

    "zx7-speaker": {
        "id": 6,
        "name": "ZX7 Speaker",
        "price": 3500,
        "description": "Stream high quality sound wirelessly with minimal to no loss. The ZX7 speaker uses high-end audiophile components that represents the top of the line powered speakers for home or studio use.",
        "features": "Reap the advantages of a flat diaphragm tweeter cone. This provides a fast response rate and excellent high frequencies that lower tiered bookshelf speakers cannot provide. The woofers are made from aluminum that produces a unique and clear sound. XLR inputs allow you to connect to a mixer for more advanced usage.The ZX7 speaker is the perfect blend of stylish design and high performance. It houses an encased MDF wooden enclosure which minimises acoustic resonance. Dual connectivity allows pairing through bluetooth or traditional optical and RCA input. Switch input sources and control volume at your finger tips with the included wireless remote. This versatile speaker is equipped to deliver an authentic listening experience.",
        "images": [
            "assets/product-zx7-speaker/desktop/image-category-page-preview.jpg"
        ],
        "gallery": [
            "assets/product-zx7-speaker/desktop/image-gallery-1.jpg",
            "assets/product-zx7-speaker/desktop/image-gallery-2.jpg",
            "assets/product-zx7-speaker/desktop/image-gallery-3.jpg"
        ],
        "box": ["1x Headphone Unit","2x Replacement Earcups","1x User Manual","1x 3.5mm 5m Audio Cable","1x 7.5m Optical Cable"]
    }
}


# ---------------- FIX: helper ----------------
def get_product_by_id(product_id):
    return technology.get(product_id)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/headphones")
def headphones():
    return render_template('headphones.html')


@app.route("/profile")
def profile():
    user_email = session.get("user")

    if not user_email:
        return redirect(url_for("login"))

    users = load_users()
    user = users.get(user_email)

    return render_template("profile.html", user=user)


@app.route("/techList")
def techList():
    return render_template("tech_list.html", technology=technology)


@app.route("/speakers")
def speakers():
    return render_template('speakers.html')


@app.route("/earphones")
def earphones():
    return render_template('earphones.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        users = load_users()

        email = request.form["email"]
        password = request.form["password"]

        if email in users and users[email]["password"] == password:
            session["user"] = email
            return redirect(url_for("home"))

        return "Invalid credentials"

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        users = load_users()

        first = request.form["first_name"]
        last = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm = request.form["confirm_password"]

        if password != confirm:
            return "Passwords do not match"

        if email in users:
            return "User already exists"

        users[email] = {
    "first": first,
    "last": last,
    "password": password,
    "balance": 5000
}

        save_users(users)

        session["user"] = email
        return redirect(url_for("home"))

    return render_template("register.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out")
    return redirect(url_for("home"))


@app.route("/checkout", methods=["POST"])
def checkout():
    user_email = session.get("user")

    if not user_email:
        return redirect(url_for("login"))

    users = load_users()
    user = users.get(user_email)

    if not user:
        return redirect(url_for("login"))

    if "balance" not in user:
        user["balance"] = 5000

    cart = session.get("cart", {})

    if not cart:
        return render_template("checkout.html", success=False, message="Cart is empty")

    total = sum(item["price"] * item["qty"] for item in cart.values())

    if user["balance"] < total:
        return render_template(
            "checkout.html",
            success=False,
            message="Not enough balance"
        )

    user["balance"] -= total
    users[user_email] = user
    save_users(users)

    session["cart"] = {}
    session.modified = True

    return render_template(
        "checkout.html",
        success=True,
        total=total,
        balance=user["balance"]
    )

@app.route("/remove-from-cart/<id>")
def remove_from_cart(id):
    cart = session.get("cart", {})

    if id in cart:
        del cart[id]
        session["cart"] = cart
        session.modified = True

    return redirect(url_for("cart"))

@app.route("/product/<product_id>")
def product(product_id):
    product = get_product_by_id(product_id)
    return render_template("product.html", product=product)


@app.route("/cart")
def cart():
    cart_items = session.get("cart", {})
    total = sum(item["price"] * item["qty"] for item in cart_items.values())

    user_email = session.get("user")

    users = load_users()
    user = users.get(user_email) if user_email else None

    if user is None:
        user = {"balance": 0}

    return render_template(
        "cart.html",
        cart=cart_items,
        total=total,
        user=user
    )

@app.route("/product/<product_id>/add-to-cart", methods=["POST"])
def add_to_cart(product_id):
    data = request.get_json()
    qty = int(data.get("qty", 1))

    product = get_product_by_id(product_id)

    if not product:
        return jsonify({"success": False}), 404

    if "cart" not in session:
        session["cart"] = {}

    cart = session["cart"]
    pid = str(product_id)

    if pid in cart:
        cart[pid]["qty"] += qty
    else:
        cart[pid] = {
            "name": product["name"],
            "price": product["price"],
            "qty": qty
        }

    session["cart"] = cart
    session.modified = True

    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
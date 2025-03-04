# Flask MVC Framework 🚀

A lightweight **Flask MVC (Model-View-Controller)**  with built-in **authentication, RBAC, REST API, and Bootstrap UI**.

---

## 🎯 **Features**
✅ MVC architecture (Models, Views, Controllers)  
✅ Bootstrap-integrated UI  
✅ Authentication (Login, Signup, SSO)  
✅ Role-Based Access Control (RBAC)  
✅ REST API support  
✅ Flask-Jinja2 templating  
✅ Modular and scalable project structure  

---

## 🏗 **Project Structure**
flask-mvc/ │ ├── app/ │ ├── init.py │ ├── models/ # Database models (User, Roles, etc.) │ ├── controllers/ # Business logic controllers │ ├── views/ # Frontend templates & static files │ │ ├── layouts/ # Base templates (header, footer) │ │ ├── auth/ # Authentication views (Login, Signup) │ │ ├── common/ # Common UI components │ │ ├── home/ # Home page templates │ │ └── static/ # CSS, JS, Images │ ├── services/ # Business logic services │ ├── utils/ # Helper utilities │ ├── tests/ # Unit tests ├── config.py # Configuration settings ├── requirements.txt # Python dependencies ├── run.py # Entry point to run Flask app ├── .gitignore # Git ignored files └── README.md # Project documentation

yaml
Copy
Edit

---

## 🛠 **Setup & Installation**
### 1️⃣ Clone the repository  
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/flask-mvc.git
cd flask-mvc
2️⃣ Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the Flask App
bash
Copy
Edit
python run.py
5️⃣ Open in Browser
Home Page → http://127.0.0.1:5000/
Login Page → http://127.0.0.1:5000/auth/login
Signup Page → http://127.0.0.1:5000/auth/signup
🔑 Authentication & RBAC
The project includes user authentication and role-based access control (RBAC):

Users can register and log in.
Roles are managed to control access.
🔐 SSO (Single Sign-On) Support
SSO can be integrated via OAuth, Google Auth, or JWT-based authentication.

🛠 API Endpoints
Method	Endpoint	Description
GET	/api/users	Get all users
POST	/api/users/signup	User signup
POST	/api/users/login	User login
GET	/api/projects	Get all projects
🎨 UI Screenshots
📌 Home Page

📌 Login Page

📌 License
This project is licensed under the MIT License.

⭐ Contribute
We welcome contributions!

Fork the repo
Create a feature branch
Submit a pull request
📬 Contact
💡 Developer: YOUR_NAME
📧 Email: your.email@example.com
🌍 GitHub: YOUR_GITHUB_USERNAME

🎉 Enjoy building with Flask MVC! 🚀🔥

yaml
Copy
Edit

---

## ✅ **Next Steps**
1. **Save this file as `README.md`** in your project.  
2. **Commit & Push to GitHub**:  
   ```bash
   git add README.md
   git commit -m "Added README file"
   git push origin main
Now your project looks professional on GitHub! 🚀🔥
Let me know if you need any changes! 😃
-----------------------------


# 📖 **Flask MVC Framework Documentation** 🚀  

## 📌 **Overview**  
This Flask-based **MVC (Model-View-Controller) framework** provides a structured approach to building scalable web applications. It follows **Ruby on Rails-style MVC**, supports **authentication, RBAC, REST APIs**, and integrates **Bootstrap for UI**.  

---

## 📂 **Project Structure**  

```
flask-mvc/
│
├── app/
│   ├── __init__.py
│   ├── models/          # Database models
│   ├── controllers/     # Business logic controllers
│   ├── views/           # Frontend templates & static files
│   │   ├── layouts/     # Base templates (header, footer)
│   │   ├── auth/        # Authentication views (Login, Signup)
│   │   ├── common/      # Common UI components
│   │   ├── home/        # Home page templates
│   │   └── static/      # CSS, JS, Images
│   ├── services/        # Business logic services
│   ├── utils/           # Helper utilities
│
├── tests/               # Unit tests
├── config.py            # Configuration settings
├── requirements.txt     # Python dependencies
├── run.py               # Entry point to run Flask app
├── .gitignore           # Git ignored files
└── README.md            # Project documentation
```

---

## 🎯 **How Does the MVC Framework Work?**  

- **Models (`app/models/`)** → Handles database structure & queries.  
- **Views (`app/views/`)** → Frontend UI (HTML, Jinja2 templates).  
- **Controllers (`app/controllers/`)** → Manages app logic & routes.  

---

# 📌 **How to Add a New Page in Flask MVC?**  

Let’s say you want to add a **"Dashboard"** page. Follow these steps:

---

## ✅ **Step 1: Create the View (UI)**  
📌 **Location:** `app/views/dashboard/index.html`  

```html
{% extends 'layouts/base.html' %}

{% block content %}
    <div class="container">
        <h1>Dashboard</h1>
        <p>Welcome to your dashboard!</p>
    </div>
{% endblock %}
```

- It **extends** `layouts/base.html`, ensuring a **consistent UI**.  
- The `content` block **injects content dynamically** into the base layout.

---

## ✅ **Step 2: Create the Controller**  
📌 **Location:** `app/controllers/dashboard_controller.py`  

```python
from flask import Blueprint, render_template

dashboard_blueprint = Blueprint("dashboard", __name__)

@dashboard_blueprint.route("/dashboard")
def dashboard_home():
    """Render the dashboard page"""
    return render_template("dashboard/index.html")
```

- The **Blueprint** defines the `dashboard` module.  
- The `dashboard_home()` function **renders** the UI.  
- The route `/dashboard` **maps** to the `index.html` template.

---

## ✅ **Step 3: Register the Controller in `run.py`**  
📌 **Location:** `run.py`  

```python
from flask import Flask
from app.controllers.dashboard_controller import dashboard_blueprint

app = Flask(__name__)

# Register routes
app.register_blueprint(dashboard_blueprint, url_prefix="")

if __name__ == "__main__":
    app.run(debug=True)
```

- The `dashboard_blueprint` is **registered** in the Flask app.  
- The `url_prefix=""` makes `/dashboard` directly accessible.  

---

## ✅ **Step 4: Add a Link in the Navigation Bar**  
📌 **Location:** `app/views/layouts/header.html`  

```html
<nav>
    <a href="/">Home</a>
    <a href="/dashboard">Dashboard</a>
</nav>
```

- The **navbar links** now include **Dashboard**.

---

## ✅ **Step 5: Run the Application**
Start the Flask server:
```bash
python run.py
```
Now visit:  
🔗 **[http://127.0.0.1:5000/dashboard](http://127.0.0.1:5000/dashboard)**  

---

# 🎯 **Additional Features**
Want to enhance the framework?  
- **Database Integration:** Add models in `app/models/`.  
- **APIs:** Use `Flask-RESTful` for building APIs.  
- **Authentication:** Extend the `auth` module for login & signup.  
- **RBAC:** Control access by user roles.  
- **Docker Deployment:** Deploy using `Docker` and `AWS`.  

---

# 📌 **Final Thoughts**
This framework ensures:  
✅ **Organized code structure**  
✅ **Scalability with MVC principles**  
✅ **Reusable UI with Bootstrap & Jinja2**  
✅ **API integration for flexibility**  



# 🚀 NutriSmart AI

### Personalized Nutrition Meets Smart Technology

---

## 🧠 Overview

**NutriSmart AI** is an advanced, user-centric web application that empowers individuals to take control of their health through personalized nutrition insights and intelligent wellness tools. Powered by the **CalorieNinjas API** and integrated with a robust, modern tech stack, NutriSmart AI delivers a smooth, engaging experience for:

* Meal tracking and nutritional breakdowns
* BMI calculation and health feedback
* Calorie goal planning
* AI-generated health advice

With a clean interface built using **Streamlit**, NutriSmart AI also supports **premium subscriptions via Stripe**, offering a comprehensive health management ecosystem.

---

## 🔑 Key Features

* **🥗 Meal Analysis**
  Analyze meals for **calories, protein, fats, and carbs** using intuitive visualizations powered by Plotly.

* **📏 BMI Calculator**
  Calculate your **Body Mass Index** and get categorized feedback along with actionable health recommendations.

* **📜 Meal History Tracking**
  Log meals with timestamps, track historical data, download records as CSV, and visualize trends over time.

* **🔥 Calorie Goal Planner**
  Set daily goals and track real-time progress with dynamic progress bars and actionable insights.

* **💡 AI-Powered Health Tips**
  Get curated health tips and input personalized advice tailored to your health profile.

* **⭐ Premium Subscription**
  Unlock advanced features such as:

  * In-depth nutritional analytics
  * AI-driven meal suggestions
  * SMS reminders
  * Available via secure **Stripe** payment integration

* **📱 Responsive Design**
  Enjoy a sleek, modern UI with **streamlit-option-menu** for elegant and intuitive navigation.

---

## ⚙️ Tech Stack

* **Language**: Python 3.13
* **Virtual Environment**: Managed with `uv`
* **Frontend**: Streamlit
* **Backend**: Flask + Flask-SQLAlchemy + Flask-Migrate

### 🔌 API Integrations

* **CalorieNinjas API** — for nutritional data
* **Stripe API** — for secure payments

### 📦 Libraries Used

* `flask` — Backend web framework
* `streamlit` — Frontend development
* `plotly` — Interactive data visualizations
* `requests` — API integration
* `pillow` — Image handling
* `streamlit-option-menu` — Custom nav menu
* `flask-cors`, `CORS` — Cross-Origin support
* `python-dotenv` — Manage environment variables
* `flask-sqlalchemy` — ORM for DB operations
* `flask-migrate` — DB migrations
* `stripe` — Stripe payment processing

### 🗃️ Database

* Default: **SQLite**
* Easily extensible to: **PostgreSQL**, etc.

---

## 🚀 Installation Guide

### ✅ Prerequisites

* Python 3.13
* `uv` for virtual environment
* CalorieNinjas API key
* Stripe account with payment link
* Git

### ⚙️ Setup Instructions

1. **Clone Repository**

   ```bash
   git clone https://github.com/HamzaImtiaz03/NutriSmart-AI
   ```

2. **Create Virtual Environment**

   ```bash
   uv venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   uv add -r requirements.txt
   ```

4. **Configure .env**

   ```env
   CALORIE_NINJAS_API_KEY=your_calorieninjas_api_key
   STRIPE_PREMIUM_URL=https://buy.stripe.com/your_stripe_payment_link
   FLASK_ENV=development
   ```

5. **Initialize Database**

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Run the App**

   ```bash
   streamlit run backend/app.py
   ```

Access the app at **[http://localhost:8501](http://localhost:8501)**

---

## 🎯 Usage Overview

* **Meal Analysis**
  Input meals (e.g., `"100g grilled chicken, 1 cup rice"`) to get macro breakdowns and pie charts.

* **BMI Calculator**
  Enter weight and height to receive BMI and health feedback.

* **Meal History**
  Review logged meals, download CSV, and visualize nutrition trends.

* **Calorie Planner**
  Set and track daily calorie intake with real-time visualization.

* **Health Tips**
  Browse or add personalized advice for smarter eating habits.

* **Premium Access**
  Subscribe via Stripe to unlock **analytics, AI meal planning, and SMS alerts**.

---

## 🌍 Deployment Guide

Deploy NutriSmart AI to platforms like **Heroku**, **AWS**, or **Render**.

### Deployment Checklist:

* Set up Python 3.13 + uv
* Add `.env` variables to dashboard
* Ensure database is initialized
* Run:

  ```bash
  streamlit run backend/app.py
  ```

Check platform-specific docs for more deployment instructions.

---

## 🛠️ Development Notes

* **Navigation**: Use `streamlit-option-menu` for customizable UI.
* **Persistence**: Use `st.session_state` for temp data, and SQLAlchemy for long-term storage.
* **Security**: Store sensitive keys in `.env`. Enable CORS for Flask APIs.
* **Extensibility**: Easily integrate new APIs or cloud services for scaling.

---

## 🧭 Roadmap

* **v1.1** – Integrate AI-generated meal suggestions
* **v1.2** – Add user authentication
* **v1.3** – Enable premium nutritional analytics
* **v2.0** – Launch mobile app with push notifications
* **v2.1** – Add multilingual support + accessibility enhancements

---

## 🐞 Troubleshooting

* **API Errors**: Check `.env` for valid API keys
* **Install Issues**: Run `uv pip install -r requirements.txt`
* **Database Errors**: Re-run `flask db upgrade`
* **Stripe Issues**: Confirm payment link is working
* **Streamlit Bugs**: Run `streamlit cache clear`

---

## 🤝 Contributing

We welcome contributions!

1. Fork the repo
2. Create your branch:

   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit and push:

   ```bash
   git commit -m "Add new feature"
   git push origin feature/your-feature
   ```
4. Open a pull request with a clear description.

Make sure to follow the **Code of Conduct** and ensure clean code with proper tests.

---

## 📜 License

Licensed under the **MIT License**. See `LICENSE` file for details.

---

## 🙏 Acknowledgements

* **CalorieNinjas** – For providing high-quality nutritional data
* **Streamlit Community** – For libraries and frontend support
* **Stripe** – For payment processing
* **Open Source Contributors** – For building the tools that make this project possible

---

## 📬 Contact

* **Email**: [hamzaimtiaz8668@gmail.com](mailto:hamzaimtiaz8668@gmail.com)
* **GitHub**: [NutriSmart AI Issues](https://github.com/HamzaImtiaz03/NutriSmart-AI)

---

© 2025 NutriSmart AI — All rights reserved.


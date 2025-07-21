## 📚 Academic Grade Optimizer

A Streamlit-based web app that predicts a student's final exam grade using academic and lifestyle inputs. Built with an enhanced linear regression model, it offers real-time feedback and performance visualization.

---

## 🚀 Key Features

- 🎯 **Grade Prediction** — Based on past performance, study hours, attendance, and sleep.
- 🖱️ **Interactive Sliders** — Intuitive controls for quick inputs.
- 📊 **Visual Insights** — Bar chart comparison of predicted grade, past score, and target.
- 💬 **Personalized Feedback** — Displays letter grade and suggestions.
- 🎨 **Custom Styling** — Responsive layout with horizontal sliders and styled dividers.

---

## 🧠 Machine Learning Behind It

Powered by `scikit-learn`'s **Linear Regression**, improved with:

- ✅ **Refined Training Data** — More realistic and representative samples.
- 🔄 **Sleep² Feature** — Captures non-linear effects of sleep using a quadratic term.
- 🧩 **Grade Clipping** — Ensures predictions stay between 0% and 100%.

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.7+
- `streamlit`, `numpy`, `matplotlib`, `scikit-learn`

### Installation

```bash
pip install streamlit numpy matplotlib scikit-learn
```

### Run the App

```bash
streamlit run appModifiedFnl1.py
```

Open the browser at `http://localhost:8501` and start predicting!

---

## 🧭 Future Roadmap

- 🔁 Use of larger, real-world datasets for better accuracy.
- 🤖 Integration of advanced models (Random Forest, SVR, MLP).
- 🛠️ Hyperparameter tuning for optimized performance.

---

> 🎓 Designed to support students, educators, and data science enthusiasts.  
> 📬 Contributions welcome!

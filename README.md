# AcadKo  
#### Video Demo:  <URL HERE>  
#### Description:  
AcadKo is a student-powered academic marketplace built by students, for students. It provides a safe platform for students in the Philippines—especially those under 18 who are often excluded from formal work—to offer and request academic services. These services include essay writing, tutoring, presentation creation, problem-solving, and more. AcadKo empowers young learners to monetize their academic skills, connect with peers, and gain valuable experience in a supportive community.

---

## 🔍 Overview

AcadKo connects students who need academic assistance with talented peers offering a variety of services. These services include writing and editing academic papers, creating multimedia presentations, tutoring in various subjects, developing study guides and reviewers, and assisting with research projects. The platform is designed to be simple and user-friendly, with a strong focus on user safety and responsible collaboration.

The target audience is students under 18 years old in the Philippines who are often restricted from formal employment but want to earn through their academic skills. By providing a dedicated space for academic services, AcadKo fosters a community where students can learn from one another and grow their skills while earning income.

---

## 🤝 Contributing

Contributions are welcome! Please contact me first at **painganedrienejames@gmail.com** before submitting any pull requests or making changes. This project is currently a prototype, and many features are still under development. Your feedback and help are appreciated to make AcadKo better.

---

### 🛠 Tech Stack

The application uses Python and Flask as the backend framework to handle web routing, sessions, and database interaction. The frontend utilizes HTML, CSS, and Bootstrap for responsive, accessible UI design. SQLite serves as a lightweight local database for managing users, service posts, and other data. Flask sessions track login status and user activity, while Jinja2 powers dynamic HTML templates.

---

### 📁 Database Design

AcadKo’s database is designed with simplicity and scalability in mind. Key tables include:

- **users**: stores user information such as username, email, password hash, profile description, and optional fields like LinkedIn URL, skills, certifications, and experience.
- **posts**: represents service listings with fields for user_id (linking to the poster), service_title, description, category, price, and timestamps.
- Future tables may include messaging, order tracking, and coin balance for an internal currency system.

This structure allows for fast queries, easy user management, and simple integration of future features.

---

### 📋 Key Features

- Secure user registration and login, with password hashing using industry-standard methods to protect user credentials.
- Posting, browsing, and managing academic service listings categorized by service type.
- User dashboards showing a personalized feed of their posts and profile information.
- Profile editing options including contact info, experience, and skills.
- Responsive UI that adapts to desktops and mobile devices.
- Planned future features such as in-platform messaging, a coin-based transaction system, order tracking, and admin moderation tools.

---

### 🔐 Security & Privacy

Security is a key priority for AcadKo. Passwords are securely hashed using `werkzeug.security` methods before storage. User sessions are managed carefully to prevent unauthorized access. Input sanitization and parameterized SQL queries protect against injection attacks. The platform respects user privacy and does not share personal data without consent.

---

### 🚀 Getting Started Locally

To set up AcadKo locally, clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/acadko.git
cd acadko
pip install -r requirements.txt
flask run

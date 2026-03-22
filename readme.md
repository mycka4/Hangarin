# Hangarin — Task Management System

**Hangarin** is a Django-based Task Management System designed to help organize daily activities by managing Tasks, SubTasks, Notes, Categories, and Priorities. It provides a structured and intuitive interface to improve productivity, backed by Django's powerful admin dashboard.

---

## Features / Key Functionalities

###  Task Management
- Create, edit, and delete tasks with deadlines and status tracking.
- Filter tasks by status, priority, category, and sort order.

###  SubTask Support
- Break down tasks into smaller, manageable subtasks.
- Track subtask status independently from the parent task.

###  Notes
- Add notes for additional context or reminders related to tasks.
- Search and filter notes by content or date.

###  Categories & Priorities
- Categorize tasks (e.g., Work, School, Personal, Projects).
- Assign priorities (e.g., High, Medium, Low, Critical).

###  Authentication (Google OAuth)
- Secure login via Google using `django-allauth`.
- Supports both username/password and Google social login.

###  Admin Dashboard (Django Admin)
- Secure admin login at `/admin/`.
- Search, filter, and organize all models easily.

###  Fake Data Generator
- Generate test Categories, Tasks, SubTasks, and Notes using `Faker`.
- Useful for testing and demonstration purposes.

---

## Color Theme Inspiration

The overall color theme of Hangarin was inspired by this palette:

![Color Palette](color_palette.jpg)

| Color | Hex | Usage |
|---|---|---|
| Dark Navy | `#1D1A39` | Sidebar background |
| Dark Purple | `#451952` | Logo header |
| Dark Rose | `#662549` | Primary buttons, active nav |
| Rose Mauve | `#AE445A` | Secondary buttons, delete |
| Amber | `#F39F5A` | Accent, active nav indicator |
| Light Blush | `#E8BCB9` | Background tones |

> Although a ready dashboard template was used, **no structural styles were changed** — only the color theme was modified to match this palette.

---

## Dashboard Templates

Hangarin uses **two dashboard frameworks**:

### 1. Ready Bootstrap Dashboard
> 🔗 [Ready Bootstrap by ThemeKita](https://github.com/themekita/ready-bootstrap-dashboard)

The first CSS framework used was **Ready Bootstrap**, originally carried over from a previous project (PSUSphere). The `static/` folder from that project was kept intact — no files were deleted — so some components and designs are shared between the two projects.

### 2. CoolAdmin Dashboard *(current)*
> 🔗 [CoolAdmin by puikinsh](https://github.com/puikinsh/CoolAdmin)

The final dashboard used is **CoolAdmin**, a clean and responsive Bootstrap 5 admin template. Its static files are placed inside `static/statics/` to avoid conflicts with the existing Ready Bootstrap files. Only `theme.css` was customized to apply the color palette above.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python + Django | Backend framework |
| Bootstrap 5 (CoolAdmin) | Frontend UI |
| django-allauth | Authentication & Google OAuth |
| SQLite | Database |
| Faker | Test data generation |
| PythonAnywhere | Deployment |


## Deployment

Hangarin is deployed on **PythonAnywhere**:
> 🌐 [mymy4.pythonanywhere.com](https://mymy4.pythonanywhere.com)

---

## Project Structure

```
Hangarin/
    hangarin/
        tasks/          ← Models, Views, URLs and other files
        templates/      ← HTML Templates
        static/         ← Ready Bootstrap static files (from PSUSphere)
            statics/    ← CoolAdmin static files
        hangarin/       ← Settings, URLs
        manage.py
```

---

## Notes on Static Files

> The `static/` folder retains the original **Ready Bootstrap** files from a previous project. The **CoolAdmin** files are placed inside `static/statics/` as a subfolder. Both are registered in `STATICFILES_DIRS` so Django can serve both.

---


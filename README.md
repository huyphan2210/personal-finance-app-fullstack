# Personal Finance App

A full-stack web application built with:

- **Frontend**: TypeScript, Vue 3, Nuxt
- **Backend**: Python 3 with Flask, SQLAlchemy as the ORM
- **Database**: PostgreSQL

## Live URL: [Personal Finance App](https://personal-finance-app-fullstack.vercel.app/overview)

## Prerequisites

Ensure you have the following installed:

- **Git** – [Download](https://git-scm.com/downloads)
- **Node.js** (Latest LTS version) – [Download](https://nodejs.org/)
- **Yarn** (or npm) – [Download](https://yarnpkg.com/)
- **Python 3** – [Download](https://www.python.org/downloads/release/python-3137/)
- **PostgreSQL** (Latest stable version) – [Download](https://www.postgresql.org/download/)

---

## Local Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/huyphan2210/personal-finance-app-fullstack.git
cd personal-finance-app-fullstack
````

---

## Frontend Setup (Vue 3 + Nuxt)

### Install Dependencies

```sh
cd client
yarn install  # or npm install
```

### Create a `.env` file for Clerk API

This application uses [Clerk](https://clerk.com/) for authentication.
You’ll need to create an account on Clerk and add the keys to your `.env` file.
See more info here: [Clerk API Key](https://clerk.com/glossary/api-key)

```env
NUXT_PUBLIC_CLERK_PUBLISHABLE_KEY=<YOUR_CLERK_PUBLISHABLE_KEY>
NUXT_CLERK_SECRET_KEY=<YOUR_CLERK_SECRET_KEY>
```

### Start the Frontend

```sh
yarn dev  # or npm run dev
```

The app should now be running at `http://localhost:3000/`.

---

## Backend Setup (Python 3 with Flask)

### Create the `financedb` database in PostgreSQL

```sql
CREATE DATABASE financedb;
```

### Install `pipenv`

```sh
py -m pip install pipenv   # Windows
python3 -m pip install pipenv   # macOS/Linux
```

### Install Dependencies

Create a virtual environment:

```sh
cd server
pipenv shell
```

Then install dependencies:

```sh
pipenv install
```

### Start the Backend

```sh
pipenv run python app.py
```

The server should now be running at `http://127.0.0.1:5000`.

---

## Deployment

* **Frontend**: Deployed on Vercel (or Netlify).
* **Backend**: Deployable on Heroku, Azure, or GCP.
* **Database**: Use a managed PostgreSQL service (e.g., Supabase, Railway, Render).

```

<h1>Cyber Security Base: Project 1</h1>

This is a simple application where you can register, login and add notes to the website.

I used the OWASP Top 10 Application Security Risks [2017](https://owasp.org/www-project-top-ten/2017/Top_10.html).

<h3>PostgreSQL</h3>

This project uses PostgreSQL. If not installed, please install it. Below simple instructions for Linux Ubuntu, Cubbli Linux, Mac and Windows. Detailed instructions at https://www.postgresql.org/download/

Linux, Ubuntu:
>sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
>
>wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
>
>sudo apt-get update
>
>sudo apt-get -y install postgresql

Mac:
> brew install postgresql

Cubbli Linux, UOH department of computer science lab computer / fuksiläppäri:
https://github.com/hy-tsoha/local-pg

Windows:
download installer from https://www.postgresql.org/download/windows/

<h3>Poetry</h3>

If you do not have poetry installed, please install it via https://python-poetry.org/docs/#installation

<h1> Instructions for the project</h1>

- Clone the project

- Create a ".env" file and enter in it the following information:
  
> DATABASE_URL="postgresql:///your_database"
>
> SECRET_KEY="your_secret_key"

- Install the project dependencies:
> poetry install --no-root

- Open your PostgreSQL connection and if needed, create a new database:
> createdb your_database

- Define database tables in terminal:
> psql your_database < schema.sql

- Run the application:
> poetry run invoke start

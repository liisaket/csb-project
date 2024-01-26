<h2>Cyber Security Base: Project 1</h2>

I used the OWASP Top 10 Application Security Risks 2017:
https://owasp.org/www-project-top-ten/2017/Top_10.html

<h3>Instructions for using locally:</h3>

- Clone the project

- Create a ".env" file and enter in it the following information:
> DATABASE_URL="postgresql:///your_database"
> SECRET_KEY="your_secret_key"

- Install the project dependencies:
> poetry install --no-root

- Install PostgreSQL:

Linux, Ubuntu:
>sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
>wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
>sudo apt-get update
>sudo apt-get -y install postgresql

Cubbli Linux, UOH department of computer science lab computer / fuksiläppäri:
https://github.com/hy-tsoha/local-pg

Mac:
brew install postgresql

Windows:
download installer from https://www.postgresql.org/download/windows/

More details and installation requirements: https://www.postgresql.org/download/

- Define database tables in terminal:
> psql your_database < schema.sql

- Run the application:
> poetry run invoke start
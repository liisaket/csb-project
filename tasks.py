from invoke import task

@task
def start(ctx):
    ctx.run("poetry run flask --app app.py run")
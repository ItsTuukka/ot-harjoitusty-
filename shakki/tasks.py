from invoke import task

@task
def start(ctx):
	ctx.run('python3 src/index.py')

@task
def test(ctx):
	ctx.run('pytest')
	
@task
def coverage(ctx):
	ctx.run('coverage run --branch -m pytest src')
	
@task(coverage)
def coverage_report(ctx):
	ctx.run('coverage html')
	

@task
def lint(ctx):
	ctx.run('pylint src')

@task
def initialize_db(ctx):
    ctx.run('python3 src/initialize_db.py')

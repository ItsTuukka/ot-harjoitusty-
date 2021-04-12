from invoke import task

@task
def start(ctx):
	ctx.run('python3 src/main.py')

@task
def test(ctx):
	ctx.run('pytest')
	
@task
def coverage(ctx):
	ctx.run('coverage run --branch -m pytest')
	
@task(coverage)
def coverage_report(ctx):
	ctx.run('coverage report -m')
	
@task(coverage)
def coverage_html(ctx):
	ctx.run('coverage html')


import nox

@nox.session
def format(session):
    """
    Format all project files in place
    """
    session.install('isort', 'yapf')
    session.run('isort', 'blog')
    session.run('yapf', '-ir', 'blog')

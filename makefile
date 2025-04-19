
MIGRATION_MSG ?= "autogenerate"

baseDB:
	source fast/bin/activate && PYTHONPATH=. sqlacodegen postgresql+psycopg2://jolo@localhost/study --outfile server/models/generated_models.py
migrate:
	source fast/bin/activate && PYTHONPATH=. alembic -c server/alembic.ini upgrade head
makemigration:
	source fast/bin/activate && PYTHONPATH=. alembic -c server/alembic.ini revision --autogenerate -m "$(MIGRATION_MSG)"
downgrade:
	source fast/bin/activate && PYTHONPATH=. alembic -c server/alembic.ini downgrade -1
history:
	source fast/bin/activate && PYTHONPATH=. alembic -c server/alembic.ini history --verbose




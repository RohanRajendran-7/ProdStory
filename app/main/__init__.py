"""Package-level glue for the `main` blueprint.

Expose the blueprint object created in `routes.py` so the application
registers the blueprint that actually has the route handlers.
"""

# Import the blueprint instance from routes.py (routes defines `main_bp`)
from .routes import main_bp

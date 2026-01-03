"""Package-level glue for the `auth` blueprint.

Expose the blueprint object created in `routes.py` so the application
registers the blueprint that actually has the route handlers.
"""

# Import the blueprint instance from routes.py (routes defines `auth_bp`)
from .routes import upload_bp

import os

# ======================
# TripAdvisor API Config
# ======================

API_KEY = os.environ("TRIPADVISOR_API_KEY")
API_URL = "https://api.content.tripadvisor.com/api/v1/"

LOCATION_SEARCH = "location/search"
LOCATION_REVIEWS = "location/{location_id}/reviews"

from JWST_IMAGE_MAKER import make_image
from JWST_IMAGE_MAKER.Astroquery_jwst import get_query_data

def test_get_query_data():
    astro_object='M17'
    get_query_data(astro_object)

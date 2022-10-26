from app.tests import client


def test_landing(client):
    landing = client.get("/")
    html = landing.data.decode()

    # check that key text for this page appears in the returned html
    assert '<p class="featured-text">Find your best nest.</p>' in html

    assert landing.status_code == 200


def test_landing_aliases(client):
    landing = client.get("/")
    assert client.get("/home").data == landing.data
    assert client.get("/about").data == landing.data


def test_map(client):
    landing = client.get("/map")
    html = landing.data.decode()

    # check that key text for this page appears in the returned html
    assert '<div id="map-section">' in html

    assert landing.status_code == 200


def test_privacy(client):
    landing = client.get("/privacy-policy")
    html = landing.data.decode()

    # check that key text for this page appears in the returned html
    assert '<h2 class="title">Privacy Policy</h2>' in html

    assert landing.status_code == 200


def test_data(client):
    landing = client.get("/data")
    html = landing.data.decode()

    # check that key text for this page appears in the returned html
    assert '<h2 class="title">Data</h2>' in html

    assert landing.status_code == 200


def test_news(client):
    landing = client.get("/news")
    html = landing.data.decode()

    # check that key text for this page appears in the returned html
    assert '<h2 class="title">News</h2>' in html

    assert landing.status_code == 200


def test_help(client):
    landing = client.get("/help")
    html = landing.data.decode()

    # check that key text for this page appears in the returned html
    assert '<h2 class="title">Help and FAQ</h2>' in html

    assert landing.status_code == 200


def test_terms(client):
    landing = client.get("/terms-and-conditions")
    html = landing.data.decode()

    # check that key text for this page appears in the returned html
    assert '<h2 class="title">Terms & Conditions</h2>' in html

    assert landing.status_code == 200
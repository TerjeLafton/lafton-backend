import json


def test_read_album(test_app_with_db):
    album = test_app_with_db.post(
        "/api/albums/",
        data=json.dumps(
            {
                "title": "Abbey Road",
                "artist": "The Beatles",
                "year": 1969,
                "image_url": "https://upload.wikimedia.org/wikipedia/en/4/42/Beatles_-_Abbey_Road.jpg",
            }
        ),
    )
    response = test_app_with_db.get("/api/albums/Abbey Road")

    assert response.status_code == 200
    assert response.json() == album.json()


def test_read_all_albums(test_app_with_db):
    test_app_with_db.post(
        "/api/albums/",
        data=json.dumps(
            {
                "title": "Abbey Roads",
                "artist": "The Beatles",
                "year": 1969,
                "image_url": "https://upload.wikimedia.org/wikipedia/en/4/42/Beatles_-_Abbey_Road.jpg",
            }
        ),
    )
    response = test_app_with_db.get("/api/albums/")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 1


def test_create_album(test_app_with_db):
    expected_response = {
        "title": "Abbey Road",
        "artist": "The Beatles",
        "year": 1969,
        "image_url": "https://upload.wikimedia.org/wikipedia/en/4/42/Beatles_-_Abbey_Road.jpg",
    }
    response = test_app_with_db.post(
        "/api/albums/",
        data=json.dumps(
            {
                "title": "Abbey Road",
                "artist": "The Beatles",
                "year": 1969,
                "image_url": "https://upload.wikimedia.org/wikipedia/en/4/42/Beatles_-_Abbey_Road.jpg",
            }
        ),
    )

    assert response.status_code == 201
    assert response.json() == expected_response


def test_create_album_missing_json(test_app):
    response = test_app.post("/api/albums/", data=json.dumps({}))

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "title"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "artist"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "year"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "image_url"],
                "msg": "field required",
                "type": "value_error.missing",
            },
        ]
    }

class TestTourPackagesData:
    post_tour_package = {
        "id": 1,
        "name": "Netherlands expo",
        "description": "This tour is fascinating, please enjoy it",
        "price": 100,
        "destinations": [
            {
                "tour_package": 2,
                "location": "Kampala A",
                "tour_type": "Scary",
                "danger_type": "Medium"
            },
            {
                "tour_package": 2,
                "location": "Kampala A",
                "tour_type": "Scary",
                "danger_type": "Medium"
            }
        ],
        "available_dates": [
            {
                "date_available": "2020-07-09",
                "tour_package": 2
            }
        ],
        "capacity": 2
    }

    updated_tour_package = {
        "id": 1,
        "name": "Europe tour",
        "description": "Enjoy the tour experiecne",
        "price": 20,
        "destinations": [
            {
                "tour_package": 1,
                "location": "Kampala A",
                "tour_type": "Scary",
                "danger_type": "Medium"
            },
            {
                "tour_package": 1,
                "location": "Kampala A",
                "tour_type": "Scary",
                "danger_type": "Medium"
            }
        ],
        "available_dates": [
            {
                "date_available": "2020-07-09",
                "tour_package": 2
            }
        ],
        "capacity": 1
    }

    user_name = "tour"
    user_email = "tour@gmail.com"
    first_name = "tour"
    last_name = "package"
    password = "466488Ll "

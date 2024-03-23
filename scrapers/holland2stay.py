import requests

from datetime import datetime
from telegram.bot_handler import direct_message

from core.settings import settings
from utiles.city import City


def graphql_request(city: City):
    url = "https://api.holland2stay.com/graphql/"
    headers = {
        "Accept-Language": "en",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Origin": "https://holland2stay.com",
        "Pragma": "no-cache",
        "Referer": "https://holland2stay.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "accept": "*/*",
        "content-type": "application/json",
        "sec-ch-ua": '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
    }

    data = {
        "operationName": "GetCategories",
        "variables": {
            "currentPage": 1,
            "id": "Nw==",
            "filters": {
                "city": {"eq": city.id},
                "available_to_book": {"eq": "179"},
                "category_uid": {"eq": "Nw=="},
            },
            "pageSize": 10,
            "sort": {"available_startdate": "ASC"},
        },
        "query": """query GetCategories($id: String!, $pageSize: Int!, $currentPage: Int!, $filters: ProductAttributeFilterInput!, $sort: ProductAttributeSortInput) {
                    categories(filters: {category_uid: {in: [$id]}}) {
                        items {
                        uid
                        ...CategoryFragment
                        __typename
                        }
                        __typename
                    }
                    products(
                        pageSize: $pageSize
                        currentPage: $currentPage
                        filter: $filters
                        sort: $sort
                    ) {
                        ...ProductsFragment
                        __typename
                    }
                    }
                    
                    fragment CategoryFragment on CategoryTree {
                    uid
                    meta_title
                    meta_keywords
                    meta_description
                    __typename
                    }
                    
                    fragment ProductsFragment on Products {
                    aggregations {
                        label
                        count
                        attribute_code
                        options {
                        label
                        count
                        value
                        __typename
                        }
                        position
                        __typename
                    }
                    items {
                        name
                        sku
                        city
                        url_key
                        available_to_book
                        available_startdate
                        building_name
                        finishing
                        living_area
                        no_of_rooms
                        resident_type
                        offer_text_two
                        offer_text
                        maximum_number_of_persons
                        type_of_contract
                        price_analysis_text
                        allowance_price
                        floor
                        basic_rent
                        lumpsum_service_charge
                        inventory
                        caretaker_costs
                        cleaning_common_areas
                        energy_common_areas
                        allowance_price
                        small_image {
                        url
                        label
                        position
                        disabled
                        __typename
                        }
                        thumbnail {
                        url
                        label
                        position
                        disabled
                        __typename
                        }
                        image {
                        url
                        label
                        position
                        disabled
                        __typename
                        }
                        media_gallery {
                        url
                        label
                        position
                        disabled
                        __typename
                        }
                        price_range {
                        minimum_price {
                            regular_price {
                            value
                            currency
                            __typename
                            }
                            final_price {
                            value
                            currency
                            __typename
                            }
                            discount {
                            amount_off
                            percent_off
                            __typename
                            }
                            __typename
                        }
                        maximum_price {
                            regular_price {
                            value
                            currency
                            __typename
                            }
                            final_price {
                            value
                            currency
                            __typename
                            }
                            discount {
                            amount_off
                            percent_off
                            __typename
                            }
                            __typename
                        }
                        __typename
                        }
                        __typename
                    }
                    page_info {
                        total_pages
                        __typename
                    }
                    total_count
                    __typename
                    }""",
    }

    response = requests.post(url, headers=headers, json=data)
    data = response.json()

    print(f" | {city.name} : {data['data']['products']['total_count']} found")

    data_parser(data, city)


def data_parser(data, city: City):
    for item in data["data"]["products"]["items"]:
        data = {
            "city": city.name,
            "name": item["name"],
            "rent": f"{item['basic_rent']:,.0f}",
            "area": f"{item['living_area']} m²",
            "link": f"https://holland2stay.com/residences/{item['url_key']}.html",
        }
        direct_message(data)


if __name__ == "__main__":
    print(f"\n | {datetime.now()}")

    for city in settings.CITY_LIST:
        graphql_request(city)

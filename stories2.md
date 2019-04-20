## Generated Story 1590844372497834712
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
* affirm
    - utter_ask_mail
* affirm{"email": "adityam7@gmail.com"}
    - slot{"email": "adityam7@gmail.com"}
    - email_restaurant_details

## Generated Story -5720442327716409010
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
* affirm
    - utter_ask_mail
* affirm{"email": "adityam7@gmail.com"}
    - slot{"email": "adityam7@gmail.com"}
    - email_restaurant_details

## Generated Story 3881199935798188255
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"location": "Pune"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "between 300 and 700"}
    - slot{"price": "between 300 and 700"}
    - action_restaurant

## Generated Story 1348051464058417043
* restaurant_search{"cuisine": "italian", "location": "delhi"}
    - slot{"cuisine": "italian"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "Delhi NCR"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
* deny
    - utter_final_bye

## Generated Story -7170538785544741681
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "london"}
    - slot{"location": "london"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
    - export


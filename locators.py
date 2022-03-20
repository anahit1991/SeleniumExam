class Signup:
    firstname = '//*[@name="first_name"]'
    lastname = '//*[@name="last_name"]'
    phone = '//*[@name="phone"]'
    email = '//*[@name="email"]'
    password = '//*[@name="password"]'
    signup_button = '//*[@class="btn btn-default btn-lg btn-block effect ladda-button waves-effect"]'


class Login:
    email = '//*[@name="email"]'
    password = '//*[@name="password"]'
    login_button = '//*[@class="btn btn-default btn-lg btn-block effect ladda-button waves-effect"]'


class Hotels:
    hotel_menu = '//*[text()="Hotels"]'


class SearchHotel:
    hotels_in_yerevan = '//*[@id="hotels-search"]/div/div/div[1]/div/div/div/span/span[1]/span/span[2]/b'
    search_button = '//*[text()=" Search"]'
    select_country_flag = '//*[@class="flag am"]'
    search_by_name = '//*[@placeholder="Hotel name."]'
    search_wishes_hotel = 'Nova'
    select_hotel = '//*[@id="nova hotel yerevan"]/div/div[2]/div/div[2]/div/a'


class SelectRoom:
    select_room = '//*[text()="Выбрать номер"]'
    booking_now = '//*[text()="Бронировать сейчас]'


class Authorization:
    xik = '/html/body/div[15]/div/div/div/svg'
    name = '//*[@name="firstName_lastName"]'
    email = '//*[@name="email"]'
    repeat_email = '//*[@name="retypeEmail"]'
    phone_number = '//*[@name="phoneNumber"]'
    submit = '//*[text()="ДАЛЕЕ: ЗАВЕРШЕНИЕ БРОНИРОВАНИЯ"]'




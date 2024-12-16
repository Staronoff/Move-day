# from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchWindowException, NoSuchElementException, ElementClickInterceptedException
import time
import random
from fake_useragent import UserAgent

EXTENSION_PATH = f'C:/Users/User/AppData/Local/Google/Chrome/User Data/Profile 1/Extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/12.6.1_0.crx'

wallets = [
    {
        "seed_phrase": ["word", "word", "word", "word", "word", "word", "word", "word", "word", "word", "word", "word"],
        "proxy": {
            'http': 'http://LOGIN:PASS@111.111.11.11:22222',
            'https': 'https://LOGIN:PASS@111.111.11.11:22222'
        },
        "name": "Account 1"
    },
    {
        "seed_phrase": ["word", "word", "word", "word", "word", "word", "word", "word", "word", "word", "word", "word"],
        "proxy": {
            'http': 'http://LOGIN:PASS@111.111.11.11:22222',
            'https': 'https://LOGIN:PASS@111.111.11.11:22222'
        },
        "name": "Account 2"
    },
]
random.shuffle(wallets)

# Поиск всплывающего окна при коннекте в квест
def check_and_click_if_exists(driver, current_window):
    all_windows = driver.window_handles
    if all_windows[-1] != current_window:
        try:
            driver.switch_to.window(all_windows[-1])
            WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div/div/div/div[3]/button[2]'))
            ).click()
            print("Окно Метамаск появилось, подтверждено.")
            time.sleep(2) 
        except NoSuchElementException:
            # Если кнопка не найдена, продолжаем выполнение
            print("Окна Метамаск не появилось, идем дальше.")

# Запустк драйвера
def start_browser(proxy_options, options):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), 
                                options=options,
                                seleniumwire_options=proxy_options,
                                )
    return driver

# Логин в метамаск
def login_metamask(driver, seed_phrase):
    driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#onboarding/welcome')
    time.sleep(4)
    current_window = driver.current_window_handle
    all_windows = driver.window_handles
    for window in all_windows:
        if window != current_window:
            driver.switch_to.window(window)
            driver.close()
    driver.switch_to.window(current_window)
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="onboarding__terms-checkbox"]'))
    ).click()
    driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/ul/li[3]/button').click()
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="metametrics-opt-in"]'))
    ).click()
    driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button[2]').click()
    time.sleep(2)
    for i, word in enumerate(seed_phrase):
        driver.find_element(By.XPATH, f'//*[@id="import-srp__srp-word-{i}"]').send_keys(word)
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[4]/div/button'))
    ).click()
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input'))
    ).send_keys('111111')
    driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input').send_keys('111111')
    driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[3]/label/span[1]/input').click()
    driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/button').click()
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[3]/button'))
    ).click()
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button'))
    ).click()
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button'))
    ).click()

# Коннект Метамаск к Galxe
def galxe_connect(driver):
    current_window = driver.current_window_handle
    all_windows = driver.window_handles
    for window in all_windows:
        if window != current_window:
            driver.switch_to.window(window)
            driver.close()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/button'))
    ).click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "radix-")]/div[2]/div/div/div[2]/div'))
    )
    driver.execute_script("arguments[0].click();", element)
    time.sleep(random.randint(5, 7))
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[-1])
    driver.find_element(by=By.XPATH, value='//*[@id="app-content"]/div/div/div/div[2]/div/div[3]/div/div[2]/button[2]').click()
    time.sleep(10)
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[-1])
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div/div/div/div[3]/button[2]'))
    ).click()
    print("Метамаск подключен к Galxe.")
    time.sleep(random.randint(5, 10))
    driver.switch_to.window(current_window)

# Квест 5 страниц
def daily_pages_quest(driver):  
    driver.get('https://app.galxe.com/quest/Movement/GCZkTtx9hF')
    print('Открылся квест Daily Move')
    current_window = driver.current_window_handle
    time.sleep(random.randint(7, 10))
    try:
        login = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/button')
        galxe_connect(driver)
    except (TimeoutException, NoSuchWindowException):
        check_and_click_if_exists(driver, current_window)
    all_windows = driver.window_handles
    for window in all_windows:
        if window != current_window:
            driver.switch_to.window(window)
            driver.close()
    driver.switch_to.window(current_window)
    # Прохождение квеста ==========================================================
    while True: # Проверяем логин 
        try:
            login = driver.find_elements(By.XPATH, '//*[contains(@id, "radix-")]/a/div')
            if login:
                print("Логин есть.")
                break
        except NoSuchElementException:
            print("Ждем логин.")
            time.sleep(10)
    time.sleep(5)
    def close_modal_if_present(driver):
        """Функция для проверки и закрытия модального окна, если оно есть."""
        try:
            modal_button = driver.find_element(By.XPATH, '//*[contains(@id, "radix-")]/div[3]/div/button[1]')
            driver.execute_script("arguments[0].click();", modal_button)
            print("Модальное окно закрыто.")
        except NoSuchElementException:
            # Если модального окна нет, просто продолжаем выполнение
            pass
    def confirm_pay(driver):
        """Функция для проверки подтверждения оплаты."""
        try:
            confirm_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[contains(@id, "radix-")]/div/div/div[4]/button[1]'))
            )
            driver.execute_script("arguments[0].click();", confirm_button)
            print("Оплата подтверждена.")
        except (NoSuchElementException, TimeoutException):
            print("Окна оплаты нет.")
            # Если модального окна нет, просто продолжаем выполнение
            pass
    # Кнопка 1
    close_modal_if_present(driver) # Проверяем модалку
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div[1]/div/div/div[1]/div/div[3]/div[1]/div[2]/div/div[1]').click()
    time.sleep(2)
    close_modal_if_present(driver)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[contains(@id, "radix-")]/div[2]/div/div[2]/div[3]'))
    ).click()
    time.sleep(2)
    driver.switch_to.window(current_window)
    close_modal_if_present(driver)
    WebDriverWait(driver, 15).until(
    EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "visited the Parthenon Website page")
    )
    print('Задание 1 ОК')
    # Кнопка 2 
    close_modal_if_present(driver)
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div[1]/div/div/div[1]/div/div[3]/div[2]/div[2]/div/div[1]').click()
    time.sleep(2)
    close_modal_if_present(driver)
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[contains(@id, "radix-")]/div[2]/div/div[2]/div[3]'))
    ).click()   
    time.sleep(2)
    driver.switch_to.window(current_window)
    close_modal_if_present(driver)
    WebDriverWait(driver, 15).until(
    EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "visited the Movement Website page")
    )
    print('Задание 2 ОК')
    # Кнопка 3
    close_modal_if_present(driver)
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div[1]/div/div/div[1]/div/div[3]/div[3]/div[2]/div/div[1]').click()
    time.sleep(2)
    close_modal_if_present(driver)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[contains(@id, "radix-")]/div[2]/div/div[2]/div[3]'))
    ).click()
    time.sleep(2)
    driver.switch_to.window(current_window)
    close_modal_if_present(driver)
    WebDriverWait(driver, 15).until(
    EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "visited the Movement Ecosystem page")
    )
    print('Задание 3 ОК')
    # Кнопка 4
    close_modal_if_present(driver)
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div[1]/div/div/div[1]/div/div[3]/div[4]/div[2]/div/div[1]').click()
    time.sleep(2)
    close_modal_if_present(driver)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[contains(@id, "radix-")]/div[2]/div/div[2]/div[3]'))
    ).click()
    time.sleep(2)
    driver.switch_to.window(current_window)
    close_modal_if_present(driver)
    WebDriverWait(driver, 15).until(
    EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "visited the MoveDrop page")
    )
    print('Задание 4 ОК')
    # Кнопка 5
    close_modal_if_present(driver)
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div[1]/div/div/div[1]/div/div[3]/div[5]/div[2]/div/div[1]').click()
    time.sleep(2)
    close_modal_if_present(driver)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[contains(@id, "radix-")]/div[2]/div/div[2]/div[3]'))
    ).click()
    time.sleep(2)
    driver.switch_to.window(current_window)
    close_modal_if_present(driver)
    WebDriverWait(driver, 15).until(
    EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "visited the Movement Blog page")
    )
    print('Задание 5 ОК')
    # Прокрут стрелочки
    close_modal_if_present(driver)
    element = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div/div/div[1]/div/div[3]/div[3]/div[2]/div/div[1]/button/div/span')
    element.click()
    time.sleep(4)
    all_windows = driver.window_handles
    for window in all_windows:
        if window != current_window:
            driver.switch_to.window(window)
            driver.close()
    driver.switch_to.window(current_window)
    # Клейм
    close_modal_if_present(driver)
    all_windows = driver.window_handles
    for window in all_windows:
        if window != current_window:
            driver.switch_to.window(window)
            driver.close()
    element = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/button')
    driver.execute_script("arguments[0].click();", element)
    print("Кнопка квеста Daily Move нажата.")
    time.sleep(2)
    confirm_pay(driver)
    # Проверка, появилось ли окно подтверждения транзакции
    try:
        new_window = WebDriverWait(driver, 20).until(
            lambda d: len(d.window_handles) > len(all_windows)
        )
        print("Окно Метамаск появилось.")
    except TimeoutException:
        print("Проблемка.")
        input('Сделай действие для продолжения: Если Метамаск появился - нажми Ентер, если НЕ появился - сделай действие для появления ММ и нажми Ентер')
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[-1])
    # Платный клейм
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div/div/div[2]/div/button[2]'))
        )
        print('Страница добавления сети')
    except TimeoutException:
        print('Кнопка добавления сети не появилась.')
    buttons = driver.find_elements(By.XPATH, '//*[@id="app-content"]/div/div/div/div[2]/div/button[2]')
    if buttons:
        # Выполняем шаги для добавления сети
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div/div/div[2]/div/button[2]'))
        ).click()
        print('Сеть добавлена')
        time.sleep(random.randint(4, 6))
        driver.switch_to.window(current_window)
        all_windows = driver.window_handles
        if len(all_windows) >= 1:
            time.sleep(10)
        close_modal_if_present(driver)
        # Повторно клеймим
        driver.switch_to.window(current_window)
        all_windows = driver.window_handles
        element = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/button')
        driver.execute_script("arguments[0].click();", element)
        print("Кнопка квеста Daily Move нажата.")
        time.sleep(2)
        confirm_pay(driver)
        driver.switch_to.window(current_window)
        # Подтверждение транзакции
        try:
            new_window = WebDriverWait(driver, 20).until(
                lambda d: len(d.window_handles) > len(all_windows)
            )
            print("Окно Метамаск появилось.")
        except TimeoutException:
            print("Проблемка.")
            input('Сделай действие для продолжения: Если Метамаск появился - нажми Ентер, если НЕ появился - сделай действие для появления ММ и нажми Ентер')
        all_windows = driver.window_handles
        driver.switch_to.window(all_windows[-1])
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div/div/div/div[3]/button[2]'))
        ).click()
        print('Транзакция подтверждена')
        driver.switch_to.window(current_window)
        time.sleep(random.randint(4, 6))
    else:
        print('Страница подтверждения транзакции')
        # Если появляется только окно подтверждения, выполняем только шаги для подтверждения
        all_windows = driver.window_handles
        driver.switch_to.window(all_windows[-1])
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div/div/div/div[3]/button[2]'))
        ).click()
        driver.switch_to.window(current_window)
        time.sleep(random.randint(4, 6))
    # Проверка клейма
    print('Проверка клейма')
    while True:
        form_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "radix-")]/button/span[1]'))
        )
        if form_element:
            print("Клейм квеста Daily Move выполнен.")
            break
    # while True:
    #     try:
    #         element = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div[2]/div/div[2]/div[2]/div/div/button')
    #         driver.execute_script("arguments[0].click();", element)
    #         print("Кнопка квеста Move Daily нажата.")
    #         time.sleep(7)
    #         form_element = driver.find_element(By.XPATH, '//*[contains(@id, "radix-")]/button/span[1]')
    #         if form_element:
    #             print("Клейм квеста Move Daily выполнен.")
    #             break
    #     except NoSuchElementException:
    #         print("Клейм квеста Move Daily не выполнен, повторный клик.")
    #         time.sleep(1)

# Квест Battle
def battle_quest(driver):
    driver.get('https://app.galxe.com/quest/Movement/GCj3gtgLqj')
    current_window = driver.current_window_handle
    print('Страница Battle открыта')
    time.sleep(random.randint(7, 10))
    try:
        login = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/button')
        galxe_connect(driver)
    except (TimeoutException, NoSuchWindowException):
        check_and_click_if_exists(driver, current_window)
    all_windows = driver.window_handles
    for window in all_windows:
        if window != current_window:
            driver.switch_to.window(window)
            driver.close()
    driver.switch_to.window(current_window)
    # Прохождение квеста ==========================================================
    while True:
        try:
            login = driver.find_element(By.XPATH, '//*[contains(@id, "radix-")]/a/div')
            if login:
                print("Логин есть.")
                break
        except NoSuchElementException:
            print("Ждем логин.")
            time.sleep(10)
    time.sleep(5)
    def close_modal_if_present(driver):
        """Функция для проверки и закрытия модального окна, если оно есть."""
        try:
            modal_button = driver.find_element(By.XPATH, '//*[contains(@id, "radix-")]/div[3]/div/button[1]')
            driver.execute_script("arguments[0].click();", modal_button)
            print("Модальное окно закрыто.")
        except NoSuchElementException:
            # Если модального окна нет, просто продолжаем выполнение
            pass
    def confirm_pay(driver):
        """Функция для проверки подтверждения оплаты."""
        try:
            confirm_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[contains(@id, "radix-")]/div/div/div[4]/button[1]'))
            )
            driver.execute_script("arguments[0].click();", confirm_button)
            print("Оплата подтверждена.")
        except (NoSuchElementException, TimeoutException):
            print("Окна оплаты нет.")
            # Если модального окна нет, просто продолжаем выполнение
            pass
    close_modal_if_present(driver) # Проверяем модалку
    WebDriverWait(driver, 8).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div[1]/div/div/div[1]/div/div[3]/div[1]/div[2]/div/div[1]'))
    ).click()
    time.sleep(2)
    close_modal_if_present(driver)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[contains(@id, "radix-")]/div[2]/div/div[2]/div[3]'))
    ).click()   
    time.sleep(2)
    driver.switch_to.window(current_window)
    close_modal_if_present(driver)
    WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "visited the Battle of Olympus page")
    )
    print('Задание ОК')
    all_windows = driver.window_handles
    for window in all_windows:
        if window != current_window:
            driver.switch_to.window(window)
            driver.close()
    driver.switch_to.window(current_window)
    # Прокрут стрелочки
    close_modal_if_present(driver)
    element = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div/div/div[1]/div/div[3]/div[1]/div[2]/div/div[1]/button/div/span')
    element.click()
    time.sleep(4)
    # Клейм
    close_modal_if_present(driver)
    all_windows = driver.window_handles
    for window in all_windows:
        if window != current_window:
            driver.switch_to.window(window)
            driver.close()
    element = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/button')
    driver.execute_script("arguments[0].click();", element)
    print("Кнопка квеста Battle нажата.")
    time.sleep(2)
    confirm_pay(driver)
    # Проверка, появилось ли окно подтверждения транзакции
    all_windows = driver.window_handles
    try:
        new_window = WebDriverWait(driver, 20).until(
            lambda d: len(d.window_handles) > len(all_windows)
        )
        print("Окно Метамаск появилось.")
    except TimeoutException:
        print("Проблемка.")
        input('Сделай действие для продолжения: Если Метамаск появился - нажми Ентер, если НЕ появился - сделай действие для появления ММ и нажми Ентер')
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[-1])
    # Платный клейм
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div/div/div[2]/div/button[2]'))
        )
        print('Страница добавления сети')
    except TimeoutException:
        print('Кнопка добавления сети не появилась.')
    buttons = driver.find_elements(By.XPATH, '//*[@id="app-content"]/div/div/div/div[2]/div/button[2]')
    if buttons:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div/div/div[2]/div/button[2]'))
        ).click()
        print('Сеть добавлена')
        time.sleep(random.randint(4, 6))
        driver.switch_to.window(current_window)
        all_windows = driver.window_handles
        if len(all_windows) >= 1:
            time.sleep(10)
        close_modal_if_present(driver)
        # Повторно клеймим
        all_windows = driver.window_handles
        driver.switch_to.window(current_window)
        element = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/button')
        driver.execute_script("arguments[0].click();", element)
        print("Кнопка квеста Battle нажата.")
        time.sleep(2)
        confirm_pay(driver)
        driver.switch_to.window(current_window)
        try:
            new_window = WebDriverWait(driver, 20).until(
                lambda d: len(d.window_handles) > len(all_windows)
            )
            print("Окно Метамаск появилось.")
        except TimeoutException:
            print("Проблемка.")
            input('Сделай действие для продолжения: Если Метамаск появился - нажми Ентер, если НЕ появился - сделай действие для появления ММ и нажми Ентер')
        all_windows = driver.window_handles
        driver.switch_to.window(all_windows[-1])
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div/div/div/div[3]/button[2]'))
        ).click()
        print('Транзакция подтверждена')
        driver.switch_to.window(current_window)
        time.sleep(random.randint(4, 6))
    else:
        print('Страница подтверждения транзакции')
        # Если появляется только окно подтверждения, выполняем только шаги для подтверждения
        all_windows = driver.window_handles
        driver.switch_to.window(all_windows[-1])
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div/div/div/div[3]/button[2]'))
        ).click()
        driver.switch_to.window(current_window)
        time.sleep(random.randint(4, 6))
    # Проверка клейма
    print('Проверка клейма')
    while True:
        form_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "radix-")]/button/span[1]'))
        )
        if form_element:
            print("Клейм квеста Battle выполнен.")
            break

    # while True:
    #     try:
    #         element = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div[2]/div/div[2]/div[2]/div/div/button')
    #         driver.execute_script("arguments[0].click();", element)
    #         print("Кнопка клейма квеста Battle нажата.")
    #         time.sleep(7)
    #         form_element = driver.find_element(By.XPATH, '//*[contains(@id, "radix-")]/button/span[1]')
    #         if form_element:
    #             print("Клейм квеста Battle выполнен.")
    #             break
    #     except NoSuchElementException:
    #         print("Клейм кваста Battle не выполнен, повторный клик.")
    #         time.sleep(1)

# Квест на роль
def role_quest(driver):
    driver.get('https://app.galxe.com/quest/Movement/GCFu4toxhQ')
    current_window = driver.current_window_handle
    print('Страница Роли открыта')
    time.sleep(random.randint(7, 10))
    try:
        login = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/button')
        galxe_connect(driver)
    except (TimeoutException, NoSuchWindowException):
        check_and_click_if_exists(driver, current_window)
    all_windows = driver.window_handles
    for window in all_windows:
        if window != current_window:
            driver.switch_to.window(window)
            driver.close()
    driver.switch_to.window(current_window)
    while True: # Проверяем логин 
        try:
            login = driver.find_elements(By.XPATH, '//*[contains(@id, "radix-")]/a/div')
            if login:
                print("Логин есть.")
                break
        except NoSuchElementException:
            print("Ждем логин.")
            time.sleep    
    def close_modal_if_present(driver):
        """Функция для проверки и закрытия модального окна, если оно есть."""
        try:
            modal_button = driver.find_element(By.XPATH, '//*[contains(@id, "radix-")]/div[3]/div/button[1]')
            driver.execute_script("arguments[0].click();", modal_button)
            print("Модальное окно закрыто.")
        except NoSuchElementException:
            # Если модального окна нет, просто продолжаем выполнение
            pass
    close_modal_if_present(driver) # Проверяем модалку
    # Клейм
    all_windows = driver.window_handles
    for window in all_windows:
        if window != current_window:
            driver.switch_to.window(window)
            driver.close()
    element = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/button')
    driver.execute_script("arguments[0].click();", element)
    print("Кнопка квеста на Роль нажата.")
    close_modal_if_present(driver)
    time.sleep(17)
    # Проверка клейма
    print('Проверка клейма')
    while True:
        form_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "radix-")]/button/span[1]'))
        )
        if form_element:
            print("Клейм Роли выполнен.")
            break

# Основной порядок выполнения
def main():
    completed_accounts = []
    for wallet in wallets:
        options = Options()
        options.add_extension(EXTENSION_PATH)
        options.add_argument("--force-device-scale-factor=0.5")
        options.add_argument(f"user-agent={UserAgent().random}")
        options.add_argument('--disable-blink-features=AutomationControlled')
        proxy_options = {
            'proxy': wallet['proxy'],
        }
        print(f"Вход в MetaMask для {wallet['name']}")
        driver = start_browser(proxy_options, options)
        login_metamask(driver, wallet["seed_phrase"]) # , wallet["name"]
        print(f"Логин в MetaMask для {wallet['name']} завершен.")
        # role_quest(driver)
        # print(f"Роль для {wallet['name']} получена.")
        # daily_pages_quest(driver)
        # print(f"Квест Move Daily {wallet['name']} завершен.")
        # battle_quest(driver)
        # print(f"Квест Battle {wallet['name']} завершен.")
        
        # Список квестов
        quests = [daily_pages_quest, battle_quest]
        random.shuffle(quests)  # Перемешиваем список квестов
        for quest in quests:
            quest(driver)
            time.sleep(random.randint(5, 10))  # Пауза между квестами
        account_number = int(wallet['name'].split(' ')[-1])  # Предполагается, что имя в формате "Account N"
        completed_accounts.append(account_number)
        completed_accounts.sort()
        print(f"Квесты для {wallet['name']} завершены.")
        print(completed_accounts)
        time.sleep(random.randint(10, 15))  # Пауза перед переключением на следующий кошелек
        driver.quit()

if __name__ == "__main__":
    main()
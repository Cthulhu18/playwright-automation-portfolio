import time
from playwright.sync_api import Page, expect

def test_successful_form_submission(page: Page):
    """TC-001: Успешное заполнение формы с валидными данными"""
    page.set_default_timeout(50000)

    page.goto("https://demoqa.com/text-box")
    page.locator("#userName").fill("Иван Иванов")
    page.locator("#userEmail").fill("IvanIvan@example.com")
    page.locator("#currentAddress").fill("Москва, ул. Примерная, 1")
    page.locator("#permanentAddress").fill("Санкт-Петербург, ул. Тестовая, 2")
    page.locator("#submit").click()

    # Проверяем что поле output отображаются введённые данные
    expect(page.locator("#output")).to_be_visible()
    expect(page.locator("#name")).to_have_text("Name:Иван Иванов")
    expect(page.locator("#email")).to_have_text("Email:IvanIvan@example.com")
    expect(page.locator("#output #currentAddress")).to_have_text("Current Address :Москва, ул. Примерная, 1")
    expect(page.locator("#output #permanentAddress")).to_have_text("Permananet Address :Санкт-Петербург, ул. Тестовая, 2")


def test_invalid_email_format(page: Page):
    """TC-002: Невалидный формат email"""
    page.set_default_timeout(100000)

    page.goto("https://demoqa.com/text-box")
    page.locator("#userEmail").fill("invalid-email")  # Невалидный email без @
    page.locator("#submit").click()

    # Форма не отправилась
    is_visible = page.locator("#output").is_visible()
    assert not is_visible, "Форма не должна отправляться при невалидном email"

    # Поле невалидно по нативной валидации
    email_element = page.locator("#userEmail").element_handle()
    is_valid = page.evaluate("el => el.checkValidity()", email_element)
    assert not is_valid, "Поле email должно быть невалидным по браузерной валидации"

    # Проверяем основные цвета рамки
    email_field = page.locator("#userEmail")

    border_color = email_field.evaluate("el => getComputedStyle(el).borderColor")
    border_top_color = email_field.evaluate("el => getComputedStyle(el).borderTopColor")

    # Должен быть именно RGB(255, 0, 0)
    is_red_border = (
            border_color == "rgb(255, 0, 0)" or
            border_top_color == "rgb(255, 0, 0)" or
            border_color == "red" or
            border_top_color == "red"
    )

    # Дополнительная проверка
    page.locator("#userEmail").fill("test@")    # email без домена
    page.locator("#submit").click()

    # Повторяем проверки

    is_visible = page.locator("#output").is_visible()
    assert not is_visible, "Форма не должна отправляться при невалидном email"

    email_element = page.locator("#userEmail").element_handle()
    is_valid = page.evaluate("el => el.checkValidity()", email_element)
    assert not is_valid, "Поле email должно быть невалидным по браузерной валидации"

    # Проверяем основные цвета рамки
    email_field = page.locator("#userEmail")

    border_color = email_field.evaluate("el => getComputedStyle(el).borderColor")
    border_top_color = email_field.evaluate("el => getComputedStyle(el).borderTopColor")

    # Должен быть именно RGB(255, 0, 0)
    is_red_border = (
            border_color == "rgb(255, 0, 0)" or
            border_top_color == "rgb(255, 0, 0)" or
            border_color == "red" or
            border_top_color == "red"
    )

    assert is_red_border, f"Требование: рамка должна быть зелёной. Фактически: {border_color}"

    print("✓ Требование выполнено: поле подсвечивается зелёным при ошибке")
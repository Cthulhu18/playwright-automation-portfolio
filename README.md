# 🚀 Playwright Automation Portfolio

Профессиональное портфолио автоматизированных тестов на Playwright

## 📋 О проекте

Этот репозиторий содержит набор автоматизированных тестов для различных веб-приложений, демонстрирующий навыки тестирования и автоматизации.

## 🛠️ Технологический стек

- **Language:** Python 3.11+
- **Testing Framework:** Playwright
- **Runner:** pytest
- **CI/CD:** GitHub Actions
- **Reporting:** Allure / HTML reports

## 📊 Охват тестирования

### 🌐 DemoQA (https://demoqa.com)
- [x] Text Box form
- [x] Check Box 
- [x] Radio Button
- [x] Web Tables
- [ ] Buttons
- [ ] Links

### 🛒 SauceDemo (https://saucedemo.com)
- [x] Login functionality
- [ ] Product catalog
- [ ] Shopping cart
- [ ] Checkout process

## 🚀 Запуск тестов

```bash
# Установка зависимостей
pip install -r requirements.txt
playwright install

# Запуск всех тестов
pytest

# Запуск тестов для DemoQA
pytest tests/demoqa/ -v

# Запуск с отчетом
pytest --html=reports/report.html

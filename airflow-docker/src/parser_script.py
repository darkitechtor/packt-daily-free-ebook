from airflow.hooks.base import BaseHook # type: ignore

import asyncio
from pyppeteer import launch # type: ignore
"""
Don't forget to change constants' values or
create your own connection for Airflow.
"""
CONFIG = BaseHook.get_connection('packt_credentials')
USERNAME = CONFIG.login
PASSWORD = CONFIG.password

async def authenticate_packt(username, password):
    # Launch the browser and create a new page
    browser = await launch(headless=True,
                           executablePath='/usr/bin/chromium',
                           args=['--no-sandbox'])
    page = await browser.newPage()

    try:
        # Navigate to the login page
        await page.goto('https://account.packtpub.com/login')

        # Wait for the username and password input fields to appear
        await page.waitForSelector('input[name="email"]')
        await page.waitForSelector('input[name="password"]')

        # Type the username and password
        await page.type('input[name="email"]', username)
        await page.type('input[name="password"]', password)

        # Click the login button
        button = await page.xpath('//button[contains(., "Log in")]')
        await page.evaluate('(btn) => btn.click()', button[0])

        # Wait for the navigation after login
        await page.waitForNavigation()

        # Navigate to the 'Free learning' page
        await page.goto('https://www.packtpub.com/free-learning')

        # Wait for the claim button to appear
        await page.waitForSelector('#freeLearningClaimButton')

        # Push the claim button
        button = await page.xpath('//button[contains(., "Access eBook now")]')
        await page.evaluate('(btn) => btn.click()', button[0])

        # Wait for the navigation after pushing
        await page.waitForNavigation()

        # Check if authentication was successful
        url = await page.evaluate("() => window.location.href")
        if url:
            print("Authenticated successfully.")
            element = await page.waitForSelector('.book-title')
            title = await page.evaluate('(element) => element.textContent', element)
            print(f"||[{title}]({url})||")
        else:
            print("Authentication failed.")

    except Exception as e:
        print("Error occurred:", e)

    finally:
        # Close the browser
        await browser.close()

if __name__ == '__main__':
    username = USERNAME
    password = PASSWORD

    asyncio.get_event_loop().run_until_complete(authenticate_packt(username, password))
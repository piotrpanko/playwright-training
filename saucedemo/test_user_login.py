from playwright.sync_api import Page, expect

valid_usernames = ['standard_user', 'problem_user', 'performance_glitch_user', 'error_user', 'visual_user']
url = 'https://www.saucedemo.com/'

def test_valid_login(page: Page):
    for username in valid_usernames:
        can_login_with_valid_params(page, username)

def can_login_with_valid_params(page, username):
    page.goto(url)

    page.get_by_placeholder('Username').fill(value=username) # why cant i locate it by the role??
    page.get_by_role('textbox', name='password').fill(value='secret_sauce')

    page.get_by_text('Login').click()

    expect(page).to_have_url('https://www.saucedemo.com/inventory.html')
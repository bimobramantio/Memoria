#!/usr/bin/env python
# coding: utf-8

# # Daily Test Critical Dashboard

# This test content will be :
# 1. sign up and login
# 2. product create and edit
# 3. withdraw 
# 4. new account bank and edit
# 5. log out

# # Testing

# ## Starting up

# In[ ]:


#starting webdriver
import time # memberikan input waktu delay
import os
import IPython
import jupyter_dojo
import requests
from random import randint
from faker import Faker # random input form
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

#%load_ext ipython_unittest 
fake = Faker('id_ID')


# ### Additional system page pass
# Additional test

# In[ ]:


def login():
    driver.get("https://gomodo.id/agent/login?userLang=id")
    driver.find_element_by_css_selector("#login_id_container > input").send_keys("username")
    driver.find_element_by_css_selector("#regForm > div > div > div:nth-child(7) #submitButton").click()

    driver.find_element_by_css_selector("#regForm > div > div > div.form-group.form-group-feedback.form-group-feedback-left.input-group.show-for-email > input").send_keys("password")
    time.sleep(6)

    #cek login tombol
    driver.find_element_by_css_selector("#regForm > div > div > div:nth-child(7) #submitButton").click()
    time.sleep(2)

def settinglogin():
    driver.get("https://gomodo.id/agent/login?userLang=id")
    driver.find_element_by_css_selector("#login_id_container > input").send_keys("username")
    driver.find_element_by_css_selector("#regForm > div > div > div:nth-child(7) #submitButton").click()

    driver.find_element_by_css_selector("#regForm > div > div > div.form-group.form-group-feedback.form-group-feedback-left.input-group.show-for-email > input").send_keys("password")
    time.sleep(6)

    #cek login tombol
    driver.find_element_by_css_selector("#regForm > div > div > div:nth-child(7) #submitButton").click()
    time.sleep(2)
    
vouchercode = "vcode2"


# ## Sign up and Login

# ### Login Negative

# #### Testing 1 Negative
# this test only at the begining

# In[ ]:


driver = webdriver.Chrome(executable_path=r'C:\Users\astro\driver\chromedriver.exe') 
driver.maximize_window()
wait = WebDriverWait(driver,20)

# validation without fill the form
driver.get("https://gomodo.id/agent/login")
driver.find_element_by_css_selector("#regForm > div > div > div:nth-child(7) #submitButton").click()
valid_login = driver.find_element_by_css_selector("#login_id_container > span").text
valid_login == "Bidang ini wajib diisi."

#validation fill the wrong input email
driver.find_element_by_css_selector("#login_id_container > input").send_keys("test.test")
driver.find_element_by_css_selector("#regForm > div > div > div:nth-child(7) #submitButton").click()
valid_login_email = driver.find_element_by_css_selector("#login_id_container > span").text
valid_login_email == "Format email salah"

#validation fill the wrong input phone number
driver.find_element_by_css_selector("#login_id_container > input").send_keys("123123")
driver.find_element_by_css_selector("#regForm > div > div > div:nth-child(7) #submitButton").click()
valid_login_email = driver.find_element_by_css_selector("#login_id_container > span").text
valid_login_email == "Format telepon salah"
driver.quit()


# #### Testing 2 Negative
# test after input email wrong

# In[ ]:


driver = webdriver.Chrome(executable_path=r'C:\Users\astro\driver\chromedriver.exe') 
driver.maximize_window()
wait = WebDriverWait(driver,20)

#validation fill the wrong password input email
driver.get("https://gomodo.id/agent/login")
driver.find_element_by_css_selector("#login_id_container > input").send_keys("username")
driver.find_element_by_css_selector("#regForm > div > div > div:nth-child(7) #submitButton").click()
driver.find_element_by_css_selector("#regForm > div > div > div.form-group.form-group-feedback.form-group-feedback-left.input-group.show-for-email > input").send_keys("salah password")
driver.find_element_by_css_selector("#regForm > div > div > div:nth-child(7) #submitButton").click()
time.sleep(4)
valid_login_email_password = driver.find_element_by_css_selector("#error_domain > span").text
valid_login_email_password == "Email atau Password Anda salah"

#validation fill the wring email input but the password its true
driver.find_element_by_css_selector("#login_id_container > div.input-group-append.show-for-email #backtoemail").click()
driver.find_element_by_css_selector("#login_id_container > input").clear()
driver.find_element_by_css_selector("#login_id_container > input").send_keys("password@gmail.com")
driver.find_element_by_css_selector("#regForm > div > div > div:nth-child(7) #submitButton").click()
driver.find_element_by_css_selector("#regForm > div > div > div.form-group.form-group-feedback.form-group-feedback-left.input-group.show-for-email > input").send_keys("password")
driver.find_element_by_css_selector("#regForm > div > div > div:nth-child(7) #submitButton").click()
time.sleep(4)
valid_login_email_password_ubah = driver.find_element_by_css_selector("#error_domain > span").text
valid_login_email_password_ubah == "Email atau Password Anda salah"

#validation password is not 6 digit character
driver.find_element_by_css_selector("#regForm > div > div > div.form-group.form-group-feedback.form-group-feedback-left.input-group.show-for-email > input").clear()
driver.find_element_by_css_selector("#regForm > div > div > div.form-group.form-group-feedback.form-group-feedback-left.input-group.show-for-email > input").send_keys("123")
driver.find_element_by_css_selector("#regForm > div > div > div:nth-child(7) #submitButton").click()
time.sleep(5)

toast_text = driver.find_element_by_css_selector("div > div.toast-message").text
toast_text =="Kolom isian password harus minimal 6 karakter."

driver.quit()


# #### Testing 3 Negative
# Otp

# In[ ]:


driver = webdriver.Chrome(executable_path=r'C:\Users\astro\driver\chromedriver.exe') 
driver.maximize_window()
wait = WebDriverWait(driver,20)

#validation OTP
driver.get("https://gomodo.id/agent/login")
driver.find_element_by_css_selector("#login_id_container > input").send_keys("089123123")
driver.find_element_by_css_selector("#regForm > div > div > div:nth-child(7) #submitButton").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#digit-1")))
driver.find_element_by_css_selector("#digit-1").send_keys("1234")
valid_otp = driver.find_element_by_css_selector("#digit-1").text
valid_otp == "#error_domain > span"

#resend OTP
time.sleep(30)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#resend_otp")))
driver.find_element_by_css_selector("#resend_otp").click()

driver.quit()


# ### Sign Up Negative

# In[ ]:


driver = webdriver.Chrome(executable_path=r'C:\Users\astro\driver\chromedriver.exe') 
driver.maximize_window()
wait = WebDriverWait(driver,20)

#validation each fill
driver.get("https://gomodo.id/agent/register")
driver.find_element_by_css_selector("#btn-register").click()
time.sleep(2)
driver.find_element_by_css_selector("#regForm > div > div > div.content-register.hide-for-otp > div:nth-child(2) > input").send_keys("Test Contoh")
driver.find_element_by_css_selector("#btn-register").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='regForm']/div/div/div[2]/div[2]/input").send_keys("testcontoh")
driver.find_element_by_css_selector("#btn-register").click()
time.sleep(2)
#validation without fill the form city
driver.find_element_by_css_selector("#select2-city_id-container").click()
time.sleep(2)
driver.find_element_by_css_selector("#btn-register").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='select2-city_id-container']").click()
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("yogyakarta")
time.sleep(5)
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)
#form input number WA
driver.find_element_by_css_selector("#regForm > div > div > div.content-register.hide-for-otp > div:nth-child(8) > input").send_keys("123")
driver.find_element_by_css_selector("#btn-register").click()
time.sleep(2)
driver.find_element_by_css_selector("#regForm > div > div > div.content-register.hide-for-otp > div:nth-child(8) > input").clear()
driver.find_element_by_css_selector("#btn-register").click()
time.sleep(2)
driver.find_element_by_css_selector("#regForm > div > div > div.content-register.hide-for-otp > div:nth-child(8) > input").send_keys("8123123123")
driver.find_element_by_css_selector("#btn-register").click()
time.sleep(2)
driver.find_element_by_css_selector("#regForm > div > div > div.content-register.hide-for-otp > div:nth-child(8) > input").clear()
driver.find_element_by_css_selector("#regForm > div > div > div.content-register.hide-for-otp > div:nth-child(8) > input").send_keys("081954123")
driver.find_element_by_css_selector("#btn-register").click()
time.sleep(2)
driver.find_element_by_css_selector("#email").send_keys("asd.aasd")
driver.find_element_by_css_selector("#btn-register").click()
time.sleep(2)
driver.find_element_by_css_selector("#email").send_keys("testcontoh@gmail.com")
driver.find_element_by_css_selector("#btn-register").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='regForm']/div/div/div[2]/div[9]/span[1]/span[1]/span").click()
driver.find_element_by_xpath("/html/body/span/span/span[2]/ul/li[3]").click()

driver.quit()


# ## Withdraw
# this test withdraw dont have balance

# In[ ]:


driver = webdriver.Chrome(executable_path=r'C:\Users\astro\driver\chromedriver.exe') 
driver.maximize_window()
wait = WebDriverWait(driver,20)

login()

driver.get("https://gomodo.id/company/withdraw")
driver.find_element_by_css_selector("#order-guest > div.widget-content > div > div:nth-child(2) > button").click()
time.sleep(1)
driver.find_element_by_css_selector("#form_ajax > div > div > div.modal-body > div > div:nth-child(2) > div #amount").send_keys("10000000000000000000000")
driver.find_element_by_xpath("//*[@id='form_ajax']/div/div/div[2]/button[2]").click()
time.sleep(2)
valid_max_withdraw = driver.find_element_by_css_selector("#swal2-content").text
valid_max_withdraw == "Saldo tidak mencukupi"
driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()
driver.find_element_by_css_selector("#form_ajax > div > div > div.modal-body > div > div:nth-child(2) > div #amount").clear()
driver.find_element_by_xpath("//*[@id='cancel']").click()

driver.quit()


# ## Product
# Create product and edit testing

# In[ ]:


driver = webdriver.Chrome(executable_path=r'C:\Users\astro\driver\chromedriver.exe') 
driver.maximize_window()
wait = WebDriverWait(driver,20)

login()

driver.get("https://gomodo.id/company/product/create")

#nama produk dan kategori produk
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#mapGoogle > div > div > div:nth-child(1) > div:nth-child(3)")))
#unik
driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-5 > div:nth-child(1) > input").send_keys("Tes Contoh 27/10/2020")
#/
driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-5 > div:nth-child(2) > span > span.selection > span > ul > li > input").click()
time.sleep(2)
driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-5 > div:nth-child(2) > span > span.selection > span > ul > li > input").send_keys("Atraksi")
time.sleep(3)
driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-5 > div:nth-child(2) > span > span.selection > span > ul > li > input").send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-5 > div:nth-child(2) > span > span.selection > span > ul > li > input").send_keys("Akrobatik")
time.sleep(3)
driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-5 > div:nth-child(2) > span > span.selection > span > ul > li > input").send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-5 > div:nth-child(2) > span > span.selection > span > ul > li > input").send_keys("Naik ATV")
time.sleep(3)
driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-5 > div:nth-child(2) > span > span.selection > span > ul > li > input").send_keys(Keys.ENTER)

#pilih negara dkk
driver.find_element_by_css_selector("#select2-country_search-container").click()
time.sleep(3)

driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("indonesia")
time.sleep(3)
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)
time.sleep(5)
#pilih provinsi dan kota
driver.find_element_by_css_selector("#select2-state_search-container").click()
time.sleep(3)
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("Yogyakarta")
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element_by_css_selector("#select2-city_search-container").click()
time.sleep(3)
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("yogyakarta")
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)

# deskripsi singkat dan tentang produk
driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-5 > div:nth-child(6) > input").send_keys("deskripsi sinkat mengenai produk,,,deskripsi sinkat mengenai produk,,,deskripsi sinkat mengenai prod")

driver.switch_to.frame(driver.find_element_by_css_selector("iframe#long_description_ifr"))
driver.find_element_by_css_selector("body[data-id=long_description]").clear()
driver.find_element_by_css_selector("body[data-id=long_description]").send_keys("Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informasi mengenai produk anda,,,Tentang produk anda berikut adalah segala informas")
driver.switch_to.default_content()

#map dan lokasi
driver.find_element_by_css_selector("#pac-input").send_keys("gojek office")
driver.find_element_by_css_selector("#pac-input").send_keys(Keys.ENTER)
driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-7 > div:nth-child(3) > span > span.selection > span > ul > li > input").click()
driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-7 > div:nth-child(3) > span > span.selection > span > ul > li > input").send_keys("english")
driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-7 > div:nth-child(3) > span > span.selection > span > ul > li > input").send_keys(Keys.ENTER)
driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-7 > div:nth-child(3) > span > span.selection > span > ul > li > input").send_keys("indonesia")
driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-7 > div:nth-child(3) > span > span.selection > span > ul > li > input").send_keys(Keys.ENTER)

#pilih tanggal dan hari 
driver.find_element_by_css_selector("#day_fix > div > div > div > div:nth-child(1) > label").click()
driver.find_element_by_css_selector("#dates > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div > input").click()
driver.find_element_by_css_selector("body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-top > div.datepicker-days > table > tbody > tr:nth-child(6) > td:nth-child(7)").click()
driver.find_element_by_css_selector("#dates > div:nth-child(1) > div:nth-child(2) > div.col-md-6.end_label > div > input").click()
driver.find_element_by_css_selector("body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-top > div.datepicker-days > table > tbody > tr:nth-child(3) > td:nth-child(6)").click()

#jam 
driver.find_element_by_css_selector("#start_time\.0").click()
driver.find_element_by_css_selector("body > div.ui-timepicker-container.ui-timepicker-standard > div > ul > li:nth-child(3) > a").click()
driver.find_element_by_css_selector("#end_time\.0").click()
driver.find_element_by_css_selector("body > div.ui-timepicker-container.ui-timepicker-standard > div > ul > li:nth-child(37) > a").click()

#Durasi aktivitas
driver.find_element_by_xpath("//*[@id='duration_activity']/div[2]/div[1]/div[1]/div/input").send_keys("3")
driver.find_element_by_css_selector("#duration_activity > div.widget-content > div:nth-child(1) > div:nth-child(2) > div > select").click()
driver.find_element_by_css_selector("#duration_activity > div.widget-content > div:nth-child(1) > div:nth-child(2) > div > select > option:nth-child(2)").click()

driver.find_element_by_css_selector("#minimum_notice").send_keys("1")

driver.switch_to.frame(driver.find_element_by_css_selector("iframe#important_notes_ifr"))
driver.find_element_by_css_selector("body[data-id=important_notes]").clear()
driver.find_element_by_css_selector("body[data-id=important_notes]").send_keys("Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catatan penting mengenai suatu produk,,,Berikut adalah catat")
driver.switch_to.default_content()

#harga produk
driver.find_element_by_css_selector("#max_people").send_keys("20")
driver.find_element_by_css_selector("#quota_type").click()
time.sleep(2)
driver.find_element_by_css_selector("#quota_type > option:nth-child(2)").click()
time.sleep(2)
driver.find_element_by_css_selector("#quota_type > option:nth-child(1)").click()
driver.find_element_by_css_selector("#min_people").clear()
driver.find_element_by_css_selector("#min_people").send_keys("3")
driver.find_element_by_css_selector("#max_order").send_keys("100")

driver.find_element_by_css_selector("#price\.0").send_keys("10000")
driver.find_element_by_css_selector("#pricing").click()
driver.find_element_by_css_selector("#pricing > option:nth-child(12)").click()#ganti hari
time.sleep(3)
driver.find_element_by_css_selector("#pricing > option:nth-child(1)").click()#ganti orang

#cek tambahan customer
#driver.find_element_by_css_selector("#custom-input > div.widget-content > div > div.col-sm-12.mb-3 > div > div:nth-child(1) > div > select").click()
driver.find_element_by_css_selector("#custom-input > div.widget-content > div > div.col-sm-12.mb-3 > div > div:nth-child(1) > div > select > option:nth-child(6)").click()#ganti ke document
time.sleep(3)
driver.find_element_by_css_selector("#custom-input > div.widget-content > div > div.col-sm-12.mb-3 > div > div:nth-child(1) > div > select > option:nth-child(1)").click()#ganti ke text pendek
driver.find_element_by_css_selector("#custom-input > div.widget-content > div > div.col-12.p-20.bg-white.p-3.border.mb-3 > div > div.col-md-4 > label > input").send_keys("Nama anda")
driver.find_element_by_css_selector("#custom-input > div.widget-content > div > div.col-12.p-20.bg-white.p-3.border.mb-3 > div > div.col-md-8 > label > input").send_keys("Berikan nama lengkap anda")
driver.find_element_by_css_selector("#custom-input > div.widget-content > div > div.col-sm-12.mb-3 > div > div:nth-child(2) > div:nth-child(4) > label").click()#peserta
time.sleep(3)
driver.find_element_by_css_selector("#custom-input > div.widget-content > div > div.col-sm-12.mb-3 > div > div:nth-child(2) > div:nth-child(3) > label").click()#pemesan


driver.find_element_by_xpath("//*[@id='custom-input']/div[2]/div/div[1]/div/div[3]/button[1]").click()
time.sleep(2)
driver.find_element_by_css_selector("#custom-input > div.widget-content > div:nth-child(1) > div.col-sm-12.mb-3 > div > div.col-sm-2 > button.btn.btn-danger.btn-sm.btn-add.remove_custom_input.mt-36.small.display-none.legitRipple").click()

#cek tambahan
#driver.find_element_by_css_selector("#add-on > div.widget-content > div > div.col-sm-12.col-md-6.mt-1 > div:nth-child(1) > label > span").click()
#driver.find_element_by_css_selector("#foot-included > span").click()
#driver.find_element_by_css_selector("#add-on > div.widget-content > div > div.col-sm-12.col-md-6.mt-1 > div.form-group.mt-3.ml-1 > div > label").click()

#diskon
driver.find_element_by_css_selector("#discount_name").send_keys("tes diskon")
driver.find_element_by_css_selector("#discount_amount_type").click()
driver.find_element_by_css_selector("#discount_amount_type > option:nth-child(2)").click()
time.sleep(2)
driver.find_element_by_css_selector("#discount_amount_type > option:nth-child(3)").click()
driver.find_element_by_css_selector("#discount_amount").send_keys("10")

#jaga diri

driver.find_element_by_css_selector("#form_ajax > div:nth-child(10) > div.widget-content > div > div.col-md-8 > div > label > span").click()

#upload image
driver.find_element_by_css_selector("input[aria-describedby=image-name-0]").send_keys(os.getcwd() + "/logo.jpg")
time.sleep(5)
driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > button.btn.btn-primary.btn-crop-image.legitRipple").click()

#tombol submit
time.sleep(3)
driver.find_element_by_css_selector("#btn-submit").click()
time.sleep(5)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success")))
driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()
time.sleep(5)

driver.quit


# ## Cancel Invoice
# Testing Cancel Invoice

# ### Cancel invoice 

# In[ ]:


driver = webdriver.Chrome(executable_path=r'C:\Users\astro\driver\chromedriver.exe') 
driver.maximize_window()
wait = WebDriverWait(driver,20)

driver.get("https://muchimug.gomodo.id/product/detail/SKU5811221602839788609")
time.sleep(4)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#product-detail > div > div.col-md-4 > form > div > div.card-footer.bg-light-blue.hide-notice-err > div #btn-book")))
driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
driver.find_element_by_css_selector("#product-detail > div > div.col-md-4 > form > div > div.card-footer.bg-light-blue.hide-notice-err > div #btn-book").click()
time.sleep(2)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > form > div.bg-white > div > div > div #booking-pay-now")))
driver.find_element_by_css_selector("#content > form > div.bg-white > div > div > div #booking-pay-now").click()

#fill the form
time.sleep(2)
driver.find_element_by_css_selector("#booking-guest > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(5) #full_name").send_keys("tes")

driver.find_element_by_css_selector("#booking-guest > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(6) #email").send_keys("dummy@gmail.com")
driver.find_element_by_css_selector("#booking-guest > div > div:nth-child(2) > div:nth-child(2) > div #phone_number").send_keys("08912312312")
driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
driver.find_element_by_css_selector("#choose-payment > div > div:nth-child(3) > label").click()

time.sleep(4)
driver.find_element_by_css_selector("#content > form > div.bg-white > div > div > div #booking-pay-now").click()
time.sleep(10)

#switch window
driver.execute_script('''window.open("https://gomodo.id/agent/login","_blank");''')
driver.switch_to.window(driver.window_handles[1])

login()

driver.get("https://gomodo.id/company/order")

#invoicenumber = driver.find_element_by_css_selector("#order_table > tbody > tr:nth-child(1) > td:nth-child(2) > a").text
time.sleep(2)
#driver.find_element_by_css_selector("#order_table_filter > label > input[type=search]").send_keys(invoicenumber)
driver.find_element_by_css_selector("#order_table > tbody > tr:nth-child(1) > td:nth-child(8) > button").click()
time.sleep(2)
driver.find_element_by_css_selector("#form_ajax_cancel > div > div > div.modal-footer.justify-content-center > button.btn.modal-trigger.btn-sm.btn-primary.legitRipple").click()
time.sleep(10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#order_table > tbody > tr:nth-child(1) > td.data-table-status > span")))
element_valid_order = driver.find_element_by_css_selector("#order_table > tbody > tr:nth-child(1) > td.data-table-status > span").text
element_valid_order == "Dibatalkan oleh Provider"

driver.quit()


# ### Cancel E-invoice

# In[ ]:


#Launch webdriver
driver = webdriver.Chrome(executable_path=r'C:\Users\astro\driver\chromedriver.exe')
driver.maximize_window()
wait = WebDriverWait(driver,20)

login()

price = 200000
qty = 1

#Go to Create E-Invoice section
driver.get('https://gomodo.id/company/manual-order/create')

#Step 1
time.sleep(5)
driver.find_element_by_xpath("//*[@id='invoice_name']").send_keys("Makan Malam Santai")
driver.find_element_by_xpath("//*[@id='description[]']").send_keys("Tuna Cabe Ijo")
driver.find_element_by_xpath("//*[@id='price[]']").send_keys(price)
driver.find_element_by_xpath("//*[@id='qty[]']").send_keys(qty)
driver.find_element_by_xpath("//*[@id='toStep2']").click()

#Step 2
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='full_name']")))
driver.find_element_by_xpath("//*[@id='full_name']").send_keys("umu")
driver.find_element_by_xpath("//*[@id='phone_number']").send_keys("089123123123")
driver.find_element_by_xpath("//*[@id='email']").send_keys('dummy@gmail.com')
driver.find_element_by_xpath("//*[@id='toStep3']").click()

time.sleep(5)

driver.get("https://gomodo.id/company/manual-order")
time.sleep(2)
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='example']/tbody/tr[1]/td[1]")))
driver.find_element_by_xpath("//*[@id='example']/tbody/tr[1]/td[1]").click()
time.sleep(1)
driver.find_element_by_css_selector("#example > tbody > tr:nth-child(1) > td:nth-child(8) > button").click()
time.sleep(2)
driver.find_element_by_css_selector("#form_ajax_cancel > div > div > div.modal-footer.justify-content-center > button.btn.modal-trigger.btn-sm.btn-primary.legitRipple").click()
time.sleep(10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#example > tbody > tr:nth-child(1) > td:nth-child(2)")))
driver.find_element_by_css_selector("#header > div > div.sidebar-content > div > div.sidebar-user-material > div > div > a > img").click()
driver.find_element_by_css_selector("#example > tbody > tr:nth-child(1) > td:nth-child(2)").click()

driver.find_element_by_css_selector("#navcol-1 > ul > li:nth-child(1) > a").click()
driver.find_element_by_css_selector("#retrieve > div > div > div > div > div > div.col-12.mt-5 > form > div > div.col > div #no_invoice").send_keys("OFINV200902319677")

status = driver.find_element_by_css_selector("#product-booking > div:nth-child(1) > div.card-header > div > div.col-sm-6.text-right > button").text
status == "Dibatalkan oleh sistem"


# ## Setting

# In[ ]:


#Setting
#Launch webdriver
driver = webdriver.Chrome(executable_path=r'C:\Users\astro\driver\chromedriver.exe')
driver.maximize_window()
wait = WebDriverWait(driver,20)

settinglogin()

driver.get('''https://gomodo.id/company/profile''')
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#btn-submit')))

#open header logo change to default logo
driver.find_element_by_css_selector("#header-operator-logo").click()
time.sleep(3)

driver.find_element_by_css_selector("#content-operator-logo > div > div:nth-child(2) > div > div > div > div > label:nth-child(1) > img").click()

driver.find_element_by_css_selector("#btn-submit").click() #submit
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success')))
time.sleep(5)

driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()
driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)
time.sleep(1)
driver.find_element_by_css_selector("#header-operator-logo").click()
time.sleep(5) # liat gambar

#upload image logo

driver.find_element_by_css_selector(" #content-operator-logo > div > div:nth-child(1) > div > div > div > div.custom-logo-block.d-lg-flex.align-items-end.justify-content-center > div.custom-logo-image.position-relative.text-center > label > input[name=logo]").send_keys(os.getcwd()+ "/logo.jpg") #mengiinput file di folder yang sama image
time.sleep(10)
driver.find_element_by_xpath("//*[@id='croppingModal']/div[1]/div/div[3]/button[1]").click()
time.sleep(5)
driver.find_element_by_css_selector("#btn-submit").click() #submit
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success')))

driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header-operator-logo")))
time.sleep(3)
driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)
driver.find_element_by_css_selector("#header-operator-logo").click()
time.sleep(5) # liat gambar 

#Open header and change to default banner

driver.find_element_by_css_selector("#header-banner").click()
time.sleep(3)
driver.find_element_by_css_selector("#content-operator-banner > div > div:nth-child(2) > div > div > div > div > label:nth-child(4) > img").click()
driver.find_element_by_css_selector("#btn-submit").click() #submit
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success')))

driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header-banner")))
time.sleep(5)
driver.find_element_by_css_selector("#header-banner").click()
time.sleep(5) # liat gambar

# Upload Image Banner

driver.find_element_by_css_selector('#content-operator-banner > div > div:nth-child(1) > div > div > div > div.custom-banner-holder.position-relative.text-center > label > input[name=banner]').send_keys(os.getcwd()+ "/banner.jpg") #mengiinput file di folder yang sama image
time.sleep(15)

driver.find_element_by_xpath("//*[@id='croppingModal']/div[1]/div/div[3]/button[1]").click()
time.sleep(5)

driver.find_element_by_css_selector("#btn-submit").click() #submit
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success')))

driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header-banner")))
driver.find_element_by_css_selector("#header-banner").click()
time.sleep(5) # liat gambar dan gambar tidak keluar

driver.find_element_by_css_selector("#header-operator-settings").click()
time.sleep(3)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content-operator-settings > div > div:nth-child(1) > input")))

# Bussiness information

driver.find_element_by_css_selector("#content-operator-settings > div > div:nth-child(1) > input").clear()
driver.find_element_by_css_selector("#content-operator-settings > div > div:nth-child(1) > input").send_keys("tes nama operator")

driver.find_element_by_css_selector("#content-operator-settings > div > div:nth-child(2) > label > a").click()
driver.switch_to.window(driver.window_handles[1])
url_data = "http://muchimug.gomodo.id/"
assert url_data == driver.current_url #  print url
driver.switch_to.window(driver.window_handles[0])

# Input Brief Description
driver.find_element_by_css_selector("#short_description").clear()
driver.find_element_by_css_selector("#short_description").send_keys("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis,")

#switch to iframe tinymce
driver.switch_to.frame(driver.find_element_by_css_selector("iframe#about_ifr"))
driver.find_element_by_css_selector("body[data-id=about]").clear()
driver.find_element_by_css_selector("body[data-id=about]").send_keys("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis,")
driver.switch_to.default_content()

driver.find_element_by_css_selector("#map  #pac-input").send_keys("jalan gurami no 30 sorosutan")
driver.find_element_by_css_selector("#map  #pac-input").send_keys(Keys.ENTER)

driver.switch_to.frame(driver.find_element_by_css_selector("iframe#address_company_ifr"))
driver.find_element_by_css_selector("body[data-id=address_company]").clear()
#alamat 300 char
driver.find_element_by_css_selector("body[data-id=address_company]").send_keys("jalan gurami no 30 sorosutan,umbulharjo,yogyakarta 55123,,,jalan gurami no 30 sorosutan,umbulharjo,yogyakarta 55123,,,jalan gurami no 30 sorosutan,umbulharjo,yogyakarta 55123,,,jalan gurami no 30 sorosutan,umbulharjo,yogyakarta 55123,,,jalan gurami no 30 sorosutan,umbulharjo,yogyakarta 55123,,,12345")
driver.switch_to.default_content()

#re-data-cover
driver.find_element_by_css_selector("#email_company").clear()
driver.find_element_by_css_selector("#email_company").send_keys("dummy@gmail.com")

driver.find_element_by_css_selector("#phone_company").clear()
driver.find_element_by_css_selector("#phone_company").send_keys("081111111111")

driver.find_element_by_css_selector("#facebook_company").clear()
driver.find_element_by_css_selector("#facebook_company").send_keys("anime")
driver.find_element_by_css_selector("#twitter_company").clear()
driver.find_element_by_css_selector("#twitter_company").send_keys("anime")

#SEO
driver.find_element_by_css_selector("#seo-header").click()
time.sleep(3)

driver.find_element_by_css_selector("#content-seo > div > div:nth-child(1) > input").clear()
driver.find_element_by_css_selector("#content-seo > div > div:nth-child(1) > input").send_keys("Muchi Mug,,,Muchi Mug,,,Muchi Mug,,,Muchi Mug,,,Muchi Mug,,,Muchi Mug,")
driver.find_element_by_css_selector("#description").clear()
driver.find_element_by_css_selector("#description").send_keys("Muchi Mug adalah perusahaan berbasis gomodo dan menunjang yang namanya kemanusian,,,,Muchi Mug adalah perusahaan berbasis gomodo dan menunjang yang na")
driver.find_element_by_css_selector("#content-seo > div > div:nth-child(3) > span > span.selection > span > ul > li:nth-child(1) > span").click()
driver.find_element_by_css_selector("#content-seo > div > div:nth-child(3) > span > span.selection > span > ul > li:nth-child(1) > span").click()
time.sleep(1)
driver.find_element_by_css_selector("#content-seo > div > div:nth-child(3) > span > span.selection > span > ul > li.select2-search.select2-search--inline > input").send_keys("Muchi Mug,platform,pemesaan,booking,dll,gomodo,Muchi Mug,platform,pemesaan,booking,dll,gomodo,Muchi Mug,platform,pemesaan,booking,dll,gomodo,Muchi Mug,platform,pemesaan,booking,dll,gomodo,Muchi Mug,platform,pemesaan,booking,dll,gomodo,Muchi Mug,platform,pemesaan,booking,dll,gomodo,Muchi Mug,platform,pemesaan,booking,dll,gomodo,Muchi Mug,platform,pemesaan,booking,dll,gomodo,Muchi Mug,platform,pemesaan,booking,dll,gomodo,Muchi Mug,platform,pemesaan,booking,dll,gomodo,Muchi Mug,platform,pemesaan,bo")

#bank
driver.find_element_by_css_selector("#header-bank").click()
time.sleep(8)

driver.find_element_by_css_selector("#content-bank > div > div:nth-child(1) > span > span.selection > span").click()
time.sleep(3)

driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("bank negara indonesia")
time.sleep(10)
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)

driver.find_element_by_css_selector("#content-bank > div > div:nth-child(2) > input").clear()
driver.find_element_by_css_selector("#content-bank > div > div:nth-child(2) > input").send_keys("om kun")
driver.find_element_by_css_selector("#account").clear()
driver.find_element_by_css_selector("#account").send_keys("09001929389182")
time.sleep(3)

driver.find_element_by_css_selector('#content-bank > div > div.form-group.bank-document-container.text-center > label.custom-input-cropping-image > input[name=bank_account_document]').send_keys(os.getcwd()+ "/banner.jpg")
time.sleep(6)
driver.find_element_by_xpath("//*[@id='croppingModal']/div[1]/div/div[3]/button[1]").click()
time.sleep(10)

#password
time.sleep(4)
driver.find_element_by_css_selector("#header-operator-settings-password").click()
driver.find_element_by_css_selector("#old_password").send_keys("password12")
driver.find_element_by_css_selector("#content-password  #password").send_keys("password21")
driver.find_element_by_css_selector("#content-password  #password_confirmation").send_keys("password21")

driver.find_element_by_css_selector("#btn-submit").click()


# In[ ]:


#keluar dan mencoba kembali login
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success")))
driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()

#tombol log out
driver.find_element_by_css_selector("#header > div > div.sidebar-content > div > div.card.card-sidebar-mobile > ul > li:nth-child(10) > a").click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#email")))
driver.find_element_by_css_selector("#email").send_keys("dummy@ygmail.com")

driver.find_element_by_css_selector("#regForm > div > div > div.form-group.form-group-feedback.form-group-feedback-left.input-group > input").send_keys("gomodo321")
time.sleep(2)

driver.find_element_by_css_selector("#submitButton").click()
time.sleep(2)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#header > div > div.sidebar-content > div > div.card.card-sidebar-mobile > ul > li:nth-child(11) > a > span')))


# In[ ]:


#mengembalikan password
#Setting

time.sleep(5)
driver.get('''http://gomodo.id/company/profile''')
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#btn-submit')))

time.sleep(4)
driver.find_element_by_css_selector("#header-operator-settings-password").click()
driver.find_element_by_css_selector("#old_password").send_keys("password21")
driver.find_element_by_css_selector("#content-password  #password").send_keys("password12")
driver.find_element_by_css_selector("#content-password  #password_confirmation").send_keys("password12")

driver.find_element_by_css_selector("#btn-submit").click()


# In[ ]:


#swal open
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success")))
driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()

#cari perubahan email
time.sleep(6)
driver.find_element_by_css_selector("#header-bank").click()
driver.find_element_by_css_selector("#content-bank > div > div.alert.alert-info.text-center").text

#email

#cek yopmail
driver.execute_script('''window.open("http://www.yopmail.com/en/");''')
driver.switch_to.window(driver.window_handles[2])
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#login")))
driver.find_element_by_css_selector("#login").clear()
driver.find_element_by_css_selector("#login").send_keys("dummy")
driver.find_element_by_css_selector("#login").send_keys(Keys.ENTER)
time.sleep(10)

driver.switch_to.window(driver.window_handles[0])
#kembali ke menu setting dan refresh
driver.get('''http://gomodo.id/company/profile''')

driver.find_element_by_css_selector("#header-bank").click()
time.sleep(5)

driver.quit()


# ### Test Image Upload 

# In[ ]:


#Setting
#Launch webdriver
driver = webdriver.Chrome(executable_path=r'C:\Users\astro\driver\chromedriver.exe')
driver.maximize_window()
wait = WebDriverWait(driver,20)

settinglogin()

#header logo bisnis
driver.get('http://gomodo.id/company/profile')
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#btn-submit")))
time.sleep(5)
driver.find_element_by_css_selector("#header-operator-logo").click()
driver.find_element_by_css_selector("#content-operator-logo > div > div:nth-child(2) > div > div > div > div > label:nth-child(2) > img").click()
driver.find_element_by_css_selector("#btn-submit").click()
time.sleep(2)
driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#btn-submit")))
driver.find_element_by_css_selector("#header-operator-logo").click()
driver.find_element_by_css_selector("#content-operator-logo > div > div:nth-child(2) > div > div > div > div > label:nth-child(3) > img").click()
driver.find_element_by_css_selector("#btn-submit").click()
time.sleep(2)
driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#btn-submit")))
driver.find_element_by_css_selector("#header-operator-logo").click()
driver.find_element_by_css_selector("#content-operator-logo > div > div:nth-child(2) > div > div > div > div > label:nth-child(4) > img").click()
driver.find_element_by_css_selector("#btn-submit").click()
time.sleep(2)
driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#btn-submit")))
driver.find_element_by_css_selector("#header-operator-logo").click()
driver.find_element_by_css_selector("#content-operator-logo > div > div:nth-child(2) > div > div > div > div > label:nth-child(5) > img").click()
driver.find_element_by_css_selector("#btn-submit").click()
time.sleep(2)
driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#btn-submit")))
driver.find_element_by_css_selector("#header-operator-logo").click()
driver.find_element_by_css_selector("#content-operator-logo > div > div:nth-child(2) > div > div > div > div > label:nth-child(1) > img").click()
driver.find_element_by_css_selector("#btn-submit").click()
time.sleep(2)
driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#btn-submit")))
driver.find_element_by_css_selector("#header-operator-logo").click()
driver.find_element_by_css_selector(" #content-operator-logo > div > div:nth-child(1) > div > div > div > div.custom-logo-block.d-lg-flex.align-items-end.justify-content-center > div.custom-logo-image.position-relative.text-center > label > input[name=logo]").send_keys(os.getcwd()+ "/image10.jpg") #mengiinput file di folder yang sama image
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > button.btn.btn-primary.btn-crop-image.legitRipple")))
driver.find_element_by_css_selector("#btn-zoom-in").click()
driver.find_element_by_css_selector("#btn-zoom-out").click()
driver.find_element_by_css_selector("#btn-up").click()
driver.find_element_by_css_selector("#btn-down").click()
driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > div > button:nth-child(5)").click()
driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > div > button:nth-child(5)").click()
driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > div > button:nth-child(5)").click()
driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > div > button:nth-child(6)").click()
driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > button.btn.btn-danger.cancel-crop.legitRipple").click()
driver.find_element_by_css_selector("#btn-submit").click()
time.sleep(2)
driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#btn-submit")))
time.sleep(5)
driver.find_element_by_css_selector("#header-operator-logo").click()
driver.find_element_by_css_selector(" #content-operator-logo > div > div:nth-child(1) > div > div > div > div.custom-logo-block.d-lg-flex.align-items-end.justify-content-center > div.custom-logo-image.position-relative.text-center > label > input[name=logo]").send_keys(os.getcwd()+ "/image10.jpg") #mengiinput file di folder yang sama image
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > button.btn.btn-primary.btn-crop-image.legitRipple")))
driver.find_element_by_css_selector("#btn-zoom-in").click()
driver.find_element_by_css_selector("#btn-zoom-out").click()
driver.find_element_by_css_selector("#btn-up").click()
driver.find_element_by_css_selector("#btn-down").click()
driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > div > button:nth-child(5)").click()
driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > div > button:nth-child(5)").click()
driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > div > button:nth-child(5)").click()
driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > div > button:nth-child(6)").click()
driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > button.btn.btn-primary.btn-crop-image.legitRipple").click()
driver.find_element_by_css_selector("#btn-submit").click()
time.sleep(2)
driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#btn-submit")))
time.sleep(5)
driver.find_element_by_css_selector("#header-operator-logo").click()
driver.find_element_by_css_selector("#content-operator-logo > div > div:nth-child(1) > div > div > div > div.custom-logo-block.d-lg-flex.align-items-end.justify-content-center > div.custom-logo-image.position-relative.text-center > div.text-center > div > div > button").click()
driver.find_element_by_css_selector("#btn-submit").click()
time.sleep(2)
driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()

# Banner test
#header banner
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#btn-submit")))
driver.find_element_by_css_selector("#header-banner").click()
driver.find_element_by_css_selector("#content-operator-banner > div > div:nth-child(2) > div > div > div > div > label:nth-child(2) > img").click()
driver.find_element_by_css_selector("#btn-submit").click()
time.sleep(2)
driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#btn-submit")))
driver.find_element_by_css_selector("#header-banner").click()
driver.find_element_by_css_selector("#content-operator-banner > div > div:nth-child(2) > div > div > div > div > label:nth-child(3) > img").click()
driver.find_element_by_css_selector("#btn-submit").click()
time.sleep(2)
driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#btn-submit")))
driver.find_element_by_css_selector("#header-banner").click()
driver.find_element_by_css_selector("#content-operator-banner > div > div:nth-child(2) > div > div > div > div > label:nth-child(4) > img").click()
driver.find_element_by_css_selector("#btn-submit").click()
time.sleep(2)
driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#btn-submit")))
driver.find_element_by_css_selector("#header-banner").click()
driver.find_element_by_css_selector("#content-operator-banner > div > div:nth-child(2) > div > div > div > div > label:nth-child(1) > img").click()
driver.find_element_by_css_selector("#btn-submit").click()
time.sleep(2)
driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#btn-submit")))
driver.find_element_by_css_selector("#header-banner").click()
driver.find_element_by_css_selector("#content-operator-banner > div > div:nth-child(1) > div > div > div > div.custom-banner-holder.position-relative.text-center > label > input").send_keys(os.getcwd()+ "/image10.jpg") #mengiinput file di folder yang sama image
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > button.btn.btn-primary.btn-crop-image.legitRipple")))
driver.find_element_by_css_selector("#btn-zoom-in").click()
driver.find_element_by_css_selector("#btn-zoom-out").click()
driver.find_element_by_css_selector("#btn-up").click()
driver.find_element_by_css_selector("#btn-down").click()
driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > div > button:nth-child(5)").click()
driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > div > button:nth-child(5)").click()
driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > div > button:nth-child(5)").click()
driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > div > button:nth-child(6)").click()
driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > button.btn.btn-danger.cancel-crop.legitRipple").click()
driver.find_element_by_css_selector("#btn-submit").click()
time.sleep(2)
driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#btn-submit")))
driver.find_element_by_css_selector("#header-banner").click()
driver.find_element_by_css_selector("#content-operator-banner > div > div:nth-child(1) > div > div > div > div.custom-banner-holder.position-relative.text-center > label > input").send_keys(os.getcwd()+ "/image10.jpg") #mengiinput file di folder yang sama image
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > button.btn.btn-primary.btn-crop-image.legitRipple")))
driver.find_element_by_css_selector("#btn-zoom-in").click()
driver.find_element_by_css_selector("#btn-zoom-out").click()
driver.find_element_by_css_selector("#btn-up").click()
driver.find_element_by_css_selector("#btn-down").click()
driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > div > button:nth-child(5)").click()
driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > div > button:nth-child(5)").click()
driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > div > button:nth-child(5)").click()
driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > div > button:nth-child(6)").click()
driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > button.btn.btn-primary.btn-crop-image.legitRipple").click()
driver.find_element_by_css_selector("#btn-submit").click()
time.sleep(2)
driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#btn-submit")))
driver.find_element_by_css_selector("#header-banner").click()
driver.find_element_by_css_selector("#content-operator-banner > div > div:nth-child(1) > div > div > div > div.custom-banner-holder.position-relative.text-center > div.text-center > div > div > button").click()
driver.find_element_by_css_selector("#btn-submit").click()
time.sleep(2)
driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()

driver.quit()


# ## Article

# In[ ]:


#Setting
#Launch webdriver
driver = webdriver.Chrome(executable_path=r'C:\Users\astro\driver\chromedriver.exe')
driver.maximize_window()
wait = WebDriverWait(driver,20)

settinglogin()

#buka artikel dan search
driver.get('''http://gomodo.id/company/article''')
time.sleep(4)
driver.find_element_by_css_selector("#content > div.content.pt-0 > div:nth-child(4) > div > div.sidebar.sidebar-light.bg-transparent.sidebar-component.sidebar-component-right.border-0.shadow-0.order-1.order-md-2.sidebar-expand-md > div > div:nth-child(1) > div.card-body > form > div > #search_data_blog").send_keys("tes 2")
driver.find_element_by_css_selector("#content > div:nth-child(1) > div > div").click()
time.sleep(4)
driver.find_element_by_css_selector("#render_blog_list > div.card > div.card-footer.bg-transparent.d-sm-flex.justify-content-sm-between.align-items-sm-center.border-top-0.pt-0.pb-3 > a").click()
time.sleep(3)
driver.find_element_by_css_selector("button[id=backToBlog]").click()
time.sleep(7)

driver.quit()


# ## Voucher 

# In[ ]:


#Launch webdriver
driver = webdriver.Chrome(executable_path=r'C:\Users\astro\driver\chromedriver.exe')
driver.maximize_window()
wait = WebDriverWait(driver,20)

login()

#test isi form
driver.get('''http://kadalmacho.top/company/voucher/create''')
#unik
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(2) > div > div > div:nth-child(1) > div > input").send_keys(vouchercode)#unik
#/
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(2) > div > div > div:nth-child(4) > div > input").send_keys("10000")
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(3) > div > div > div:nth-child(1) > div > input").send_keys("1")
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(3) > div > div > div:nth-child(2) > div > input").send_keys("100")

#pilih tanggal
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(3) > div > div > div:nth-child(3) > div > input").click()
time.sleep(1)
#driver.find_element_by_css_selector("body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-top > div.datepicker-days > table > tbody > tr:nth-child(6) > td:nth-child(5)").click()
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(3) > div > div > div:nth-child(3) > div > input").clear()
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(3) > div > div > div:nth-child(3) > div > input").send_keys("16/07/2020")
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(3) > div > div > div:nth-child(4) > div > input").send_keys(Keys.ENTER)

time.sleep(3)
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(3) > div > div > div:nth-child(4) > div > input").click()
time.sleep(2)
#driver.find_element_by_css_selector("body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-bottom > div.datepicker-days > table > tbody > tr:nth-child(4) > td:nth-child(6)").click()
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(3) > div > div > div:nth-child(4) > div > input").clear()
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(3) > div > div > div:nth-child(4) > div > input").send_keys("25/10/2020")
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(3) > div > div > div:nth-child(4) > div > input").send_keys(Keys.ENTER)

driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(4) > div > div > div:nth-child(1) > div > input").send_keys("10000")
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(4) > div > div > div:nth-child(2) > div > input").send_keys("1")
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(4) > div > div > div:nth-child(4) > div > span > span.selection > span > ul > li > input").send_keys("tes 16/3/2020")
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(4) > div > div > div:nth-child(4) > div > span > span.selection > span > ul > li > input").send_keys(Keys.ENTER)

driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(5) > div > div > div > div > input").send_keys("tes voucer")


# ## Insurance

# In[ ]:


#Launch webdriver
driver = webdriver.Chrome(executable_path=r'C:\Users\astro\driver\chromedriver.exe')
driver.maximize_window()
wait = WebDriverWait(driver,20)

login()

driver.switch_to.window(driver.window_handles[0])
driver.get('''http://gomodo.id/company/insurance''')
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#form_ajax_insurance > div.dashboard-cta.d-md-flex.justify-content-between > button")))
driver.find_element_by_css_selector("#form_ajax_insurance > div.widget.card > div.widget-content > div > div:nth-child(2) > div > div > textarea").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Libero enim sed faucibus turpis in. Lorem dolor sed viverra ipsum nunc aliquet. Nunc vel risus commodo viverra. Sem fringilla ut morbi tincidunt augue interdum velit. Suspendis")
driver.find_element_by_css_selector("#form_ajax_insurance > div.dashboard-cta.d-md-flex.justify-content-between > button").click()

driver.quit()


# ## Distribution

# In[ ]:


#Launch webdriver
driver = webdriver.Chrome(executable_path=r'C:\Users\astro\driver\chromedriver.exe')
driver.maximize_window()
wait = WebDriverWait(driver,20)

login()

driver.switch_to.window(driver.window_handles[0])
driver.get('''http://gomodo.id/company/distribution''')
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#form_ajax_distribution > div.dashboard-cta.d-md-flex.justify-content-between > button")))
driver.find_element_by_css_selector("#form_ajax_distribution > div.widget.card > div.widget-content > div > div:nth-child(2) > div > div > textarea").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Libero enim sed faucibus turpis in. Lorem dolor sed viverra ipsum nunc aliquet. Nunc vel risus commodo viverra. Sem fringilla ut morbi tincidunt augue interdum velit. Suspendis")
driver.find_element_by_css_selector("#form_ajax_distribution > div.dashboard-cta.d-md-flex.justify-content-between > button").click()


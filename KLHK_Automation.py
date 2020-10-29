#!/usr/bin/env python
# coding: utf-8

# # Starting

# In[5]:


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

 
get_ipython().run_line_magic('load_ext', 'ipython_unittest')
fake = Faker('id_ID')

driver = webdriver.Chrome(executable_path=r'C:\Users\Lenovo\driver\chromedriver.exe') #Launch Chrome Webdriver

wait = WebDriverWait(driver,30)
driver.maximize_window()


# In[6]:


#variable

newproviderklhk = ["klhktest1"]
emailklhk = ["klhk1@yopmail.com"]
productklhk = ["tes klhk product 28/5/2020"]


def filterd():
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#main > div.row > div.col-sm-4.col-md-3.sidebar #apply-filter")))
    slide = driver.find_element_by_xpath("//*[@id='price-range']/a[2]")
    move = AC(driver)
    move.click_and_hold(slide).move_by_offset(40,0).release().perform()
    time.sleep(2)
    #move.click_and_hold(slide).move_by_offset(10,0).release().perform()
    driver.find_element_by_css_selector("#main > div.row > div.col-sm-4.col-md-3.sidebar > div > div:nth-child(2) > h4 > a").click()
    time.sleep(1)
    driver.find_element_by_css_selector("#product-categories > li:nth-child(1) > a").click()
    driver.find_element_by_css_selector("#main > div.row > div.col-sm-4.col-md-3.sidebar > div > div:nth-child(3) > h4 > a").click()
    time.sleep(1)
    driver.find_element_by_css_selector("#guides > li > a").click()
    driver.find_element_by_css_selector("#main > div.row > div.col-sm-4.col-md-3.sidebar #apply-filter").click()


# In[15]:


#validation string
errorfin_string = ["#amount-error"]


# ## Form universal

# ### Product form input

# In[7]:


#create product
def product():
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#mapGoogle > div > div > div:nth-child(1) > div:nth-child(3)")))
    #unik
    time.sleep(3)
    driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-5 > div:nth-child(1) > input").send_keys(productklhk)
    #/
    driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-5 > div:nth-child(2) > span > span.selection > span > ul > li > input").click()
    time.sleep(2)
    driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-5 > div:nth-child(2) > span > span.selection > span > ul > li > input").send_keys("Atraksi")
    time.sleep(1)
    driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-5 > div:nth-child(2) > span > span.selection > span > ul > li > input").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-5 > div:nth-child(2) > span > span.selection > span > ul > li > input").send_keys("Akrobatik")
    time.sleep(1)
    driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-5 > div:nth-child(2) > span > span.selection > span > ul > li > input").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-5 > div:nth-child(2) > span > span.selection > span > ul > li > input").send_keys("Naik ATV")
    time.sleep(1)
    driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-5 > div:nth-child(2) > span > span.selection > span > ul > li > input").send_keys(Keys.ENTER)
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
    driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-7 > div:nth-child(3) > span > span.selection > span > ul > li > input").click()
    driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-7 > div:nth-child(3) > span > span.selection > span > ul > li > input").send_keys("english")
    driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-7 > div:nth-child(3) > span > span.selection > span > ul > li > input").send_keys(Keys.ENTER)
    driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-7 > div:nth-child(3) > span > span.selection > span > ul > li > input").send_keys("indonesia")
    driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-7 > div:nth-child(3) > span > span.selection > span > ul > li > input").send_keys(Keys.ENTER)
    driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-7 > div.form-group.select-icon-dropdown > #product_type").click()
    driver.find_element_by_css_selector("#product_type > option:nth-child(2)").click()
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
    time.sleep(2)
    #driver.find_element_by_css_selector("#add-on > div.widget-content > div > div.col-sm-12.col-md-6.mt-1 > div:nth-child(1) > label > span").click()
    #driver.find_element_by_css_selector("/html/body/div[3]/div[2]/section/div[2]/div[4]/div/div/form/div[6]/div[2]/div/div[1]/div[2]/label/span").click()
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
    driver.find_element_by_css_selector("#croppingModal > div.modal-dialog.modal-lg > div > div.modal-footer > button.btn.btn-success.btn-crop-image.legitRipple").click()
    #isi rute perjalanan
    driver.switch_to.frame(driver.find_element_by_css_selector("iframe#itinerary_0_ifr"))
    driver.find_element_by_css_selector("body[data-id=itinerary_0]").clear()
    driver.find_element_by_css_selector("body[data-id=itinerary_0]").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc mi ipsum faucibus vitae aliquet nec ullamcorper. Eget nunc lobortis mattis aliquam faucibus purus in. Blandit volutpat maecenas volutpat blandit aliquam etiam erat velit. Etiam sit amet nisl purus in mollis nunc sed id. Euismod in pellentesque massa placerat duis ultricies. Enim sed faucibus turpis in eu. Sed pulvinar proin gravida hendrerit lectus a. Nisl nunc mi ipsum faucibus vitae aliquet nec ullamcorper sit. Diam quam nulla porttitor massa id neque. Vitae proin sagittis nisl rhoncus mattis rhoncus. Nunc congue nisi vitae suscipit tellus mauris a. Donec pretium vulputate sapien nec sagittis. Quisque sagittis purus sit amet volutpat consequat mauris nunc congue. Metus dictum at tempor commodo. Morbi tempus iaculis urna id volutpat. Quis auctor elit sed vulputate. Volutpat blandit aliquam etiam erat velit scelerisque in. Amet tellus cras adipiscing enim. Dolor sed viverra ipsum nunc aliquet bibendum enim facilisis. Auctor elit sed vulputate mi sit amet mauris. Feugiat scelerisque varius morbi enim nunc faucibus a pellentesque sit. Vulputate odio ut enim blandit volutpat maecenas volutpat blandit aliquam. Neque laoreet suspendisse interdum consectetur libero id faucibus. Tincidunt nunc pulvinar sapien et. Elit ut aliquam purus sit amet luctus. Vestibulum lorem sed risus ultricies. Enim tortor at auctor urna nunc. Nullam vehicula ipsum a arcu. Tincidunt augue interdum velit euismod in pellentesque massa placerat. Faucibus et molestie ac feugiat sed. Commodo elit at imperdiet dui accumsan sit amet nulla facilisi. Commodo quis imperdiet massa tincidunt nunc pulvinar. Egestas integer eget aliquet nibh praesent tristique. Eget egestas purus viverra accumsan in nisl nisi. Elementum pulvinar etiam non quam lacus suspendisse. Egestas fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate. Amet nulla facilisi morbi tempus iaculis urna id volutpat. Id velit ut tortor pretium viverra suspendisse potenti. Imperdiet massa tincidunt nunc pulvinar sapien et ligula ullamcorper. Eget nunc scelerisque viverra mauris in aliquam sem fringilla ut. In est ante in nibh mauris cursus mattis. Molestie a iaculis at erat pellentesque adipiscing commodo elit at. Molestie a iaculis at erat pellentesque adipiscing commodo. Suspendisse interdum consectetur libero id faucibus nisl tincidunt eget. Faucibus pulvinar elementum integer enim neque. Condimentum mattis pellentesque id nibh tortor id aliquet. Pellentesque nec nam aliquam sem et. Habitasse platea dictumst quisque sagittis purus sit amet volutpat consequat. Morbi tincidunt ornare massa eget. Mauris sit amet massa vitae tortor condimentum. Adipiscing diam donec adipiscing tristique risus nec feugiat. Nec nam aliquam sem et tortor consequat id porta. Posuere sollicitudin aliquam ultrices sagittis orci a. Sagittis eu volutpat odio facilisis mauris sit. Leo a diam sollicitudin tempor id eu. Id diam vel quam elementum. Ultrices mi tempus imperdiet nulla. Et egestas quis ipsum suspendisse ultrices gravida dictum fusce. Eleifend quam adipiscing vitae proin sagittis nisl rhoncus. Quis hendrerit dolor magna eget est lorem ipsum dolor sit. Posuere sollicitudin aliquam ultrices sagittis orci a. Tortor pretium viverra suspendisse potenti. Adipiscing at in tellus integer. Sem et tortor consequat id. Vitae tempus quam pellentesque nec nam. Tortor at auctor urna nunc id cursus metus aliquam eleifend. Feugiat in ante metus dictum at tempor. Sollicitudin tempor id eu nisl. Fames ac turpis egestas sed tempus. Iaculis nunc sed augue lacus. Vel quam elementum pulvinar etiam non quam lacus suspendisse faucibus. Pellentesque adipiscing commodo elit at. Rhoncus urna neque viverra justo nec ultrices dui. Elementum sagittis vitae et leo duis ut diam quam nulla. At lectus urna duis convallis. Odio tempor orci dapibus ultrices in iaculis. Sit amet nisl suscipit adipiscing bibendum. Orci porta non pulvinar neque laoreet suspendisse. Volutpat lacus laoreet non curabitur gravida arcu. Tristique senectus et netus et malesuada fames. Vitae purus faucibus ornare suspendisse sed nisi lacus. Fusce id velit ut tortor pretium viverra suspendisse potenti. Vivamus at augue eget arcu dictum varius. Sem integer vitae justo eget magna fermentum iaculis eu. Vulputate mi sit amet mauris commodo quis imperdiet. Tortor dignissim convallis aenean et tortor at. Morbi non arcu risus quis varius quam quisque. Id diam maecenas ultricies mi eget mauris. In aliquam sem fringilla ut morbi tincidunt. Enim ut sem viverra aliquet eget sit amet. Odio ut enim blandit volutpat. Congue eu consequat ac felis donec. Facilisi cras fermentum odio eu feugiat pretium. At consectetur lorem donec massa sapien faucibus. Pretium nibh ipsum consequat nisl vel pretium lectus quam id. Massa massa ultricies mi quis hendrerit dolor. Phasellus vestibulum lorem sed risus ultricies tristique nulla aliquet enim. Et ligula ullamcorper malesuada proin libero nunc consequat. Consectetur adipiscing elit ut aliquam purus sit amet luctus venenatis. Risus nullam eget felis eget. Congue mauris rhoncus aenean vel. Dui vivamus arcu felis bibendum ut tristique. Mauris cursus mattis molestie a iaculis at erat. Sem fringilla ut morbi tincidunt augue. A iaculis at erat pellentesque adipiscing commodo elit at imperdiet. Vestibulum morbi blandit cursus risus at ultrices mi tempus. Mi eget mauris pharetra et ultrices neque ornare. Tortor dignissim convallis aenean et tortor at risus. Scelerisque mauris pellentesque pulvinar pellentesque habitant morbi tristique. Pretium vulputate sapien nec sagittis aliquam malesuada bibendum. Consectetur purus ut faucibus pulvinar elementum integer enim. Sapien pellentesque habitant morbi tristique senectus et netus. Risus nullam eget felis eget. Eu sem integer vitae justo eget magna fermentum iaculis eu. Sed risus ultricies tristique nulla aliquet enim tortor at. Platea dictumst vestibulum rhoncus est pellentesque elit ullamcorper. Facilisi cras fermentum odio eu feugiat pretium nibh ipsum consequat. Risus feugiat in ante metus dictum at tempor commodo ullamcorper. Tincidunt nunc pulvinar sapien et ligula ullamcorper malesuada proin libero. Senectus et netus et malesuada fames ac. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed. Tellus pellentesque eu tincidunt tortor aliquam nulla. In dictum non consectetur a erat. Velit euismod in pellentesque massa placerat. Nibh sit amet commodo nulla. Placerat orci nulla pellentesque dignissim. Aliquet nibh praesent tristique magna sit. Nunc eget lorem dolor sed. Varius quam quisque id diam vel quam. Viverra nibh cras pulvinar mattis. Nunc lobortis mattis aliquam faucibus purus in massa tempor. Leo vel fringilla est ullamcorper eget. Lorem mollis aliquam ut porttitor. Dictum varius duis at consectetur lorem. Enim nec dui nunc mattis enim ut tellus elementum sagittis. Est ante in nibh mauris cursus. In tellus integer feugiat scelerisque varius morbi enim. Rhoncus dolor purus non enim praesent elementum facilisis leo vel. Amet nulla facilisi morbi tempus iaculis. Aliquam sem fringilla ut morbi. Tincidunt augue interdum velit euismod in pellentesque massa. Posuere morbi leo urna molestie at elementum eu facilisis. Aenean pharetra magna ac placerat vestibulum. Et malesuada fames ac turpis. Dui id ornare arcu odio ut sem nulla pharetra. Leo vel fringilla est ullamcorper eget nulla facilisi etiam. Facilisi cras fermentum odio eu feugiat pretium nibh ipsum consequat. In nisl nisi scelerisque eu ultrices vitae auctor. Erat velit scelerisque in dictum non consectetur a erat nam. Gravida rutrum quisque non tellus orci ac auctor augue. Vestibulum rhoncus est pellentesque elit ullamcorper dignissim cras tincidunt. Consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus. Ut morbi tincidunt augue interdum velit euismod. Diam ut venenatis tellus in metus vulputate eu. Nisl nunc mi ipsum faucibus. Consectetur adipiscing elit ut aliquam purus sit amet luctus venenatis. Condimentum lacinia quis vel eros donec ac odio. Ut morbi tincidunt augue interdum. Leo a diam sollicitudin tempor id eu nisl. Donec enim diam vulputate ut. Dolor sit amet consectetur adipiscing elit ut aliquam purus. Fusce ut placerat orci nulla pellentesque dignissim enim. Mattis rhoncus urna neque viverra justo nec ultrices dui sapien. Vulputate enim nulla aliquet porttitor lacus luctus accumsan tortor posuere. Id neque aliquam vestibulum morbi blandit cursus risus. Eget aliquet nibh praesent tristique. Scelerisque varius morbi enim nunc faucibus a. Interdum velit laoreet id donec ultrices tincidunt arcu. Elementum curabitur vitae nunc sed velit dignissim sodales ut eu. Massa tempor nec feugiat nisl pretium fusce id velit. Ultrices vitae auctor eu augue ut lectus. Id diam vel quam elementum pulvinar etiam non. In arcu cursus euismod quis viverra nibh cras pulvinar. At varius vel pharetra vel. Aliquet porttitor lacus luctus accumsan tortor posuere ac. A iaculis at erat pellentesque adipiscing commodo elit at. Massa tincidunt dui ut ornare lectus sit. Pellentesque nec nam aliquam sem et tortor consequat id. Tristique magna sit amet purus gravida. Quam adipiscing vitae proin sagittis nisl. Eget nunc lobortis mattis aliquam faucibus. Cursus eget nunc scelerisque viverra mauris in. Aliquam ut porttitor leo a diam sollicitudin tempor id eu. Etiam dignissim diam quis enim lobortis. Vel turpis nunc eget lorem dolor. Consequat interdum varius sit amet mattis vulputate enim nulla aliquet. Tristique senectus et netus et malesuada. Mattis vulputate enim nulla aliquet porttitor lacus luctus accumsan tortor. Et malesuada fames ac turpis egestas maecenas pharetra convallis. Venenatis lectus magna fringilla urna porttitor rhoncus dolor. Ac odio tempor orci dapibus ultrices in iaculis nunc. Vitae justo eget magna fermentum. Amet commodo nulla facilisi nullam vehicula ipsum a. Maecenas pharetra convallis posuere morbi leo urna molestie at elementum. Consectetur a erat nam at lectus urna. Suscipit adipiscing bibendum est ultricies integer quis. Tincidunt augue interdum velit euismod. Iaculis urna id volutpat lacus laoreet non curabitur. Eu lobortis elementum nibh tellus.")
    driver.switch_to.default_content()

    #tambah hari
    driver.find_element_by_css_selector("#add_day").click()
    time.sleep(2)
    driver.switch_to.frame(driver.find_element_by_css_selector("iframe#itinerary_1_ifr"))
    driver.find_element_by_css_selector("body[data-id=itinerary_1]").clear()
    driver.find_element_by_css_selector("body[data-id=itinerary_1]").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nunc mi ipsum faucibus vitae aliquet nec ullamcorper. Eget nunc lobortis mattis aliquam faucibus purus in. Blandit volutpat maecenas volutpat blandit aliquam etiam erat velit. Etiam sit amet nisl purus in mollis nunc sed id. Euismod in pellentesque massa placerat duis ultricies. Enim sed faucibus turpis in eu. Sed pulvinar proin gravida hendrerit lectus a. Nisl nunc mi ipsum faucibus vitae aliquet nec ullamcorper sit. Diam quam nulla porttitor massa id neque. Vitae proin sagittis nisl rhoncus mattis rhoncus. Nunc congue nisi vitae suscipit tellus mauris a. Donec pretium vulputate sapien nec sagittis. Quisque sagittis purus sit amet volutpat consequat mauris nunc congue. Metus dictum at tempor commodo. Morbi tempus iaculis urna id volutpat. Quis auctor elit sed vulputate. Volutpat blandit aliquam etiam erat velit scelerisque in. Amet tellus cras adipiscing enim. Dolor sed viverra ipsum nunc aliquet bibendum enim facilisis. Auctor elit sed vulputate mi sit amet mauris. Feugiat scelerisque varius morbi enim nunc faucibus a pellentesque sit. Vulputate odio ut enim blandit volutpat maecenas volutpat blandit aliquam. Neque laoreet suspendisse interdum consectetur libero id faucibus. Tincidunt nunc pulvinar sapien et. Elit ut aliquam purus sit amet luctus. Vestibulum lorem sed risus ultricies. Enim tortor at auctor urna nunc. Nullam vehicula ipsum a arcu. Tincidunt augue interdum velit euismod in pellentesque massa placerat. Faucibus et molestie ac feugiat sed. Commodo elit at imperdiet dui accumsan sit amet nulla facilisi. Commodo quis imperdiet massa tincidunt nunc pulvinar. Egestas integer eget aliquet nibh praesent tristique. Eget egestas purus viverra accumsan in nisl nisi. Elementum pulvinar etiam non quam lacus suspendisse. Egestas fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate. Amet nulla facilisi morbi tempus iaculis urna id volutpat. Id velit ut tortor pretium viverra suspendisse potenti. Imperdiet massa tincidunt nunc pulvinar sapien et ligula ullamcorper. Eget nunc scelerisque viverra mauris in aliquam sem fringilla ut. In est ante in nibh mauris cursus mattis. Molestie a iaculis at erat pellentesque adipiscing commodo elit at. Molestie a iaculis at erat pellentesque adipiscing commodo. Suspendisse interdum consectetur libero id faucibus nisl tincidunt eget. Faucibus pulvinar elementum integer enim neque. Condimentum mattis pellentesque id nibh tortor id aliquet. Pellentesque nec nam aliquam sem et. Habitasse platea dictumst quisque sagittis purus sit amet volutpat consequat. Morbi tincidunt ornare massa eget. Mauris sit amet massa vitae tortor condimentum. Adipiscing diam donec adipiscing tristique risus nec feugiat. Nec nam aliquam sem et tortor consequat id porta. Posuere sollicitudin aliquam ultrices sagittis orci a. Sagittis eu volutpat odio facilisis mauris sit. Leo a diam sollicitudin tempor id eu. Id diam vel quam elementum. Ultrices mi tempus imperdiet nulla. Et egestas quis ipsum suspendisse ultrices gravida dictum fusce. Eleifend quam adipiscing vitae proin sagittis nisl rhoncus. Quis hendrerit dolor magna eget est lorem ipsum dolor sit. Posuere sollicitudin aliquam ultrices sagittis orci a. Tortor pretium viverra suspendisse potenti. Adipiscing at in tellus integer. Sem et tortor consequat id. Vitae tempus quam pellentesque nec nam. Tortor at auctor urna nunc id cursus metus aliquam eleifend. Feugiat in ante metus dictum at tempor. Sollicitudin tempor id eu nisl. Fames ac turpis egestas sed tempus. Iaculis nunc sed augue lacus. Vel quam elementum pulvinar etiam non quam lacus suspendisse faucibus. Pellentesque adipiscing commodo elit at. Rhoncus urna neque viverra justo nec ultrices dui. Elementum sagittis vitae et leo duis ut diam quam nulla. At lectus urna duis convallis. Odio tempor orci dapibus ultrices in iaculis. Sit amet nisl suscipit adipiscing bibendum. Orci porta non pulvinar neque laoreet suspendisse. Volutpat lacus laoreet non curabitur gravida arcu. Tristique senectus et netus et malesuada fames. Vitae purus faucibus ornare suspendisse sed nisi lacus. Fusce id velit ut tortor pretium viverra suspendisse potenti. Vivamus at augue eget arcu dictum varius. Sem integer vitae justo eget magna fermentum iaculis eu. Vulputate mi sit amet mauris commodo quis imperdiet. Tortor dignissim convallis aenean et tortor at. Morbi non arcu risus quis varius quam quisque. Id diam maecenas ultricies mi eget mauris. In aliquam sem fringilla ut morbi tincidunt. Enim ut sem viverra aliquet eget sit amet. Odio ut enim blandit volutpat. Congue eu consequat ac felis donec. Facilisi cras fermentum odio eu feugiat pretium. At consectetur lorem donec massa sapien faucibus. Pretium nibh ipsum consequat nisl vel pretium lectus quam id. Massa massa ultricies mi quis hendrerit dolor. Phasellus vestibulum lorem sed risus ultricies tristique nulla aliquet enim. Et ligula ullamcorper malesuada proin libero nunc consequat. Consectetur adipiscing elit ut aliquam purus sit amet luctus venenatis. Risus nullam eget felis eget. Congue mauris rhoncus aenean vel. Dui vivamus arcu felis bibendum ut tristique. Mauris cursus mattis molestie a iaculis at erat. Sem fringilla ut morbi tincidunt augue. A iaculis at erat pellentesque adipiscing commodo elit at imperdiet. Vestibulum morbi blandit cursus risus at ultrices mi tempus. Mi eget mauris pharetra et ultrices neque ornare. Tortor dignissim convallis aenean et tortor at risus. Scelerisque mauris pellentesque pulvinar pellentesque habitant morbi tristique. Pretium vulputate sapien nec sagittis aliquam malesuada bibendum. Consectetur purus ut faucibus pulvinar elementum integer enim. Sapien pellentesque habitant morbi tristique senectus et netus. Risus nullam eget felis eget. Eu sem integer vitae justo eget magna fermentum iaculis eu. Sed risus ultricies tristique nulla aliquet enim tortor at. Platea dictumst vestibulum rhoncus est pellentesque elit ullamcorper. Facilisi cras fermentum odio eu feugiat pretium nibh ipsum consequat. Risus feugiat in ante metus dictum at tempor commodo ullamcorper. Tincidunt nunc pulvinar sapien et ligula ullamcorper malesuada proin libero. Senectus et netus et malesuada fames ac. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed. Tellus pellentesque eu tincidunt tortor aliquam nulla. In dictum non consectetur a erat. Velit euismod in pellentesque massa placerat. Nibh sit amet commodo nulla. Placerat orci nulla pellentesque dignissim. Aliquet nibh praesent tristique magna sit. Nunc eget lorem dolor sed. Varius quam quisque id diam vel quam. Viverra nibh cras pulvinar mattis. Nunc lobortis mattis aliquam faucibus purus in massa tempor. Leo vel fringilla est ullamcorper eget. Lorem mollis aliquam ut porttitor. Dictum varius duis at consectetur lorem. Enim nec dui nunc mattis enim ut tellus elementum sagittis. Est ante in nibh mauris cursus. In tellus integer feugiat scelerisque varius morbi enim. Rhoncus dolor purus non enim praesent elementum facilisis leo vel. Amet nulla facilisi morbi tempus iaculis. Aliquam sem fringilla ut morbi. Tincidunt augue interdum velit euismod in pellentesque massa. Posuere morbi leo urna molestie at elementum eu facilisis. Aenean pharetra magna ac placerat vestibulum. Et malesuada fames ac turpis. Dui id ornare arcu odio ut sem nulla pharetra. Leo vel fringilla est ullamcorper eget nulla facilisi etiam. Facilisi cras fermentum odio eu feugiat pretium nibh ipsum consequat. In nisl nisi scelerisque eu ultrices vitae auctor. Erat velit scelerisque in dictum non consectetur a erat nam. Gravida rutrum quisque non tellus orci ac auctor augue. Vestibulum rhoncus est pellentesque elit ullamcorper dignissim cras tincidunt. Consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus. Ut morbi tincidunt augue interdum velit euismod. Diam ut venenatis tellus in metus vulputate eu. Nisl nunc mi ipsum faucibus. Consectetur adipiscing elit ut aliquam purus sit amet luctus venenatis. Condimentum lacinia quis vel eros donec ac odio. Ut morbi tincidunt augue interdum. Leo a diam sollicitudin tempor id eu nisl. Donec enim diam vulputate ut. Dolor sit amet consectetur adipiscing elit ut aliquam purus. Fusce ut placerat orci nulla pellentesque dignissim enim. Mattis rhoncus urna neque viverra justo nec ultrices dui sapien. Vulputate enim nulla aliquet porttitor lacus luctus accumsan tortor posuere. Id neque aliquam vestibulum morbi blandit cursus risus. Eget aliquet nibh praesent tristique. Scelerisque varius morbi enim nunc faucibus a. Interdum velit laoreet id donec ultrices tincidunt arcu. Elementum curabitur vitae nunc sed velit dignissim sodales ut eu. Massa tempor nec feugiat nisl pretium fusce id velit. Ultrices vitae auctor eu augue ut lectus. Id diam vel quam elementum pulvinar etiam non. In arcu cursus euismod quis viverra nibh cras pulvinar. At varius vel pharetra vel. Aliquet porttitor lacus luctus accumsan tortor posuere ac. A iaculis at erat pellentesque adipiscing commodo elit at. Massa tincidunt dui ut ornare lectus sit. Pellentesque nec nam aliquam sem et tortor consequat id. Tristique magna sit amet purus gravida. Quam adipiscing vitae proin sagittis nisl. Eget nunc lobortis mattis aliquam faucibus. Cursus eget nunc scelerisque viverra mauris in. Aliquam ut porttitor leo a diam sollicitudin tempor id eu. Etiam dignissim diam quis enim lobortis. Vel turpis nunc eget lorem dolor. Consequat interdum varius sit amet mattis vulputate enim nulla aliquet. Tristique senectus et netus et malesuada. Mattis vulputate enim nulla aliquet porttitor lacus luctus accumsan tortor. Et malesuada fames ac turpis egestas maecenas pharetra convallis. Venenatis lectus magna fringilla urna porttitor rhoncus dolor. Ac odio tempor orci dapibus ultrices in iaculis nunc. Vitae justo eget magna fermentum. Amet commodo nulla facilisi nullam vehicula ipsum a. Maecenas pharetra convallis posuere morbi leo urna molestie at elementum. Consectetur a erat nam at lectus urna. Suscipit adipiscing bibendum est ultricies integer quis. Tincidunt augue interdum velit euismod. Iaculis urna id volutpat lacus laoreet non curabitur. Eu lobortis elementum nibh tellus.")
    driver.switch_to.default_content()
    #delete
    driver.find_element_by_css_selector("#remove-day").click()


def submitproduct():
    #tombol submit
    time.sleep(3)
    driver.find_element_by_css_selector("#btn-submit").click()
    time.sleep(5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success")))
    driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()
    time.sleep(5)


# # KLHK directory test

# In[9]:


driver.get((('http://pesona.gomodo.id/')))
driver.find_element_by_css_selector("#homepage > div > div > div.row > div > form > div > div.col-md-8.form-group > input").send_keys("Paket 01")
driver.find_element_by_css_selector("#homepage > div > div > div.row > div > form > div > div.col-md-8.form-group > input").send_keys(Keys.ENTER)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#main > div.row > div.col-sm-4.col-md-3.sidebar > div #apply-filter")))
driver.find_element_by_css_selector("#main > div.row > div.col-sm-4.col-md-3.sidebar > div > div:nth-child(1) > h4 > a").click()
time.sleep(2)
filterd()

#aktivitas tes
time.sleep(2)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#main-menu > ul > li:nth-child(2) > a")))
driver.find_element_by_css_selector("#main-menu > ul > li:nth-child(2) > a").click()
driver.get('''http://pesona.gomodo.id/explore/all-activities/search''')
driver.find_element_by_css_selector("#main > div.row > div.col-sm-4.col-md-3.sidebar > div > div:nth-child(1) > h4 > a").click()
time.sleep(5)
filterd()

#destionation
time.sleep(2)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#main-menu > ul > li:nth-child(3) > a")))
driver.find_element_by_css_selector("#main-menu > ul > li:nth-child(3) > a").click()
driver.get('''http://pesona.gomodo.id/explore/all-destination''')
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#main > div.tour-packages.row.add-clearfix.image-box > div > article > figure > a > figcaption")))
driver.find_element_by_css_selector("#main > div.tour-packages.row.add-clearfix.image-box > div > article > figure > a > figcaption").click()
driver.find_element_by_css_selector("#main > div.row > div.col-sm-4.col-md-3.sidebar > div > div:nth-child(1) > h4 > a").click()
time.sleep(5)
filterd()


#bantuan 
time.sleep(2)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#main-menu > ul > li:nth-child(4) > a")))
driver.find_element_by_css_selector("#main-menu > ul > li:nth-child(4) > a").click()
driver.get('''http://pesona.gomodo.id/explore/help''')
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#main > div > div.col-sm-8.col-md-9 > div > div > div:nth-child(1) > h4 > a")))

#search
driver.find_element_by_css_selector("#search-word").send_keys("bantuan")
driver.find_element_by_css_selector("#search-word").send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element_by_css_selector("#search-word").clear()
driver.find_element_by_css_selector("#search-word").send_keys("pemesanan")
driver.find_element_by_css_selector("#search-word").send_keys(Keys.ENTER)

#open tab
driver.find_element_by_css_selector("#main > div > div.col-sm-8.col-md-9 > div > div > div:nth-child(5) > h4 > a").click()
time.sleep(6)
driver.find_element_by_css_selector("#main > div > div.col-sm-4.col-md-3 > div.travelo-box.filters-container.faq-topics > ul #help_all").click()
time.sleep(2)
driver.find_element_by_css_selector("#main > div > div.col-sm-4.col-md-3 > div.travelo-box.filters-container.faq-topics > ul #help_coupon").click()
time.sleep(2)
driver.find_element_by_css_selector("#help_order_process").click()
time.sleep(2)
driver.find_element_by_css_selector("#main > div > div.col-sm-4.col-md-3 > div.travelo-box.filters-container.faq-topics #help_cancelation").click()
time.sleep(2)


#tentang kami footer
driver.find_element_by_css_selector("#footer > div.footer-wrapper.text-md-center > div > div > div:nth-child(1) > ul > li:nth-child(1) > a").click()
driver.find_element_by_css_selector("#footer > div.footer-wrapper.text-md-center > div > div > div:nth-child(1) > ul > li:nth-child(2) > a")

#KUPS Login
driver.find_element_by_css_selector("#main-menu > ul > li.provider-login-nav.text-white").click()
time.sleep(2)
driver.find_element_by_css_selector("#provider-modal > div > div.provider-login > a > button").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#regForm > div > div > div:nth-child(12) #submitButton")))
driver.find_element_by_css_selector("#regForm > div #backBtn").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#homepage > div > div > div.row > div > form > div > div.col-md-4.row > div > button")))

#KUPS Register
driver.find_element_by_css_selector("#main-menu > ul > li.provider-login-nav.text-white").click()
time.sleep(2)
driver.find_element_by_css_selector("#provider-modal > div > div.provider-signup > a > button").click()
#close pop up
time.sleep(4)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#stayUpToDate > div > div > button")))
driver.find_element_by_css_selector("#stayUpToDate > div > div > button").click()
time.sleep(1)
driver.find_element_by_css_selector("#top-navbar > div > a > span").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#homepage > div > div > div.row > div > form > div > div.col-md-4.row > div > button")))


# # register via klhk test

# In[ ]:


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#main-menu > ul > li.provider-login-nav.text-white > a")))
driver.find_element_by_css_selector("#main-menu > ul > li.provider-login-nav.text-white > a").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#provider-modal > div > div.provider-signup > a > button")))
driver.find_element_by_css_selector("#provider-modal > div > div.provider-login > a > button").click()

#web landing page
driver.find_element_by_css_selector("#regForm > div > div > div:nth-child(14) > a").click()
driver.find_element_by_css_selector("#regForm > div > div > div:nth-child(3) > input").send_keys(newproviderklhk)
driver.find_element_by_css_selector("#regForm > div > div > div.form-group.form-group-feedback.form-group-feedback-left.input-group.mb-1 > input").send_keys(newproviderklhk)
driver.find_element_by_css_selector("#email").send_keys(emailklhk)
driver.find_element_by_css_selector("#e_mail > div.form-group.form-group-feedback.form-group-feedback-left.input-group > input").send_keys("gomodo123")
driver.find_element_by_css_selector("#regForm > div > div > div:nth-child(11) > div > label").click()
time.sleep(1)
driver.find_element_by_css_selector("#modalTermConditionSignUp > div > div > div.modal-header > button > span").click()
driver.find_element_by_css_selector("#invalidCheck").click()

#submit
driver.find_element_by_css_selector("#regForm > div #btn-register").click()


# In[ ]:


#buka yopmail
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_css_selector("#login").clear()
driver.find_element_by_css_selector("#login").send_keys(emailklhk)
driver.find_element_by_css_selector("#login").send_keys(Keys.ENTER)
time.sleep(10)
driver.find_element_by_css_selector("#lrefr > span").click()
time.sleep(10)

#ganti ke tab ke 3 untuk log out
driver.switch_to.window(driver.window_handles[2])
time.sleep(4)
driver.find_element_by_css_selector("#header > div > div.sidebar-content > div > div.card.card-sidebar-mobile > ul > li:nth-child(15) > a").click()
time.sleep(2)
driver.find_element_by_css_selector("#logout_modal > div > div > div.modal-footer.mt-3 > div > button").click()
driver.find_element_by_css_selector("#header > div > div.sidebar-content > div > div.card.card-sidebar-mobile > ul > li:nth-child(15) > a").click()
time.sleep(2)
driver.find_element_by_css_selector("#logout_modal > div > div > div.modal-footer.mt-3 > div > a > button").click()

driver.close()

driver.switch_to.window(driver.window_handles[0])


# ## Gamification test

# In[ ]:


#login
driver.find_element_by_css_selector("#email").send_keys(emailklhk)
driver.find_element_by_css_selector("#regForm > div > div > div.form-group.form-group-feedback.form-group-feedback-left.input-group > input").send_keys("gomodo123")
driver.find_element_by_css_selector("#regForm > div > div > div:nth-child(12) #submitButton").click()

#gamification
#step 1
time.sleep(3)
driver.find_element_by_css_selector("#btn-show-gamification").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#business_type_gamification > div > div:nth-child(1) > span > span.selection > span > ul > li > input")))
driver.find_element_by_css_selector("#business_type_gamification > div > div:nth-child(1) > span > span.selection > span > ul > li > input").send_keys("Travel agent")
driver.find_element_by_css_selector("#business_type_gamification > div > div:nth-child(1) > span > span.selection > span > ul > li > input").send_keys(Keys.ENTER)

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#business_type_gamification > div > div:nth-child(1) > span > span.selection > span > ul > li.select2-selection__choice > span")))
driver.find_element_by_css_selector("#business_type_gamification > div > div:nth-child(1) > span > span.selection > span > ul > li.select2-selection__choice > span").click()

driver.find_element_by_css_selector("#business_type_gamification > div > div:nth-child(1) > span > span.selection > span > ul > li > input").send_keys("Travel agent")
driver.find_element_by_css_selector("#business_type_gamification > div > div:nth-child(1) > span > span.selection > span > ul > li > input").send_keys(Keys.ENTER)

driver.find_element_by_css_selector("#business_type_gamification > div > div:nth-child(2) > span > span.selection > span").click()
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("corporate")
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)
driver.find_element_by_css_selector("#business_type_gamification > div > div:nth-child(2) > span > span.selection > span").click()
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("personal")
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)

driver.find_element_by_css_selector("#business_type_gamification > div > button").click()

#step 2
time.sleep(6)
driver.find_element_by_css_selector("#about_company_gamification > div > div:nth-child(1) > input").send_keys("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis p")

#switch to iframe tinymce
driver.switch_to.frame(driver.find_element_by_css_selector("iframe#about_ifr"))
driver.find_element_by_css_selector("body[data-id=about]").clear()
driver.find_element_by_css_selector("body[data-id=about]").send_keys("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis,Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis ")
driver.switch_to.default_content()

driver.find_element_by_css_selector("#about_company_gamification > div > div.row.mt-3 > button").click()

#step 3
time.sleep(6)
driver.find_element_by_css_selector("#select2-country_search_gamification-container").click()
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("indonesia")
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)
time.sleep(3)

driver.find_element_by_css_selector("#select2-state_search_gamification-container").click()
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("Yogyakarta")
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)
time.sleep(3)

driver.find_element_by_css_selector("#select2-city_search_gamification-container").click()
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("Yogyakarta")
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)
time.sleep(3)

driver.find_element_by_css_selector("#pac-input-gamification").send_keys("gojek office")
driver.find_element_by_css_selector("#pac-input-gamification").send_keys(Keys.ENTER)
time.sleep(3)

driver.switch_to.frame(driver.find_element_by_css_selector("iframe#address_company_ifr"))
driver.find_element_by_css_selector("body[data-id=address_company]").clear()
#alamat 300 char
driver.find_element_by_css_selector("body[data-id=address_company]").send_keys("jalan gurami no 30 sorosutan,umbulharjo,yogyakarta 55123,,,jalan gurami no 30 sorosutan,umbulharjo,yogyakarta 55123,,,jalan gurami no 30 sorosutan,umbulharjo,yogyakarta 55123,,,jalan gurami no 30 sorosutan,umbulharjo,yogyakarta 55123,,,jalan gurami no 30 sorosutan,umbulharjo,yogyakarta 55123,,,12345")
driver.switch_to.default_content()

driver.find_element_by_css_selector("#address_company_gamification > div > div:nth-child(7) > input").send_keys("55232")

driver.find_element_by_css_selector("#address_company_gamification > div > div.row.mt-3 > button").click()

#step 4
time.sleep(6)
driver.find_element_by_css_selector("#contact_us_gamification > div > div:nth-child(1) > input").clear()
driver.find_element_by_css_selector("#contact_us_gamification > div > div:nth-child(1) > input").send_keys(newproviderklhk)

driver.find_element_by_css_selector("#contact_us_gamification > div > div:nth-child(2) > input").send_keys("089123123123")
driver.find_element_by_css_selector("#contact_us_gamification > div > div:nth-child(4) > input").send_keys("anime")
driver.find_element_by_css_selector("#contact_us_gamification > div > div:nth-child(5) > input").send_keys("anime")

driver.find_element_by_css_selector("#contact_us_gamification > div > div.row.mt-3 > button").click()

#step 5
time.sleep(12)
driver.find_element_by_css_selector("#gamificationModal > div > div > div.modal-header.text-center > h5 > a").click()
driver.find_element_by_css_selector("#seo_gamification > div > div:nth-child(1) > input").clear()
driver.find_element_by_css_selector("#seo_gamification > div > div:nth-child(1) > input").send_keys("Muchi Mug,,,Muchi Mug,,,Muchi Mug,,,Muchi Mug,,,Muchi Mug,,,Muchi Mug,")
driver.find_element_by_css_selector("#seo_gamification > div > div:nth-child(2) > textarea").clear()
driver.find_element_by_css_selector("#seo_gamification > div > div:nth-child(2) > textarea").send_keys("Muchi Mug adalah perusahaan berbasis gomodo dan menunjang yang namanya kemanusian,,,,Muchi Mug adalah perusahaan berbasis gomodo dan menunjang yang na")
driver.find_element_by_css_selector("#seo_gamification > div > div:nth-child(3) > span > span.selection > span > ul > li > input").clear()
driver.find_element_by_css_selector("#seo_gamification > div > div:nth-child(3) > span > span.selection > span > ul > li > input").send_keys("Muchi Mug,platform,pemesaan,booking,dll,gomodo,Muchi Mug,platform,pemesaan,booking,dll,gomodo,Muchi Mug,platform,pemesaan,booking,dll,gomodo,Muchi Mug,platform,pemesaan,booking,dll,gomodo,Muchi Mug,platform,pemesaan,booking,dll,gomodo,Muchi Mug,platform,pemesaan,booking,dll,gomodo,Muchi Mug,platform,pemesaan,booking,dll,gomodo,Muchi Mug,platform,pemesaan,booking,dll,gomodo,Muchi Mug,platform,pemesaan,booking,dll,gomodo,Muchi Mug,platform,pemesaan,booking,dll,gomodo,Muchi Mug,platform,pemesaan,bo,")

driver.find_element_by_css_selector("#seo_gamification > div > div.row.mt-3 > button").click()

#step 6
time.sleep(10)
driver.find_element_by_xpath("//*[@id='select2-bank-l2-container']").click()
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("bank central asia")
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)

driver.find_element_by_css_selector("#bank_account_gamification > div > div:nth-child(2) > input").send_keys("mas tejo")
driver.find_element_by_css_selector("#bank_account_gamification > div > div:nth-child(3) > input").send_keys("0900123123")
driver.find_element_by_css_selector("#bank_account_gamification > div > div:nth-child(5) > div > input").send_keys(os.getcwd()+ "/bank.jpg")

driver.find_element_by_css_selector("#bank_account_gamification > div > div.row.mt-3 > button").click()

#finish step
time.sleep(10)
driver.find_element_by_css_selector("#gamificationModal > div > div > div.modal-header.text-center > h5").text
driver.find_element_by_css_selector("#finish_gamification > div > div.row.mt-3 > button").click()
time.sleep(10)


# # BUPSHA

# ## Dashboard
# cek di fungsionalitas pada dashbard dan tombol yang tersedia

# In[ ]:


#login
driver.get('''http://bupsha.gomodo.id/login''')
time.sleep(1)
driver.find_element_by_css_selector("body > div > div > div > form > div > div.card-body > div:nth-child(2) > input").send_keys("klhk@gmail.com")
driver.find_element_by_css_selector("body > div > div > div > form > div > div.card-body > div:nth-child(3) > input").send_keys("123456")
driver.find_element_by_css_selector("body > div > div > div > form > div > div.card-body > div:nth-child(5) > button").click()

#check dashboard (tab today,30,90 day)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#card-dashboard > div > ul > li:nth-child(4) > a")))
time.sleep(2)
driver.find_element_by_css_selector("#card-dashboard > div > ul > li:nth-child(2) > a").click()
time.sleep(2)
driver.find_element_by_css_selector("#card-dashboard > div > ul > li:nth-child(3) > a").click()
time.sleep(2)
driver.find_element_by_css_selector("#card-dashboard > div > ul > li:nth-child(4) > a").click()

#top kups (days)
driver.find_element_by_css_selector("#change-top > option:nth-child(2)").click()
time.sleep(2)
driver.find_element_by_css_selector("#change-top > option:nth-child(3)").click()
time.sleep(2)
driver.find_element_by_css_selector("#change-top > option:nth-child(4)").click()
time.sleep(2)
driver.find_element_by_css_selector("#change-top > option:nth-child(5)").click()
time.sleep(2)
driver.find_element_by_css_selector("#change-top > option:nth-child(1)").click()


# ## Pemesanan

# ### Pemesanan Online

# In[ ]:


#pemesanan online
driver.get('''http://bupsha.gomodo.id/transaction/online''')
driver.find_element_by_css_selector("#dt_filter > label > input[type=search]").send_keys("klhk1")
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr:nth-child(1) > td.text-center > a > i")))
driver.find_element_by_css_selector("#dt > tbody > tr:nth-child(1) > td.text-center > a").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#data-booking-online > div > div > ul > li:nth-child(2) > a")))
time.sleep(4)
driver.find_element_by_css_selector("#data-booking-online > div > div > ul > li:nth-child(2) > a").click()
time.sleep(4)
driver.find_element_by_css_selector("#data-booking-online > div > div > ul > li:nth-child(3) > a").click()
time.sleep(4)

#download per order
driver.get('''http://pesona.gomodo.id/transaction/online''')
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr:nth-child(1) > td.text-center > form > button")))
driver.find_element_by_css_selector("#dt > tbody > tr:nth-child(1) > td.text-center > form > button").click()
time.sleep(2)

#downlaod semua
driver.find_element_by_css_selector("#header > div > button").click()
time.sleep(2)
driver.find_element_by_css_selector("#data-provider > div.modal.fade.modal-download.show > div > form > div > div.modal-footer > button.btn.bg-green-klhk.legitRipple").click()
time.sleep(2)
driver.find_element_by_css_selector("#data-provider > div.modal.fade.modal-download.show > div > form > div > div.modal-header > button").click()

#download semua dengan yang lunas saja
driver.find_element_by_css_selector("#header > div > button").click()
time.sleep(2)
driver.find_element_by_css_selector("#status").click()
driver.find_element_by_css_selector("#data-provider > div.modal.fade.modal-download.show > div > form > div > div.modal-footer > button.btn.bg-green-klhk.legitRipple").click()
time.sleep(2)
driver.find_element_by_css_selector("#data-provider > div.modal.fade.modal-download.show > div > form > div > div.modal-header > button").click()


# ### Transaksi di lokasi

# In[ ]:


#Transaksi di Lokasi
driver.get('''http://bupsha.gomodo.id/transaction/offline''')
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header > div > button")))
driver.find_element_by_css_selector("#header > div > button").click()
time.sleep(2)
driver.find_element_by_css_selector("#data-provider > div.modal.fade.modal-download.show > div > form > div > div.modal-footer > button.btn.bg-green-klhk.legitRipple").click()
time.sleep(2)
driver.find_element_by_css_selector("#data-provider > div.modal.fade.modal-download.show > div > form > div > div.modal-header > button").click()

#Download semua transaksi demgan lunas saja
driver.find_element_by_css_selector("#header > div > button").click()
time.sleep(2)
driver.find_element_by_css_selector("#status").click()
driver.find_element_by_css_selector("#data-provider > div.modal.fade.modal-download.show > div > form > div > div.modal-footer > button.btn.bg-green-klhk.legitRipple").click()
time.sleep(2)
driver.find_element_by_css_selector("#data-provider > div.modal.fade.modal-download.show > div > form > div > div.modal-header > button").click()


# ## Produk

# ### Rincian

# In[ ]:


driver.get('''http://bupsha.gomodo.id/product''')
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr:nth-child(1) > td.text-center > a:nth-child(1)")))

driver.find_element_by_css_selector("#dt_filter > label > input[type=search]").send_keys("Paket 01")
time.sleep(2)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr:nth-child(1) > td.text-center > a:nth-child(1)")))
driver.find_element_by_css_selector("#dt > tbody > tr:nth-child(1) > td.text-center > a:nth-child(1)").click()

#melihat produk
driver.switch_to.window(driver.window_handles[1])
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#navcol-1 > ul > li:nth-child(1) > a")))
time.sleep(5)
driver.close()
driver.switch_to.window(driver.window_handles[0])

#edit lokasi produk
driver.find_element_by_css_selector("#dt > tbody > tr.odd > td.text-center > a:nth-child(2)").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#edit-product > div > form > div.col-12.text-center.mt-3 > button")))
driver.find_element_by_css_selector("#edit-product > div > form > div.col-6 > div:nth-child(2) > span > span.selection > span").click()
time.sleep(3)
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("jawa tengah")
time.sleep(2)
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(keys.ENTER)
driver.find_element_by_css_selector("#edit-product > div > form > div.col-6 > div:nth-child(3) > span > span.selection > span").click()
time.sleep(3)
driver.find_element_by_css_selectpr("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("banyumas")
time.sleep(2)
driver.find_element_by_css_selectpr("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(keys.ENTER)

driver.find_element_by_css_selector("#edit-product > div > form > div.col-12.text-center.mt-3 > button").click()


# ### Tag

# In[ ]:


driver.get('''http://bupsha.gomodo.id/product-tag''')
driver.find_element_by_css_selector("#dt_filter > label > input[type=search]").send_keys("car rental")
time.sleep(4)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr > td.text-center > a > i")))
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > a > i").click()
time.sleep(5)
#print(driver.title)


# ## Anggota

# ### KUPS

# #### Profil perusahaan

# In[ ]:


driver.get('''http://bupsha.gomodo.id/providers''')
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt_filter > label > input[type=search]")))
driver.find_element_by_css_selector("#dt_filter > label > input[type=search]").send_keys("klhk1")
time.sleep(4)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr:nth-child(1) > td.text-center > a > i")))
driver.find_element_by_css_selector("#dt > tbody > tr:nth-child(1) > td.text-center > a > i").click()

#form profil perusahaan EDIT
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#tab1-product > form > div.col-12.text-center > button")))
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(1) > div:nth-child(1) > input").clear()
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(1) > div:nth-child(1) > input").send_keys("klhk1edit.gomodo.id")
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(1) > div:nth-child(2) > input").clear()
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(1) > div:nth-child(2) > input").send_keys("klhk1edit")
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(1) > div:nth-child(3) > input").clear()
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(1) > div:nth-child(3) > input").send_keys("klhk1edit@yopmail.com")
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(1) > div:nth-child(4) > input").clear()
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(1) > div:nth-child(4) > input").send_keys("08989898989")
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(1) > div:nth-child(5) > select > option:nth-child(2)").click()
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(1) > div:nth-child(6) > select > option:nth-child(1)").click()
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(2) > div:nth-child(1) > div > div.note-editing-area > div.note-editable.card-block").clear()
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(2) > div:nth-child(1) > div > div.note-editing-area > div.note-editable.card-block").send_keys("edit tentang perusahaan klhk")
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(2) > div:nth-child(3) > select > option:nth-child(1)").click()

#submit
time.sleep(2)
driver.find_element_by_css_selector("#tab1-product > form > div.col-12.text-center > button").click()


#form profil perusahaan kembali semula
time.sleep(4)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr:nth-child(1) > td.text-center > a > i")))
driver.find_element_by_css_selector("#dt > tbody > tr:nth-child(1) > td.text-center > a > i").click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#tab1-product > form > div.col-12.text-center > button")))
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(1) > div:nth-child(1) > input").clear()
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(1) > div:nth-child(1) > input").send_keys("klhk1.gomodo.id")
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(1) > div:nth-child(2) > input").clear()
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(1) > div:nth-child(2) > input").send_keys("klhk1")
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(1) > div:nth-child(3) > input").clear()
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(1) > div:nth-child(3) > input").send_keys("klhk1@yopmail.com")
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(1) > div:nth-child(4) > input").clear()
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(1) > div:nth-child(4) > input").send_keys("082111111111")
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(1) > div:nth-child(5) > select > option:nth-child(1)").click()
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(1) > div:nth-child(6) > select > option:nth-child(2)").click()
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(2) > div:nth-child(1) > div > div.note-editing-area > div.note-editable.card-block").clear()
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(2) > div:nth-child(1) > div > div.note-editing-area > div.note-editable.card-block").send_keys("")
driver.find_element_by_css_selector("#tab1-product > form > div.row > div:nth-child(2) > div:nth-child(3) > select > option:nth-child(2)").click()

#submit
time.sleep(2)
driver.find_element_by_css_selector("#tab1-product > form > div.col-12.text-center > button").click()


# #### Login akun

# In[ ]:


#mengedit form login akun
time.sleep(4)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr:nth-child(1) > td.text-center > a > i")))
driver.find_element_by_css_selector("#dt > tbody > tr:nth-child(1) > td.text-center > a > i").click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#tab1-product > form > div.col-12.text-center > button")))
driver.find_element_by_css_selector("body > div.page-content > div.content-wrapper > div.content.pt-0 > div > div > ul > li:nth-child(2) > a").click()
time.sleep(1)
driver.find_element_by_css_selector("#tab2-product > form > div > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)").clear()
driver.find_element_by_css_selector("#tab2-product > form > div > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)").send_keys("klhk1edit")
driver.find_element_by_css_selector("#tab2-product > form > div > div:nth-child(1) > div:nth-child(2) > input").clear()
driver.find_element_by_css_selector("#tab2-product > form > div > div:nth-child(1) > div:nth-child(2) > input").send_keys("edition")
driver.find_element_by_css_selector("#tab2-product > form > div > div:nth-child(1) > div:nth-child(3) > input").clear()
driver.find_element_by_css_selector("#tab2-product > form > div > div:nth-child(1) > div:nth-child(3) > input").send_keys("klhk1edit@yopmail.com")
driver.find_element_by_css_selector("#tab2-product > form > div > div:nth-child(2) > div:nth-child(1) > input").clear()
driver.find_element_by_css_selector("#tab2-product > form > div > div:nth-child(2) > div:nth-child(1) > input").send_keys("gomodo321")
driver.find_element_by_css_selector("#tab2-product > form > div > div:nth-child(2) > div:nth-child(2) > select > option:nth-child(1)").click()

#submit
time.sleep(2)
driver.find_element_by_css_selector("#tab2-product > form > div > div.col-12.text-center > button > i").click()

#mengembalikan form login akun
time.sleep(4)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr:nth-child(1) > td.text-center > a > i")))
driver.find_element_by_css_selector("#dt > tbody > tr:nth-child(1) > td.text-center > a > i").click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#tab1-product > form > div.col-12.text-center > button")))
driver.find_element_by_css_selector("body > div.page-content > div.content-wrapper > div.content.pt-0 > div > div > ul > li:nth-child(2) > a").click()
time.sleep(1)
driver.find_element_by_css_selector("#tab2-product > form > div > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)").clear()
driver.find_element_by_css_selector("#tab2-product > form > div > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)").send_keys("klhk1")
driver.find_element_by_css_selector("#tab2-product > form > div > div:nth-child(1) > div:nth-child(2) > input").clear()
driver.find_element_by_css_selector("#tab2-product > form > div > div:nth-child(1) > div:nth-child(2) > input").send_keys("editor")
driver.find_element_by_css_selector("#tab2-product > form > div > div:nth-child(1) > div:nth-child(3) > input").clear()
driver.find_element_by_css_selector("#tab2-product > form > div > div:nth-child(1) > div:nth-child(3) > input").send_keys("klhk1@yopmail.com")
driver.find_element_by_css_selector("#tab2-product > form > div > div:nth-child(2) > div:nth-child(1) > input").clear()
driver.find_element_by_css_selector("#tab2-product > form > div > div:nth-child(2) > div:nth-child(1) > input").send_keys("gomodo123")
driver.find_element_by_css_selector("#tab2-product > form > div > div:nth-child(2) > div:nth-child(2) > select > option:nth-child(2)").click()

#submit
time.sleep(2)
driver.find_element_by_css_selector("#tab2-product > form > div > div.col-12.text-center > button > i").click()


# # KLHK Dashboard

# ## Product

# In[ ]:


#produk login
driver.get('''http://pesona.gomodo.id/agent/login''')
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#regForm > div > div > div:nth-child(12) #submitButton")))
driver.find_element_by_css_selector("#login_mail #email").send_keys(emailklhk)
driver.find_element_by_css_selector("#regForm > div > div > div.form-group.form-group-feedback.form-group-feedback-left.input-group > input").send_keys("gomodo123")
driver.find_element_by_css_selector("#regForm > div > div > div:nth-child(12) #submitButton").click()

#produk
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header > div > div.sidebar-content > div > div.card.card-sidebar-mobile > ul > li:nth-child(13) > a")))
driver.get('''http://pesona.gomodo.id/company/product/create''')
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#btn-submit")))

product()

submitproduct()

#mengganti nama
driver.find_element_by_css_selector("#product-detail > div.widget-content > div > div > div.col-sm-12.col-md-12.col-lg-6.col-xl-5 > div:nth-child(1) > input").send_keys(" edited fixed")

#memilih tanggal fixed date
driver.find_element_by_css_selector("#availability > option:nth-child(2)").click()
time.sleep(1)
driver.find_element_by_css_selector("body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-top > div.datepicker-days > table > thead > tr:nth-child(2) > th.next").click()
driver.find_element_by_css_selector("body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-top > div.datepicker-days > table > tbody > tr:nth-child(3) > td:nth-child(7)").click()

#mengganti durasi aktivitas
driver.find_element_by_css_selector("#duration_activity > div.widget-content > div:nth-child(1) > div:nth-child(2) > div > select > option:nth-child(1)").click()
driver.find_element_by_css_selector("#duration_activity > div.widget-content > div:nth-child(1) > div:nth-child(1) > div > input").clear()
driver.find_element_by_css_selector("#duration_activity > div.widget-content > div:nth-child(1) > div:nth-child(1) > div > input").send_keys("55")

#mengganti minimal pemberitahuan
driver.find_element_by_css_selector("#minimum_notice").clear()
driver.find_element_by_css_selector("#minimum_notice").send_keys("0")

#mengganti status dan tampilkan produk
driver.find_element_by_css_selector("#status > option:nth-child(2)").click()
driver.find_element_by_css_selector("#publish > option:nth-child(2)").click()

#mengubah harga produk
driver.find_element_by_css_selector("#max_people").clear()
driver.find_element_by_css_selector("#max_people").send_keys("1")

driver.find_element_by_css_selector("#min_people").clear()
driver.find_element_by_css_selector("#min_people").send_keys("1")
driver.find_element_by_css_selector("#max_order").clear()
driver.find_element_by_css_selector("#max_order").send_keys("10")

#mengubah tipe harga
driver.find_element_by_css_selector("#product-pricing > div.widget-content > div:nth-child(5) > div > div > div:nth-child(3) > label").click()
driver.find_element_by_css_selector("#display_id > option:nth-child(7)").click()

driver.find_element_by_css_selector("#price\.0").clear()
driver.find_element_by_css_selector("#price\.0").send_keys("20000")

driver.find_element_by_css_selector("#product-pricing > div.widget-content > div:nth-child(8) > div > button").click()
driver.find_element_by_css_selector("#product-pricing > div.widget-content > div.box-clone > div > div.col-lg-4.price-type-d-none > div #price_from\.0").click()
driver.find_element_by_css_selector("#price\.1").send_keys("10000")

#mengubah isi junlah diskon
driver.find_element_by_css_selector("#discount_amount_type > option:nth-child(2)").click()
driver.find_element_by_css_selector("#discount_amount").clear()
driver.find_element_by_css_selector("#discount_amount").send_keys("10000")

submitproduct()


# ## Pembiayaan

# In[23]:


driver.get('''http://pesona.gomodo.id/company/finance''')
#Test 10000 
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > div.content.pt-0 > div.loan-funds.front-page > div:nth-child(1) > div > div.col-12.col-lg-3.text-center.justify-content-center #btn-loan")))
driver.find_element_by_css_selector("#content > div.content.pt-0 > div.loan-funds.front-page > div:nth-child(1) > div > div.col-12.col-lg-3.text-center.justify-content-center #btn-loan").click()
time.sleep(2)
driver.find_element_by_css_selector("#steps-validate-p-0 > div > div > div.form-group #amount").send_keys("100000")
driver.find_element_by_css_selector("#steps-validate-p-0 > div > div > div.card-body.p-0 > ul > li:nth-child(3) > a").click()
#submit
driver.find_element_by_css_selector("#steps-validate > div.actions.clearfix > ul > li:nth-child(2) > a").click()

#memilih bulan
driver.find_element_by_css_selector("#steps-validate-p-0 > div > div > div.card-body.p-0 > ul > li:nth-child(1) > a").click()
driver.find_element_by_css_selector("#steps-validate-p-0 > div > div > div.card-body.p-0 > ul > li:nth-child(2) > a").click()

def test_pembiayaan1(self):
    self.assertIn(errofin_string == "Jumlah pinjaman yang dapat diajukan min. Rp. 10,000,000")
    


# In[ ]:


driver.find_element_by_css_selector("#steps-validate-p-0 > div > div > div.form-group #amount").send_keys("9999999999")
driver.find_element_by_css_selector("#steps-validate-p-0 > div > div > div.card-body.p-0 > ul > li:nth-child(3) > a").click()
#submit
driver.find_element_by_css_selector("#steps-validate > div.actions.clearfix > ul > li:nth-child(2) > a").click()

def test_pembiayaan2(self):
    self.assertIn(errofin_string == "Jumlah pinjaman yang dapat diajukan min. Rp. 10,000,000")


# ## Kode Promo

# In[ ]:


#test isi form
driver.get('''http://pesona.gomodo.id/company/voucher/create''')
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
#driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(4) > div > div > div:nth-child(4) > div > span > span.selection > span > ul > li > input").send_keys("tes 16/3/2020")
#driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(4) > div > div > div:nth-child(4) > div > span > span.selection > span > ul > li > input").send_keys(Keys.ENTER)

driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(5) > div > div > div > div > input").send_keys("tes voucer")


# In[ ]:


#submit 
driver.find_element_by_css_selector("#btn-submit").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success")))

driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#voucher-list_filter > label > input[type=search]")))


# In[ ]:


driver.find_element_by_css_selector("#voucher-list_filter > label > input[type=search]").send_keys(vouchercode)#unik


#pilih list voucher
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#voucher-list > tbody > tr > td.sorting_1 > a")))
driver.find_element_by_css_selector("#voucher-list > tbody > tr > td.sorting_1 > a").click()

#edit form
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(2) > div > div > div:nth-child(3) > div > select > option:nth-child(3)").click()
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(2) > div > div > div:nth-child(4) > div > input").clear()
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(2) > div > div > div:nth-child(4) > div > input").send_keys("20")
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(3) > div > div > div:nth-child(1) > div > input").clear()
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(3) > div > div > div:nth-child(1) > div > input").send_keys("2")
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(3) > div > div > div:nth-child(2) > div > input").clear()
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(3) > div > div > div:nth-child(2) > div > input").send_keys("70")

#edit tanggal
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(3) > div > div > div:nth-child(3) > div > input").click()
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(3) > div > div > div:nth-child(3) > div > input").clear()
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(3) > div > div > div:nth-child(3) > div > input").send_keys("27/03/2020")
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(3) > div > div > div:nth-child(4) > div > input").click()
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(3) > div > div > div:nth-child(4) > div > input").clear()
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(3) > div > div > div:nth-child(4) > div > input").send_keys("04/04/2020")
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(3) > div > div > div:nth-child(4) > div > input").send_keys(Keys.ENTER)

driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(4) > div > div > div:nth-child(1) > div > input").clear()
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(4) > div > div > div:nth-child(1) > div > input").send_keys("20000")
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(4) > div > div > div:nth-child(2) > div > input").clear()
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(4) > div > div > div:nth-child(2) > div > input").send_keys("3")

#set status
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(4) > div > div > div:nth-child(3) > div > select > option:nth-child(2)").click()

driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(4) > div > div > div:nth-child(4) > div > span > span.selection > span > ul > li.select2-selection__choice > span").click()
#driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(4) > div > div > div:nth-child(4) > div > span > span.selection > span > ul > li.select2-search.select2-search--inline > input").send_keys("tes 2/3/2020")
#driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(4) > div > div > div:nth-child(4) > div > span > span.selection > span > ul > li.select2-search.select2-search--inline > input").send_keys(Keys.ENTER)

driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(5) > div > div > div > div > input").clear()
driver.find_element_by_css_selector("#form_ajax > div.widget.card > div:nth-child(5) > div > div > div > div > input").send_keys("tes kupon edit")

#submit edit
time.sleep(3)
driver.find_element_by_css_selector("#btn-submit").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success")))
driver.find_element_by_css_selector("body > div.swal2-container.swal2-center.swal2-fade.swal2-shown > div > div.swal2-actions > button.swal2-confirm.btn.btn-success").click()


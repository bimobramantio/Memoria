#!/usr/bin/env python
# coding: utf-8

# # Starting

# In[1]:


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

driver = webdriver.Chrome(executable_path=r'C:\Users\Lenovo\driver\chromedriver.exe') #Launch Chrome Webdriver

wait = WebDriverWait(driver,15)
driver.maximize_window()


# In[2]:


#Promo general unique code
promogeneral = ['tespromogene22']
promocode = ['tespromoco30']
blog_b2b_eng = ['Test English Title that will announce your blog to provider 6']
blog_b2b_ind = ['Tes Indonesia judul yang akan menampilkan bahasa indonesia di blog provider 6']
content_blog_eng = ['Blog Content Test that wll display at content section at customer side 6']
content_blog_ind = ['Tes konten blog indonesia yang akan di tampilkan pada sebuah konten 6']


# # Open browser and login Back office

# In[3]:


#open login
driver.get('http://gomodo.id/back-office')


# In[4]:


driver.find_element_by_css_selector("#m_login > div > div > div.m-login__signin > form > div:nth-child(2) > input").send_keys("dummy@gmail.com")


# In[5]:


driver.find_element_by_css_selector("#m_login > div > div > div.m-login__signin > form > div:nth-child(3) > input").send_keys("password")


# In[6]:


driver.find_element_by_css_selector("#m_login_signin_submit").click()


# ## State check

# In[7]:


#state
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#m_ver_menu > ul > li:nth-child(4) > a > span")))


# In[8]:


driver.find_element_by_css_selector("#m_ver_menu > ul > li:nth-child(4) > a > span").click()
time.sleep(5)


# In[9]:


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr:nth-child(2) > td.text-center > button")))
driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div.row.mt-3.mb-5 > div > span > span.selection > span > span.select2-selection__arrow").click()


# In[10]:


driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("iceland")
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)
driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div.row.mt-3.mb-5 > div > span > span.selection > span > span.select2-selection__arrow").click()
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("indonesia")
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)


# In[11]:


driver.find_element_by_css_selector("#dt > tbody > tr:nth-child(1) > td.text-center > button").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#add_name")))


# In[12]:


driver.find_element_by_css_selector("#add_name").clear()
driver.find_element_by_css_selector("#add_name").send_keys("aceh")

driver.find_element_by_css_selector("#add_name_indo").clear()
driver.find_element_by_css_selector("#add_name_indo").send_keys("aceh")

driver.find_element_by_css_selector("#btn-do-delete").click()


# In[13]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# ## City Check

# In[16]:


#city
driver.find_element_by_css_selector("#m_ver_menu > ul > li:nth-child(5) > a > span").click()


# In[17]:


driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div.row.mt-3.mb-5 > div:nth-child(1) > span > span.selection > span > span.select2-selection__arrow").click()
time.sleep(5)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > span > span > span.select2-search.select2-search--dropdown > input")))


# In[18]:


#edit country iceland
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("iceland")
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)
time.sleep(5)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div.row.mt-3.mb-5 > div:nth-child(1) > span > span.selection > span > span.select2-selection__arrow")))


#edit country indonesia
driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div.row.mt-3.mb-5 > div:nth-child(1) > span > span.selection > span > span.select2-selection__arrow").click()
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("indonesia")
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)
time.sleep(5)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div.row.mt-3.mb-5 > div:nth-child(2) > span > span.selection > span > span.select2-selection__arrow")))


# In[19]:


#edit state
driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div.row.mt-3.mb-5 > div:nth-child(2) > span > span.selection > span > span.select2-selection__arrow").click()

driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("yogyakarta")
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)
time.sleep(5)

driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div.row.mt-3.mb-5 > div:nth-child(2) > span > span.selection > span > span.select2-selection__arrow").click()
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("aceh")
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)
time.sleep(5)


# In[20]:


#edit city
driver.find_element_by_css_selector("#dt > tbody > tr:nth-child(1) > td.text-center > button").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#add_name")))


# In[21]:


driver.find_element_by_css_selector("#add_name").clear()
driver.find_element_by_css_selector("#add_name").send_keys("KAB. ACEH BARAT DAYA")


# In[22]:


driver.find_element_by_css_selector("#add_name_indo").clear()
driver.find_element_by_css_selector("#add_name_indo").send_keys("KAB. ACEH BARAT DAYA")

driver.find_element_by_css_selector("#btn-do-delete").click()


# In[23]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# ## Bussiness Category Check

# In[24]:


#bussines category
driver.find_element_by_css_selector("#m_ver_menu > ul > li:nth-child(6) > a > span").click()
time.sleep(4)


# In[25]:


driver.find_element_by_css_selector("#btn-add").click()
time.sleep(3)


# In[26]:


driver.find_element_by_css_selector("#business_category_name").send_keys("tes buat")


# In[27]:


driver.find_element_by_css_selector("#business_category_name_id").send_keys("test create")


# In[28]:


driver.find_element_by_css_selector("#modal-add > div > form > div > div.modal-footer > #btn-do-delete").click()


# In[29]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# In[30]:


driver.find_element_by_css_selector("#dt_filter > label > input").send_keys("tes buat")
time.sleep(5)


# In[31]:


driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button.btn.btn-outline-info.btn-preview.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air").click()
time.sleep(5)


# In[32]:


driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-body > div:nth-child(2) #business_category_name").clear()
driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-body > div:nth-child(2) #business_category_name").send_keys("test edit")
driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-body > div:nth-child(3) #business_category_name_id").clear()
driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-body > div:nth-child(3) #business_category_name_id").send_keys("tes edit")


# In[33]:


driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-footer #btn-do-delete").click()
time.sleep(5)


# In[34]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# In[35]:


driver.find_element_by_css_selector("#dt_filter > label > input").clear()
driver.find_element_by_css_selector("#dt_filter > label > input").send_keys("tes edit")
time.sleep(4)


# In[36]:


driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button.btn-delete.btn.btn-outline-danger.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air").click()
time.sleep(5)


# In[37]:


driver.find_element_by_css_selector("#modal-delete > div > form > div > div.modal-footer #btn-do-delete").click()


# In[38]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# ## Language Check

# In[39]:


##Language
driver.find_element_by_css_selector("#m_ver_menu > ul > li:nth-child(7) > a > span").click()
time.sleep(3)


# In[40]:


driver.find_element_by_xpath("//*[@id='btn-add']").click()
time.sleep(3)


# In[41]:


wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='modal-add']/div/form/div/div[3]/button[1]")))
driver.find_element_by_xpath("//*[@id='language_name']").send_keys("Tes Language")


# In[42]:


driver.find_element_by_css_selector("#modal-add #btn-do-delete").click() # cara nya ringgo kampret kok simpel asem


# In[43]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# In[44]:


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt_filter > label > input")))
driver.find_element_by_css_selector("#dt_filter > label > input").send_keys("tes language")


# In[45]:


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr > td.text-center > button.btn.btn-outline-info.btn-preview.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air")))
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button.btn.btn-outline-info.btn-preview.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air").click()


# In[46]:


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#modal-edit #language_name")))

driver.find_element_by_css_selector("#modal-edit #language_name").clear()
driver.find_element_by_css_selector("#modal-edit #language_name").send_keys("Tes Language Edit")


# In[47]:


driver.find_element_by_css_selector("#modal-edit #btn-do-delete").click()


# In[48]:


driver.find_element_by_css_selector("#dt_filter > label > input").clear()
driver.find_element_by_css_selector("#dt_filter > label > input").send_keys("Tes Language Edit")


# In[49]:


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr > td.text-center > button.btn-delete.btn.btn-outline-danger.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air")))


driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button.btn-delete.btn.btn-outline-danger.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air").click()


# In[50]:


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#modal-delete #btn-do-delete")))
driver.find_element_by_css_selector("#modal-delete #btn-do-delete").click()


# In[51]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# ## Association Check

# In[52]:


#tes Asosiasi
driver.get('http://gomodo.id/back-office/association')
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#m_ver_menu > ul > li:nth-child(11) > a > span")))
#driver.find_element_by_css_selector("#m_ver_menu > ul > li:nth-child(11) > a > span").click()


# In[53]:


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div > div.col-12.mb-3.text-right >#btn-add")))

driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div > div.col-12.mb-3.text-right >#btn-add").click()


# In[54]:


time.sleep(4)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#form-add  #btn-do-delete")))

driver.find_element_by_css_selector("#form-add #association_name").send_keys("Tes Asosiasi")
driver.find_element_by_css_selector("#form-add  #association_desc").send_keys("Tes Deskripsi Asosiasi")
driver.find_element_by_css_selector("#form-add #association_logo").send_keys(os.getcwd() + "/logo.jpg") #Image Upload


# In[55]:


driver.find_element_by_css_selector("#form-add  #btn-do-delete").click()


# In[56]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# In[57]:


driver.find_element_by_css_selector("#dt_filter > label > input").send_keys("Tes Asosiasi")
time.sleep(5)


# In[58]:


#edit asosiasi
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr > td.text-center > button.btn.btn-outline-info.btn-preview.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air")))
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button.btn.btn-outline-info.btn-preview.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air").click()


# In[59]:


#wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#form-add  #btn-do-delete")))
time.sleep(10)

driver.find_element_by_css_selector("#form-edit #association_name").clear()
driver.find_element_by_css_selector("#form-edit #association_name").send_keys("Tes Asosiasi Edit")
driver.find_element_by_css_selector("#form-edit #association_desc").clear()
driver.find_element_by_css_selector("#form-edit #association_desc").send_keys("Tes Deskripsi Asosiasi Edit")
driver.find_element_by_css_selector("#form-edit #association_logo").send_keys(os.getcwd() + "/banner.jpg") #Image Upload


# In[60]:


driver.find_element_by_css_selector("#form-edit  #btn-do-delete").click()


# In[61]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# In[62]:


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr > td.text-center > button.btn.btn-outline-success.btn-add-provider.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air" )))
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button.btn.btn-outline-success.btn-add-provider.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air").click()


# In[63]:


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#select2-provider_id-container")))

driver.find_element_by_css_selector("#select2-provider_id-container").click()
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("tes nama operator")
time.sleep(10)
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)


# In[64]:


driver.find_element_by_css_selector("#membership_id").send_keys("member01-qwerty")
driver.find_element_by_css_selector("#btn-do-add-provider").click()


# In[65]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# In[66]:


time.sleep(6)
#wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "#dt > tbody > tr > td:nth-child(4)")))
driver.find_element_by_css_selector("#dt > tbody > tr > td:nth-child(4)").text


# In[67]:


driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button.btn-delete.btn.btn-outline-danger.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air").click()


# In[68]:


time.sleep(4)
driver.find_element_by_css_selector("#btn-do-delete").click()


# In[69]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# ## Product tag Check

# In[70]:


#tes produk tag
driver.find_element_by_css_selector("#m_ver_menu > ul > li:nth-child(8) > a").click()
driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div > div.col-12.mb-3.text-right > #btn-add").click()


# In[71]:


time.sleep(4)

driver.find_element_by_css_selector("#modal-add  #name").send_keys("Tes Produk tag en")
driver.find_element_by_css_selector("#modal-add  #name_ind").send_keys("Tes Produk tag indo")


# In[72]:


driver.find_element_by_css_selector("#modal-add  #btn-do-delete").click()


# In[73]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# In[74]:


driver.find_element_by_css_selector("#dt_filter > label > input").send_keys("Tes Produk tag en")


# In[75]:


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr > td.text-center > button.btn.btn-outline-info.btn-preview.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air")))
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button.btn.btn-outline-info.btn-preview.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air").click()


# In[76]:


time.sleep(3)
driver.find_element_by_css_selector("#modal-edit  #name").clear()
driver.find_element_by_css_selector("#modal-edit  #name").send_keys("Tes Produk tag en Edit")
driver.find_element_by_css_selector("#modal-edit  #name_ind").clear()
driver.find_element_by_css_selector("#modal-edit  #name_ind").send_keys("Tes Produk tag indo Edit")


# In[77]:


driver.find_element_by_css_selector("#modal-edit  #btn-do-delete").click()


# In[78]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# In[79]:


time.sleep(4)

driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button.btn-delete.btn.btn-outline-danger.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air").click()


# In[80]:


time.sleep(3)

driver.find_element_by_css_selector("#modal-delete  #btn-do-delete").click()


# In[81]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# ## Insurance check

# In[82]:


#tes Insurance
driver.find_element_by_css_selector("#m_ver_menu > ul > li:nth-child(10) > a").click()


# In[83]:


driver.find_element_by_css_selector("#m_ver_menu > ul > li.m-menu__item.m-menu__item--submenu.m-menu__item--open > div > ul > li:nth-child(2) > a").click()


# In[84]:


#cek status
time.sleep(3)
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button").click()
time.sleep(2)
driver.find_element_by_css_selector("#form-status > div > div.modal-footer > button.btn.btn-primary").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr > td:nth-child(4) > span")))


# In[85]:


driver.find_element_by_css_selector("#dt > tbody > tr > td:nth-child(4) > span").text


# In[86]:


driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button").click()
time.sleep(2)
driver.find_element_by_css_selector("#form-status > div > div.modal-footer > button.btn.btn-primary").click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr > td:nth-child(4) > span")))
driver.find_element_by_css_selector("#dt > tbody > tr > td:nth-child(4) > span").text


# In[87]:


driver.get('http://gomodo.id/back-office/insurance/data-customer')
driver.find_element_by_css_selector("#header > div > button").click()


# In[88]:


#download xls insurance ## mis dalam pencarian selector
time.sleep(5)
#wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div:nth-child(1) > div > div.modal.fade.modal-download.show > div > form > div > div.modal-footer > button.btn.btn-primary")))
#driver.find_element_by_xpath("//*[@id='header']/div/button").click()


# In[89]:


time.sleep(2)
driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div:nth-child(1) > div > div.modal.fade.modal-download.show > div > form > div > div.modal-header > button").click()


# ## Promo General Check (selalu ubah unik code)

# In[90]:


time.sleep(3)
#driver.switch_to.window(driver.window_handles[0])
#driver.find_element_by_xpath("//*[@id='m_ver_menu']/ul/li[12]/a/span").click()
driver.get("http://gomodo.id/back-office/promo-code-gomodo")


# In[91]:


driver.find_element_by_css_selector("#btn-add").click()


# In[92]:


driver.find_element_by_css_selector("#select2-id_company-container").click()
time.sleep(2)


# In[93]:


driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("tes nama operator")
time.sleep(6)
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)


# In[94]:


driver.find_element_by_css_selector("#voucher_code").send_keys(promogeneral) #unik send keys harus diganti


# In[95]:


#mengganti vocer tipe
driver.find_element_by_css_selector("#voucher_amount_type").click()
driver.find_element_by_css_selector("#voucher_amount_type > option:nth-child(2)").click()


# In[96]:


driver.find_element_by_css_selector("#voucher_amount").send_keys("10000")


# In[97]:


driver.find_element_by_css_selector("#minimum_amount").send_keys("10000")


# In[98]:


driver.find_element_by_css_selector("#up_to").send_keys("10000")


# In[99]:


driver.find_element_by_css_selector("#max_use").send_keys("2")


# In[100]:


driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div > div > div > div > form > div.form-group.text-right > #btn-save-promo").click()


# In[101]:


time.sleep(10)
driver.find_element_by_css_selector("#dt_filter > label > input").send_keys(promogeneral) #Unik send keys harus diganti
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr > td.text-center > button")))


# In[102]:


time.sleep(8)
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button").click()
time.sleep(8)
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button").text


# In[103]:


time.sleep(8)
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button").click()
time.sleep(8)
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button").text


# In[104]:


driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 'T')


# In[105]:


#mencoba tes promo code 
driver.execute_script('''window.open("http://muchimug.gomodo.id/product/book/SKU194312615807209019614");''')
driver.switch_to.window(driver.window_handles[1])


# In[106]:


driver.get('''http://muchimug.gomodo.id/product/detail/SKU194712615879634522837''')
time.sleep(2)
driver.find_element_by_css_selector("#product-detail  #btn-book").click()


# In[107]:


driver.find_element_by_css_selector("#promotion-code  #voucher_code").send_keys(promogeneral) #Unik send keys harus diganti
time.sleep(2)
driver.find_element_by_css_selector("#promotion-code #btn-apply-voucher").click()
time.sleep(4)


# In[108]:


#jika hapus maka sukses promo code masuk
print(driver.find_element_by_css_selector("#promotion-code #btn-delete-voucher").text)
time.sleep(5)
#text pada detail harga jika tercantum
driver.find_element_by_css_selector("#discount_voucher > tbody > tr > td:nth-child(1)").text
time.sleep(5)
driver.close()


# In[109]:


driver.switch_to.window(driver.window_handles[0])


# In[110]:


time.sleep(3)
#driver.find_element_by_css_selector("#m_ver_menu > ul > li:nth-child(12) > a").click()


# In[111]:


driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > a").click()


# In[112]:


driver.find_element_by_css_selector("#voucher_amount_type").click()
driver.find_element_by_css_selector("#voucher_amount_type > option:nth-child(1)").click()


# In[113]:


driver.find_element_by_css_selector("#voucher_amount").clear()
driver.find_element_by_css_selector("#voucher_amount").send_keys(50)
driver.find_element_by_css_selector("#minimum_amount").clear()
driver.find_element_by_css_selector("#minimum_amount").send_keys(10000)
driver.find_element_by_css_selector("#up_to").clear()
driver.find_element_by_css_selector("#up_to").send_keys(2000)
driver.find_element_by_css_selector("#max_use").clear()
driver.find_element_by_css_selector("#max_use").send_keys(2)


# In[114]:


driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div > div > div > div > form > div.form-group.text-right #btn-save-promo").click()


# In[115]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# In[116]:


#50 brarti brubah
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr > td:nth-child(4)")))
driver.find_element_by_css_selector("#dt > tbody > tr > td:nth-child(4)").text


# ## Unit Name Check

# In[117]:


#tes ubah unit name
#driver.find_element_by_css_selector("#m_ver_menu > ul > li:nth-child(14) > a").click()
driver.get("http://gomodo.id/back-office/unit_name")


# In[118]:


time.sleep(5)
driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div > div.col-12.mb-3.text-right #btn-add").click()


# In[119]:


time.sleep(3)
driver.find_element_by_css_selector("#modal-add > div > form > div > div.modal-body > div:nth-child(1) #name_en").send_keys("Test Name Unit")
driver.find_element_by_css_selector("#modal-add > div > form > div > div.modal-body > div:nth-child(2) #name_id").send_keys("Tes Nama Unit")


# In[120]:


driver.find_element_by_css_selector("#modal-add #btn-do-delete").click()


# In[121]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# In[122]:


driver.find_element_by_css_selector("#dt_filter > label > input").send_keys("Test Name Unit")


# In[123]:


time.sleep(3)
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button.btn.btn-outline-info.btn-preview.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air").click()


# In[124]:


time.sleep(3)
driver.find_element_by_css_selector("#modal-edit #name_en").clear()
driver.find_element_by_css_selector("#modal-edit #name_en").send_keys("Test Name Unit Edit")
driver.find_element_by_css_selector("#modal-edit #name_id").clear()
driver.find_element_by_css_selector("#modal-edit #name_id").send_keys("Tes Nama Unit Edit")


# In[125]:


driver.find_element_by_css_selector("#modal-edit #btn-do-delete").click()


# In[126]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# In[127]:


time.sleep(5)
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button.btn-delete.btn.btn-outline-danger.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air").click()


# In[128]:


time.sleep(3)
driver.find_element_by_css_selector("#modal-delete > div > form > div > div.modal-footer #btn-do-delete").click()


# In[129]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# ## Premium Check [++Maintenance++]

# In[130]:


#tes premium
time.sleep(5)
driver.get('''http://gomodo.id/back-office/premium''')
#driver.find_element_by_css_selector("#m_ver_menu > ul > li:nth-child(16) > a").click()


# In[131]:


#driver.find_element_by_css_selector("#dt_filter > label > input").send_keys("tes nama operator")


# In[132]:


#time.sleep(3)
#driver.find_element_by_css_selector("#dt > tbody > tr:nth-child(1) > td.text-center > a").click()


# In[133]:


#driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > a").click()

#time.sleep(5)
#wait.until(EC.visibilty_of_element_located((By.CSS_SELECTOR, "#m_ver_menu > ul > li:nth-child(17) > a > span")))
#driver.find_element_by_css_selector(" #dt > tbody > tr:nth-child(1) > td >  #btn-edit").click()
#time.sleep(3)
#driver.find_element_by_css_selector("#status_active > option:nth-child(3)").click()
#time.sleep(2)

#driver.find_element_by_css_selector("#modal-edit > div > form > div > div > #btn-update").click()
#time.sleep(2)

#SET AKTIFASI 
#driver.find_element_by_css_selector(" #dt > tbody > tr:nth-child(1) > td >  #btn-edit").click()
#time.sleep(3)

#driver.find_element_by_css_selector("#status_active > option:nth-child(2)").click()
#time.sleep(2)
#driver.find_element_by_css_selector("#modal-edit > div > form > div > div > #btn-update").click()


# ## Promo Code Check (Unik promo code diganti)

# In[134]:


#tes promo code premium
driver.get("http://gomodo.id/back-office/premium/promo-code")
time.sleep(3)


# In[135]:


driver.find_element_by_css_selector("#btn-add").click()


# In[136]:


#isi form create
time.sleep(4)
driver.find_element_by_css_selector("#code").send_keys(promocode) #unik
driver.find_element_by_css_selector("#amount").send_keys("50")
driver.find_element_by_css_selector("#minimum_transaction").send_keys("10000")
driver.find_element_by_css_selector("#max_amount").send_keys("110000")
driver.find_element_by_css_selector("#provider_max_use").send_keys("2")
driver.find_element_by_css_selector("#general_max_use").send_keys("3")
driver.find_element_by_css_selector("#btn-save-promo").click()


# In[137]:


#mencari promo code dan mengedit
time.sleep(3)
driver.find_element_by_css_selector("#dt_filter > label > input").send_keys(promocode) #unik
time.sleep(5)
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > a").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#type")))
driver.find_element_by_css_selector("#type").click()
driver.find_element_by_css_selector("#type > option:nth-child(2)").click()
driver.find_element_by_css_selector("#amount").clear()
driver.find_element_by_css_selector("#amount").send_keys("10000")
driver.find_element_by_css_selector("#max_amount").clear()
driver.find_element_by_css_selector("#max_amount").send_keys("10000")
driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div > div > div > div > form > div:nth-child(7) > label").click()
#driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div > div > div > div > form > div:nth-child(7) > label > span").click()
time.sleep(3)

driver.find_element_by_css_selector("#range").click()
time.sleep(3)
driver.find_element_by_css_selector("body > div.daterangepicker.dropdown-menu.ltr.show-calendar.opensbottom > div.calendar.left > div.daterangepicker_input > input").clear()
driver.find_element_by_css_selector("body > div.daterangepicker.dropdown-menu.ltr.show-calendar.opensbottom > div.calendar.left > div.daterangepicker_input > input").send_keys("02/03/2020")
driver.find_element_by_css_selector("body > div.daterangepicker.dropdown-menu.ltr.show-calendar.opensbottom > div.calendar.right > div.daterangepicker_input > input").clear()
driver.find_element_by_css_selector("body > div.daterangepicker.dropdown-menu.ltr.show-calendar.opensbottom > div.calendar.right > div.daterangepicker_input > input").send_keys("05/05/2021")
driver.find_element_by_css_selector("body > div.daterangepicker.dropdown-menu.ltr.show-calendar.opensbottom > div.ranges > div > button.applyBtn.btn.btn-sm.btn-success").click()
driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div > div > div > div > form > div.form-group.text-right #btn-save-promo").click()


# In[138]:


#jika edit fixed maka sukses
time.sleep(5)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr > td:nth-child(4)")))
driver.find_element_by_css_selector("#dt > tbody > tr > td:nth-child(4)").text


# In[139]:


driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button").click()
time.sleep(3)
driver.find_element_by_css_selector("#btn-do-delete").click()


# In[140]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# ## List Provider

# ### Profile company

# In[141]:


time.sleep(4)

driver.get('''http://gomodo.id/back-office/providers''')
driver.find_element_by_css_selector("#dt_filter > label > input").send_keys("tes nama operator")
time.sleep(5)
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > a").click()

#edit nama domain
driver.find_element_by_css_selector("#domain_memoria").clear()
driver.find_element_by_css_selector("#domain_memoria").send_keys("muchimugedit.gomodo.id")

#edit nama operator
driver.find_element_by_css_selector("#company_name").clear()
driver.find_element_by_css_selector("#company_name").send_keys("tes nama operator edit")

#edit company bisnis
driver.find_element_by_css_selector("#email_company").clear()
driver.find_element_by_css_selector("#email_company").send_keys("dummy@gmail.com")

#edit phone
driver.find_element_by_css_selector("#phone_company").clear()
driver.find_element_by_css_selector("#phone_company").send_keys("089123123123")

#edit status perusahaan
driver.find_element_by_css_selector("#ownership_status > option:nth-child(1)").click()

#edit status verified provider
driver.find_element_by_css_selector("#verified_provider > option:nth-child(2)").click()

#edit deskripsi
driver.find_element_by_css_selector("#m_tabs_6_1 > form > div > div:nth-child(2) > div:nth-child(1) > div > div.note-editing-area > div.note-editable").clear()
driver.find_element_by_css_selector("#m_tabs_6_1 > form > div > div:nth-child(2) > div:nth-child(1) > div > div.note-editing-area > div.note-editable").send_keys("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec.")

#edit google analytic
driver.find_element_by_css_selector("#m_tabs_6_1 > form > div > div:nth-child(2) > div:nth-child(2) > input").clear()
driver.find_element_by_css_selector("#m_tabs_6_1 > form > div > div:nth-child(2) > div:nth-child(2) > input").send_keys("GOOGLE-321")

#edit KLHK status
driver.find_element_by_css_selector("#m_tabs_6_1 > form > div > div:nth-child(2) > div:nth-child(3) > select > option:nth-child(1)").click()

#edit banned status
driver.find_element_by_css_selector("#status > option:nth-child(1)").click()

#summit
driver.find_element_by_css_selector("#m_tabs_6_1 > form > div > div.col-md-12.text-center.mt-4 > button").click()


# In[ ]:





# In[142]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# In[143]:


time.sleep(4)
driver.find_element_by_css_selector("#dt > tbody > tr:nth-child(1) > td:nth-child(5)").text


# In[144]:


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt_filter > label > input")))
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > a").click()


#edit nama domain
driver.find_element_by_css_selector("#domain_memoria").clear()
driver.find_element_by_css_selector("#domain_memoria").send_keys("muchimug.gomodo.id")

#edit nama operator
driver.find_element_by_css_selector("#company_name").clear()
driver.find_element_by_css_selector("#company_name").send_keys("tes nama operator ")

#edit company bisnis
driver.find_element_by_css_selector("#email_company").clear()
driver.find_element_by_css_selector("#email_company").send_keys("bisnis.jasa.anda007@gmail.com")

#edit phone
driver.find_element_by_css_selector("#phone_company").clear()
driver.find_element_by_css_selector("#phone_company").send_keys("089123412341")

#edit status perusahaan
driver.find_element_by_css_selector("#ownership_status > option:nth-child(2)").click()

#edit status verified provider
driver.find_element_by_css_selector("#verified_provider > option:nth-child(1)").click()

#edit deskripsi
driver.find_element_by_css_selector("#m_tabs_6_1 > form > div > div:nth-child(2) > div:nth-child(1) > div > div.note-editing-area > div.note-editable").clear()
driver.find_element_by_css_selector("#m_tabs_6_1 > form > div > div:nth-child(2) > div:nth-child(1) > div > div.note-editing-area > div.note-editable").send_keys("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec.")

#edit google analytic
driver.find_element_by_css_selector("#m_tabs_6_1 > form > div > div:nth-child(2) > div:nth-child(2) > input").clear()
driver.find_element_by_css_selector("#m_tabs_6_1 > form > div > div:nth-child(2) > div:nth-child(2) > input").send_keys("GOOGLE-123")

#edit KLHK status
driver.find_element_by_css_selector("#m_tabs_6_1 > form > div > div:nth-child(2) > div:nth-child(3) > select > option:nth-child(2)").click()

#edit banned status
driver.find_element_by_css_selector("#status > option:nth-child(2)").click()

#summit
driver.find_element_by_css_selector("#m_tabs_6_1 > form > div > div.col-md-12.text-center.mt-4 > button").click()


# In[145]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# In[146]:


time.sleep(4)
driver.find_element_by_css_selector("#dt > tbody > tr:nth-child(1) > td:nth-child(5)").text


# ### Login user

# In[147]:


#cek login
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr > td.text-center > a")))
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > a").click()
driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div > div > div > div.m-portlet__head > div > ul > li:nth-child(2) > a").click()
driver.find_element_by_css_selector("#first_name").clear()
driver.find_element_by_css_selector("#first_name").send_keys("gramedit")
driver.find_element_by_css_selector("#last_name").clear()
driver.find_element_by_css_selector("#last_name").send_keys("lastedit")
driver.find_element_by_css_selector("#email").clear()
driver.find_element_by_css_selector("#email").send_keys("bim1edit@yopmail.com")
driver.find_element_by_css_selector("#password").send_keys("gomodo321")
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div/div/form/div[6]/select/option[2]").click()


# In[148]:


#submit
time.sleep(4)
driver.find_element_by_css_selector("#m_tabs_6_2 > div > div > form > div:nth-child(8) > button > i").click()


# In[149]:


#mengembalikan seperti semula
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr > td.text-center > a")))
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > a").click()
driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div > div > div > div.m-portlet__head > div > ul > li:nth-child(2) > a").click()
driver.find_element_by_css_selector("#first_name").clear()
driver.find_element_by_css_selector("#first_name").send_keys("gram")
driver.find_element_by_css_selector("#last_name").clear()
driver.find_element_by_css_selector("#last_name").send_keys("last")
driver.find_element_by_css_selector("#email").clear()
driver.find_element_by_css_selector("#email").send_keys("bim1@yopmail.com")
driver.find_element_by_css_selector("#password").send_keys("gomodo123")
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div/div/form/div[6]/select/option[1]").click()

#submit
time.sleep(4)
driver.find_element_by_css_selector("#m_tabs_6_2 > div > div > form > div:nth-child(8) > button > i").click()


# In[ ]:





# ### Bank account and Association

# In[150]:


#cek bank account
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr > td.text-center > a")))
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > a").click()
driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div > div > div > div.m-portlet__head > div > ul > li:nth-child(3) > a").click()
time.sleep(4)

#cek asosiasi
driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div > div > div > div.m-portlet__head > div > ul > li:nth-child(4) > a").click()
driver.find_element_by_css_selector("#m_tabs_6_4 > div:nth-child(1) > div > #btn-add-associaton").click()
time.sleep(3)
driver.find_element_by_css_selector("#form-add > div > div.modal-body > div:nth-child(2) > #association_name").send_keys("123-asosiasi")
time.sleep(4)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div[2]/div/form/div/div[3]/button[2]").click()
time.sleep(4)
driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div > div > div > div.m-portlet__head > div > ul > li:nth-child(4) > a").click()
driver.find_element_by_css_selector("#m_tabs_6_4 > div:nth-child(2) > div:nth-child(3) > div > div.m-portlet__foot > div > div > button").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div[4]/div/form/div/div[3]/button[2]").click()


# ## Product Check

# In[151]:


#produk cek
driver.get('''http://gomodo.id/back-office/product''')
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt_filter > label > input")))
driver.find_element_by_css_selector("#dt_filter > label > input").send_keys("tes nama operator")
time.sleep(4)
driver.find_element_by_css_selector("#dt > tbody > tr:nth-child(1) > td.text-center > a").click()
driver.find_element_by_css_selector("#select2-country-container").click()
time.sleep(1)
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("iceland")
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)
time.sleep(4)
driver.find_element_by_css_selector("#select2-country-container").click()
time.sleep(1)
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("indonesia")
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)
time.sleep(4)

#submit
driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div > div > form > div > div:nth-child(2) > div > div > div.form-group.text-right > button").click()


# ## Order Check

# In[152]:


#cek order berdasar nomer invoice
driver.get('http://gomodo.id/back-office/transaction')
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt_filter > label > input")))
driver.find_element_by_css_selector("#dt_filter > label > input").send_keys("OFINV200226522440")
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr > td.text-center > a")))
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > a").click()
time.sleep(5)
driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div > div > div > div > div > div.m-portlet__head > div > ul > li:nth-child(2) > a").click()
time.sleep(5)
driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div > div > div > div > div > div.m-portlet__head > div > ul > li:nth-child(3) > a").click()
time.sleep(5)

#cek order berdasar alamat operator
driver.get('http://gomodo.id/back-office/transaction')
driver.find_element_by_css_selector("#dt_filter > label > input").clear()
driver.find_element_by_css_selector("#dt_filter > label > input").send_keys("grom")
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr > td.text-center > a")))
driver.find_element_by_css_selector("#dt > tbody > tr:nth-child(1) > td.text-center > a").click()


# ## B2B Blog

# ### category 

# In[153]:


#cek blog b2b blog categori
driver.get('http://gomodo.id/back-office/b2b/blog/category')
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div > div.col-12.mb-3.text-right > #btn-add")))
driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div > div.col-12.mb-3.text-right > #btn-add").click()
time.sleep(3)
#isi data
driver.find_element_by_css_selector("#modal-add > div > form > div > div.modal-body > div > #category_name_ind").send_keys("tes kategori1")
driver.find_element_by_css_selector("#category_name_eng").send_keys("category test")
#submit
driver.find_element_by_css_selector("#modal-add > div > form > div > div.modal-footer > #btn-do-delete").click()
time.sleep(4)

#mencari kategori
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt_filter > label > input")))
driver.find_element_by_css_selector("#dt_filter > label > input").clear()
driver.find_element_by_css_selector("#dt_filter > label > input").send_keys("tes kategori1")
time.sleep(4)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr > td.text-center > button.btn.btn-outline-info.btn-preview.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air")))
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button.btn.btn-outline-info.btn-preview.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air").click()

#edit kategori
time.sleep(2)
driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-body > div > #category_name_ind").clear()
driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-body > div > #category_name_ind").send_keys("tes kategori1 edit")
driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-body > div:nth-child(2) #category_name_eng").clear()
driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-body > div:nth-child(2) #category_name_eng").send_keys("category test1 edit")

#submit
driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-footer > #btn-do-delete").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt_filter > label > input")))
time.sleep(4)

#delete kategori
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button.btn-delete.btn.btn-outline-danger.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air").click()
time.sleep(2)
driver.find_element_by_css_selector("#modal-delete > div > form > div > div.modal-footer #btn-do-delete").click()


# In[154]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# ### tag

# In[155]:


#cek tag b2b
driver.get('http://gomodo.id/back-office/b2b/blog/tags')
time.sleep(4)
#wait.until(EC.visibility_of_element_by_css_selector((By.CSS_SELECTOR, "body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div > div.col-12.mb-3.text-right #btn-add")))
driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div > div.col-12.mb-3.text-right #btn-add").click()
time.sleep(2)
driver.find_element_by_css_selector("#modal-add > div > form > div > div.modal-body > div:nth-child(1) #tag_name_ind").send_keys("Tes1 tag")
driver.find_element_by_css_selector("#modal-add > div > form > div > div.modal-body > div:nth-child(2) #tag_name_eng").send_keys("Tag1 Test")

#summit
driver.find_element_by_css_selector("#modal-add > div > form > div > div.modal-footer #btn-do-delete").click()

#mencari tag
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt_filter > label > input")))
driver.find_element_by_css_selector("#dt_filter > label > input").send_keys("tes tag")
time.sleep(4)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr > td.text-center > button.btn.btn-outline-info.btn-preview.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air")))
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button.btn.btn-outline-info.btn-preview.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air").click()
time.sleep(4)

#edit tag
driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-body > div:nth-child(1) > #tag_name_ind").clear()
driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-body > div:nth-child(1) > #tag_name_ind").send_keys("Tes Tag1 Edit")

driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-body > div:nth-child(2)  #tag_name_eng").clear()
driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-body > div:nth-child(2)  #tag_name_eng").send_keys("Tag Test1 Edit")

#summit
driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-footer #btn-do-delete").click()
time.sleep(4)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt > tbody > tr > td.text-center > button.btn-delete.btn.btn-outline-danger.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air")))

#delete produk
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button.btn-delete.btn.btn-outline-danger.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div[2]/div/form/div/div[3]/button[2]").click()


# In[156]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# ### blog

# In[157]:


#blog post
driver.get('''http://gomodo.id/back-office/b2b/blog/post''')
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#btn-add")))
driver.find_element_by_css_selector("#btn-add").click()
time.sleep(3)

#isi form
driver.find_element_by_css_selector("#title_eng").send_keys(blog_b2b_eng)
driver.find_element_by_css_selector("#title_ind").send_keys(blog_b2b_ind)
driver.find_element_by_css_selector("#select2-m_select2_1-container").click()
time.sleep(1)
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("studi kasus")
time.sleep(2)
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)
#english note
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(4) > div > div.note-editing-area > div.note-editable").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Vivamus arcu felis bibendum ut tristique et egestas quis. Ullamcorper malesuada proin libero nunc consequat interdum. Non consectetur a erat nam at lectus urna duis convallis. Velit scelerisque in dictum non consectetur. Dictum sit amet justo donec enim diam vulputate ut pharetra. Sed ullamcorper morbi tincidunt ornare massa eget egestas purus viverra. Elementum eu facilisis sed odio morbi quis commodo. Amet consectetur adipiscing elit ut aliquam purus sit amet. Urna id volutpat lacus laoreet. Nulla at volutpat diam ut venenatis tellus in. Id porta nibh venenatis cras sed. Volutpat commodo sed egestas egestas fringilla phasellus faucibus. Tincidunt eget nullam non nisi est sit amet. Iaculis at erat pellentesque adipiscing commodo elit at. Nec dui nunc mattis enim ut tellus. Netus et malesuada fames ac turpis egestas integer eget. Ultricies leo integer malesuada nunc vel risus. Ultrices tincidunt arcu non sodales neque. Scelerisque felis imperdiet proin fermentum leo vel orci porta non. Integer enim neque volutpat ac tincidunt vitae. Etiam dignissim diam quis enim lobortis scelerisque. Bibendum enim facilisis gravida neque convallis a cras semper auctor. Mauris pellentesque pulvinar pellentesque habitant. Sed blandit libero volutpat sed cras ornare arcu. Sed faucibus turpis in eu mi bibendum neque egestas congue. Eget est lorem ipsum dolor sit amet. Elementum curabitur vitae nunc sed velit. Mi proin sed libero enim sed faucibus turpis in. Fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate sapien nec. Dolor purus non enim praesent elementum facilisis leo vel. Eget velit aliquet sagittis id consectetur purus ut faucibus. Vel facilisis volutpat est velit egestas dui. Magnis dis parturient montes nascetur ridiculus mus. Et malesuada fames ac turpis egestas integer eget aliquet nibh. Nunc sed blandit libero volutpat sed cras ornare arcu. Eget mi proin sed libero enim sed faucibus. Scelerisque felis imperdiet proin fermentum. Id venenatis a condimentum vitae. Amet consectetur adipiscing elit pellentesque. Aliquam ut porttitor leo a diam. Vitae purus faucibus ornare suspendisse sed. Tellus orci ac auctor augue mauris augue neque gravida. Nisi quis eleifend quam adipiscing vitae proin. Aliquet enim tortor at auctor urna nunc id. Ut faucibus pulvinar elementum integer enim neque. Condimentum lacinia quis vel eros donec ac odio tempor orci. Ornare lectus sit amet est placerat in egestas. Vestibulum lorem sed risus ultricies tristique nulla. Leo duis ut diam quam nulla porttitor. Odio pellentesque diam volutpat commodo sed egestas. Sapien nec sagittis aliquam malesuada bibendum arcu vitae. Suspendisse faucibus interdum posuere lorem ipsum dolor sit. Senectus et netus et malesuada fames ac turpis egestas. Nunc mattis enim ut tellus elementum sagittis vitae et. Ut enim blandit volutpat maecenas volutpat blandit aliquam etiam erat. Tempor id eu nisl nunc. Odio pellentesque diam volutpat commodo sed egestas. Augue ut lectus arcu bibendum at. Ut placerat orci nulla pellentesque dignissim. Dis parturient montes nascetur ridiculus mus mauris vitae ultricies. Feugiat sed lectus vestibulum mattis ullamcorper velit. Tellus rutrum tellus pellentesque eu tincidunt tortor. Netus et malesuada fames ac turpis. Est velit egestas dui id ornare arcu. Mattis molestie a iaculis at erat pellentesque adipiscing. Fringilla ut morbi tincidunt augue interdum velit. Vel elit scelerisque mauris pellentesque pulvinar pellentesque habitant. Feugiat pretium nibh ipsum consequat nisl vel. Feugiat in fermentum posuere urna nec tincidunt. Urna duis convallis convallis tellus id interdum velit. At quis risus sed vulputate odio ut. Iaculis urna id volutpat lacus laoreet non curabitur gravida arcu. Elementum pulvinar etiam non quam lacus suspendisse faucibus interdum. In eu mi bibendum neque egestas congue quisque. Eu nisl nunc mi ipsum faucibus vitae aliquet nec. Viverra vitae congue eu consequat ac felis. Vulputate ut pharetra sit amet aliquam id diam maecenas ultricies. Malesuada bibendum arcu vitae elementum curabitur vitae nunc sed. Lectus quam id leo in vitae turpis. Congue nisi vitae suscipit tellus mauris a. Amet consectetur adipiscing elit ut aliquam purus sit amet luctus. Facilisi etiam dignissim diam quis enim lobortis scelerisque. In hac habitasse platea dictumst quisque sagittis. Ante metus dictum at tempor commodo ullamcorper. Quam viverra orci sagittis eu volutpat odio facilisis mauris. Nisi est sit amet facilisis magna etiam tempor orci. Odio morbi quis commodo odio aenean. Neque viverra justo nec ultrices dui sapien eget mi. Neque sodales ut etiam sit amet nisl purus in. Interdum varius sit amet mattis. Interdum varius sit amet mattis vulputate. Sollicitudin nibh sit amet commodo nulla facilisi nullam. Massa eget egestas purus viverra accumsan in nisl. Fames ac turpis egestas sed tempus urna. Neque sodales ut etiam sit amet nisl. Pellentesque diam volutpat commodo sed. Diam ut venenatis tellus in metus vulputate eu. Senectus et netus et malesuada fames. Imperdiet dui accumsan sit amet nulla.")
#indo note
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(5) > div > div.note-editing-area > div.note-editable").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Gravida dictum fusce ut placerat. Egestas purus viverra accumsan in nisl nisi scelerisque eu. Amet justo donec enim diam vulputate ut pharetra sit. Urna condimentum mattis pellentesque id nibh tortor id aliquet. Egestas dui id ornare arcu odio ut sem. Pulvinar etiam non quam lacus suspendisse faucibus interdum. Quam vulputate dignissim suspendisse in est ante in nibh mauris. Tristique senectus et netus et malesuada fames ac. Porttitor rhoncus dolor purus non enim praesent elementum facilisis leo. Dictum varius duis at consectetur. Ultricies leo integer malesuada nunc. Rhoncus est pellentesque elit ullamcorper dignissim cras tincidunt lobortis feugiat. Elementum curabitur vitae nunc sed velit dignissim sodales ut. Tincidunt arcu non sodales neque sodales ut etiam sit amet. Leo integer malesuada nunc vel risus commodo. Ut lectus arcu bibendum at varius vel pharetra. Arcu dui vivamus arcu felis. Malesuada nunc vel risus commodo viverra maecenas accumsan. Lacinia quis vel eros donec ac odio. Viverra orci sagittis eu volutpat odio facilisis. Convallis aenean et tortor at risus viverra adipiscing. Suspendisse interdum consectetur libero id faucibus nisl. Viverra nam libero justo laoreet sit amet cursus sit amet. Semper feugiat nibh sed pulvinar proin. Ultricies mi quis hendrerit dolor magna eget est lorem ipsum. Libero id faucibus nisl tincidunt eget nullam non. Gravida quis blandit turpis cursus in hac habitasse. Ut tortor pretium viverra suspendisse potenti nullam ac tortor. Placerat duis ultricies lacus sed turpis tincidunt. Nisl suscipit adipiscing bibendum est ultricies integer quis auctor elit. Lorem dolor sed viverra ipsum nunc aliquet bibendum enim. Proin libero nunc consequat interdum varius sit amet mattis. Duis at tellus at urna condimentum mattis pellentesque. Dignissim enim sit amet venenatis urna cursus eget. In est ante in nibh mauris cursus mattis molestie. Vulputate odio ut enim blandit. Gravida in fermentum et sollicitudin. Enim ut tellus elementum sagittis vitae. Libero id faucibus nisl tincidunt eget. Sed viverra ipsum nunc aliquet. Ornare arcu odio ut sem nulla pharetra diam sit. Convallis a cras semper auctor neque vitae tempus. Arcu cursus vitae congue mauris rhoncus aenean vel elit. In metus vulputate eu scelerisque felis imperdiet proin fermentum leo. At volutpat diam ut venenatis tellus in metus vulputate. Et netus et malesuada fames. Et ultrices neque ornare aenean euismod elementum nisi quis. Pellentesque id nibh tortor id aliquet lectus. Sit amet venenatis urna cursus eget nunc scelerisque. Commodo ullamcorper a lacus vestibulum. Blandit aliquam etiam erat velit scelerisque in dictum non. Pharetra diam sit amet nisl suscipit adipiscing. Posuere sollicitudin aliquam ultrices sagittis orci a. Tellus in hac habitasse platea dictumst vestibulum rhoncus est pellentesque. Etiam dignissim diam quis enim lobortis scelerisque fermentum dui faucibus. Libero id faucibus nisl tincidunt eget nullam non nisi. Nunc sed augue lacus viverra vitae congue eu. Vitae semper quis lectus nulla at. Neque gravida in fermentum et sollicitudin ac orci. Dui accumsan sit amet nulla facilisi. In cursus turpis massa tincidunt. Convallis aenean et tortor at risus viverra adipiscing. Nascetur ridiculus mus mauris vitae ultricies leo integer malesuada. Volutpat maecenas volutpat blandit aliquam etiam. Amet consectetur adipiscing elit duis tristique sollicitudin. Et magnis dis parturient montes nascetur ridiculus mus mauris vitae. Ipsum faucibus vitae aliquet nec ullamcorper sit amet risus. Faucibus scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam. Lobortis elementum nibh tellus molestie. Ultricies leo integer malesuada nunc vel risus commodo. Velit dignissim sodales ut eu sem integer. Fermentum leo vel orci porta non pulvinar neque laoreet suspendisse. Est ullamcorper eget nulla facilisi etiam. Scelerisque eu ultrices vitae auctor eu augue ut. Lacus luctus accumsan tortor posuere ac ut consequat semper. Adipiscing diam donec adipiscing tristique. Vitae aliquet nec ullamcorper sit amet risus nullam. Nibh cras pulvinar mattis nunc. Nisi est sit amet facilisis magna etiam. Sem integer vitae justo eget magna. Sagittis purus sit amet volutpat consequat mauris. Dictum sit amet justo donec enim diam vulputate ut. Velit dignissim sodales ut eu sem integer vitae. Vel quam elementum pulvinar etiam. Facilisi etiam dignissim diam quis enim. Non diam phasellus vestibulum lorem sed. Leo in vitae turpis massa sed elementum tempus egestas sed. Ullamcorper eget nulla facilisi etiam dignissim diam quis enim lobortis. Ac felis donec et odio. Est ante in nibh mauris cursus mattis. Donec ac odio tempor orci dapibus ultrices in. In iaculis nunc sed augue. Aliquam eleifend mi in nulla posuere sollicitudin aliquam. Id ornare arcu odio ut sem nulla pharetra diam sit. Vitae sapien pellentesque habitant morbi. Habitasse platea dictumst quisque sagittis purus sit amet volutpat. Donec adipiscing tristique risus nec feugiat in fermentum. Felis eget velit aliquet sagittis id consectetur purus. Enim blandit volutpat maecenas volutpat blandit. Id nibh tortor id aliquet. Imperdiet nulla malesuada pellentesque elit eget gravida cum sociis. Sociis natoque penatibus et magnis dis parturient montes nascetur. Cursus eget nunc scelerisque viverra mauris in. Risus viverra adipiscing at in tellus integer feugiat scelerisque. Tempus imperdiet nulla malesuada pellentesque elit eget. Magnis dis parturient montes nascetur ridiculus mus mauris. Libero id faucibus nisl tincidunt eget. Lacus vestibulum sed arcu non odio euismod lacinia. Et netus et malesuada fames ac turpis. Leo duis ut diam quam nulla porttitor massa id. Porttitor massa id neque aliquam vestibulum morbi. Id faucibus nisl tincidunt eget. Sem viverra aliquet eget sit amet tellus cras adipiscing. Ipsum consequat nisl vel pretium lectus quam id leo in. Diam quis enim lobortis scelerisque fermentum. Tortor consequat id porta nibh venenatis. Vitae congue mauris rhoncus aenean vel elit scelerisque mauris pellentesque. In hac habitasse platea dictumst quisque sagittis purus. Eu non diam phasellus vestibulum lorem sed. Ultricies mi eget mauris pharetra. Dignissim sodales ut eu sem integer. Arcu cursus vitae congue mauris rhoncus. Odio pellentesque diam volutpat commodo sed egestas egestas. Diam vel quam elementum pulvinar etiam. Posuere morbi leo urna molestie at elementum. Nunc faucibus a pellentesque sit amet porttitor eget dolor. Sit amet consectetur adipiscing elit. Nulla facilisi cras fermentum odio eu feugiat. Ipsum consequat nisl vel pretium. Rhoncus urna neque viverra justo nec ultrices dui. Justo donec enim diam vulputate ut pharetra sit amet aliquam. Dolor purus non enim praesent elementum facilisis leo vel fringilla. Risus quis varius quam quisque id diam. At lectus urna duis convallis convallis tellus. At tellus at urna condimentum mattis pellentesque id. Faucibus ornare suspendisse sed nisi lacus sed viverra tellus in. Euismod nisi porta lorem mollis aliquam ut. Laoreet non curabitur gravida arcu ac tortor dignissim convallis aenean. Ac turpis egestas sed tempus urna. Quis viverra nibh cras pulvinar. Nulla malesuada pellentesque elit eget. Id velit ut tortor pretium viverra suspendisse potenti. Nullam ac tortor vitae purus faucibus ornare suspendisse sed. Tellus orci ac auctor augue mauris augue neque gravida in. Ac turpis egestas sed tempus urna et pharetra pharetra massa. Id velit ut tortor pretium viverra suspendisse potenti. Felis bibendum ut tristique et. Odio eu feugiat pretium nibh ipsum consequat nisl. Faucibus vitae aliquet nec ullamcorper sit amet risus nullam. Tellus mauris a diam maecenas sed enim ut sem viverra. Dictum fusce ut placerat orci nulla pellentesque dignissim enim sit. Nunc faucibus a pellentesque sit amet. Nunc non blandit massa enim nec dui nunc. Gravida neque convallis a cras semper auctor neque. Felis imperdiet proin fermentum leo vel orci porta non pulvinar. Ligula ullamcorper malesuada proin libero. Amet dictum sit amet justo. Vitae tempus quam pellentesque nec nam. Quam lacus suspendisse faucibus interdum posuere lorem. Enim blandit volutpat maecenas volutpat blandit aliquam etiam. Pellentesque elit ullamcorper dignissim cras. Massa sapien faucibus et molestie ac. Velit sed ullamcorper morbi tincidunt ornare massa. Fermentum odio eu feugiat pretium nibh. Tellus rutrum tellus pellentesque eu tincidunt. Mi in nulla posuere sollicitudin aliquam ultrices. Proin libero nunc consequat interdum varius. Nam at lectus urna duis convallis convallis. Lacinia at quis risus sed. Bibendum neque egestas congue quisque egestas diam in. Rhoncus aenean vel elit scelerisque mauris. Pulvinar mattis nunc sed blandit libero. Amet facilisis magna etiam tempor. Consectetur a erat nam at. Ornare arcu odio ut sem nulla pharetra diam sit amet. Eget gravida cum sociis natoque penatibus. Sodales ut etiam sit amet nisl purus. Massa eget egestas purus viverra accumsan in. Fringilla urna porttitor rhoncus dolor purus non enim praesent. Urna porttitor rhoncus dolor purus non enim. Metus dictum at tempor commodo ullamcorper a lacus vestibulum sed. Nibh sit amet commodo nulla facilisi nullam vehicula. Enim tortor at auctor urna nunc id cursus. Vel turpis nunc eget lorem dolor sed viverra ipsum. Leo integer malesuada nunc vel risus. Est velit egestas dui id ornare. Mi ipsum faucibus vitae aliquet nec ullamcorper sit amet risus. In est ante in nibh. Sit amet commodo nulla facilisi nullam vehicula. Volutpat odio facilisis mauris sit amet. Lacus sed turpis tincidunt id aliquet risus. Velit sed ullamcorper morbi tincidunt ornare. Id aliquet lectus proin nibh nisl. Scelerisque mauris pellentesque pulvinar pellentesque habitant morbi tristique senectus et. Fermentum leo vel orci porta non pulvinar neque laoreet suspendisse. Quam nulla porttitor massa id neque aliquam vestibulum morbi. Ut faucibus pulvinar elementum integer enim neque volutpat ac. In dictum non consectetur a erat. Et ligula ullamcorper malesuada proin libero nunc consequat interdum.")
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(7) #image_blog").send_keys(os.getcwd() + "/banner.jpg")

#alternative
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(8) #alternative").clear()
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(8) #alternative").send_keys("alternative test")

#tag
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(9) > span > span.selection > span > ul > li > input").send_keys("tip")
time.sleep(2)
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(9) > span > span.selection > span > ul > li > input").send_keys(Keys.ENTER)

driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(10) > label").click()

driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(11) > div #btn-save").click()


# In[158]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# In[161]:


#edit(belum kommplit)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt_filter > label > input")))
driver.find_element_by_css_selector("#dt_filter > label > input").send_keys(blog_b2b_ind)
time.sleep(4)
driver.find_element_by_css_selector("#dt > tbody > tr:nth-child(1) > td.text-center > a").click()
driver.find_element_by_css_selector("#title_eng").clear()
time.sleep(1)
driver.find_element_by_css_selector("#title_eng").send_keys(blog_b2b_eng + "edit")
driver.find_element_by_css_selector("#title_ind").clear()
driver.find_element_by_css_selector("#title_ind").send_keys(blog_b2b_ind + "edit")

driver.find_element_by_css_selector("#category").click()
time.sleep(1)
driver.find_element_by_css_selector("#category > option:nth-child(3)").click()
time.sleep(2)


driver.find_element_by_css_selector("#f-save-ad > div.form-group.text-right #btn-save").click()


# ## Carrer Check

# In[162]:


#karir
driver.get('''http://gomodo.id/back-office/directory/career''')
driver.find_element_by_css_selector("#btn-add").click()
#isi form
time.sleep(5)
driver.find_element_by_css_selector("#location").send_keys("Yogyakarta")
driver.find_element_by_css_selector("#title").send_keys("Tes nama karir")
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(3) > div > div.note-editing-area > div.note-editable").send_keys("egestas dui id ornare arcu odio ut sem nulla pharetra diam sit amet nisl suscipit adipiscing bibendum est ultricies integer quis auctor elit sed vulputate mi sit amet mauris commodo quis imperdiet massa tincidunt nunc pulvinar sapien et ligula ullamcorper malesuada proin libero nunc consequat interdum varius sit amet mattis vulputate enim nulla aliquet porttitor lacus luctus accumsan tortor posuere ac ut consequat semper viverra nam libero justo laoreet sit amet cursus sit amet dictum sit amet justo donec enim diam vulputate ut pharetra sit amet aliquam id diam maecenas ultricies mi eget mauris pharetra et ultrices neque ornare aenean")
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(4) > label").click()
#submit
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(5) > div #btn-save").click()

#search 
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt_filter > label > input")))
driver.find_element_by_css_selector("#dt_filter > label > input").send_keys("tes nama karir")
time.sleep(4)
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > a").click()

#edit karir
time.sleep(5)
driver.find_element_by_css_selector("#location").clear()
driver.find_element_by_css_selector("#location").send_keys("Jakarta")
driver.find_element_by_css_selector("#title").clear()
driver.find_element_by_css_selector("#title").send_keys("Tes nama karir Edit")
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(3) > div > div.note-editing-area > div.note-editable").clear()
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(3) > div > div.note-editing-area > div.note-editable").send_keys("blandit aliquam etiam erat velit scelerisque in dictum non consectetur a erat nam at lectus urna duis convallis convallis tellus id interdum velit laoreet id donec ultrices tincidunt arcu non sodales neque sodales ut etiam sit amet nisl purus in mollis nunc sed id semper risus in hendrerit gravida rutrum quisque non tellus orci ac auctor augue mauris augue neque gravida in fermentum et sollicitudin ac orci phasellus egestas tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum odio eu feugiat pretium nibh ipsum consequat nisl vel pretium lectus quam id leo in vitae turpis massa sed elementum tempus egestas sed sed risus pretium quam vulputate dignissim suspendisse in est ante in nibh mauris cursus mattis molestie a iaculis at erat pellentesque adipiscing commodo elit at imperdiet dui accumsan sit amet nulla facilisi morbi tempus iaculis urna id volutpat lacus laoreet non curabitur gravida arcu ac tortor dignissim convallis aenean et tortor at risus viverra adipiscing at in tellus integer feugiat scelerisque varius morbi enim nunc faucibus a pellentesque sit amet porttitor eget dolor morbi non arcu risus quis varius quam quisque id diam vel quam elementum pulvinar etiam non quam lacus suspendisse faucibus interdum posuere lorem")
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(4) > label").click()

#submit
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(5) > div #btn-save").click()


# In[ ]:





# In[163]:


#jika not publish lulus
time.sleep(3)
driver.find_element_by_css_selector("#dt > tbody > tr > td:nth-child(5) > span").text


# In[164]:


#delete karir
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button").click()
time.sleep(2)
driver.find_element_by_css_selector("#btn-do-delete").click()


# In[165]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# In[166]:


#aplicant
driver.get('''http://gomodo.id/back-office/directory/job-applicant''')
driver.find_element_by_xpath("//*[@id='dt']/tbody/tr[1]/td[7]/a").click() #download 
#driver.find_element_by_css_selector("")


# ## Content Blog Check

# In[167]:


#test blog category
driver.get('''http://gomodo.id/back-office/directory/blog/category''')
driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div > div.col-12.mb-3.text-right #btn-add").click()
time.sleep(3)
driver.find_element_by_css_selector("#modal-add > div > form > div > div.modal-body > div:nth-child(1) #category_name_ind").send_keys(content_blog_ind)
driver.find_element_by_css_selector("#modal-add > div > form > div > div.modal-body > div:nth-child(2) #category_name_eng").send_keys(content_blog_eng)
driver.find_element_by_css_selector("#modal-add > div > form > div > div.modal-footer  #btn-do-delete").click()

#edit konten kategori
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt_filter > label > input")))
driver.find_element_by_css_selector("#dt_filter > label > input").send_keys("tes konten blog indonesia")
time.sleep(3)
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button.btn.btn-outline-info.btn-preview.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air").click()
time.sleep(2)
driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-body > div:nth-child(1) #category_name_ind").clear()
driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-body > div:nth-child(1) #category_name_ind").send_keys( contebt_blog_ind + "EDIT")
driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-body > div:nth-child(2) #category_name_eng").clear()
driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-body > div:nth-child(2) #category_name_eng").send_keys( contebt_blog_eng + "EDIT")

driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-footer #btn-do-delete").click()


# In[ ]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# In[ ]:


#cek tag blog
driver.get('''http://gomodo.id/back-office/directory/blog/tags''')
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div > div.col-12.mb-3.text-right #btn-add")))
driver.find_element_by_css_selector("body > div.m-grid.m-grid--hor.m-grid--root.m-page > div > div.m-grid__item.m-grid__item--fluid.m-wrapper > div.m-content > div.m-portlet > div > div > div.col-12.mb-3.text-right #btn-add").click()
time.sleep(2)
driver.find_element_by_css_selector("#modal-add > div > form > div > div.modal-body > div:nth-child(1) #tag_name_ind").send_keys("Tes tag indonesia")
driver.find_element_by_css_selector("#modal-add > div > form > div > div.modal-body > div:nth-child(2) #tag_name_eng").send_keys("Test tag english")
#submit
driver.find_element_by_css_selector("#modal-add > div > form > div > div.modal-footer #btn-do-delete").click()

#mencari
time.sleep(2)
driver.find_element_by_css_selector("#dt_filter > label > input").send_keys("tes tag indonesia")
time.sleep(3)
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > button.btn.btn-outline-info.btn-preview.btn-sm.m-btn.m-btn--icon.m-btn--icon-only.m-btn--custom.m-btn--pill.m-btn--air").click()
time.sleep(1)

#isi edit form
driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-body > div:nth-child(1) #tag_name_ind").clear()
driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-body > div:nth-child(1) #tag_name_ind").send_keys("Tes tag Indonesia EDIT")
driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-body > div:nth-child(2) #tag_name_eng").clear()
driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-body > div:nth-child(2) #tag_name_eng").send_keys("Test tag English EDIT")
driver.find_element_by_css_selector("#modal-edit > div > form > div > div.modal-footer #btn-do-delete").click()
    


# In[ ]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# In[ ]:


#cek blog post
driver.get('''http://gomodo.id/back-office/directory/blog/post''')
driver.find_element_by_css_selector("#btn-add").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#f-save-ad > div > div > div:nth-child(5) > div > div.note-editing-area > div.note-editable")))

#isi blog
driver.find_element_by_css_selector("#title_eng").send_keys("Tes Blog post di directory")
driver.find_element_by_css_selector("#title_ind").send_keys("Test Blog post at directory")
driver.find_element_by_css_selector("#select2-m_select2_1-container").click()
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("tes konten blog indonesia yang akan di tampilkan pada sebuah konten")
driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(4) > div > div.note-editing-area > div.note-editable").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Vulputate mi sit amet mauris commodo quis imperdiet. Arcu non odio euismod lacinia at quis risus sed vulputate. Sed felis eget velit aliquet. Tellus rutrum tellus pellentesque eu tincidunt tortor aliquam. Aliquam ultrices sagittis orci a scelerisque purus semper eget duis. Nibh cras pulvinar mattis nunc sed blandit. Eu augue ut lectus arcu bibendum at. Id volutpat lacus laoreet non curabitur gravida. Eget est lorem ipsum dolor sit amet consectetur adipiscing elit. Risus in hendrerit gravida rutrum quisque non. Purus sit amet luctus venenatis lectus magna fringilla urna. Morbi tristique senectus et netus et malesuada fames ac turpis. Et sollicitudin ac orci phasellus egestas tellus. Aliquam ut porttitor leo a diam sollicitudin. Vulputate ut pharetra sit amet aliquam id diam maecenas. Pretium quam vulputate dignissim suspendisse. Sit amet est placerat in egestas erat imperdiet sed. Fusce id velit ut tortor pretium viverra suspendisse potenti. Dapibus ultrices in iaculis nunc sed augue lacus viverra. Eget mauris pharetra et ultrices neque ornare. Suscipit tellus mauris a diam maecenas. Et netus et malesuada fames ac turpis egestas integer. Netus et malesuada fames ac. Maecenas volutpat blandit aliquam etiam. Non consectetur a erat nam. Sit amet tellus cras adipiscing enim eu. Porttitor rhoncus dolor purus non enim. Nunc lobortis mattis aliquam faucibus. Tempus imperdiet nulla malesuada pellentesque elit eget gravida. Ullamcorper morbi tincidunt ornare massa eget egestas purus viverra accumsan. Amet venenatis urna cursus eget nunc scelerisque viverra mauris. Nunc id cursus metus aliquam eleifend mi in nulla posuere. Elementum nibh tellus molestie nunc. Felis eget velit aliquet sagittis id consectetur purus ut. Aliquet risus feugiat in ante metus. Aliquam vestibulum morbi blandit cursus. Pharetra convallis posuere morbi leo urna molestie. Libero id faucibus nisl tincidunt eget nullam non. Aenean vel elit scelerisque mauris pellentesque pulvinar pellentesque. Sed velit dignissim sodales ut eu. Congue eu consequat ac felis donec et odio pellentesque diam. Dignissim diam quis enim lobortis scelerisque fermentum dui faucibus in. Facilisi morbi tempus iaculis urna id. Aliquam sem fringilla ut morbi tincidunt augue. Nulla aliquet porttitor lacus luctus accumsan. Venenatis cras sed felis eget velit. Convallis posuere morbi leo urna molestie at. Purus non enim praesent elementum facilisis leo. Cursus in hac habitasse platea dictumst quisque. Eget lorem dolor sed viverra ipsum nunc aliquet bibendum. Odio tempor orci dapibus ultrices in iaculis nunc sed. A cras semper auctor neque. Morbi tristique senectus et netus et malesuada fames ac. At volutpat diam ut venenatis. Volutpat ac tincidunt vitae semper quis lectus nulla at. Aliquam id diam maecenas ultricies mi eget mauris. Ut eu sem integer vitae justo eget magna. Eu mi bibendum neque egestas congue quisque egestas. Convallis tellus id interdum velit laoreet. Amet commodo nulla facilisi nullam vehicula ipsum a arcu. Donec adipiscing tristique risus nec feugiat in fermentum. Ipsum a arcu cursus vitae congue. Ante in nibh mauris cursus mattis molestie a iaculis. Quis lectus nulla at volutpat diam ut venenatis. Id ornare arcu odio ut sem nulla pharetra diam sit. Tempus quam pellentesque nec nam aliquam. In cursus turpis massa tincidunt dui ut ornare. Nunc mattis enim ut tellus elementum. Aliquam nulla facilisi cras fermentum odio eu feugiat. Elit sed vulputate mi sit amet mauris commodo. Adipiscing bibendum est ultricies integer quis auctor elit. Fringilla urna porttitor rhoncus dolor purus non enim praesent. Dapibus ultrices in iaculis nunc sed augue lacus viverra vitae. Enim nulla aliquet porttitor lacus luctus. Consectetur a erat nam at lectus urna duis convallis convallis. Diam quis enim lobortis scelerisque fermentum. Vitae justo eget magna fermentum iaculis. Ultrices in iaculis nunc sed. Tincidunt ornare massa eget egestas purus viverra. In fermentum et sollicitudin ac orci phasellus egestas. Cursus vitae congue mauris rhoncus aenean vel elit scelerisque. Nibh sed pulvinar proin gravida hendrerit lectus a. Cras semper auctor neque vitae tempus quam pellentesque nec. Amet nisl purus in mollis nunc sed id semper risus. Ullamcorper morbi tincidunt ornare massa. Urna nunc id cursus metus aliquam eleifend mi in nulla. Enim neque volutpat ac tincidunt vitae semper quis lectus. Iaculis eu non diam phasellus. Posuere lorem ipsum dolor sit amet consectetur adipiscing elit. Suspendisse in est ante in. Aliquam ut porttitor leo a diam sollicitudin tempor id eu. Placerat in egestas erat imperdiet sed euismod. Lacus vestibulum sed arcu non odio euismod lacinia. Risus in hendrerit gravida rutrum quisque non tellus orci ac. Et molestie ac feugiat sed lectus vestibulum. Nisi vitae suscipit tellus mauris a diam maecenas. Neque egestas congue quisque egestas diam in. Non blandit massa enim nec dui. Sed elementum tempus egestas sed sed risus pretium quam.")
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(5) > div > div.note-editing-area > div.note-editable").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Vulputate mi sit amet mauris commodo quis imperdiet. Arcu non odio euismod lacinia at quis risus sed vulputate. Sed felis eget velit aliquet. Tellus rutrum tellus pellentesque eu tincidunt tortor aliquam. Aliquam ultrices sagittis orci a scelerisque purus semper eget duis. Nibh cras pulvinar mattis nunc sed blandit. Eu augue ut lectus arcu bibendum at. Id volutpat lacus laoreet non curabitur gravida. Eget est lorem ipsum dolor sit amet consectetur adipiscing elit. Risus in hendrerit gravida rutrum quisque non. Purus sit amet luctus venenatis lectus magna fringilla urna. Morbi tristique senectus et netus et malesuada fames ac turpis. Et sollicitudin ac orci phasellus egestas tellus. Aliquam ut porttitor leo a diam sollicitudin. Vulputate ut pharetra sit amet aliquam id diam maecenas. Pretium quam vulputate dignissim suspendisse. Sit amet est placerat in egestas erat imperdiet sed. Fusce id velit ut tortor pretium viverra suspendisse potenti. Dapibus ultrices in iaculis nunc sed augue lacus viverra. Eget mauris pharetra et ultrices neque ornare. Suscipit tellus mauris a diam maecenas. Et netus et malesuada fames ac turpis egestas integer. Netus et malesuada fames ac. Maecenas volutpat blandit aliquam etiam. Non consectetur a erat nam. Sit amet tellus cras adipiscing enim eu. Porttitor rhoncus dolor purus non enim. Nunc lobortis mattis aliquam faucibus. Tempus imperdiet nulla malesuada pellentesque elit eget gravida. Ullamcorper morbi tincidunt ornare massa eget egestas purus viverra accumsan. Amet venenatis urna cursus eget nunc scelerisque viverra mauris. Nunc id cursus metus aliquam eleifend mi in nulla posuere. Elementum nibh tellus molestie nunc. Felis eget velit aliquet sagittis id consectetur purus ut. Aliquet risus feugiat in ante metus. Aliquam vestibulum morbi blandit cursus. Pharetra convallis posuere morbi leo urna molestie. Libero id faucibus nisl tincidunt eget nullam non. Aenean vel elit scelerisque mauris pellentesque pulvinar pellentesque. Sed velit dignissim sodales ut eu. Congue eu consequat ac felis donec et odio pellentesque diam. Dignissim diam quis enim lobortis scelerisque fermentum dui faucibus in. Facilisi morbi tempus iaculis urna id. Aliquam sem fringilla ut morbi tincidunt augue. Nulla aliquet porttitor lacus luctus accumsan. Venenatis cras sed felis eget velit. Convallis posuere morbi leo urna molestie at. Purus non enim praesent elementum facilisis leo. Cursus in hac habitasse platea dictumst quisque. Eget lorem dolor sed viverra ipsum nunc aliquet bibendum. Odio tempor orci dapibus ultrices in iaculis nunc sed. A cras semper auctor neque. Morbi tristique senectus et netus et malesuada fames ac. At volutpat diam ut venenatis. Volutpat ac tincidunt vitae semper quis lectus nulla at. Aliquam id diam maecenas ultricies mi eget mauris. Ut eu sem integer vitae justo eget magna. Eu mi bibendum neque egestas congue quisque egestas. Convallis tellus id interdum velit laoreet. Amet commodo nulla facilisi nullam vehicula ipsum a arcu. Donec adipiscing tristique risus nec feugiat in fermentum. Ipsum a arcu cursus vitae congue. Ante in nibh mauris cursus mattis molestie a iaculis. Quis lectus nulla at volutpat diam ut venenatis. Id ornare arcu odio ut sem nulla pharetra diam sit. Tempus quam pellentesque nec nam aliquam. In cursus turpis massa tincidunt dui ut ornare. Nunc mattis enim ut tellus elementum. Aliquam nulla facilisi cras fermentum odio eu feugiat. Elit sed vulputate mi sit amet mauris commodo. Adipiscing bibendum est ultricies integer quis auctor elit. Fringilla urna porttitor rhoncus dolor purus non enim praesent. Dapibus ultrices in iaculis nunc sed augue lacus viverra vitae. Enim nulla aliquet porttitor lacus luctus. Consectetur a erat nam at lectus urna duis convallis convallis. Diam quis enim lobortis scelerisque fermentum. Vitae justo eget magna fermentum iaculis. Ultrices in iaculis nunc sed. Tincidunt ornare massa eget egestas purus viverra. In fermentum et sollicitudin ac orci phasellus egestas. Cursus vitae congue mauris rhoncus aenean vel elit scelerisque. Nibh sed pulvinar proin gravida hendrerit lectus a. Cras semper auctor neque vitae tempus quam pellentesque nec. Amet nisl purus in mollis nunc sed id semper risus. Ullamcorper morbi tincidunt ornare massa. Urna nunc id cursus metus aliquam eleifend mi in nulla. Enim neque volutpat ac tincidunt vitae semper quis lectus. Iaculis eu non diam phasellus. Posuere lorem ipsum dolor sit amet consectetur adipiscing elit. Suspendisse in est ante in. Aliquam ut porttitor leo a diam sollicitudin tempor id eu. Placerat in egestas erat imperdiet sed euismod. Lacus vestibulum sed arcu non odio euismod lacinia. Risus in hendrerit gravida rutrum quisque non tellus orci ac. Et molestie ac feugiat sed lectus vestibulum. Nisi vitae suscipit tellus mauris a diam maecenas. Neque egestas congue quisque egestas diam in. Non blandit massa enim nec dui. Sed elementum tempus egestas sed sed risus pretium quam.")
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(7) #image_blog").send_keys(os.getcwd() + "/banner.jpg")
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(8) #alternative").clear()
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(8) #alternative").send_keys("Tes alternative image blog post")
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(9) > span > span.selection > span > ul > li > input").send_keys("tes tag indonesia")
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(9) > span > span.selection > span > ul > li > input").send_keys(Keys.ENTER)
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(10) > label").click()

#submit
driver.find_element_by_css_selector("#f-save-ad > div > div > div:nth-child(11) > div #btn-save").click()


# In[ ]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# In[ ]:


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dt_filter > label > input")))
driver.find_element_by_css_selector("#dt_filter > label > input").send_keys("test blog post at directory")
time.sleep(2)

#edit form
driver.find_element_by_css_selector("#dt > tbody > tr > td.text-center > a").click()
driver.find_element_by_css_selector("#title_eng").clear()
driver.find_element_by_css_selector("#title_eng").send_keys("test blog post at directory2edit")
driver.find_element_by_css_selector("#title_ind").clear()
driver.find_element_by_css_selector("#title_ind").send_keys("Test Blog post at directory2edit")
driver.find_element_by_css_selector("#category > option:nth-child(5)").click()
driver.find_element_by_css_selector("#f-save-ad > div:nth-child(5) > div > div.note-editing-area > div.note-editable").clear()
driver.find_element_by_css_selector("#f-save-ad > div:nth-child(5) > div > div.note-editing-area > div.note-editable").send_keys("edit")

driver.find_element_by_css_selector("#f-save-ad > div:nth-child(6) > div > div.note-editing-area").clear()
driver.find_element_by_css_selector("#f-save-ad > div:nth-child(6) > div > div.note-editing-area").send_keys("perubahan")

driver.find_element_by_css_selector("#f-save-ad > div:nth-child(7) > div > div > div > button").send_keys(os.getcwd() + "/logo.jpg)

driver.find_element_by_css_selector("#f-save-ad > div:nth-child(8) #alternative").clear()
driver.find_element_by_css_selector("#f-save-ad > div:nth-child(8) #alternative").send_keys("Tes alternative image blog post EDIT")        
                                                                                                          
driver.find_element_by_css_selector("#f-save-ad > div:nth-child(9) > span > span.selection > span > ul > li.select2-selection__choice > span").click()
driver.find_element_by_css_selector("#f-save-ad > div:nth-child(9) > span > span.selection > span > ul").send_keys("tempatwisata")
driver.find_element_by_css_selector("#f-save-ad > div:nth-child(9) > span > span.selection > span > ul").send_keys(Keys.ENTER) 
driver.find_element_by_css_selector("#f-save-ad > div:nth-child(10) > label").click()
driver.find_element_by_css_selector("#f-save-ad > div.form-group.text-right #btn-save").click()


# In[ ]:


wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))#tunggu toastr
           
text_toast = driver.find_element_by_class_name("toast-message").text #mencari element
           
print(text_toast) #menampilkan pesan


# In[ ]:





# In[ ]:





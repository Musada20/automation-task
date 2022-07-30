import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_valid_resgister(self): #1
        # steps
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar") 
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("musadada") 
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("musadq@gmail.com") 
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("amamamama9") 
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click()
        time.sleep(3)   
        
        #validation
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('berhasil', response_data)
        self.assertEqual(response_message, 'created user!')


    def test_registered_email(self): #2
       # steps
        browser = self.browser 
        browser.get("http://barru.pythonanywhere.com/daftar") 
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() 
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("musadada") 
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("musadada@gmail.com") 
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("amamamama9")
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click()
        time.sleep(3)

        #validation
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Email sudah terdaftar, gunakan Email lain', response_data)
        self.assertEqual(response_message, 'Gagal Registrasi')

   
    def test_a_empty_email_and_password(self): #3
     # steps
        browser = self.browser 
        browser.get("http://barru.pythonanywhere.com/daftar") 
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() 
        time.sleep(3)

        #validation
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Email/Username/Password tidak boleh kosong', response_data)
        self.assertEqual(response_message, 'Gagal Registrasi')
 
    
    def test_registered_name_new_email(self): #4
     # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("musadada") # isi Name
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("musadaw@gmail.com") # isi Name
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("musadali") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('berhasil', response_data)
        self.assertEqual(response_message, 'created user!')

    def test_empty_password(self): #5
     # steps
        browser = self.browser 
        browser.get("http://barru.pythonanywhere.com/daftar") 
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("murid")
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("musadar@gmail.com") 
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() 
        time.sleep(3)

        #validation
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Email/Username/Password tidak boleh kosong', response_data)
        self.assertEqual(response_message, 'Gagal Registrasi')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()

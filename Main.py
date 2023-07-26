from selenium import webdriver
import time

def run_bot(url):
    driver_path = '/chemin/vers/le/ChromeDriver'
    driver = webdriver.Chrome(executable_path=driver_path)
    
    try:
        driver.get(url)
        time.sleep(45)
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    tiktok_url = "Replace this link."
    
    while True:
        run_bot(tiktok_url)
        time.sleep(120) #Attendre deux minutes avant de répeter l'action.
